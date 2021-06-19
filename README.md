# Webdev <b>Auto-Setup</b> for [node.js](https://nodejs.org/en/docs/)

Webdev <b>Auto-Setup</b> is a simple script to create boilerplate folders structure, files and installs <b>npm</b> packages for you.
<br></br>

# How to Use
```bash
{ } = Mandatory Parameter
( ) = Optional Parameter
```
* **Note** &rarr; *Leave the parentheses out when entering the actual command.*
* **Note** &rarr; *The single ticks **' '** around the path have to be provided*.

```bash
python setup.py {Folder name} {'Path to folder'} (Package names)
```

## Example:
```bash
python setup.py myWebsite 'C:\Users\Example\Desktop\Webdev\'
```
* Notice how there are only two parameters provided and how the path is wrapped in **parentheses**

<br>

Lets install some packages:
```bash
python setup.py myWebsite 'C:\Users\Example\Desktop\Webdev\' express nodemon
```
* Notice how the optional packages are each **seperated** by **spaces**

* Note &rarr; *The default packages are **node**, **dotenv** and **express***

* Note  &rarr; *The packages you are allowed to install are limited to **npm***

## Result:

```
 ┣ 📂node_modules
 ┣ 📂public
 ┃ ┣ 📂css
 ┃ ┃ ┗ 📜styles.css
 ┃ ┣ 📜client.js
 ┃ ┗ 📜index.html
 ┣ 📜.env
 ┣ 📜.gitignore
 ┣ 📜package-lock.json
 ┣ 📜package.json
 ┣ 📜README.md
 ┗ 📜server.js
```

# Errors
What errors you could encounter:
```python
No path provided or spelled wrong!
errors.WrongPathError: <exception str() failed>
```
```python
Not enough parameters provided | Try: python setup.py {folderName} "{pathToFolder}"
errors.MissingParameterError: <exception str() failed>
```
* As the error messages suggest, the problem is most likely a spelling mistake. 
