from PIL import Image
import sys

def adjust_temperature(input_path, output_path, temperature):
    try:
        # Open the input image
        image = Image.open(input_path)

        # Adjust the image temperature
        adjusted_image = apply_temperature(image, temperature)

        # Save the resulting image to the output file
        adjusted_image.save(output_path)
        print(f"Image saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

def apply_temperature(image, temperature):
    # Split the image into channels (R, G, B)
    r, g, b = image.split()

    # Adjust each channel based on the temperature
    r = r.point(lambda i: i + temperature)
    b = b.point(lambda i: i - temperature)

    # Merge the channels back into an RGB image
    adjusted_image = Image.merge("RGB", (r, g, b))

    return adjusted_image

if __name__ == "__main__":
    # Check for correct number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python adjust_temperature.py <input_image_path> <output_image_path> <temperature>")
        sys.exit(1)

    # Get input parameters from command line
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    try:
        temperature = float(sys.argv[3])
    except ValueError:
        print("Error: Temperature must be a numeric value.")
        sys.exit(1)

    # Call the function to adjust temperature and save the image
    adjust_temperature(input_path, output_path, temperature)
