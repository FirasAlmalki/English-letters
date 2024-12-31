import os
from PIL import Image

# Define the main folder path and labels folder path
main_folder = r"C:\Users\Admin\Desktop\Arabic\الحروف العربية"
labels_folder = r"C:\Users\Admin\Desktop\eng\dataset\labels"

# Ensure the labels folder exists
if not os.path.exists(labels_folder):
    os.makedirs(labels_folder)

# Loop through all subfolders (class IDs)
for subdir in os.listdir(main_folder):
    subdir_path = os.path.join(main_folder, subdir)

    # Skip files and only process folders
    if os.path.isdir(subdir_path):
        class_id = subdir  # Use the subfolder name as the class ID

        # Loop through all images in the subfolder
        for filename in os.listdir(subdir_path):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):  # Check for image files
                # Get the base name of the image (without the extension)
                image_name = os.path.splitext(filename)[0]

                # Get the image file path
                image_path = os.path.join(subdir_path, filename)

                # Open the image and get its dimensions
                with Image.open(image_path) as img:
                    img_width, img_height = img.size

                    # Example values for center_x, center_y, width, height as relative to the image size
                    center_x = 0.5  # Example relative value, adjust based on your data
                    center_y = 0.5  # Example relative value, adjust based on your data
                    width = 0.8     # Example relative value, adjust based on your data
                    height = 0.8    # Example relative value, adjust based on your data

                    # Ensure the bounding box values are within the image boundaries
                    center_x = min(max(center_x, 0), 1)
                    center_y = min(max(center_y, 0), 1)
                    width = min(max(width, 0), 1)
                    height = min(max(height, 0), 1)

                    # Convert the relative coordinates into the image's dimensions
                    # Ensure the bounding box fits within the image dimensions
                    left = max(center_x - width / 2, 0)
                    right = min(center_x + width / 2, 1)
                    top = max(center_y - height / 2, 0)
                    bottom = min(center_y + height / 2, 1)

                    # Calculate width and height based on the new bounding box
                    width = right - left
                    height = bottom - top
                    center_x = (left + right) / 2
                    center_y = (top + bottom) / 2

                    # Create the label file path
                    label_file_path = os.path.join(labels_folder, f"{image_name}.txt")

                    # Open the label file and write the class ID and bounding box values
                    with open(label_file_path, 'w') as label_file:
                        label_file.write(f"{class_id} {center_x} {center_y} {width} {height}\n")

print("Label files created successfully!")
