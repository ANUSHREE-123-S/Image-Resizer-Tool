# Image-Resizer-Tool
his Python script automatically creates a sample image, then resizes all images inside the input_images folder and saves the resized versions to output_images.

It supports: PNG, JPG, JPEG, WEBP, BMP.

🧰 Requirements

Install Pillow (PIL):

pip install pillow

▶️ How to Use
1. Run the script
python app.py

What will happen?

A folder input_images/ will be created (if missing)

A sample.png image will be auto-created

All images inside input_images/ will be resized to 800 × 800

Resized images will be saved in output_images/ as JPEG

🖼️ Supported Input Formats

.png

.jpg

.jpeg

.webp

.bmp

⚙️ Script Settings

Inside the script:

new_size = (800, 800)
output_format = "JPEG"
input_folder = "input_images"
output_folder = "output_images"


You can change:

Output dimensions

Output format

Folder names

🧪 Example Output

After running the script:

input_images/
    sample.png

output_images/
    sample.jpeg

