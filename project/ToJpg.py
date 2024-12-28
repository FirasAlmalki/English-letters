from PIL import Image
import os

# Path to the root "Arabic" folder
root_folder = "C:/Users/Admin/Desktop/Arabic"

# Loop through all subdirectories and files
for subdir, _, files in os.walk(root_folder):
    for file in files:
        if file.endswith((".png", ".jpeg", ".jpg")):  # Check for supported formats
            file_path = os.path.join(subdir, file)

            # Open the image and convert to .jpg
            try:
                img = Image.open(file_path)
                new_file_path = os.path.splitext(file_path)[0] + ".jpg"  # Change extension to .jpg

                # Convert and save in place
                img.convert("RGB").save(new_file_path, "JPEG")

                # Remove the original file if the format was not already .jpg
                if not file.endswith(".jpg"):
                    os.remove(file_path)

                print(f"Converted: {file_path} -> {new_file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

print("All images converted to .jpg format in place!")
