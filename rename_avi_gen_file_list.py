import os
import random
import string
import csv
import cv2

# Function to generate a random filename
def generate_random_filename():
    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    return f"0X{random_chars}"

# Function to get video file information
def get_video_info(file_path):
    video = cv2.VideoCapture(file_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video.release()
    return fps, frame_count, frame_width, frame_height

# Folder containing the files.avi
folder_path = "C:\\Users\\mfrde\\echonet\\dynamic\\a4c-video-dir\\Athlete_reduced_avi1"

# List all files in the folder
file_list = os.listdir(folder_path)

# Create a CSV file
csv_file_path = os.path.join(folder_path, "FileList.csv")

# Open the CSV file in write mode
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the column names to the CSV
    writer.writerow(["FileName", "EF", "ESV", "EDV", "FrameHeight", "FrameWidth", "FPS", "NumberOfFrames", "Split"])
    
    # Process each files.avi in the folder
    for file_name in file_list:
        if file_name.endswith(".avi"):
            file_path = os.path.join(folder_path, file_name)
            
            # Generate a random filename
            new_file_name = generate_random_filename()
            
            # Rename the file
            new_file_path = os.path.join(folder_path, new_file_name + ".avi")
            os.rename(file_path, new_file_path)
            
            # Get video information
            fps, frame_count, frame_width, frame_height = get_video_info(new_file_path)
            
            # Write the file information to the CSV
            writer.writerow([new_file_name, 0, 0, 0, frame_height, frame_width, fps, frame_count, "EXTERNAL_DATA"])

print("Files renamed and information recorded in FileList.csv.")
