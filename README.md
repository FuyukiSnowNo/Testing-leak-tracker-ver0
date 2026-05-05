# Sneaker Leak Monitor

Automatically monitors sneaker leaks across Google News, RSS sites, and Instagram.
Alerts you via Windows notification, Telegram, and log file when a match is found against your sample list.

## Setup

### 1. Install
pip install -r requirements.txt

### 2. Create your sample list
python main.py make-template
# Fill in samples_template.xlsx then rename to samples.xlsx

### 3. Configure config.py
- Add your Telegram bot token and chat ID
- Adjust RSS sources and search terms if needed

### 4. Instagram login (optional)
python main.py ig-login

### 5. Run
python main.py scan          # run once
python main.py schedule      # run every hour automatically
python main.py matches       # see all matches found

## Sample Excel Format

| Season | Model Name | Model Code | Search Terms |
|--------|-----------|------------|--------------|
| SS25   | Nike Dunk Low Panda | DD1391-100 | Dunk Low, Panda, DD1391-100 |
| FW25   | Air Jordan 1 High OG | DZ5485-612 | AJ1, Jordan 1, DZ5485-612 |

## Telegram Setup
1. Message @BotFather on Telegram -> /newbot -> copy token
2. Message @userinfobot on Telegram -> copy your chat ID
3. Paste both into config.py

## How matching works
Each scraped article/post is checked against every search term in your sample list.
If any term matches -> you get notified with model name, code, season, source, and URL.
Already-notified matches are not sent again.
