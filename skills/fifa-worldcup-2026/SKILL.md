---
name: fifa-worldcup-2026
description: FIFA World Cup 2026 content creation system. Covers news scraping, viral script writing, royalty-free media sourcing, FFmpeg video assembly, and YouTube publishing. Use when creating automated soccer/FIFA content for YouTube channels.
origin: ECC
---

# When to Activate

- User wants to create FIFA or soccer YouTube content automatically
- User asks to run the FIFA content pipeline
- User wants to post World Cup 2026 hype videos without manual work
- User mentions `/fifa-content` command
- Debugging any component of the FIFA automation pipeline

# Pipeline Architecture

```
scripts/fifa/
├── index.js          ← orchestrator (run this)
├── scheduler.js      ← cron daemon (runs daily)
├── setup.js          ← one-time YouTube OAuth setup
├── config.js         ← env var loader + validator
├── .env              ← your API keys (copy from .env.example)
└── lib/
    ├── newsScraper.js    ← RSS + NewsAPI multi-source scraping
    ├── scriptWriter.js   ← Claude API → structured video script
    ├── mediaFinder.js    ← Pexels + Pixabay royalty-free media
    ├── imageGenerator.js ← Stability AI fallback image generation
    ├── ttsNarrator.js    ← ElevenLabs / OpenAI TTS audio
    ├── videoBuilder.js   ← FFmpeg slideshow + text overlay assembly
    └── youtubeUploader.js← YouTube Data API v3 OAuth2 upload
```

# Setup (One-Time)

## Step 1 — Install dependencies
```bash
cd scripts/fifa
npm install
```

## Step 2 — Configure API keys
```bash
cp .env.example .env
# Edit .env and fill in your keys
```

Required keys:
| Key | Where to get | Cost |
|-----|-------------|------|
| `ANTHROPIC_API_KEY` | console.anthropic.com | Pay-per-use |
| `YOUTUBE_CLIENT_ID` + `SECRET` | console.cloud.google.com → YouTube Data API v3 | Free quota |
| `PEXELS_API_KEY` | pexels.com/api | Free |

Optional (each adds capability):
| Key | Adds |
|-----|------|
| `PIXABAY_API_KEY` | More stock image sources |
| `NEWS_API_KEY` | Broader news from 80,000+ sources |
| `ELEVENLABS_API_KEY` | Premium AI voice narration |
| `OPENAI_API_KEY` | OpenAI TTS narration fallback |
| `STABILITY_API_KEY` | AI image generation when stock fails |

## Step 3 — Authorize YouTube
```bash
node scripts/fifa/setup.js
# Opens browser → paste auth code → saves refresh token
```

## Step 4 — Run once to verify
```bash
node scripts/fifa/index.js --skip-upload
# Builds video locally without uploading
```

## Step 5 — Start the scheduler
```bash
node scripts/fifa/scheduler.js
# Runs at noon UTC daily by default (configure SCHEDULE_CRON)
```

# Command Reference

```bash
# Full pipeline (news → script → media → video → upload)
node scripts/fifa/index.js

# Build video only, skip YouTube upload
node scripts/fifa/index.js --skip-upload

# Force short format (YouTube Shorts, <60s)
node scripts/fifa/index.js --format=short

# Force long format (7-10 minute video)
node scripts/fifa/index.js --format=long

# Automated scheduling (stays running, uses SCHEDULE_CRON)
node scripts/fifa/scheduler.js

# View run history
cat scripts/fifa/data/history.json
```

# News Sources

The scraper pulls from these RSS feeds automatically:
- BBC Sport Football — `feeds.bbci.co.uk/sport/football/rss.xml`
- The Guardian Football — `theguardian.com/football/rss`
- Sky Sports Football — `skysports.com/rss/12040`
- ESPN Soccer — `espn.com/espn/rss/soccer/news`
- Goal.com — `goal.com/en/news/feed`
- NewsAPI.org — if `NEWS_API_KEY` is set (80,000+ sources)

Articles are scored by keyword relevance + recency and the top 5 are passed to Claude.

# Script Generation Prompts

Claude (opus) receives the top news articles and writes a JSON-structured script. The system prompt instructs it to:

1. Pick the single most compelling angle from the news
2. Write in punchy YouTube creator voice (energy level: 9/10)
3. Structure: Hook → Context → Deep Dive → Hot Take → CTA
4. Choose format automatically: Short for news/reactions, Long for analysis
5. Include `searchQuery` per scene for media sourcing

The JSON output drives every downstream step (media search terms, video durations, YouTube metadata).

# Media Sourcing Strategy

For each scene, `mediaFinder.js` searches:

**Pexels** (primary):
```
GET /v1/search?query={scene.searchQuery}&per_page=3&orientation=landscape
GET /videos/search?query={scene.searchQuery}&per_page=2
```

**Pixabay** (fallback):
```
GET /api/?key=...&q={scene.searchQuery}&image_type=photo&category=sports
```

**AI generation** (last resort, requires Stability AI key):
```
POST /v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image
prompt: "Professional sports photography, {visualDescription}, FIFA World Cup 2026, 4K"
```

Downloaded files land in `scripts/fifa/temp/media/` and are auto-cleaned on each run.

# Video Assembly Details

`videoBuilder.js` uses `fluent-ffmpeg` with the bundled `ffmpeg-static` binary (no system FFmpeg required).

Per-scene pipeline:
1. Scale image → target resolution with letterbox padding
2. `drawbox` — semi-transparent black bar at bottom 200px
3. `drawtext` — wrapped white text with drop shadow, centered in box
4. Export ~5-15 second MP4 clip

Concatenate via concat demuxer → final video.

If audio: mix TTS narration with `-shortest` flag.

Output formats:
- **Landscape** 1920×1080 (standard YouTube): `format: "long"`
- **Vertical** 1080×1920 (YouTube Shorts): `format: "short"`

# YouTube Upload Metadata

```json
{
  "snippet": {
    "title": "<Claude-generated title>",
    "description": "<Claude-generated multi-paragraph description + hashtags>",
    "tags": ["FIFA", "World Cup 2026", "soccer", "football", ...],
    "categoryId": "17"
  },
  "status": {
    "privacyStatus": "public",
    "selfDeclaredMadeForKids": false
  }
}
```

Custom thumbnail (1280×720) is set immediately after upload via `thumbnails.set`.

# Troubleshooting

| Problem | Fix |
|---------|-----|
| `No YouTube token found` | Run `node scripts/fifa/setup.js` |
| `Pexels returned no results` | Add `PIXABAY_API_KEY` or `STABILITY_API_KEY` as fallback |
| `FFmpeg error: no such file` | `npm install` in scripts/fifa to get ffmpeg-static |
| `Script writer returned invalid JSON` | Claude occasionally wraps JSON in markdown — the extractor handles this, but retry once if it fails |
| `YouTube quota exceeded` | Free tier allows ~6 uploads/day. Reduce `SCHEDULE_CRON` frequency |
| `News score all zero` | Sources may be down. Check network, try again in 1h |

# FIFA 2026 Quick Facts for Scripts

- **Dates**: June 11 – July 19, 2026
- **Hosts**: USA (11 cities), Mexico (3), Canada (2)
- **Teams**: 48 (up from 32 in 2022)
- **Matches**: 104 (up from 64)
- **Final**: MetLife Stadium, New Jersey (82,500 capacity)
- **Format**: 12 groups of 4 → Round of 32 → knockout

**Players to hype:**
- Lionel Messi (Argentina) — 38 at tournament, defending champion, almost certain farewell
- Cristiano Ronaldo (Portugal) — 41, all-time top scorer, last shot at glory
- Kylian Mbappe (France) — 27, peak years, heavy favorite
- Erling Haaland (Norway) — 25, could be a qualifier surprise
- Vinicius Jr (Brazil) — 25, Ballon d'Or winner, Brazil's hope
- Jude Bellingham (England) — 22, carrying England's dreams

**Dark horses to spotlight:**
- Morocco (first African semi-finalist in 2022, improving squad)
- Japan (world-class club players, tactical excellence)
- USA (home advantage, rising MLS and European talent pool)
- Ecuador, Senegal, South Korea

# Scheduling Examples

```bash
# Daily at noon UTC (default)
SCHEDULE_CRON="0 12 * * *"

# Twice daily — morning and evening
SCHEDULE_CRON="0 8,20 * * *"

# Every 6 hours (max YouTube quota usage)
SCHEDULE_CRON="0 */6 * * *"

# Weekdays only at 10am UTC
SCHEDULE_CRON="0 10 * * 1-5"
```
