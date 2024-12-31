from PIL import Image
import os

# Define the main folder path
main_folder = r"C:\Users\Admin\Desktop\Arabic\الحروف العربية"

# Loop through all subfolders and files
for subdir, dirs, files in os.walk(main_folder):
    for filename in files:
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # Check for image file extensions
            img_path = os.path.join(subdir, filename)
            img = Image.open(img_path)

            # Resize the image to 100x100 pixels
            img_resized = img.resize((100, 100))

            # Save the resized image, overwriting the original one
            img_resized.save(img_path)

print("Images resized successfully!")
