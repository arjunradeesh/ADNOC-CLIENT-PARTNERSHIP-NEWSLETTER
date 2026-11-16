# ADNOC Partnership News: summary bullet style

These are the rules Claude follows when it writes the two bullets for each story.
Edit this file to change the style. No code changes are needed.

## The two bullets

- Exactly **two bullets** per story, **100–150 words in total** across both.
- Each bullet is two to three sentences: fact-dense and closely paraphrased from the article.
- Keep the specific figures, names, dates, venues, competitions and deal lengths.
- **Bullet one** covers the core news: who, what, when, and the key numbers.
- **Bullet two** covers a different angle from the same story, such as background, context, what happens next, or a quote paraphrased into reported speech.
- British English spelling.
- No editorialising, hype or opinion ("huge", "stunning", "massive boost"). Report the facts.
- Don't start a bullet with the headline repeated back.
- Use only facts from the article itself. Never invent or guess details.
- **Arabic articles:** write the bullets in English. Keep names in their usual English spelling (Al Ain, Shabab Al Ahli, Hazza bin Zayed Stadium).
- **ADNOC naming:** write "ADNOC" in capitals. ADNOC is the founding partner of the Abu Dhabi Grand Prix; never describe it as an F1 team sponsor. If an article gets ADNOC's role wrong, report what the article says and don't repeat the error as fact.

## Example

Headline: *UAE Pro League and ADNOC extend partnership until 2029* (Sharjah24)

1. ADNOC and the UAE Pro League have renewed their title partnership for three more seasons, keeping the ADNOC name on the league until 2029. The extension was announced at Al Ain FC's championship ceremony at Hazza bin Zayed Stadium, after the club won the 2025-26 ADNOC Pro League title.
2. The announcement was made in the presence of Dr Sultan Ahmed Al Jaber, Minister of Industry and Advanced Technology and ADNOC Managing Director and Group CEO. Both parties framed the renewal around promoting sport, wellbeing and active lifestyles in the UAE, and around the continued development of the domestic league.

## Competitor News: what counts

Competitor News tracks **these brands only** doing sponsorship or partnership deals in
**sport**, anywhere in the world. They are the brands ADNOC is benchmarked against:

- **Energy peers:** Aramco, TotalEnergies, Shell, Petronas, ExxonMobil
- **UAE sponsorship peers:** Emirates, e& (formerly Etisalat), DP World, Aldar, Mubadala

Examples of stories that belong:

- FIFA signs four-year worldwide partnership deal with Saudi Aramco
- Saudi Arabia sports sponsorship: Fifa, F1 and ICC challenged over Aramco deals
- Al Ahly renew partnership with global energy company Shell
- ExxonMobil lands deals with three NBA teams
- TotalEnergies Qatar named official sponsor of FIP World Cup Qatar 2026

**Named events are not deals.** A story about an event or competition that carries the
brand's name (DP World Tour golf results, the Mubadala Citi DC Open draw, Aramco Team
Series scores) only counts if it's about the sponsorship itself: a new or renewed title
deal, an exit, or an activation.

New deals, renewals, extensions, exits and activations all count. Stories about any other
company, takeovers, earnings and general energy or business news don't count.

**ADNOC's own deals are not competitor news.** They belong in ADNOC & Partner News,
for example:

- UAE Pro League and ADNOC extend partnership until 2029
- Abu Dhabi Grand Prix retains ADNOC as key partner under new extension
- Abu Dhabi Turf Club, ADNOC sign three-year sponsorship agreement for inaugural Abu Dhabi Gold Cup

**For every story in every section**, set `"competitor": true` if the story is
mainly about a listed brand's sports deal. It will then be moved into Competitor News.
For example, a Sportcal story in Wider Sports News about Emirates renewing a club
sponsorship should be flagged. Never flag a story that is mainly about ADNOC or XRG.

## When to skip a story

Mark a story as skipped (no bullets) if any of these apply:
- It isn't a real news article, for example a video page, gallery, live blog, podcast, product review, betting tips, racecards or a homepage.
- **ADNOC & Partner News** only: the story is about ADNOC's oil, gas, finance, trading or corporate news rather than sport, sponsorship or community sport programmes.
- **Competitor News** only: the story doesn't meet the definition above.
- **Wider Sports News** only: the story isn't about sport or the business of sport (rights, sponsorship, media, events, governing bodies). General business, politics or lifestyle pieces are skipped.
- Any section: the story falls under "Never included" or a section's "Drop" list in EDITORIAL_GUIDE.md.

## The Bigger Game extras

The Bigger Game is ADNOC's sports and partnership newsletter. As well as the two
bullets, Claude drafts these for every story it summarises. They are first drafts:
the team edits them on the page before sending.

- **label:** one to three words in capitals naming the topic, used as the row label
  in "The week in 60 seconds". Prefer these: PRO LEAGUE, GCC FOOTBALL, F1, F1 BUSINESS,
  MOTORSPORT, CYCLING, RUNNING, GOLF, SPORTS BUSINESS, COMPETITORS, ADNOC. Use another
  short label only if none fit.
- **line:** one sentence, 25 words at most, that gives the whole story at a glance for
  "The week in 60 seconds". Lead with the fact and keep the key number or date,
  Put [square brackets] around the three to six words that should link to the article,
  e.g. "[Al Jazira beat Al Wasl 2-1] to go top of the ADNOC Pro League on 17 points."
- **angle:** one sentence, 30 words at most, on what the story means for ADNOC or
  its properties. Practical, not promotional. Used if the story becomes "Watch this".
- **activation:** only when the story describes a brand activation, campaign or fan
  experience that ADNOC could learn from. Otherwise null.
  - **title:** the brand and the event, five words at most, e.g. "Shell, São Paulo GP".
  - **what:** what the brand did, 20 words at most.
  - **borrow:** how ADNOC could borrow the idea for one of its own properties (Abu Dhabi
    Grand Prix, ADNOC Pro League, ADNOC Abu Dhabi Marathon, UAE Team Emirates XRG),
    15 words at most, starting with a verb, e.g. "race week that drives people to
    ADNOC stations, not just the track."
- **stat:** only when the story has a striking number worth a stat box. Otherwise null.
  - **value:** the number on its own, as short as possible: "17", "$2m", "–23", "3".
  - **label:** eight words at most saying what the number is, e.g. "points: Al Jazira
    top the ADNOC Pro League".

### The edition draft

Once per run, Claude also drafts the edition's editorial parts from the best stories:

- **headline:** two short parts, together 10 words at most. The first part states what
  happened, the second what comes next, e.g. "The double is done." + "Abu Dhabi is next."
  Punchy and factual. No puns that need explaining, no hype words.
- **stats:** four stat boxes, each from a different story, using that story's facts.
- **watch:** the one story ADNOC most needs to know about or act on. A bold lead
  sentence (15 words at most) and one or two more sentences (40 words at most) on why
  it matters for ADNOC. Put [square brackets] around the source's name or the words
  that should link to the article.
