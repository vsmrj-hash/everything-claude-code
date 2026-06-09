---
description: Run the FIFA World Cup 2026 automated YouTube content pipeline — scrape news, write script, find media, build video, upload to YouTube.
---

Run the FIFA content creation pipeline end to end.

1. Check that `scripts/fifa/.env` exists with required keys. If missing, tell the user to run `cp scripts/fifa/.env.example scripts/fifa/.env` and fill in their API keys, then run `node scripts/fifa/setup.js` for YouTube OAuth.

2. Install dependencies if `scripts/fifa/node_modules` doesn't exist:
   ```bash
   cd scripts/fifa && npm install
   ```

3. Parse any flags the user provided:
   - `--shorts` or `--short` → pass `--format=short` (YouTube Shorts, <60s)
   - `--long` → pass `--format=long` (7-10 minute video)
   - `--dry-run` or `--no-upload` → pass `--skip-upload` (build video, don't upload)
   - `--schedule` → start the scheduler daemon instead of a single run

4. Run the appropriate command:
   ```bash
   # Single run (default)
   node scripts/fifa/index.js [flags]

   # Start scheduler
   node scripts/fifa/scheduler.js
   ```

5. Stream the output so the user can see progress through each pipeline stage:
   - Scraping news
   - Writing script
   - Sourcing media
   - Building video
   - Uploading to YouTube

6. When complete, report:
   - Video title generated
   - Format (Short / Long) and duration
   - YouTube URL (if uploaded)
   - Output file path (if `--skip-upload`)

7. If any step fails, show the error clearly and suggest the fix from the troubleshooting table in `skills/fifa-worldcup-2026/SKILL.md`.
