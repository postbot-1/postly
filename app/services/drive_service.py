from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from app.auth.google_auth import GoogleAuth


def upload_to_drive(filepath, filename, account):
    auth = GoogleAuth(
        account["client_id"],
        account["client_secret"],
        account["refresh_token"]
    )

    access_token = auth.get_access_token()

    drive = build("drive", "v3", credentials=None)
    drive._http.headers["Authorization"] = f"Bearer {access_token}"

    media = MediaFileUpload(filepath, resumable=True)

    uploaded = drive.files().create(
        body={"name": filename},
        media_body=media,
        fields="id"
    ).execute()

    file_id = uploaded["id"]

    drive.permissions().create(
        fileId=file_id,
        body={"type": "anyone", "role": "reader"}
    ).execute()

    return f"https://drive.google.com/uc?export=download&id={file_id}"
