import re
from googleapiclient.discovery import build
import os
import sys

API_KEY = os.environ.get("YOUTUBE_API_KEY", "")
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_channel_id(youtube, channel_name="LuxAlgo"):
    request = youtube.search().list(
        part="snippet",
        q=channel_name,
        type="channel",
        maxResults=1
    )
    response = request.execute()
    if response['items']:
        return response['items'][0]['id']['channelId']
    return None

def get_all_videos(youtube, channel_id):
    # First get the uploads playlist ID
    request = youtube.channels().list(
        part="contentDetails",
        id=channel_id
    )
    response = request.execute()
    uploads_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    videos = []
    next_page_token = None

    print("Fetching video list...")
    while True:
        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=uploads_playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response['items']:
            video_id = item['contentDetails']['videoId']
            title = item['snippet']['title']
            videos.append({"id": video_id, "title": title})

        next_page_token = response.get('nextPageToken')
        sys.stdout.write(f"\rFetched {len(videos)} videos...")
        sys.stdout.flush()

        if not next_page_token:
            break

    print("\nVideo fetch complete.")
    return videos

def extract_links_from_comments(youtube, video_id):
    links = []
    try:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            order="relevance",
            maxResults=5 # Top comments including pinned
        )
        response = request.execute()

        for item in response.get('items', []):
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            # Find URLs
            urls = re.findall(r'(https?://[^\s]+)', comment)
            for url in urls:
                clean_url = re.sub(r'<[^>]+>', '', url)
                clean_url = re.sub(r'">https.*', '', clean_url) # Clean up duplicate hrefs from API html
                clean_url = clean_url.replace('&amp;', '&')

                # Only keep luxalgo strategy links to reduce noise
                if "luxalgo.com" in clean_url and clean_url not in links:
                    links.append(clean_url)
    except Exception as e:
        # Many videos have comments disabled or fail
        pass

    return links

def main():
    try:
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

        print("Finding LuxAlgo channel...")
        channel_id = get_channel_id(youtube)
        if not channel_id:
            print("Could not find channel.")
            return

        print(f"Found Channel ID: {channel_id}.")
        videos = get_all_videos(youtube, channel_id)

        results = []

        print(f"Analyzing {len(videos)} videos for strategy links in comments (this will take a few minutes)...")
        for i, vid in enumerate(videos):
            if i % 50 == 0:
                print(f"Processed {i}/{len(videos)} videos...")

            links = extract_links_from_comments(youtube, vid['id'])
            if links:
                vid_url = f"https://www.youtube.com/watch?v={vid['id']}"
                results.append(f"Title: {vid['title']}\nVideo URL: {vid_url}\nStrategy Links:\n" + "\n".join(f"  - {l}" for l in links) + "\n")

        with open("luxalgo_all_strategy_links.txt", "w", encoding="utf-8") as f:
            if not results:
                f.write("No links found.")
            else:
                f.write("\n==============================\n".join(results))

        print(f"\nDone. Found links in {len(results)} videos. Saved to luxalgo_all_strategy_links.txt")

    except Exception as e:
        print(f"\nCritical API Error: {e}")

if __name__ == "__main__":
    main()
