from youtube_transcript_api import YouTubeTranscriptApi

try:
    print(dir(YouTubeTranscriptApi))
    print(hasattr(YouTubeTranscriptApi, "list_transcripts"))
    print(hasattr(YouTubeTranscriptApi, "get_transcript"))
    print(hasattr(YouTubeTranscriptApi, "get_transcripts"))
except Exception as e:
    print(e)
