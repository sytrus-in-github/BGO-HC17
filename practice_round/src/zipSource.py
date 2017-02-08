# this script will zip up all source code in this directory to out/source.zip
import zipfile
import os
from time import gmtime, strftime

def isSourceCode(filename):
    # determines if the file is a valid source file
    return filename.endswith('.py') and filename != 'zipSource.py'

def zipall(path, ziph):
    # zip all source files in "path", ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            if isSourceCode(file):
                ziph.write(os.path.join(root, file))

if __name__ == '__main__':
    # get folder of this file
    dirPath = os.path.dirname(os.path.realpath(__file__))
    # get timestamp
    timeStamp = strftime("%H%M%S")
    # zip the code
    with zipfile.ZipFile(dirPath+'/../out/source_'+timeStamp+'.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipall('./', zipf)