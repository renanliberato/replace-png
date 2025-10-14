#!/usr/bin/env python3
"""
Script to replace a PNG file with a 1x1 white pixel.
Usage: python app.py <filepath|folder>

Requires: pip install pypng
"""

import sys
import os
import png
import glob

def create_white_pixel_png(filepath):
    """Create a 1x1 white pixel PNG and save it to the specified filepath."""
    try:
        dir_path = os.path.dirname(filepath)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        png.from_array([[255, 255, 255, 255]], 'L').save(filepath)

        print(f"Successfully replaced {filepath} with 1x1 white pixel PNG")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def process_folder(folder_path):
    """Process all PNG files in the specified folder."""
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory")
        sys.exit(1)
    
    png_files = glob.glob(os.path.join(folder_path, "*.png"))
    png_files.extend(glob.glob(os.path.join(folder_path, "**", "*.png"), recursive=True))
    
    if not png_files:
        print(f"No PNG files found in {folder_path}")
        return
    
    print(f"Found {len(png_files)} PNG files in {folder_path}")
    
    for png_file in png_files:
        create_white_pixel_png(png_file)

def main():
    if len(sys.argv) != 2:
        print("Usage: python app.py <filepath|folder>")
        print("  filepath: Path to a single PNG file")
        print("  folder: Path to a folder containing PNG files")
        sys.exit(1)
    
    path = sys.argv[1]
    
    if os.path.isfile(path):
        if not path.lower().endswith('.png'):
            print("Error: File must have .png extension")
            sys.exit(1)
        create_white_pixel_png(path)
    elif os.path.isdir(path):
        process_folder(path)
    else:
        print(f"Error: {path} is not a valid file or directory")
        sys.exit(1)

if __name__ == "__main__":
    main()