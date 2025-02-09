from PIL import Image, ImageDraw, ImageFilter


# Create a brick image with a shadow
def create_brick(color, filename):
    # Create a blank image with transparent background
    width, height = 100, 40
    brick_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(brick_image)

    # Draw shadow (offset by 5 pixels)
    shadow_color = (0, 0, 0, 100)  # Semi-transparent black
    draw.rounded_rectangle([(5, 5), (width, height)], radius=10, fill=shadow_color)

    # Draw brick
    draw.rounded_rectangle([(0, 0), (width - 5, height - 5)], radius=10, fill=color)

    # Save the image
    brick_image.save(filename)


# Generate 4 bricks with different colors
colors = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
    "yellow": (255, 255, 0),
}

for name, color in colors.items():
    create_brick(color, f"{name}_brick.gif")

print("Brick images generated successfully!")