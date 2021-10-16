#YOUTUBE DOWNLOADER USING PYTHON SCRIPT
from pytube import Playlist
# 'pip install pytube'

#SET PATH FOR WOWNLOAD VIDEO
path = 'G:/python/youtube-downloader/downloads/'

#CREATE PLAYLIST OBJECT 
p = Playlist('https://www.youtube.com/playlist?list=RDCLAK5uy_n9Fbdw7e6ap-98_A-8JYBmPv64v-Uaq1g')

#INTERACTING WITH PLAYLIST
print(f'Downloading: {p.title}')
path = path + p.title

for video in p.videos:
    video.streams.first().download(path)

print('Downloaded PlayList')

#IF YOU ARE ONLY INTERESTED IN THE URLS OF VIDEOS
for url in p.video_urls[:3]:
    print(url)