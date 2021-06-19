import os
import sys
from typing import List, Union
from errors import MissingParameterError, WrongPathError, CheckParameters


class WebdevSetup():
    def __init__(self, dirName: str = None, path: str = None, packages: List[str] = None) -> None:
        self.dirName: Union[str, None] = dirName
        self.path: Union[str, None] = path
        self.packages: Union[List[str], None] = packages
        self.defaultCommands: List[str] = [
            'npm init -y', 'npm i node', 'npm i dotenv', 'npm i epxress']
        self.defaultFiles: List[str] = ['.env', '.gitignore', 'README.md', 'server.js',
                                        'public/index.html', 'public/client.js', 'public/css/styles.css']
        self.defaultFolders: List[str] = ['public', 'public/css']

        if self.path == '.':
            self.path: str = os.curdir

    def main(self) -> None:
        if CheckParameters().checkIfPathExists(self.path):
            self.createDirectory()

        else:
            raise WrongPathError()

        os.chdir(f'{self.path}\\{self.dirName}')

        self.createFolders()
        self.createFiles()
        self.executeCommands()

        if self.packages != None:
            self.installExtraPackages()

    def executeCommands(self) -> None:
        for command in self.defaultCommands:
            os.system(command)

    def installExtraPackages(self) -> None:
        for package in self.packages:
            os.system(f'npm i {package}')

    def createFiles(self) -> None:
        for file in self.defaultFiles:
            if file == '.gitignore':
                with open(file, 'w') as files:
                    files.write('node_modules\n.gitignore')

            else:
                open(file, 'x')

    def createFolders(self) -> None:
        for folder in self.defaultFolders:
            os.mkdir(folder)

    def createDirectory(self) -> None:
        os.mkdir(f'{self.path}/{self.dirName}')


if __name__ == '__main__':
    try:
        dirName: str = sys.argv[1]

    except IndexError:
        raise MissingParameterError()

    try:
        path: str = sys.argv[2]

    except IndexError:
        raise MissingParameterError()

    if len(sys.argv) > 3:
        try:
            packages: List[str] = sys.argv[3:]

        except IndexError:
            packages: None = None

    else:
        packages: List[str] = None

    WebdevSetup(dirName, path, packages).main()
