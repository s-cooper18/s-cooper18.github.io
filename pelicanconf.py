AUTHOR = 'Suzannah Cooper'
SITENAME = 'Suzannah Cooper'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Australia/Brisbane'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
)

DEFAULT_PAGINATION = 10

CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
CHECK_MODIFIED_METHOD = "md5"
GZIP_CACHE = False
CONTENT_CACHING_LAYER = "generator"
WITH_FUTURE_DATES = False
CACHE_PATH = "__cache__"
OUTPUT_PATH = "__output__"
