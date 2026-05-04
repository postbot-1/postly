import os
from app.services.youtube_service import upload_to_youtube
from app.services.drive_service import upload_to_drive
from app.utils.retry import retry


def execute_post(filepath, caption, title, selected_accounts, accounts_data):
    results = []
    filename = os.path.basename(filepath)

    public_url = None

    instagram_accounts = [a for a in selected_accounts if a["platform"] == "instagram"]

    if instagram_accounts:
        gdrive_accounts = accounts_data.get("gdrive", [])
        if gdrive_accounts:
            public_url = retry(lambda: upload_to_drive(filepath, filename, gdrive_accounts[0]))

    for item in selected_accounts:
        platform = item["platform"]
        account = item["account"]

        try:
            if platform == "youtube":
                result = retry(lambda: upload_to_youtube(filepath, title, caption, account))
            else:
                result = {"success": False, "error": "Platform not yet implemented"}

            results.append({
                "platform": platform,
                "name": account["name"],
                **result
            })

        except Exception as e:
            results.append({
                "platform": platform,
                "name": account["name"],
                "success": False,
                "error": str(e)
            })

    return results
