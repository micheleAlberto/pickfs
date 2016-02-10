# pickfs
A simple curse based gui to pick files and folders in python
A simple filesystem navigation is supported, path of the chosen file or folder is returned as a string
##Install
```
python setup.py install
```

##pick a file
```python 
pick_file()
pick_file(
    text='the text to tell your user what to chose',
    path='/home/',
    extensions=['txt','py','cpp'])
```

##pick a folder
```python 
pick_folder(text='chose a directory',path='.')
pick_folder()
```
