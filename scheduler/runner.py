"""# scheduler/runner.py
import logging
import time
from datetime import datetime, timezone, timedelta

import schedule
from rich.console import Console

from database.db import Database
from utils.image_downloader import ImageDownloader
import config

# New add this
def safe_print(msg: str):
    console.out(msg)

console = Console(highlight=False)
logger  = logging.getLogger(__name__)


def _get_scrapers() -> list:
    from scrapers.sneakernews       import SneakerNewsScraper
    from scrapers.sneakerbardetroit import SneakerBarDetroitScraper
    from scrapers.others            import (
        SneakerFreakerScraper, HypebeastScraper, KicksOnFireScraper
    )
    rss_map = {
        "sneakernews":       SneakerNewsScraper,
        "sneakerbardetroit": SneakerBarDetroitScraper,
        "sneakerfreaker":    SneakerFreakerScraper,
        "hypebeast":         HypebeastScraper,
        "kicksonfire":       KicksOnFireScraper,
    }
    scrapers = [
        cls() for src in config.SOURCES
        if src["enabled"]
        for sid, cls in rss_map.items()
        if sid == src["id"]
    ]

    if getattr(config, "INSTAGRAM_ENABLED", True):
        try:
            from scrapers.instagram import InstagramScraper
            scrapers.append(InstagramScraper())
        except Exception as e:
            logger.warning(f"Instagram scraper skipped: {e}")

    if getattr(config, "GOOGLE_ENABLED", True):
        api_key = getattr(config, "GOOGLE_API_KEY", "")
        cx      = getattr(config, "GOOGLE_CX", "")
        if api_key and api_key not in ("", "YOUR_GOOGLE_API_KEY"):
            try:
                from scrapers.google_search import GoogleSearchScraper
                scrapers.append(GoogleSearchScraper())
            except Exception as e:
                logger.warning(f"Google scraper skipped: {e}")
        else:
            logger.info("Google Search: set GOOGLE_API_KEY + GOOGLE_CX in config.py to enable")

    return scrapers


def run_scan(db: Database, since: datetime = None, download_images: bool = True) -> dict:
    scrapers = _get_scrapers()
    since    = since or datetime.now(timezone.utc) - timedelta(hours=config.DEFAULT_INTERVAL_HOURS)
    downloader = ImageDownloader() if download_images else None

    total_new = total_skip = total_imgs = 0
    source_results = {}

    # console.print(f"\n[bold red]▶ SCAN STARTED[/bold red]  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    # console.print(f"[dim]  Since: {since.strftime('%Y-%m-%d %H:%M')} UTC · Sources: {len(scrapers)} · Images: {'yes' if download_images else 'no'}[/dim]\n")

    safe_print(f"\n>> SCAN STARTED  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    safe_print(f"   Since: ...{len(scrapers)} | Images:...\n")

    all_new_items = []

    for scraper in scrapers:
        # console.print(f"  [yellow]→[/yellow] {scraper.source_name}...", end=" ")
        safe_print(f"  -> {scraper.source_name}...")
        try:
            items = scraper.scrape(since=since)

            # Download images before inserting so image_path is stored immediately
            if downloader and items:
                imgs_dl, imgs_skip = downloader.download_all(items)
                total_imgs += imgs_dl
                console.print(
                    f"[green]{len(items)} scraped[/green]  "
                    f"[dim]{imgs_dl} imgs downloaded · ", end=""
                )
            else:
                # console.print(f"[green]{len(items)} scraped[/green]  [dim]", end="")
                safe_print(f"     {len(items)} scraped | {new} new | {skip} dupes | {imgs_dl} imgs")
            new, skip = db.insert_many(items)
            total_new  += new
            total_skip += skip
            all_new_items.extend(items)
            source_results[scraper.source_name] = {
                "scraped": len(items), "new": new, "skip": skip
            }
            console.print(f"{new} new · {skip} dupes[/dim]")

        except Exception as e:
            source_results[scraper.source_name] = {"error": str(e)}
            # console.print(f"[red]ERROR:[/red] {str(e)!r}")
            err = str(e).replace("[", "(").replace("]", ")")
            safe_print(f"ERROR: {err}")
            logger.exception(f"Scraper {scraper.source_id} failed")

    #console.print(
    #    f"\n[bold green]✓ DONE[/bold green]  "
    #    f"{total_new} new leaks · {total_imgs} images downloaded  "
    #    f"[dim](DB total: {db.count()})[/dim]\n"
    #)
    safe_print(f"\n>> DONE  {total_new} new leaks | {total_imgs} images | DB total: {db.count()}\n")

    return {
        "scanned_at":        datetime.now(timezone.utc).isoformat(),
        "new":               total_new,
        "skipped":           total_skip,
        "images_downloaded": total_imgs,
        "sources":           source_results,
    }


def start_scheduler(db: Database, interval_hours: int = config.DEFAULT_INTERVAL_HOURS):
    console.print(f"[bold]Scheduler started — every {interval_hours}h[/bold]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")
    run_scan(db)
    schedule.every(interval_hours).hours.do(run_scan, db=db)
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)
    except KeyboardInterrupt:
        console.print("\n[yellow]Scheduler stopped.[/yellow]")
"""
"""

# scheduler/runner.py

import logging
import time
from datetime import datetime, timezone, timedelta

import schedule

from database.db import Database
from utils.image_downloader import ImageDownloader
import config

logger = logging.getLogger(**name**)

def log(msg: str):
print(msg, flush=True)

def _get_scrapers() -> list:
    from scrapers.sneakernews       import SneakerNewsScraper
    from scrapers.sneakerbardetroit import SneakerBarDetroitScraper
    from scrapers.others            import (
    SneakerFreakerScraper, HypebeastScraper, KicksOnFireScraper
    )
rss_map = {
"sneakernews":       SneakerNewsScraper,
"sneakerbardetroit": SneakerBarDetroitScraper,
"sneakerfreaker":    SneakerFreakerScraper,
"hypebeast":         HypebeastScraper,
"kicksonfire":       KicksOnFireScraper,
}
scrapers = [
cls() for src in config.SOURCES
if src["enabled"]
for sid, cls in rss_map.items()
if sid == src["id"]
]

if getattr(config, "INSTAGRAM_ENABLED", True):
   try:
       from scrapers.instagram import InstagramScraper
       scrapers.append(InstagramScraper())
   except Exception as e:
       logger.warning(f"Instagram scraper skipped: {e}")

if getattr(config, "GOOGLE_ENABLED", True):
   api_key = getattr(config, "GOOGLE_API_KEY", "")
   cx      = getattr(config, "GOOGLE_CX", "")
   if api_key and cx and "YOUR" not in api_key and len(api_key) > 10:
       try:
           from scrapers.google_search import GoogleSearchScraper
           scrapers.append(GoogleSearchScraper())
       except Exception as e:
           logger.warning(f"Google scraper skipped: {e}")
   else:
       logger.info("Google Images: set GOOGLE_API_KEY + GOOGLE_CX in config.py to enable")

return scrapers

def run_scan(db: Database, since: datetime = None, download_images: bool = True) -> dict:
scrapers   = _get_scrapers()
since      = since or datetime.now(timezone.utc) - timedelta(hours=config.DEFAULT_INTERVAL_HOURS)
downloader = ImageDownloader() if download_images else None

total_new = total_skip = total_imgs = 0
source_results = {}

log(f"\n>> SCAN STARTED  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
log(f"   Since: {since.strftime('%Y-%m-%d %H:%M')} UTC | Sources: {len(scrapers)} | Images: {'yes' if download_images else 'no'}\n")

for scraper in scrapers:
   log(f"  -> {scraper.source_name}...")
   try:
       items = scraper.scrape(since=since)

       imgs_dl = 0
       if downloader and items:
           imgs_dl, _ = downloader.download_all(items)
           total_imgs += imgs_dl

       new, skip  = db.insert_many(items)
       total_new  += new
       total_skip += skip
       source_results[scraper.source_name] = {"scraped": len(items), "new": new, "skip": skip}
       log(f"     {len(items)} scraped | {new} new | {skip} dupes | {imgs_dl} imgs")

   except Exception as e:
       err = str(e).replace("[", "(").replace("]", ")")
       source_results[scraper.source_name] = {"error": str(e)}
       log(f"     ERROR: {err}")
       logger.exception(f"Scraper {scraper.source_id} failed")

log(f"\n>> DONE  {total_new} new leaks | {total_imgs} images | DB total: {db.count()}\n")

return {
   "scanned_at":        datetime.now(timezone.utc).isoformat(),
   "new":               total_new,
   "skipped":           total_skip,
   "images_downloaded": total_imgs,
   "sources":           source_results,
}

def start_scheduler(db: Database, interval_hours: int = config.DEFAULT_INTERVAL_HOURS):
log(f"Scheduler started - every {interval_hours}h. Press Ctrl+C to stop.\n")
run_scan(db)
schedule.every(interval_hours).hours.do(run_scan, db=db)
try:
while True:
schedule.run_pending()
time.sleep(60)
except KeyboardInterrupt:
log("\nScheduler stopped.")
"""


import logging
import time
from datetime import datetime, timezone, timedelta

import schedule
 
from database.db import Database
from utils.image_downloader import ImageDownloader
import config
import time
 
logger = logging.getLogger(__name__)
 
 
def log(msg: str):
    print(msg, flush=True)
 
 
def _get_scrapers() -> list:
    from scrapers.sneakernews import SneakerNewsScraper
    from scrapers.sneakerbardetroit import SneakerBarDetroitScraper
    from scrapers.others import (
            SneakerFreakerScraper, HypebeastScraper, KicksOnFireScraper,
            NiceKicksScraper, FinishLineScraper, SoleCollectorScraper,
            HighsnobietyScraper)

    rss_map = {
        "sneakernews":       SneakerNewsScraper,
        "sneakerbardetroit": SneakerBarDetroitScraper,
        "sneakerfreaker":    SneakerFreakerScraper,
        "hypebeast":         HypebeastScraper,
        "kicksonfire":       KicksOnFireScraper,
        "nicekicks":         NiceKicksScraper,
        "finishline":        FinishLineScraper,
        "solecollector":     SoleCollectorScraper,
        "highsnobiety":      HighsnobietyScraper,
        
    }
 
    scrapers = [
        cls() for src in config.SOURCES
        if src["enabled"]
        for sid, cls in rss_map.items()
        if sid == src["id"]
    ]
 
    if getattr(config, "INSTAGRAM_ENABLED", True):
        try:
            from scrapers.instagram import InstagramScraper
            scrapers.append(InstagramScraper())
        except Exception as e:
            logger.warning(f"Instagram scraper skipped: {e}")
 
    if getattr(config, "GOOGLE_ENABLED", True):
        api_key = getattr(config, "GOOGLE_API_KEY", "")
        cx      = getattr(config, "GOOGLE_CX", "")
        if api_key and cx and "YOUR" not in api_key and len(api_key) > 10:
            try:
                from scrapers.google_search import GoogleSearchScraper
                scrapers.append(GoogleSearchScraper())
            except Exception as e:
                logger.warning(f"Google scraper skipped: {e}")
        else:
            logger.info("Google Images: set GOOGLE_API_KEY + GOOGLE_CX in config.py to enable")
 
    return scrapers
 
 
def run_scan(db: Database, since: datetime = None, download_images: bool = True) -> dict:
    scrapers   = _get_scrapers()
    since      = since or datetime.now(timezone.utc) - timedelta(hours=config.DEFAULT_INTERVAL_HOURS)
    downloader = ImageDownloader() if download_images else None
 
    total_new = total_skip = total_imgs = 0
    source_results = {}
 
    log(f"\n>> SCAN STARTED  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log(f"   Since: {since.strftime('%Y-%m-%d %H:%M')} UTC | Sources: {len(scrapers)} | Images: {'yes' if download_images else 'no'}\n")
 
    for scraper in scrapers:
        log(f"  -> {scraper.source_name}...")
        try:
            items   = scraper.scrape(since=since)
            imgs_dl = 0
 
            if downloader and items:
                imgs_dl, _ = downloader.download_all(items)
                total_imgs += imgs_dl
 
            new, skip   = db.insert_many(items)
            total_new  += new
            total_skip += skip
 
            source_results[scraper.source_name] = {"scraped": len(items), "new": new, "skip": skip}
            log(f"     {len(items)} scraped | {new} new | {skip} dupes | {imgs_dl} imgs")
 
        except Exception as e:
            err = str(e).replace("[", "(").replace("]", ")")
            source_results[scraper.source_name] = {"error": str(e)}
            log(f"     ERROR: {err}")
            logger.exception(f"Scraper {scraper.source_id} failed")
 
    log(f"\n>> DONE  {total_new} new leaks | {total_imgs} images | DB total: {db.count()}\n")
 
    return {
        "scanned_at":        datetime.now(timezone.utc).isoformat(),
        "new":               total_new,
        "skipped":           total_skip,
        "images_downloaded": total_imgs,
        "sources":           source_results,
    }
 
 
def start_scheduler(db: Database, interval_hours: int = config.DEFAULT_INTERVAL_HOURS):
    log(f"Scheduler started - every {interval_hours}h. Press Ctrl+C to stop.\n")
 
    run_scan(db)  # immediate first run
 
    schedule.every(interval_hours).hours.do(run_scan, db=db)
 
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)
    except KeyboardInterrupt:
        log("\nScheduler stopped.")
 
