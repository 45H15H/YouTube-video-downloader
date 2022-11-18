from functions import download_video, display_title
from variables import LINK

def run():
    display_title()
    download_video(link = LINK)

if __name__ == '__main__':
    run()