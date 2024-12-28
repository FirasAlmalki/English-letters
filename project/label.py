
import os

# Path to the root "Arabic" folder
root_folder = "C:/Users/Admin/Desktop/Arabic"

# Create a "labels" folder in the root directory
labels_folder = os.path.join(root_folder, "labels")
os.makedirs(labels_folder, exist_ok=True)

# Loop through all subdirectories and files
for subdir, _, files in os.walk(root_folder):
    # Use the subfolder name as the class_id
    class_id = os.path.basename(subdir)

    # Skip the "labels" folder or invalid subfolder names
    if not class_id.isdigit():
        continue

    for file in files:
        if file.endswith((".png", ".jpg", ".jpeg")):  # Process image files
            # Create the corresponding label file
            file_name = os.path.splitext(file)[0]  # Get the file name without extension
            label_path = os.path.join(labels_folder, f"{file_name}.txt")

            # Write the label data
            with open(label_path, "w") as label_file:
                label_file.write(f"{class_id} 0.500000 0.500000 1.000000 1.000000\n")

            print(f"Created label: {label_path}")

print("Label files created successfully in the 'labels' folder!")
