import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# --- Oauth stuff ---
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"] 
TOKEN_FILE = "token.json"
CLIENT_SECRETS_FILE = "client_secret_387236413925-ahop594daki00eeqf71ubkk0fm92bpsb.apps.googleusercontent.com.json"
creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
youtube = build("youtube", "v3", credentials=creds)
#--------------------






#------test_fields------
file = "testOutput/test.mp4"
TESTPRIVACYSTATUS = "unlisted"
title = "test_Video"
desc = "this is a test"
category = 1


body=dict(
    snippet=dict(
        title=title,
        description=desc,
        categoryId=category
    ),
    status=dict(
        privacyStatus=TESTPRIVACYSTATUS
    )
)

#------------------------

def ytRun():
    request = youtube.videos().insert(
        part=",".join(body.keys()),
        body=body,
        media_body=MediaFileUpload(file, chunksize=-1, resumable=True)
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Uploading: {int(status.progress() * 100)}%")
    print("Done — video id:", response.get("id"))