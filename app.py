from flask import request

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
