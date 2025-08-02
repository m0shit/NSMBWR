import os, random, shutil
from datetime import datetime

seed_input = input("Enter a seed number (leave blank for random): ").strip()

if seed_input:
    try:
        seed = int(seed_input)
        random.seed(seed)
        print(f"Using seed: {seed}")
    except ValueError:
        print("Invalid seed entered. Going random!!")
else:
    print("No seed entered — going random!!")

# change this to your actual Stage folder path!!!
stage_dir = r"C:\Users\oscar\OneDrive\Skrivebord\Stage"
texture_dir = os.path.join(stage_dir, "Texture")

if not os.path.exists(stage_dir):
    print("Error: 'Stage' folder not found!! Please check the path!!")

stage_backup = os.path.join(stage_dir, "backup")
texture_backup = os.path.join(texture_dir, "backup")
log_dir = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(log_dir, exist_ok=True)

if not os.path.exists(stage_backup):
    os.makedirs(stage_backup)
    for file in os.listdir(stage_dir):
        if file.endswith(".arc"):
            shutil.copy(os.path.join(stage_dir, file), os.path.join(stage_backup, file))
    print("'Stage' backup created!!")

if os.path.exists(texture_dir) and not os.path.exists(texture_backup):
    os.makedirs(texture_backup)
    for file in os.listdir(texture_dir):
        if file.endswith(".arc"):
            shutil.copy(os.path.join(texture_dir, file), os.path.join(texture_backup, file))
    print("'Texture' backup created!!")

EXCLUDED_FILES = {"02-24.arc"}

stage_files = [f for f in os.listdir(stage_dir)
               if f.endswith(".arc") and f not in EXCLUDED_FILES]
shuffled_stage = stage_files[:]
random.shuffle(shuffled_stage)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_name = f"shuffle_log_{timestamp}.txt"
log_path = os.path.join(log_dir, log_name)

with open(log_path, "w") as log:
    log.write("[Stage]\n")
    for orig, new in zip(stage_files, shuffled_stage):
        log.write(f"{orig} <- {new}\n")
        shutil.copy(os.path.join(stage_backup, new), os.path.join(stage_dir, orig))

print(f"Shuffled {len(stage_files)} levels!!!")
