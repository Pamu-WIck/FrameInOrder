import cv2
from datetime import datetime

# Open the video file
video_path = "video.mp4"
cap = cv2.VideoCapture(video_path)

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error opening video file")
    exit()

frame_count = 0
frame_rate = 3  # Desired frame rate (frames per second)
interval = round(cap.get(cv2.CAP_PROP_FPS) / frame_rate)  # Calculate the frame interval

while True:
    # Read the next frame from the video
    ret, frame = cap.read()

    # If the frame was not read successfully, then we have reached the end of the video
    if not ret:
        break

    # Check if the frame count matches the desired interval
    if frame_count % interval == 0:
        # Get the current time
        current_time = datetime.now().strftime("%M%S%f")[:-3]

        # Save the frame as an image file with the current time in the name
        frame_path = f"vid/frame_{current_time}_{frame_count}.jpg"
        cv2.imwrite(frame_path, frame)

    # Increment the frame counter
    frame_count += 1

# Release the video file
cap.release()
