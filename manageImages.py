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

def changeTimeStamp(prefix, dirPath = '.'):
    """
    change the time stamp of files in batch
    """

    for filename in os.listdir(dirPath):
        if filename.startswith(prefix):
            touchFile(filename);
            # changeFileCreationTime(filename, time.time())

def touchFile(fname, times=None):
    with file(fname, 'a'):
        os.utime(fname, times)

def rename(newPrefix, oldPrefix = 'IMGP', dirPath = '.'):
    """
    rename the files in a dir with names starting with 
    input prefix
    """

    i = 1
    for filename in os.listdir(dirPath):
        if filename.startswith("IMGP"):
            os.rename(filename, newPrefix + '-' + str(i) + '.jpg')
            i = i + 1

def main():
    cameraPrefix = 'IMGP'
    filePrefix = 'abc'
    dirPath = '.'
    osType = 'unix'
    # rename(filePrefix, cameraPrefix)
    changeTimeStamp(filePrefix, dirPath)
    

if __name__ == "__main__":    
    main()
