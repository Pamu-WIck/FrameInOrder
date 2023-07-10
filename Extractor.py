import cv2


def extractor(name, frame_rate):
    # Open the video file
    video_path = "vid/" + name
    cap = cv2.VideoCapture(video_path)

    # Check if the video file was opened successfully
    if not cap.isOpened():
        print("Error opening video file")
        exit()

    frame_count = frame_rate  # Start with frame number 1
    frame_rate = 8  # Desired frame rate (frames per second)
    interval = round(cap.get(cv2.CAP_PROP_FPS) / frame_rate)  # Calculate the frame interval
    frame_num = 1  # Start with frame number 1

    while True:
        # Read the next frame from the video
        ret, frame = cap.read()

        # If the frame was not read successfully, then we have reached the end of the video
        if not ret:
            break

        # Check if the frame count matches the desired interval
        if frame_count % interval == 0:
            # Save the frame as an image file with sequential numbering
            frame_path = f"frames/{frame_num}.jpg"
            cv2.imwrite(frame_path, frame)
            frame_num += 1  # Increment the frame number

        # Increment the frame counter
        frame_count += 1

    # Release the video file
    cap.release()


extractor("cat.mp4", 1)
