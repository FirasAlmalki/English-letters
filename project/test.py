import os
from ultralytics import YOLO
import cv2

# Initialize the model with the trained weights
model = YOLO('C:/Users/Admin/Desktop/Project/SignSpotter/runs/detect/train5/weights/best.pt')

# Directory containing test files (images and videos)
file_dir = 'C:/Users/Admin/Desktop/test/'  # Change to your directory path
output_dir = 'C:/Users/Admin/Desktop/result/'  # Directory to save processed videos
# Supported file formats
supported_image_formats = ['.jpg', '.png']
supported_video_formats = ['.mp4']

# Iterate over all files in the directory
for filename in os.listdir(file_dir):
    file_path = os.path.join(file_dir, filename)

    # Process images
    if filename.lower().endswith(tuple(supported_image_formats)):
        image = cv2.imread(file_path)
        if image is None:
            print(f"Error: Could not load the image {filename}.")
            continue

        # Predict objects in the image
        results = model.predict(source=image, imgsz=640)

        for result in results[0].boxes.data:
            x1, y1, x2, y2, confidence, class_id = result
            # Draw rectangle around detected object
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            # Add label text (class and confidence)
            cv2.putText(image, f'{model.names[int(class_id)]} {confidence:.2f}', (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

        # Display the image with detections
        cv2.imshow(f'YOLOv8 Detection - {filename}', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Process videos
    elif filename.lower().endswith(tuple(supported_video_formats)):
        video = cv2.VideoCapture(file_path)

        # Get the video parameters (width, height, frames per second)
        frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = video.get(cv2.CAP_PROP_FPS)

        # Define the codec and create a VideoWriter object to save the processed video
        output_path = os.path.join(output_dir, f"processed_{filename}")
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for mp4 videos
        out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

        # Process each frame in the video
        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                break

            # Predict objects in the frame
            results = model.predict(source=frame, imgsz=640)

            for result in results[0].boxes.data:
                x1, y1, x2, y2, confidence, class_id = result
                # Draw rectangle around detected object
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                # Add label text (class and confidence)
                cv2.putText(frame, f'{model.names[int(class_id)]} {confidence:.2f}', (int(x1), int(y1) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

            # Write the frame to the new video file
            out.write(frame)

            # Optional: Display the frame being processed
            cv2.imshow(f'Processing {filename}', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release resources
        video.release()
        out.release()
        cv2.destroyAllWindows()

        print(f"Processed video saved as {output_path}")
