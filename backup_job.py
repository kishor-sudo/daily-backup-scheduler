import shutil
import os
import logging
from datetime import datetime

SOURCE_DIR = "./data"
BACKUP_ROOT = "./backups"
LOCK_FILE = "job.lock"

logging.basicConfig(
    filename="logs/backup.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def run_backup():
    if os.path.exists(LOCK_FILE):
        logging.warning("Lock file present — previous run may still be active. Skipping.")
        return

    open(LOCK_FILE, "w").close()
    try:
        if not os.path.exists(SOURCE_DIR):
            logging.error(f"Source dir missing: {SOURCE_DIR}")
            return

        today_tag = datetime.now().strftime("%Y%m%d")
        dest = os.path.join(BACKUP_ROOT, f"backup_{today_tag}")

        if os.path.exists(dest):
            logging.info(f"Backup for {today_tag} already exists — skipping (idempotent).")
            return

        shutil.copytree(SOURCE_DIR, dest)
        logging.info(f"Backup created at {dest}")
    except Exception as e:
        import requests

        WEBHOOK_URL = "https://your-webhook-url-here"

        def notify_failure(error_msg):
            try:
                requests.post(WEBHOOK_URL, json={"text": f"Backup job failed: {error_msg}"})
            except Exception as notify_err:
                logging.error(f"Failed to send alert: {notify_err}")

        # in run_backup(), inside except block:
            except Exception as e:
                logging.error(f"Backup failed: {e}")
                notify_failure(e)
    finally:
        os.remove(LOCK_FILE)

if __name__ == "__main__":
    run_backup()