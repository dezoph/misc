
import os
import time
import sys
from datetime import datetime
import pywintypes, win32file, win32con

def changeFileCreationTime(fname, newtime):
    wintime = pywintypes.Time(newtime)
    winfile = win32file.CreateFile(
        fname, win32con.GENERIC_WRITE,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
        None, win32con.OPEN_EXISTING,
        win32con.FILE_ATTRIBUTE_NORMAL, None)

    win32file.SetFileTime(winfile, wintime, None, None)

    winfile.close()
    print 'here'

def touchWin(prefix, dirName = '.'):
    for filename in os.listdir(dirName):
        if filename.startswith(prefix):
            changeFileCreationTime(filename, time.time())

def touch(fname, times=None):
    with file(fname, 'a'):
        os.utime(fname, times)

def rename(newPrefix, oldPrefix = 'IMGP'):
    i = 1
    for filename in os.listdir("."):
        if filename.startswith("IMGP"):
            os.rename(filename, newPrefix + '-' + str(i) + '.jpg')
            i = i + 1

def scrap():
    path="full dir path"

    fileList = []
    dirList=os.listdir(path)

    for fname in dirList:
        if "IMG" in fname:
            fileList.append(fname);

    print sorted(fileList)
    sys.stdout.flush()

    # retouch the file in sequential order
    for i, f in enumerate(sorted(fileList)):
        touch(f);
        print '%d' % (i+1)
        sys.stdout.flush()
        time.sleep(1)

def main():
    # rename('lakeGeorgeOct2012', 'IMGP')
    touchWin('lakeGeorgeOct2012', '.')
    

if __name__ == "__main__":    
    main()
