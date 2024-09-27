import os
import shutil


def segregate_files(input_folder, output_image_folder, output_text_folder):
    # Create output folders if they don't exist
    os.makedirs(output_image_folder, exist_ok=True)
    os.makedirs(output_text_folder, exist_ok=True)

    # Iterate through files in the input folder
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)

        # Check if file is an image
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            shutil.copy(file_path, output_image_folder)
        # Check if file is a text file
        elif file_name.lower().endswith('.txt'):
            shutil.copy(file_path, output_text_folder)


# Example usage
input_folder = r'D:\ProjectAmit\finalimages'
output_image_folder = r'D:\ProjectAmit\finalimages2'
output_text_folder = r'D:\ProjectAmit\finallabels2'

segregate_files(input_folder, output_image_folder, output_text_folder)
