# ============================================================
#  config.py  -  Sneaker Leak Monitor Settings
# ============================================================

# -- Sample list ----------------------------------------------
SAMPLES_FILE = "samples.xlsx"   # put your Excel file here

# -- News RSS sources -----------------------------------------
RSS_SOURCES = [
    {"id": "sneakernews",      "name": "Sneaker News",       "rss": "https://news.google.com/rss/search?q=site:sneakernews.com+sneaker&hl=en-US&gl=US&ceid=US:en"},
    {"id": "sneakerbardetroit","name": "Sneaker Bar Detroit", "rss": "https://sneakerbardetroit.com/feed/"},
    {"id": "hypebeast",        "name": "Hypebeast",           "rss": "https://hypebeast.com/footwear/feed"},
    {"id": "nicekicks",        "name": "Nice Kicks",          "rss": "https://nicekicks.com/feed/"},
    {"id": "solecollector",    "name": "Sole Collector",      "rss": "https://solecollector.com/rss"},
    {"id": "highsnobiety",     "name": "Highsnobiety",        "rss": "https://www.highsnobiety.com/feed/"},
    {"id": "kicksonfire",      "name": "Kicks on Fire",       "rss": "https://www.kicksonfire.com/feed/"},
]

# -- Google News search terms ----------------------------------
# These run via Google News RSS - free, no API needed
GOOGLE_SEARCH_TERMS = [
    "nike shoes leaked -kit -uniform -jersey",
    "jordan sneaker leaked unreleased",
    "adidas yeezy leaked 2025",
    "sneaker collab leaked exclusive",
    "new balance sneaker leak",
]

# -- Instagram accounts to monitor ----------------------------
INSTAGRAM_ACCOUNTS = [
    "sneakerfreakermag",
    "sneakerbardetroit",
    "sneakernews",
    "donniebsoles",
]
INSTAGRAM_ENABLED        = True
INSTALOADER_SESSION_FILE = "ig_session"   # run: python main.py ig-login
INSTAGRAM_POSTS_PER_ACCT = 12
INSTAGRAM_DELAY          = 5   # seconds between accounts

# -- Telegram notification -------------------------------------
# Get token: message @BotFather on Telegram -> /newbot
# Get chat_id: message @userinfobot on Telegram
TELEGRAM_ENABLED = True
TELEGRAM_TOKEN   = ""   # paste your bot token here
TELEGRAM_CHAT_ID = ""   # paste your chat ID here

# -- Windows notification --------------------------------------
WINDOWS_NOTIFY_ENABLED = True

# -- Log file -------------------------------------------------
LOG_FILE    = "matches.log"
SCAN_LOG    = "scan.log"

# -- Scheduler ------------------------------------------------
SCAN_INTERVAL_HOURS = 1   # auto-scan every N hours

# -- Database -------------------------------------------------
DATABASE_PATH = "monitor.db"

# -- Scraper settings -----------------------------------------
REQUEST_TIMEOUT = 12
REQUEST_DELAY   = 1.0
USER_AGENT      = "Mozilla/5.0 (compatible; SneakerMonitor/1.0)"

# -- Google Custom Search API (Image Search) --------------------------
# Reuse your existing key and CX from before
# Free: 100 queries/day (10 results each)
GOOGLE_API_KEY      = ""   # paste your AIzaSy... key here
GOOGLE_CX           = ""   # paste your Search Engine ID here
GOOGLE_ENABLED      = True
GOOGLE_DATE_RESTRICT = "d30"  # d7=last week, d30=last month
