from pytube import YouTube

# for in-built progress bar of pytube
from pytube.cli import on_progress 
# its not good looking but fine

import re


def display_title(link):
    """
    Display the title
    """
    print("Video found: {}".format(YouTube(link).title))

def get_size(link):
    """
    Display the download size
    """
    youtubeObject = YouTube(link)
    size = youtubeObject.streams.get_highest_resolution().filesize
    return size

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
        
        # import Selenium for web scraping
        from selenium import webdriver
        from selenium.webdriver.common.by import By

        import os
        os.environ['PATH'] += r"C:\Users\Ashish Singh\Documents\GitHub\YouTube-video-downloader\msedgedriver.exe"

        # In web scrapping window is not required
        options = webdriver.EdgeOptions()
        options.add_argument('--headless')
        driver = webdriver.Edge(options = options)

        driver.get(playlistlink)

        videoTitles = driver.find_elements(By.CSS_SELECTOR, 'h3[class="style-scope ytd-playlist-video-renderer"]')
        titles = [title.text for title in videoTitles]

        videoLinks = driver.find_elements(By.CSS_SELECTOR, 'a[id="video-title"]')
        links = [link.get_attribute('href') for link in videoLinks]

        print("\nTotal {} videos found:".format(len(titles)))
        print('\n'.join(titles))

        totalSize = 0
        for i in range(len(links)):
            totalSize += get_size(links[i])

        print("\nTotal download size: {}".format(totalSize))
        
        '''
        try:
            for link in links:
                youtubeObject = YouTube(link, on_progress_callback = on_progress)
                youtubeObject = youtubeObject.streams.get_highest_resolution()
                youtubeObject.download()

            print("Download successful")

        except:
            print("An error has occurred!!!")
        '''

    else:
        print('Invalid YouTube playlist link')