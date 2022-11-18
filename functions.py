from pytube import YouTube

import variables

# this is for manual progress bar
from tqdm import tqdm
import time

# for in-built progress bar of pytube
from pytube.cli import on_progress 
# its not good looking but fine

def display_title():
    """
    Display the title
    """
    print("Video found: {}".format(variables.TITLE))

def get_size(link):
    """
    Display the download size
    """
    youtubeObject = YouTube(link)
    size = youtubeObject.streams.get_highest_resolution().filesize
    print("Download size: {}".format(size))

def download_video(link):
    """
    function to download video from the link
    """

    # to get the progress bar while downloading pass the on_progress_callback parameter with on_progress
    youtubeObject = YouTube(link, on_progress_callback = on_progress)
    # other arguments are;
    # youtubeObject = YouTube(link, on_progress_callback, oc_complete_callback, proxies, use_oauth, allow_oauth_cache)
    
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    # .stream.get_highest_resolution() will automatically download the highest resolution available

    

    try:
        youtubeObject.download()
        # inside download you can pass the location to download
    except:
        print("An error has occurred!!!")
    
    print("Download successful")

def progress_bar():
    j = 1
    for i in tqdm(range(100)):
        # time.sleep(0.01 * j)
        time.sleep(0.01)
        j += 1    