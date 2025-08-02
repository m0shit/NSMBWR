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

# change this to your actual stream folder path!!! (found in /Sound/)
music_dir = r"C:\Users\oscar\OneDrive\Skrivebord\stream"
backup_dir = os.path.join(music_dir, "backup")
log_dir = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(log_dir, exist_ok=True)

if not os.path.exists(music_dir):
    print("Error: 'stream' folder not found!! Please check the path!!")

if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)
    for file in os.listdir(music_dir):
        if file.endswith(".brstm"):
            shutil.copy(os.path.join(music_dir, file), backup_dir)
    print("'stream' backup created!!")

music_files = [f for f in os.listdir(music_dir) if f.endswith(".brstm")]
shuffled = music_files[:]
random.shuffle(shuffled)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_name = f"music_shuffle_log_{timestamp}.txt"
log_path = os.path.join(log_dir, log_name)

with open(log_path, "w") as log:
    log.write("[Music]\n")
    for orig, new in zip(music_files, shuffled):
        log.write(f"{orig} <- {new}\n")
        shutil.copy(os.path.join(backup_dir, new), os.path.join(music_dir, orig))

print(f"Shuffled {len(music_files)} tracks!!!")
