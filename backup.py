import shutil
import os

# Get the current directory
current_dir = os.getcwd()

# Get the parent directory
parent_dir = os.path.dirname(current_dir)

# Create a backup directory in the parent directory
backup_dir = os.path.join(parent_dir, 'backup')
if not os.path.exists(backup_dir):
    os.mkdir(backup_dir)

# Create a backup of the current directory in the backup directory
backup_name = os.path.basename(current_dir)
backup_path = os.path.join(backup_dir, backup_name)
shutil.make_archive(backup_path, 'zip', current_dir)

print(f"Backup created at {backup_path}.zip")

