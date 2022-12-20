from pytube import YouTube
from pytube import Playlist

# for in-built progress bar of pytube
from pytube.cli import on_progress 
# its not good looking but fine

import re


def display_title(link):
    """
    Display the title
    """
    print("Video found: {}".format(YouTube(link).title))

def display_playlist_title(playlistlink):
    """
    Display the playlist title
    """
    print("Playlist found: {}".format(Playlist(playlistlink).title))

def get_size(link):
    """
    Display the download size
    """
    youtubeObject = YouTube(link)
    size = youtubeObject.streams.get_highest_resolution().filesize
    return size

def get_playlist_size(playlistlink):
    totalSize = 0
    for url in Playlist(playlistlink).video_urls:
        totalSize += get_size(url)
    return totalSize

def download_video(link):
    """
    function to download video from the link
    """

    # Validate the link
    pattern = re.compile(r'^(https?\:\/\/)?(www\.)?(youtube\.com|youtu\.?be)\/.+$')

    # search for a match
    match = pattern.search(link)

    # check if a match was found
    if match:
        print('Valid YouTube link')

        display_title(link)

        print("Download size: {}".format(get_size(link)))

        # to get the progress bar while downloading pass the on_progress_callback parameter with on_progress
        youtubeObject = YouTube(link, on_progress_callback = on_progress)
        # other arguments are;
        # youtubeObject = YouTube(link, on_progress_callback, oc_complete_callback, proxies, use_oauth, allow_oauth_cache)
        
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        # .stream.get_highest_resolution() will automatically download the highest resolution available

        try:
            youtubeObject.download()
            # inside download you can pass the location to download

            print("Download successful")

        except:
            print("An error has occurred!!!")

    else:
        print('Invalid YouTube link')

def download_playlist(playlistlink):

    # Validate the link
    pattern = re.compile(r'^(https?\:\/\/)?(www\.)?(youtube\.com|youtu\.?be)\/playlist\?list=.+$')
    
    # search for a match
    match = pattern.search(playlistlink)

    # check if a match was found
    if match:
        print('Valid YouTube playlist link')
        
        # Using Playlist module

        display_playlist_title(playlistlink)

        p = Playlist(playlistlink)
        
        print("{} videos in playlist".format(len(p.videos)))

        for videos in p.videos:
            print(videos.title)
        
        print("Download size: {}".format(get_playlist_size(playlistlink)))

        print("Continue download[Y/n]?")
        response = input()
        if response == "Y" or response == "y":
            flag = True
            for i in p.video_urls:
                youtubeObject = YouTube(i, on_complete_callback = on_progress)
                youtubeObject = youtubeObject.streams.get_highest_resolution()
                try:
                    youtubeObject.download()
                except:
                    print("An error has occurred!!!")
                    flag = False
                    break
            if flag == True: print("Download Successful.")
            

        else:
            print("Download canceled!!!")

    else:
        print('Invalid YouTube playlist link')