import os

# Define the main folder path
main_folder = r"C:\Users\Admin\Desktop\Arabic\الحروف العربية"

# Arabic alphabet mapping (class ID to Arabic letter)
arabic_letters = {
    26: "أ", 27: "ب", 28: "ت", 29: "ث", 30: "ج", 31: "ح", 32: "خ", 33: "د", 34: "ذ", 35: "ر", 36: "ز",
    37: "س", 38: "ش", 39: "ص", 40: "ض", 41: "ط", 42: "ظ", 43: "ع", 44: "غ", 45: "ف", 46: "ق", 47: "ك",
    48: "ل", 49: "م", 50: "ن", 51: "هـ", 52: "و", 53: "ي"
}

# Loop through all subfolders (class IDs)
for subdir in os.listdir(main_folder):
    subdir_path = os.path.join(main_folder, subdir)

    # Skip files and only process folders
    if os.path.isdir(subdir_path):
        class_id = int(subdir)  # Use the subfolder name (class ID)

        # Check if the class ID exists in the Arabic alphabet mapping
        if class_id in arabic_letters:
            letter = arabic_letters[class_id]  # Get the Arabic letter corresponding to the class ID

            # Loop through all images in the subfolder and rename them
            for idx, filename in enumerate(os.listdir(subdir_path)):
                if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):  # Check for image files
                    # Get the file extension
                    file_extension = os.path.splitext(filename)[1]

                    # Create the new image name following the pattern
                    new_name = f"{letter}-{idx}{file_extension}"

                    # Get the old and new image paths
                    old_image_path = os.path.join(subdir_path, filename)
                    new_image_path = os.path.join(subdir_path, new_name)

                    # Rename the image
                    os.rename(old_image_path, new_image_path)

print("Image files renamed successfully!")
