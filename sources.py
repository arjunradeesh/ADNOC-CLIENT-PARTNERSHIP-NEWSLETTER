"""
Source definitions for the ADNOC Partnership News scraper.

Each source has:
  section : which bulletin section it feeds
  name    : the publisher name shown in the bulletin (e.g. "BBC Sport")
  kind    : "direct"  -> a normal RSS feed (we get the real article link + can fetch body text)
            "gnews"   -> Google News RSS, UAE edition (used for sites that block scrapers)
  url      : (direct) the RSS feed URL
  query    : (gnews)  the Google News search query
  lang     : (gnews, optional) "ar" for an Arabic search; default English
  wide     : (gnews)  True for searches across all publishers — each story then shows
             its real publisher instead of the search's name, and Claude checks each
             headline is relevant before summarising it
  title_filter : (optional) list of names; a result is kept only if its headline
             contains one of them as a whole word (case-sensitive)
  max      : (optional) most stories kept from this source per run

Sections are listed in SECTION_ORDER, which is the fixed order they appear in the bulletin.
Section names must match EDITORIAL_GUIDE.md and SUMMARY_STYLE.md exactly.
"""

# Fixed order the sections appear in the bulletin.
SECTION_ORDER = [
    "ADNOC & Partner News",
    "Competitor News",
    "Wider Sports News",
    "Formula 1 & Motorsport",
    "Cycling",
    "UAE Pro League & GCC Football",
    "Running & Endurance",
]

# Sections that have been renamed or merged, so older saved stories move across.
SECTION_RENAMES = {}

# How many hours back each run collects. Runs are daily; the archive keeps
# KEEP_DAYS (14, set in the workflow) so a bi-weekly edition has the full fortnight.
DEFAULT_WINDOW_HOURS = 48

ADNOC_NAMES = ["ADNOC", "Adnoc", "XRG", "أدنوك"]

SOURCES = [
    # ---- Wider Sports News: trade press ----
    {"section": "Wider Sports News", "name": "Sportcal",       "kind": "gnews",  "query": "site:sportcal.com"},
    {"section": "Wider Sports News", "name": "SportsPro",      "kind": "direct", "url": "https://www.sportspro.com/feed/"},
    {"section": "Wider Sports News", "name": "Sport Industry", "kind": "direct", "url": "https://sportindustry.co.uk/feed/"},
    {"section": "Wider Sports News", "name": "SportBusiness",  "kind": "direct", "url": "https://www.sportbusiness.com/feed/"},

    # ---- Wider Sports News: Gulf outlets ----
    {"section": "Wider Sports News", "name": "The National",   "kind": "gnews", "max": 10,
     "query": "site:thenationalnews.com/sport (sponsorship OR partnership OR deal OR rights OR hosting)"},
    {"section": "Wider Sports News", "name": "Arab News",      "kind": "gnews", "max": 8,
     "query": "site:arabnews.com/sport (sponsorship OR partnership OR deal OR rights OR hosting)"},

    # ---- Formula 1 & Motorsport ----
    {"section": "Formula 1 & Motorsport", "name": "BBC Sport",    "kind": "direct", "url": "https://feeds.bbci.co.uk/sport/formula1/rss.xml"},
    {"section": "Formula 1 & Motorsport", "name": "Autosport",    "kind": "gnews",  "query": "site:autosport.com f1"},
    {"section": "Formula 1 & Motorsport", "name": "Motorsport.com", "kind": "gnews", "query": "site:motorsport.com f1"},

    # ---- Cycling ----
    {"section": "Cycling", "name": "BBC Sport",   "kind": "direct", "url": "https://feeds.bbci.co.uk/sport/cycling/rss.xml"},
    {"section": "Cycling", "name": "Cyclingnews", "kind": "gnews",  "query": "site:cyclingnews.com"},

    # ---- UAE Pro League & GCC Football ----
    {"section": "UAE Pro League & GCC Football", "name": "The National", "kind": "gnews",
     "query": "site:thenationalnews.com/sport/football"},

    # ---- Safety-net searches across ALL of Google News -------------------------
    # These catch ADNOC-property stories in less obvious outlets. Kept tight to
    # ADNOC's actual properties and capped with "max".
    {"section": "ADNOC & Partner News", "name": "ADNOC watch", "kind": "gnews", "max": 10, "wide": True,
     "title_filter": ADNOC_NAMES,
     "query": 'ADNOC (sport OR sponsorship OR partnership OR "Grand Prix" OR marathon OR cycling '
              'OR "Pro League" OR "Gold Cup" OR triathlon) when:2d'},
    {"section": "ADNOC & Partner News", "name": "XRG watch", "kind": "gnews", "max": 6, "wide": True,
     "title_filter": ADNOC_NAMES,
     "query": '"XRG" ("UAE Team Emirates" OR sponsorship OR sport) when:2d'},
    {"section": "ADNOC & Partner News", "name": "ADNOC watch (Arabic)", "kind": "gnews", "max": 8, "wide": True,
     "lang": "ar", "title_filter": ADNOC_NAMES,
     "query": "أدنوك (رعاية OR رياضة OR شراكة OR ماراثون OR دوري) when:2d"},

    {"section": "Formula 1 & Motorsport", "name": "Abu Dhabi GP watch", "kind": "gnews", "max": 8, "wide": True,
     "query": '"Abu Dhabi Grand Prix" OR "Yas Marina" when:2d'},
    {"section": "Formula 1 & Motorsport", "name": "Rashid Al Dhaheri watch", "kind": "gnews", "max": 5, "wide": True,
     "query": '"Rashid Al Dhaheri" when:2d'},
    {"section": "Formula 1 & Motorsport", "name": "Feeder series watch", "kind": "gnews", "max": 8, "wide": True,
     "query": '"FIA Formula 3" OR "FIA Formula 2" OR "F1 Academy" OR "F4 UAE" OR "Formula Regional Middle East" when:2d'},

    {"section": "Cycling", "name": "UAE Team Emirates watch", "kind": "gnews", "max": 10, "wide": True,
     "query": '"UAE Team Emirates" OR Pogacar OR "UAE Tour" when:2d'},

    {"section": "UAE Pro League & GCC Football", "name": "Pro League watch", "kind": "gnews", "max": 12, "wide": True,
     "query": '"ADNOC Pro League" OR "UAE Pro League" when:2d'},
    {"section": "UAE Pro League & GCC Football", "name": "Pro League watch (Arabic)", "kind": "gnews", "max": 10,
     "wide": True, "lang": "ar",
     "query": '"دوري أدنوك للمحترفين" when:2d'},

    {"section": "Running & Endurance", "name": "Marathon watch", "kind": "gnews", "max": 8, "wide": True,
     "query": '"Abu Dhabi Marathon" OR "Dubai Marathon" OR "RAK Half Marathon" OR "Challenge Sir Bani Yas" when:2d'},

    # ---- Wider Google searches per section ------------------------------------
    # Broad searches to catch what the fixed sources miss. They bring in noise too,
    # so Claude checks every headline against EDITORIAL_GUIDE.md before summarising.
    {"section": "Wider Sports News", "name": "Sports business search", "kind": "gnews", "max": 15, "wide": True,
     "query": '(sport OR sports) (sponsorship OR "media rights" OR "broadcast rights" OR "naming rights" '
              'OR "commercial partner" OR "title partner") when:1d'},
    {"section": "Wider Sports News", "name": "Gulf sports business search", "kind": "gnews", "max": 12, "wide": True,
     "query": '(UAE OR "Abu Dhabi" OR Dubai OR Saudi OR Qatar) sport (sponsorship OR partnership '
              'OR "naming rights" OR hosting) when:2d'},
    {"section": "Formula 1 & Motorsport", "name": "F1 search", "kind": "gnews", "max": 15, "wide": True,
     "query": '"Formula 1" OR F1 (team OR driver OR "Grand Prix") when:1d'},
    {"section": "Cycling", "name": "Cycling search", "kind": "gnews", "max": 12, "wide": True,
     "query": 'cycling ("WorldTour" OR "Tour de France" OR Giro OR Vuelta OR UCI) when:1d'},
    {"section": "UAE Pro League & GCC Football", "name": "GCC football search", "kind": "gnews", "max": 15, "wide": True,
     "query": '"Saudi Pro League" OR "AFC Champions League" OR "Qatar Stars League" OR "Al Ain" '
              'OR "Shabab Al Ahli" OR "Al Wahda" OR "Al Jazira" when:2d'},
]

# ---- Competitor News --------------------------------------------------------
# The brands ADNOC is benchmarked against, doing sponsorship or partnership deals
# in sport. One Google News search per brand (grouped searches miss real stories).
# Each entry: (name, Google search terms, names that must appear in the headline,
#              whether the search also needs a deal word, not just a sport word).
# Add, remove or edit brands here, and keep the list in SUMMARY_STYLE.md in step.
COMPETITORS = [
    # Energy peers
    ("Aramco",        'Aramco',                                          ["Aramco"],                       False),
    ("TotalEnergies", 'TotalEnergies',                                   ["TotalEnergies"],                False),
    ("Shell",         'Shell',                                           ["Shell"],                        False),
    ("Petronas",      'Petronas',                                        ["Petronas", "PETRONAS"],         False),
    ("ExxonMobil",    'ExxonMobil OR "Mobil 1"',                         ["ExxonMobil", "Mobil 1"],        False),
    # UAE sponsorship peers. Brands with events named after them (DP World Tour,
    # Mubadala Citi DC Open) need a deal word too, or tournament results flood in.
    ("Emirates",      '"Emirates airline" OR "Fly Emirates" OR "Emirates Group"',
                                                                         ["Emirates airline", "Fly Emirates", "Emirates Group"], False),
    ("e&",            'Etisalat OR "e& UAE" OR "e& life"',               ["e&", "Etisalat"],               False),
    ("DP World",      '"DP World"',                                      ["DP World"],                     True),
    ("Aldar",         'Aldar',                                           ["Aldar"],                        False),
    ("Mubadala",      'Mubadala',                                        ["Mubadala"],                     True),
]
_SPORT = ('sport OR sports OR football OR soccer OR tennis OR golf OR cricket OR NBA OR NFL OR MLS '
          'OR Olympics OR cycling OR stadium OR F1 OR "Formula 1" OR motorsport OR padel OR esports')
_DEAL = ('sponsorship OR sponsor OR partnership OR "official partner" OR "naming rights" OR "jersey patch" '
         'OR "presenting partner" OR "title sponsor" OR "title partner" OR ambassador')
_NOISE = ('-earnings -shares -stock -"price target" -dividend -barrels -crude -"oil price" '
          '-refinery -LNG -profit')
for _name, _terms, _aliases, _deal_only in COMPETITORS:
    _context = f"({_DEAL})" if _deal_only else f"({_SPORT} OR {_DEAL})"
    SOURCES.append({
        "section": "Competitor News",
        "name": f"{_name} search",
        "kind": "gnews",
        "wide": True,
        "max": 8,
        "title_filter": _aliases,
        "query": f"({_terms}) {_context} {_NOISE} when:2d",
    })
