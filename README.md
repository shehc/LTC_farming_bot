# Litecoin Farming Bot

This project is an advanced automation bot for interacting with Telegram reward bots like `Litecoin_click_bot`. It automates tasks such as visiting websites, messaging other bots, and joining Telegram channels to complete tasks and earn rewards.

## Features

### 1. **Website Surfing Automation**
   - Simulates visiting websites through a headless browser using `undetected_chromedriver`.
   - Detects and handles CAPTCHA challenges or Cloudflare protections.
   - Efficiently retrieves and processes task URLs from Telegram messages.

### 2. **Message Bots**
   - Automates messaging other bots as part of reward tasks.
   - Extracts bot usernames and interacts with them via the Telegram API.
   - Handles message validation and forwards the required response back to the reward bot.

### 3. **Join Channels**
   - Automatically joins Telegram channels using the `JoinChannelRequest` method from the Telegram API.
   - Verifies task completion by interacting with the reward bot.

### 4. **Cycle Management**
   - Executes tasks in a loop, seamlessly switching between surfing, messaging, and joining tasks.
   - Includes delay mechanisms to mimic natural user behavior and avoid detection.

## Technical Stack

- **Telegram API**: Interaction with Telegram bots and accounts using the `telethon` library.
- **Selenium & Undetected Chromedriver**: For headless browser automation, bypassing bot detection systems.
- **Regex Matching**: Extracting task URLs and bot usernames efficiently.
- **Asyncio**: Ensuring non-blocking, asynchronous execution for optimal performance.
- **Colorama**: For enhanced console output with colored text.

## How It Works

1. The bot logs in to your Telegram account using `telethon` with your API credentials.
2. It interacts with the specified reward bot (`Litecoin_click_bot`) by sending task commands like:
   - `🖥 Visit sites`
   - `🤖 Message bots`
   - `/join`
3. The bot parses the task details from the bot’s responses, processes the tasks, and returns results to the reward bot.
4. Handles challenges such as CAPTCHA or invalid URLs gracefully with retry mechanisms.

## Requirements

- Python 3.8+
- Telegram API credentials (API ID and Hash)
- Dependencies:
  - `telethon`
  - `selenium`
  - `undetected_chromedriver`
  - `colorama`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/telegram-surfing-bot.git
   cd telegram-surfing-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Telegram API credentials:
   - Obtain your `api_id` and `api_hash` from [my.telegram.org](https://my.telegram.org).
   - Replace the placeholders in the script with your credentials.

4. Run the bot:
   ```bash
   python bot.py
   ```

## Disclaimer

This bot is intended for educational purposes only. Automating interactions with third-party services may violate their terms of service. Use responsibly and at your own risk.
