import shutil
import os
import logging
from datetime import datetime

SOURCE_DIR = "./data"
BACKUP_ROOT = "./backups"

logging.basicConfig(
    filename="logs/backup.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def run_backup():
    try:
        if not os.path.exists(SOURCE_DIR):
            logging.error(f"Source dir missing: {SOURCE_DIR}")
            return
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        dest = os.path.join(BACKUP_ROOT, f"backup_{timestamp}")
        shutil.copytree(SOURCE_DIR, dest)
        logging.info(f"Backup created at {dest}")
    except Exception as e:
        logging.error(f"Backup failed: {e}")

if __name__ == "__main__":
    run_backup()