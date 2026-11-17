# Client-Partnership-Newsletter-ADNOC

A small tool that collects the day's sports-business news from your usual sources and
has Claude write **two summary bullets (100–150 words)** for every story. The team
then picks the stories they want and copies a ready-formatted bulletin into an email.

## How it works (plain English)

1. **`scrape.py`** visits every source in `sources.py`: fixed news feeds, broad Google
   searches for each section, and one search per competitor brand (energy and UAE sponsorship peers). Claude checks the
   broad-search headlines against **`EDITORIAL_GUIDE.md`** and drops noise and
   duplicates. The collector then turns Google News links back into real article links,
   reads each kept article, and saves the stories to **`data/news.json`**. Stories still
   waiting for bullets go into `data/pending.json`.
2. **`summarise.py`** sends the waiting stories to Claude, which writes the two bullets
   following **`SUMMARY_STYLE.md`**. Claude also flags off-topic stories, such as
   Competitor News that isn't really about a competitor's sports deal.
3. **`index.html`** is the web page the team uses: pick stories, tweak bullets, then
   click **Copy newsletter**.
4. A **GitHub Action** (`.github/workflows/scrape.yml`) runs steps 1 and 2 at
   **08:50 and 09:45 UAE time** every day. GitHub sometimes starts scheduled runs 5–30 minutes late.

## The Bigger Game (the newsletter)

The page builds **The Bigger Game**, ADNOC's sports and partnership newsletter, in the
house layout: headline, four stat boxes, Watch this, The week in 60 seconds,
The business end (up to three sports-business deals), Activations worth stealing
and On the radar.

- **Claude drafts the words** on every run: a one-line summary, a row label, an ADNOC
  angle, a "Borrow" idea for activations and a stat for each story, plus the edition's
  headline, four stats and Watch this. The rules are in `SUMMARY_STYLE.md`
  ("The Bigger Game extras").
- **On the radar** comes from `radar.json`. Add upcoming events there (start and end
  dates, event name, and `"adnoc": true` for ADNOC's own properties). Past dates drop
  off by themselves.
- **Your edition is saved in your browser** until you click **Start new edition**, so you
  can build a bi-weekly edition over several days.
- In the email, links are the words in [square brackets]; with no brackets the source
  name is linked at the end of the line.

## Using it each morning

1. Open the page (your GitHub Pages link).
2. **Pick stories:** on each story, click where it goes: **60 seconds**, **Business**, **Activation**, **Watch this** or **Stat**. The live preview on the right
   shows exactly what will paste.
3. Edit any text in **Edit & preview**. A story marked **No draft yet** couldn't be read
   automatically: open the article and type two bullets.
4. Open **Edit & preview**, check Claude's drafts, then click **Copy newsletter** and paste into a new email.

Your edition is saved in your own browser until you click **Start new edition**.

## One-off setup: the Claude token

The summaries run on your Claude subscription (Pro or Max) and need no separate API bill.

1. In Terminal, run `claude setup-token` and follow the sign-in steps. It prints a long token.
2. On GitHub, open the repo → **Settings → Secrets and variables → Actions →
   New repository secret**. Name: `CLAUDE_CODE_OAUTH_TOKEN`. Value: the token.

## Changing things

- **Sources:** edit `sources.py`. Each source is either a direct RSS feed
  (`"kind": "direct"`) or a Google News search (`"kind": "gnews"`).
- **Bullet style:** edit `SUMMARY_STYLE.md`.
- **What gets kept or dropped:** edit `EDITORIAL_GUIDE.md`. Pasting in past bulletins
  as examples makes the judgement better.
- **Competitor brands:** edit `COMPETITORS` in `sources.py` and the list in `SUMMARY_STYLE.md`.
- **Section names** must match exactly across `sources.py`, `EDITORIAL_GUIDE.md` and `SUMMARY_STYLE.md`.
- **Which Claude model:** set `SUMMARY_MODEL` in the workflow (default `sonnet`).

## Running it yourself (optional)

```bash
pip install -r requirements.txt
python3 scrape.py          # collects stories
python3 summarise.py       # writes the bullets (needs the claude command, signed in)
python3 -m http.server     # then open http://localhost:8000

## Brand colour and font

- **Colour:** ADNOC Royal Blue `#0047BA`, set as `--brand` at the top of `index.html`.
- **Font:** the page uses ADNOC's brand font if the viewer has it installed, or if the
  font files are in a `fonts/` folder (`fonts/adnoc-regular.woff2`, `fonts/adnoc-bold.woff2`).
  Otherwise it falls back to IBM Plex Sans, which also covers Arabic headlines.
  Check the font's exact installed name and put it in the `local("...")` lines in `index.html`.
- **Don't upload the font files while this repo is public.** Brand fonts are licensed,
  and anything in a public repo can be downloaded by anyone. Ask ADNOC's brand team what
  the licence allows first.
