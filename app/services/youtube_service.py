from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from app.auth.google_auth import GoogleAuth


def upload_to_youtube(filepath, title, description, account):
    auth = GoogleAuth(
        account["client_id"],
        account["client_secret"],
        account["refresh_token"]
    )

    access_token = auth.get_access_token()

    youtube = build("youtube", "v3", credentials=None)
    youtube._http.headers["Authorization"] = f"Bearer {access_token}"

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title or "New Video",
                "description": description
            },
            "status": {"privacyStatus": "public"}
        },
        media_body=MediaFileUpload(filepath, resumable=True)
    )

    response = request.execute()

    return {
        "success": True,
        "url": f"https://youtube.com/watch?v={response['id']}"
    }
