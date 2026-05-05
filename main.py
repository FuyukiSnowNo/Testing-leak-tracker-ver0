# main.py  -  Sneaker Leak Monitor CLI
# Usage:
#   python main.py scan              # run once now
#   python main.py schedule          # run every hour automatically
#   python main.py matches           # show all matches found so far
#   python main.py ig-login          # save Instagram session
#   python main.py make-template     # create blank Excel sample template

import sys
import logging
import config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(config.SCAN_LOG, encoding="utf-8"),
    ]
)


def cmd_scan():
    from scheduler.runner import run_scan
    run_scan()


def cmd_schedule():
    from scheduler.runner import start_scheduler
    start_scheduler()


def cmd_matches():
    from database.db import DB
    db = DB()
    matches = db.get_matches(limit=50)
    if not matches:
        print("No matches found yet. Run: python main.py scan")
        return
    print("
" + str(len(matches)) + " matches found:
")
    for m in matches:
        print("  [" + m["sample_season"] + "] " + m["sample_model_name"] + " (" + m["sample_model_code"] + ")")
        print("  Source: " + m["source"])
        print("  Title:  " + m["title"])
        print("  URL:    " + m["url"])
        print("  Found:  " + m["notified_at"])
        print()


def cmd_ig_login():
    username = input("Instagram username: ").strip()
    password = input("Instagram password: ").strip()
    try:
        import instaloader
        L = instaloader.Instaloader()
        L.login(username, password)
        L.save_session_to_file("ig_session")
        print("Session saved to ig_session")
    except Exception as e:
        print("Login failed: " + str(e))


def cmd_make_template():
    from samples.loader import create_template
    create_template("samples_template.xlsx")


commands = {
    "scan":          cmd_scan,
    "schedule":      cmd_schedule,
    "matches":       cmd_matches,
    "ig-login":      cmd_ig_login,
    "make-template": cmd_make_template,
}

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd in commands:
        commands[cmd]()
    else:
        print("Commands:")
        for k in commands:
            print("  python main.py " + k)
