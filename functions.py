from pytube import YouTube

import variables

def display_title():
    print("Video found: {}".format(variables.TITLE))

def download_video(link):
    """
    function to download video from the link.
    """

    youtubeObject = YouTube(link)
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
