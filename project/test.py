import os
from ultralytics import YOLO
import cv2

def test_image_with_model(model_path, image_path, output_dir):
    # Load the YOLO model
    model = YOLO(model_path)

    # Load the test image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load the image {image_path}.")
        return

    # Predict objects in the image
    results = model.predict(source=image, imgsz=640)

    for result in results[0].boxes.data:
        x1, y1, x2, y2, confidence, class_id = result
        # Draw bounding box and label
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(image, f'{model.names[int(class_id)]} {confidence:.2f}', (int(x1), int(y1) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Save the processed image
    result_path = os.path.join(output_dir, f'processed_{os.path.basename(image_path)}')
    cv2.imwrite(result_path, image)
    print(f"Processed image saved as {result_path}")

# Example usage
model_path = 'C:/Users/Admin/Desktop/Project/SignSpotter/runs/detect/train12/weights/best.pt'
image_path = 'C:/Users/Admin/Desktop/test_image.jpg'
output_dir = 'C:/Users/Admin/Desktop/result/'

test_image_with_model(model_path, image_path, output_dir)
