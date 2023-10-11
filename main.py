from flask import Flask, jsonify
import requests
import threading
import time

app = Flask(__name__)

# Read the token from the file
TELEGRAM_TOKEN = open("telegram_token.txt", "r").read().strip()
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"

# In-memory storage for the messages
messages_store = []
response_json = {
    "ok": True,
    "result": []
}


def poll_telegram():
    global messages_store
    last_update_id = 0
    while True:
        try:
            response = requests.get(TELEGRAM_API_URL, params={"offset": last_update_id + 1, "timeout": 60})
            if response.status_code == 200:
                updates = response.json().get('result', [])
                for update in updates:
                    if 'channel_post' in update and \
                            'chat' in update['channel_post'] and \
                            'text' in update['channel_post'] and \
                            ('title' in update['channel_post']['chat'] and
                             "bot" in update['channel_post']['chat']['title'].lower()):
                        print(f"Got new message: {update['channel_post']['text']}")
                        response_json["result"].append(update)

                        # Keep only the last 10 messages
                        response_json["result"] = response_json["result"][-15:]

                    last_update_id = max(last_update_id, update['update_id'])
        except Exception as e:
            print(f"Error while polling: {e}")
        time.sleep(5)  # Sleep for 5 seconds before polling again


@app.route('/get_messages', methods=['GET'])
def get_messages():
    try:
        return jsonify(response_json)
    except Exception as e:
        print(f"Error while getting messages: {e}")

# Prevent the server from crashing


if __name__ == '__main__':
    # Start the polling thread
    threading.Thread(target=poll_telegram, daemon=True).start()

    # Run the Flask app as public
    app.run(host='0.0.0.0', port=3008)
