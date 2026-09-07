# Daily Backup Scheduler

A small Python automation that backs up a folder on a daily schedule, safely and unattended —
with logging, lock-file protection against overlapping runs, idempotent output, and optional
failure alerts.

## What it does

Copies the contents of `SOURCE_DIR` into a new dated folder under `BACKUP_ROOT`
(`backups/backup_YYYYMMDD`) once per day. If a backup for that day already exists, it skips
the run instead of duplicating work. If the source folder is missing or the copy fails, it
logs the error (and optionally sends a webhook alert) instead of failing silently.

## Requirements

- Python 3.8+
- `requests` (only needed if using the optional webhook alert — see `requirements.txt`)

Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Edit the constants at the top of `backup_job.py`:

| Variable      | Description                                  |
|---------------|-----------------------------------------------|
| `SOURCE_DIR`  | Folder to back up                             |
| `BACKUP_ROOT` | Where dated backup copies are stored          |
| `LOCK_FILE`   | Lock file path (default: `job.lock`)          |
| `WEBHOOK_URL` | (Optional) Slack/Discord webhook for failures |

## Running manually

```bash
python backup_job.py
```

## How it's scheduled

Runs daily via cron at 2 AM. To install:

```bash
crontab -e
```

Add this line: