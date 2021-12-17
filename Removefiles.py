import os
import shutil
import time

def main():

    deleteFoldersCount=0
    deleteFilesCount=0

    path="/PATH_TO_DELETE"

    days=30

    seconds=time.time() - (days*24*60*60)

    if os.path.exists(path):
        for root,folders,files in os.walk(path):
            if seconds >= getAge(root):
                removeFolder(root)
                deleteFoldersCount+=1
                break
            else:
                for folder in folders:
                    folderPath = os.path.join(root,folder)
                    if seconds >= getAge(folderPath):
                        removeFolder(folderPath)
                        deleteFoldersCount+=1
                for file in files:
                    filePath = os.path.join(root,file)
                    if seconds >= getAge(filePath):
                        removeFile(filePath)
                        deleteFilesCount+=1
        else:
            if seconds >= getAge(path):
                removeFile(path)
                deleteFilesCount+=1
    else:
        print(f"{path} is not found")
        deleteFilesCount+=1
    print(f"Total folders deleted: {deleteFoldersCount}")
    print(f"Total files deleted: {deleteFilesCount}")

def removeFolder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed successfully")
    else:
        print(f"Unable to delete the "+path)

def removeFile(path):
    if not os.remove(path):
        print(f"{path} is removed successfully")
    else:
        print("Unable to delete the"+path)

def getAge(path):
    ctime = os.stat(path).st_ctime
    return ctime

if __name__ == '__main__':
    main()