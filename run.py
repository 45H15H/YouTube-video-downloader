
def run():
    """
    Main function
    """

    print("Youtube video downloader".center(50, "_"))

    print("""
    1. Download video
    2. Download playlist
    """)

    option = int(input("Choose option: "))

    if option == 1:
        from variables import LINK
        LINK = LINK()
        from functions import download_video
        download_video(link = LINK)

    elif option == 2:
        from variables import PLAYLISTLINK
        PLAYLISTLINK = PLAYLISTLINK()
        from functions import download_playlist
        download_playlist(playlistlink = PLAYLISTLINK)

    else:
        print("Goodbye!!!")

if __name__ == '__main__':
    run()