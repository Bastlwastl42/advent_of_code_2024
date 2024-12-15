from pathlib import Path
from utils.file import readin_files


def generateMap(file_content) -> dict[tuple[int, int], int]:
    retDict: dict[tuple[int, int], int] = {}
    for row, line in enumerate(file_content):
        for col, height in enumerate(line.strip()):
            retDict[col, row] = int(height)
    return retDict


def getThemZero(mapDict: dict[tuple[int, int], int]) -> list[tuple[int, int]]:
    retList: list[tuple[int, int]] = [coordinates for coordinates, height in mapDict.items()
                                      if height == 0]
    return retList


def canContinueTrail(mapDict: dict[tuple[int, int], int], nextHeight: int, currentPos):
    nextPos = [(currentPos[0] + 1, currentPos[1]),
               (currentPos[0] - 1, currentPos[1]),
               (currentPos[0], currentPos[1] + 1),
               (currentPos[0], currentPos[1] - 1)]

    return [pos for pos in nextPos if mapDict.get(pos, -1) == nextHeight]


def part_one(input_file: str, input_path: Path) -> int:
    """some linalg, why not :)"""
    file_content = readin_files(input_file, input_path)
    mapDict = generateMap(file_content)
    resultingPaths: dict[tuple[int, int], int] = {}
    for startPos in getThemZero(mapDict):
        listOfPaths: list[list] = [[startPos]]
        for height in range(1, 10):
            listOfNextPaths = []
            for path in listOfPaths:
                nextSteps = canContinueTrail(mapDict, height, path[-1])
                for step in nextSteps:
                    newPath = [x for x in path]
                    newPath.append(step)
                    listOfNextPaths.append(newPath)
            listOfPaths = listOfNextPaths
        reachedPeaks = [x[-1] for x in listOfPaths]
        assert all([(mapDict[x] == 9) for x in reachedPeaks])
        resultingPaths[startPos] = len(set(reachedPeaks))
    return sum([x for x in resultingPaths.values()])


def part_two(input_file, input_path: Path = Path.cwd()) -> int:
    file_content = readin_files(input_file, input_path)
    mapDict = generateMap(file_content)
    resultingPaths: dict[tuple[int, int], int] = {}
    for startPos in getThemZero(mapDict):
        listOfPaths: list[list] = [[startPos]]
        for height in range(1, 10):
            listOfNextPaths = []
            for path in listOfPaths:
                nextSteps = canContinueTrail(mapDict, height, path[-1])
                for step in nextSteps:
                    newPath = [x for x in path]
                    newPath.append(step)
                    listOfNextPaths.append(newPath)
            listOfPaths = listOfNextPaths
        reachedPeaks = [x[-1] for x in listOfPaths]
        assert all([(mapDict[x] == 9) for x in reachedPeaks])
        resultingPaths[startPos] = len(listOfPaths)
    return sum([x for x in resultingPaths.values()])


if __name__ == "__main__":
    my_input_path = Path.cwd() / 'assets'
    print(part_one('input.txt', my_input_path))
    print(part_two('input.txt', my_input_path))
