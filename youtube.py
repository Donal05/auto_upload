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

# def get_service():
#     creds = None
#     if os.path.exists(TOKEN_FILE):
#         creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
#     if not creds or not creds.valid:
#         flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
#         creds = flow.run_local_server(port=8080) 
#         with open(TOKEN_FILE, "w") as f:
#             f.write(creds.to_json())
#     return build("youtube", "v3", credentials=creds)

def ytRun():
    #get_service()

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