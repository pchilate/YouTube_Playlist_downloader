
from pytube import Playlist

def Download_Playlist(link):
    plist = Playlist(link)

    print(f'Downloading... {link.title}')

    for video in plist.videos:
        print(video.title)
        st = video.streams.get_highest_resolution()
        st.download()
        
    return " ***Check your current director to get your playlist*** "
