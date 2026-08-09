from youtube_transcript_api import YouTubeTranscriptApi
api = YouTubeTranscriptApi()
print(dir(api))
print(hasattr(api, "list_transcripts"))
