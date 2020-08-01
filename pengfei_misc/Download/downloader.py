"""
Author: Pengfei Ren
Email: rpfly0818@gmail.com

╔┓┏╦━━╦┓╔┓╔━━╗
║┗┛║┗━╣┃║┃║oo║
║┏┓║┏━╣┗╣┗╣╰╯║
╚┛┗╩━━╩━╩━╩━━╝
"""

import requests
from clint.textui import progress


def download_files(files):
    """
    Download files with a dictionary of [save_path, file_url].

    Parameters:
        files(dict): Keys are file save pathes, values are file urls.
    
    Returns:
        None
    """

    for save_path, file_url in files.items():
        response = requests.get(file_url, stream=True)

        with open(save_path, "wb") as f:
            total_length = int(response.headers.get('content-length'))
            for ch in progress.bar(response.iter_content(chunk_size=2391975), 
                expected_size=(total_length/1024) + 1):
                if ch:
                    f.write(ch)
    
