import shutil
import os
from datetime import datetime

SOURCE_DIR = "./data"
BACKUP_ROOT = "./backups"

def run_backup():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(BACKUP_ROOT, f"backup_{timestamp}")
    shutil.copytree(SOURCE_DIR, dest)
    print(f"Backup created at {dest}")

if __name__ == "__main__":
    run_backup()