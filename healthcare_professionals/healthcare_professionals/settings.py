# Scrapy settings for healthcare_professionals project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'healthcare_professionals'

SPIDER_MODULES = ['healthcare_professionals.spiders']
NEWSPIDER_MODULE = 'healthcare_professionals.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
#     'Connection': 'keep-alive',
#     'Host': 'www.eventscribe.com',
#     'Referer': 'https://www.eventscribe.com/2018/ADEA/speakers.asp?h=Browse%20By%20Speaker',
# }
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive",
    "Cookie": "AUTH_SESSION=mPYzn2pphJFj3FcKB8K1P8MPEIy-70jGXHLNQz2C2Zw; _gcl_au=1.1.1789204358.1674680995; _ga_MP4MYK7MMT=GS1.1.1674687935.2.1.1674687940.0.0.0; _ga=GA1.1.521731209.1674680997; __veroc4=^%^5B^%^7B^%^22command^%^22^%^3A^%^5B^%^22events_track^%^22^%^2C^%^22Visited^%^20site^%^22^%^2C^%^7B^%^22userAgent^%^22^%^3A^%^22Mozilla^%^2F5.0^%^20^%^28Windows^%^20NT^%^2010.0^%^3B^%^20Win64^%^3B^%^20x64^%^3B^%^20rv^%^3A109.0^%^29^%^20Gecko^%^2F20100101^%^20Firefox^%^2F110.0^%^22^%^2C^%^22platform^%^22^%^3A^%^22Win32^%^22^%^2C^%^22language^%^22^%^3A^%^22en-US^%^22^%^7D^%^2C^%^7B^%^22time^%^22^%^3A1674680997076^%^2C^%^22order^%^22^%^3A1^%^7D^%^5D^%^2C^%^22job_id^%^22^%^3A^%^221674680997075_4058^%^22^%^7D^%^5D; __vero_visit=true; mixpanel-events={^%^22s^%^22:1674687935126^%^2C^%^22u^%^22:^%^22/pesquisa?q=Ginecologista&loc=&filters^%^255Bspecializations^%^255D^%^255B0^%^255D=36&page=1^%^22^%^2C^%^22p^%^22:^%^22/search_results_visits_new^%^22^%^2C^%^22r^%^22:^%^22^%^22}",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "TE": "trailers"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'healthcare_professionals.middlewares.HealthcareProfessionalsSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'healthcare_professionals.middlewares.HealthcareProfessionalsDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'healthcare_professionals.pipelines.HealthcareProfessionalsPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
HTTPCACHE_ENABLED = False
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.DbmCacheStorage'

FEED_EXPORT_ENCODING = "utf-8"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
