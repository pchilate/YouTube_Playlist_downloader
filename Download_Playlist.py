import YouTube_Playlist_Downloader

link = input("Enter your playlist url: ")
result = YouTube_Playlist_Downloader.Download_Playlist(link)
print(result)