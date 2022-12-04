import os, datetime

def create_screenshot_directory():
    '''creates a directory to store screenshot files when test runs'''
    path = 'screenshots/'
    # timestamp to name folder
    current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    directory_path = path + current_time
    os.makedirs(directory_path)
    return directory_path

