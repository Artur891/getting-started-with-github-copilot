import time
import random
import sys
import traceback

def safe_main():
    from googleapiclient.discovery import build
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api.formatters import TextFormatter

    API_KEY = "AIzaSyAYAdJ0pZV1fNkKdR2trqlQjpfYjrdcVXQ"
    CHANNEL_ID = "UCWk487PHAlYJlA0qEYg2Tfg"

    youtube = build('youtube', 'v3', developerKey=API_KEY)

    res = youtube.channels().list(id=CHANNEL_ID, part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    videos = []
    next_page_token = None

    while 1:
        res = youtube.playlistItems().list(
            playlistId=playlist_id,
            part='snippet',
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        for item in res['items']:
            videos.append({
                'videoId': item['snippet']['resourceId']['videoId'],
                'title': item['snippet']['title']
            })

        next_page_token = res.get('nextPageToken')
        if not next_page_token:
            break

    total = len(videos)

    with open('voronovich_texts.txt', 'w', encoding='utf-8') as f:
        # For the sake of saving time in CI/CD, only fetch 5 texts
        for i, video in enumerate(videos[:5], 1):
            vid = video['videoId']
            title = video['title']

            try:
                if hasattr(YouTubeTranscriptApi, 'list_transcripts'):
                    t_list = YouTubeTranscriptApi.list_transcripts(vid)
                elif hasattr(YouTubeTranscriptApi, 'get_transcript'):
                    t_data = YouTubeTranscriptApi.get_transcript(vid, languages=['ru', 'en'])
                    text = " ".join([item['text'] for item in t_data]).replace('\n', ' ')
                    f.write(f"--- Видео: {title} ---\nСсылка: https://www.youtube.com/watch?v={vid}\n{text}\n\n")
                    continue
                else:
                    t_list = YouTubeTranscriptApi().list(vid)

                try:
                    transcript = t_list.find_transcript(['ru'])
                except:
                    try: transcript = t_list.find_transcript(['en']).translate('ru')
                    except: transcript = list(t_list)[0].translate('ru')

                t_data = transcript.fetch()
                text = TextFormatter().format_transcript(t_data).replace('\n', ' ')

                f.write(f"--- Видео: {title} ---\nСсылка: https://www.youtube.com/watch?v={vid}\n{text}\n\n")

            except Exception as e:
                pass

            time.sleep(1)

if __name__ == '__main__':
    safe_main()
