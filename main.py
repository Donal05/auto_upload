# import os
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.http import MediaFileUpload
# from google.oauth2.credentials import Credentials



# def get_service():
#     creds = None
#     if os.path.exists(TOKEN_FILE):
#         creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
#     if not creds or not creds.valid:
#         flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
#         creds = flow.run_local_server(port=8080)   # opens browser for consent
#         with open(TOKEN_FILE, "w") as f:
#             f.write(creds.to_json())
#     return build("youtube", "v3", credentials=creds)

# def upload(video_path, title="Test upload", description="", tags=None, privacy="unlisted"):
#     youtube = get_service()
#     body = {
#         "snippet": {"title": title, "description": description, "tags": tags or []},
#         "status": {"privacyStatus": privacy}
#     }
#     media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
#     request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
#     response = None
#     while response is None:
#         status, response = request.next_chunk()
#         if status:
#             print(f"Uploading: {int(status.progress() * 100)}%")
#     print("Done — video id:", response.get("id"))

# if __name__ == "__main__":
#     upload("output.mp4", title="My test video", description="Auto upload demo", tags=["demo"], privacy="unlisted")





import moviepy
import tkinter as tk
from youtube import *

#-----inputs for testing-----
AUDIO = "testData/Human_Music.mp3"
IMAGE = "testData/frog.jpg"

#----------------------------



def makeVid(image, audio):
    sound = moviepy.AudioFileClip(audio, fps = 44100)
    visual = moviepy.ImageClip(image, duration=sound.duration).resized(height= 1080)
    visual = visual.with_audio(sound) 
    visual.write_videofile("testOutput/test.mp4",fps = 30)



#makeVid(IMAGE,AUDIO)


ytRun()










# --- upload ---
# call youtube.videos().insert(...) here
