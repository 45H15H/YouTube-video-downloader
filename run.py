from functions import download_video, display_title
from variables import LINK

# from functions import progress_bar

from functions import get_size

def run():
    """
    Main function
    """
    print("Youtube video downloader".center(50, "_"))

    display_title()
    get_size(link = LINK)
    download_video(link = LINK)

if __name__ == '__main__':
    run()