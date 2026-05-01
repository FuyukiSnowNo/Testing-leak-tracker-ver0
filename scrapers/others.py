# scrapers/sneakerfreaker.py
from scrapers.base import BaseScraper

class SneakerFreakerScraper(BaseScraper):
    source_id   = "sneakerfreaker"
    source_name = "Sneaker Freaker"
    rss_url     = "https://www.sneakerfreaker.com/feed"
    base_url    = "https://www.sneakerfreaker.com"


# scrapers/hypebeast.py
from scrapers.base import BaseScraper

class HypebeastScraper(BaseScraper):
    source_id   = "hypebeast"
    source_name = "Hypebeast"
    rss_url     = "https://hypebeast.com/footwear/feed"
    base_url    = "https://hypebeast.com/footwear"


# scrapers/kicksonfire.py
from scrapers.base import BaseScraper

class KicksOnFireScraper(BaseScraper):
    source_id   = "kicksonfire"
    source_name = "Kicks on Fire"
    rss_url     = "https://www.kicksonfire.com/feed/"
    base_url    = "https://www.kicksonfire.com"


# scrapers/others.py
from scrapers.base import BaseScraper
 
class SneakerFreakerScraper(BaseScraper):
    source_id   = "sneakerfreaker"
    source_name = "Sneaker Freaker"
    rss_url     = "https://news.google.com/rss/search?q=sneakerfreaker.com+sneaker&hl=en-US&gl=US&ceid=US:en"
    base_url    = "https://www.sneakerfreaker.com"
 
 
class HypebeastScraper(BaseScraper):
    source_id   = "hypebeast"
    source_name = "Hypebeast"
    rss_url     = "https://hypebeast.com/footwear/feed"
    base_url    = "https://hypebeast.com"
 
 
class KicksOnFireScraper(BaseScraper):
    source_id   = "kicksonfire"
    source_name = "Kicks on Fire"
    rss_url     = "https://www.kicksonfire.com/feed/"
    base_url    = "https://www.kicksonfire.com"
 
 
class NiceKicksScraper(BaseScraper):
    source_id   = "nicekicks"
    source_name = "Nice Kicks"
    rss_url     = "https://nicekicks.com/feed/"
    base_url    = "https://nicekicks.com"
 
 
class FinishLineScraper(BaseScraper):
    source_id   = "finishline"
    source_name = "Finish Line"
    rss_url     = "https://blog.finishline.com/feed/"
    base_url    = "https://blog.finishline.com"
 
 
class SoleCollectorScraper(BaseScraper):
    source_id   = "solecollector"
    source_name = "Sole Collector"
    rss_url     = "https://solecollector.com/rss"
    base_url    = "https://solecollector.com"
 
 
class HighsnobietyScraper(BaseScraper):
    source_id   = "highsnobiety"
    source_name = "Highsnobiety"
    rss_url     = "https://www.highsnobiety.com/feed/"
    base_url    = "https://www.highsnobiety.com"


