from pathlib import Path
from utils.file import readin_files


class Block:
    lenght: int
    content: str
    isEmpty: bool

    def __init__(self, lenght, content, isEmtpy):
        self.lenght = lenght
        self.content = content
        self.isEmpty = isEmtpy


def generteDiskContent(fileContent: list[str]) -> (list[str], dict[str, int], dict[int, int]):
    disk_content: list[str] = []
    file_lengths: dict[str, int] = {}
    free_space: dict[int, int] = {}
    this_content = ''
    positionCounter = 0
    for counter, val in enumerate(fileContent[0]):
        if val == '\n':
            continue
        if counter % 2 == 0:
            # create file, content is id, length this value
            this_content = str(int(counter / 2))
            file_lengths[this_content] = int(val)
        else:
            this_content = '.'
            free_space[positionCounter] = int(val)
        for _ in range(int(val)):
            disk_content.append(this_content)
            positionCounter += 1
    return disk_content, file_lengths, free_space


def diskIsCompact(diskContent: list[str]) -> bool:
    firstFreeSpot = diskContent.index('.')
    for nextVal in diskContent[firstFreeSpot:]:
        if nextVal != ".":
            return False
    return True


def getCheckSum(diskContent: list[str]) -> int:
    total_sum = 0
    for counter, val in enumerate(diskContent):
        if val == '.':
            continue
        total_sum += counter * int(val)
    return total_sum


def compactDisk(disk_content: list[str]):
    disk_length = len(disk_content)
    while not diskIsCompact(disk_content):
        # swap the first free spot with the last filed
        firstFreeSpot = disk_content.index('.')
        for counter in reversed(range(disk_length)):
            val = disk_content[counter]
            if val == '.':
                continue
            disk_content[firstFreeSpot] = val
            disk_content[counter] = '.'
            break


def part_one(input_file: str, input_path: Path) -> int:
    """some linalg, why not :)"""
    file_content = readin_files(input_file, input_path)
    disk_content, _, _ = generteDiskContent(file_content)
    # print(disk_content)
    disk_length = len(disk_content)
    while not diskIsCompact(disk_content):
        # swap the first free spot with the last filed
        firstFreeSpot = disk_content.index('.')
        for counter in reversed(range(disk_length)):
            val = disk_content[counter]
            if val == '.':
                continue
            disk_content[firstFreeSpot] = val
            disk_content[counter] = '.'
            break

    return getCheckSum(disk_content)


def part_two(input_file, input_path: Path = Path.cwd()) -> int:
    file_content = readin_files(input_file, input_path)
    discContent, fileDict, freespaces = generteDiskContent(file_content)

    fileIds = fileDict.keys()
    freespacesPositions = freespaces.keys()

    for file in reversed(fileIds):
        currentFileLength:int = int(fileDict[file])
        filePos: int = discContent.index(file)
        # find first free spot to move
        for freepos in sorted(freespacesPositions):
            if freepos > filePos:
                break
            if freespaces[freepos] < currentFileLength:
                continue
            # move the file block, clean up the free space list
            availSpace:int = int(freespaces[freepos])
            for oldPos in range(filePos, filePos+currentFileLength):
                discContent[oldPos] = '.'
            freespaces[filePos] = currentFileLength
            for newPos in range(freepos, freepos+currentFileLength):
                discContent[newPos] = file
            freespaces.__delitem__(freepos)
            if availSpace > currentFileLength:
                freespaces[freepos+currentFileLength] = availSpace-currentFileLength

            freespacesPositions = freespaces.keys()
            break

    return getCheckSum(discContent)


if __name__ == "__main__":
    my_input_path = Path.cwd() / 'assets'
    #print(part_one('input.txt', my_input_path))
    print(part_two('input.txt', my_input_path))
