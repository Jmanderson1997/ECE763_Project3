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
        with tarfile.open(os.path.join(get_data_dir(), 'FDDB-folds.tgz'), 'r') as tar:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tar, get_data_dir())

    print("Downloading and Extracting Images")
    if not os.path.exists(os.path.join(get_data_dir(), '2002')):
        wget.download(IMG_URL, get_data_dir())
        with tarfile.open(os.path.join(get_data_dir(), 'originalPics.tar.gz'), 'r:gz') as tar:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tar)
            # for file_ in tar: 
            #     try:
            #         tar.extract(file_)
            #     except IOError as e:
            #         pass


if __name__ == '__main__':
    downloadFDDB()

