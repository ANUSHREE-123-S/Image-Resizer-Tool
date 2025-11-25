import os
from PIL import Image, ImageDraw

input_folder = "input_images"
output_folder = "output_images"
new_size = (800, 800)
output_format = "JPEG"

def create_sample_image():
    """Create a sample image so user doesn't need to add one manually."""
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)

    sample_path = os.path.join(input_folder, "sample.png")

    # Create a simple image
    img = Image.new("RGB", (400, 400), color="skyblue")
    draw = ImageDraw.Draw(img)
    draw.text((120, 180), "TEST", fill="black")

    img.save(sample_path)
    print("✔ Sample image created:", sample_path)

def resize_images():
    print("Reading folder:", input_folder)
    print("Files found:", os.listdir(input_folder))

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp')):
            print("Processing:", filename)

            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            img = img.resize(new_size)

            base_name = os.path.splitext(filename)[0]
            save_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")
            img.save(save_path, output_format)

            print("✔ Saved:", save_path)

if __name__ == "__main__":
    create_sample_image()
    resize_images()
