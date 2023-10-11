# Telegram Channel Poller

## Overview
A Flask-based application that polls Telegram channels for new messages and provides an API to retrieve them.

## Features
- **Real-time Polling**: Checks for new messages every few seconds.
- **Channel Filtering**: Specifically captures messages from channels with "bot" in their title.
- **Message Limit**: Stores up to the last 15 messages to optimize memory usage.
- **API Endpoint**: Fetch stored messages using the `/get_messages` endpoint.

## Prerequisites
- Python 3.x
- Flask
- Requests

## Setup Instructions

1. Clone this repository:
    ```bash
    git clone <repository-url>
    cd <repository-dir>
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
   
3. Add your Telegram bot token:
Save your Telegram bot token in a file named `telegram_token.txt` in the root directory.

## Running the Application

Run the application:
    ```
    python main.py
    ```


Once running, you can access the API to retrieve messages at:
    ```
    http://localhost:3008/get_messages
    ```


## Contribution

Feel free to fork this repository, make changes, and submit pull requests. Feedback and suggestions are welcome!

