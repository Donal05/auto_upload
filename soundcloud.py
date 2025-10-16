import soundcloud

#------test fields------

def scRun():
    client = soundcloud.Client(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    username='YOUR_EMAIL',
    password='YOUR_PASSWORD'
    )


    track = client.post('/tracks', track={
        'title': 'test',
        'sharing': 'private',
        'asset_data': open('path/to/your_track.mp3', 'rb')
        'artwork_data': open('path/to/cover.jpg', 'rb')

    })


    print("Uploaded successfully:", track.permalink_url)