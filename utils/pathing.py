from os import path 


def get_util_dir():
    return path.dirname(path.realpath(__file__))


def get_project_dir():
    return path.dirname(get_util_dir())


def get_data_dir():
    return path.join(get_project_dir(), 'data')

def get_pickled_data_dir():
    return path.join(get_data_dir(), 'pickled_data')


def get_fold_dir():
    return path.join(get_data_dir(), 'FDDB-folds')


def get_dataprocessing_dir():
    return path.join(get_project_dir(), 'dataprocessing')


