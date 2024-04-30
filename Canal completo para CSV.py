# Import modules
import googleapiclient.discovery
import csv

# Create YouTube object
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = "sua_chave")

# Define channel IDs list

channel_ids = ['UCJ6KZTTnkE-s2XFJJmoTAkw' , 'UCpqCsO-fb2_OzVxm7J9MslA' ]

# Create an empty list to store video data
video_data = []

# Iterate over channel IDs
for channel_id in channel_ids:
    # Make a request to the YouTube API to get the latest 50 videos of the channel
    request = youtube.search().list(
        part = "snippet",
        type = "video",
        order = "date",
        channelId = channel_id,
        maxResults = 50
    )
    response = request.execute()

    # Iterate over the items in the response
    for item in response["items"]:
        # Get video ID
        video_id = item["id"]["videoId"]
        
        # Make another request to the YouTube API to get more details about the video
        request2 = youtube.videos().list(
            part = "snippet,contentDetails,statistics",
            id = video_id
        )
        response2 = request2.execute()
        
        # Get video details from the response
        title = response2["items"][0]["snippet"]["title"]
        channel_title = response2["items"][0]["snippet"]["channelTitle"]
        views = response2["items"][0]["statistics"]["viewCount"]
        upload_time = response2["items"][0]["snippet"]["publishedAt"]
        comments = response2["items"][0]["statistics"]["commentCount"]
        duration = response2["items"][0]["statistics"]["commentCount"]
        
       
        # Create a dictionary with video data and append it to the list
        video_dict = {
            "Video Name": title,
            "Video ID": video_id,
            "Channel Name": channel_title,
            "Views": views,
            "Upload Time": upload_time,
            "Comments": comments,
            "Duration": duration,
            
        }
        
        video_data.append(video_dict)


# Open CSV file for writing
with open("data.csv", "w") as f:
    # Create CSV writer object with field names as header row
    field_names = ["Video Name", "Video ID", "Channel Name", "Views", "Upload Time" , "Comments", "Duration"]
    writer = csv.DictWriter(f, fieldnames=field_names)
    
    # Write header row 
    writer.writeheader()
    
    # Write data rows 
    writer.writerows(video_data)

print
