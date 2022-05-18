
from pytube import Playlist

link = input("Enter your playlist url: ")
plist = Playlist(link)

print(f'Downloading... {link.title}')

for video in plist.videos:
    print(video.title)
    st = video.streams.get_highest_resolution()
    st.download()
print(" ***Check your current director to get your playlist*** ")
