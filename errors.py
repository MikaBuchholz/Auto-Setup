import os


class Error(Exception):
    pass


class WrongPathError(Error):
    def __str__(self) -> str:
        print('No path provided or spelled wrong!')


class MissingParameterError(Error):
    def __str__(self) -> str:
        print(
            'Not enough parameters provided | Try: python setup.py {folderName} "{pathToFolder}"')


class CheckParameters():
    @staticmethod
    def checkIfPathExists(path: str) -> bool:
        return os.path.isdir(path)
