# docMaster
This project is for creating a short document on the data source, variable information and the scripts in a Lumira Document. 

>This project is entirely experimental and by using this you agree that you are aware of it and I will not be held liable for any errors that this project causes.

**Steps**
1. Collect all the .lumx files for which you need to create documents in one directory.
2. Run _docMaster.py_ from the terminal.
```python
python docMaster.py "folder location that contains all the .lumx files"
```
3. Note that the file location should __always__ be in _double quotes_ - this is to ensure that the spaces in the folder path are parsed correctly
4. When run, _docMaster.py_ will run _docPrinter.py_ for every .lumx file that is present in the directory. This will result in multiple terminal windows popping up. This will be fixed in future releases.
5. Once done, you will find the documents in the directory that contains the .lumx files.
6. There will also be directories created in the names of the .lumx files - these are simply the extracted versions of the .lumx files. Feel free to delete them if they aren't required. _docPrinter.py_ generates these directories everytime it is run.

**Package Dependencies**
Following packages are required:
1. python-docx (requries installation)
2. zipfile (requires installation)
3. re
4. sys
5. os
