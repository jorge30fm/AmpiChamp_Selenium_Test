import os, datetime

def create_screenshot_directory():
    path = 'screenshots/'
    current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    directory_path = path + current_time
    os.makedirs(directory_path)
    print(directory_path)
    return directory_path

