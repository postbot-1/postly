from flask import request, jsonify
import threading

@app.route("/run", methods=["GET"])
def run_post():
    def job():
        try:
            print("🚀 Job started")

            # --- TEMP SAFE TEST (no local file dependency) ---
            import requests
            filename = "test.jpg"
            img = requests.get("https://via.placeholder.com/600.jpg")
            with open(filename, "wb") as f:
                f.write(img.content)

            caption = "Test post from Postly"
            title = "Test Title"

            selected_accounts = ["instagram"]

            accounts_data = {
                "instagram": {
                    "ig_user_id": "YOUR_IG_USER_ID",
                    "access_token": "YOUR_ACCESS_TOKEN"
                }
            }

            from app.core.executor import execute_post
            result = execute_post(
                filename,
                caption,
                title,
                selected_accounts,
                accounts_data
            )

            print("✅ Job completed:", result)

        except Exception as e:
            print("❌ ERROR:", str(e))

    # Run in background (prevents Railway timeout)
    threading.Thread(target=job).start()

    return jsonify({
        "status": "started",
        "message": "Job running in background. Check logs."
    })from flask import request

@app.route("/run", methods=["GET"])
def run_post():
    try:
        # TEMP test values (you can later replace with real input)
        filepath = "test.jpg"  # must exist or be handled in executor
        caption = "Test caption from API"
        title = "Test Title"

        selected_accounts = ["instagram"]  # can add youtube later

        accounts_data = {
            "instagram": {
                "ig_user_id": "YOUR_IG_USER_ID",
                "access_token": "YOUR_ACCESS_TOKEN"
            }
        }

        result = execute_post(
            filepath,
            caption,
            title,
            selected_accounts,
            accounts_data
        )

        return jsonify({"status": "success", "data": result})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
