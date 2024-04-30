import os
import pandas
from googleapiclient.discovery import build

api_key = 'sua_chave'

youtube = build('youtube','v3', developerKey=api_key)


channel_id = 'UCJ6KZTTnkE-s2XFJJmoTAkw'

ch_request = youtube.channels().list(
        part = 'contentDetails' ,
        id = channel_id,
        maxResults=50,
     
    )

ch_response  = ch_request.execute()



for item in ch_response['items']:
    Playlists = item['contentDetails']['relatedPlaylists']['uploads']


playlist_id = Playlists



playlist_id = 'PL3HQROiT_CEG0H4rUpHU3_4ypOiPhrRnC'

videos = []


nextPageToken = None
while True:

    pl_request = youtube.playlistItems().list(
        part = 'contentDetails',
        playlistId = playlist_id ,
        maxResults=50,
        pageToken = nextPageToken
    )

    pl_response  = pl_request.execute()

    vid_ids = []

    for item in pl_response['items']: 
        vid_ids.append (item['contentDetails']['videoId'] )



    vid_request = youtube.videos().list(
        part="statistics",
        id=','.join(vid_ids)
    )

    vid_response = vid_request.execute()




    for item in vid_response['items']:
        vid_views = item['statistics']['viewCount']
        

    vid_id = item['id']
    yt_link = f'https://youtu.be/{vid_id}'

    videos.append(
        {
            'views': int(vid_views), 
            'url': yt_link 
        }
    )
    

    nextPageToken = pl_response.get('nextPageToken')
    if not nextPageToken:
        break


videos.sort(key=lambda vid: vid['views'], reverse=True)

for video in videos[:10]:
    print(video['url'], video['views'])



list1 = [video['url']]
list2 = [video['views']]
col1 = "url"
col2 = "views"
data = pandas.DataFrame({col1:list1,col2:list2})
print(data)
