from pytube import YouTube

LINK = input("Enter the YouTube video URL: ")

TITLE = YouTube(LINK).title