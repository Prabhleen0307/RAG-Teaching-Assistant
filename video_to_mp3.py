#converts the videos to mp3 and creates a folder named process_video and dumps it in
import os
import subprocess
files = os.listdir("videos")
#now we will process all the files
for file in files:
    # print(file)
    tutorial_number = file.split("#")[-1].split(".")[0]
    # print(file, "→ Tutorial", tutorial_number)
    file_name = file.split(" -",1)[0]
    # print(file, "→ File Name", file_name)
    print(file_name , tutorial_number)
    subprocess.run([
    "ffmpeg",
    "-y",
    "-i", f"videos/{file}",
    "-vn",
    "-acodec", "mp3",
    f"audios/{tutorial_number}_{file_name}.mp3"
])