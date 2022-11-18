from functions import download_video, display_title
from variables import LINK

from functions import progress_bar

from functions import get_size

def run():
    # progress_bar()
    get_size(link = LINK)
    display_title()
    download_video(link = LINK)

if __name__ == '__main__':
    run()