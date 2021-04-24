import os
import wget 
from utils.pathing import *
import tarfile

FOLD_URL = 'http://vis-www.cs.umass.edu/fddb/FDDB-folds.tgz'
IMG_URL = 'http://vis-www.cs.umass.edu/fddb/originalPics.tar.gz'

def downloadFDDB(): 

    if not os.path.exists(get_data_dir()): 
        os.mkdir(get_data_dir())

    print("Downloading and Extracting Folds")
    if not os.path.exists(os.path.join(get_data_dir(), 'FDDB-folds')):
        wget.download(FOLD_URL, get_data_dir())
        with tarfile.open(os.path.join(get_data_dir(), 'FDDB-folds.tgz'), 'r') as zip:
            zip.extractall(get_data_dir())

    print("Downloading and Extracting Images")
    if not os.path.exists(os.path.join(get_data_dir(), '2002')):
        wget.download(IMG_URL, get_data_dir())
        with tarfile.open(os.path.join(get_data_dir(), 'originalPics.tar.gz'), 'r') as zip:
            zip.extractall(get_data_dir())


if __name__ == '__main__':
    downloadFDDB()

