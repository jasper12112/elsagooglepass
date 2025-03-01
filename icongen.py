from PIL import Image, ImageDraw, ImageFont
import os

def generate_pwa_icons():
    """Generate all required icons for the PWA"""
    # Create icons directory if it doesn't exist
    if not os.path.exists('icons'):
        os.makedirs('icons')
    
    # Icon sizes needed
    sizes = [72, 96, 128, 144, 152, 192, 384, 512]
    
    # Load the logo image
    logo = Image.open('logo.png')
    
    # Use the logo for the icon
    for size in sizes:
        # Resize the logo for the current size
        logo_resized = logo.resize((size, size))

        # Save the resized logo as an icon
        logo_resized.save(f'icons/icon-{size}x{size}.png')
        print(f"Created icon: icon-{size}x{size}.png")

if __name__ == "__main__":
    generate_pwa_icons()
    print("All icons generated successfully")