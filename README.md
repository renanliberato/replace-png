# 🖼️ Replace PNG

A lightweight Python utility that replaces PNG files with optimized 1x1 white pixel PNGs. Perfect for creating placeholders, reducing file sizes, or testing image handling in your applications.

## ✨ Features

- 🎯 **Single File Processing**: Replace individual PNG files with 1x1 white pixels
- 📁 **Batch Processing**: Process entire directories recursively
- ⚡ **Lightweight**: Minimal dependencies and fast execution
- 🛡️ **Safe**: Preserves directory structure and file paths
- 🚀 **Easy Setup**: Simple installation and usage

## 📦 Installation

### Option 1: Using the executable script (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/replace-png.git
cd replace-png

# Make the script executable
chmod +x bin/replace-png

# Run it!
./bin/replace-png path/to/your/file.png
```

### Option 2: Manual setup

```bash
# Clone the repository
git clone https://github.com/yourusername/replace-png.git
cd replace-png

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the script
python app.py path/to/your/file.png
```

## 🚀 Usage

### Replace a single PNG file

```bash
python app.py path/to/image.png
# or
./bin/replace-png path/to/image.png
```

### Replace all PNG files in a directory

```bash
python app.py path/to/directory
# or
./bin/replace-png path/to/directory
```

### Example

```bash
# Replace a single file
python app.py ./assets/logo.png
# Output: Successfully replaced ./assets/logo.png with 1x1 white pixel PNG

# Process an entire directory
python app.py ./images/
# Output: Found 5 PNG files in ./images/
#         Successfully replaced ./images/pic1.png with 1x1 white pixel PNG
#         Successfully replaced ./images/pic2.png with 1x1 white pixel PNG
#         ...
```

## 🎯 Use Cases

- **🧪 Testing**: Replace placeholder images in test environments
- **📦 Size Optimization**: Create minimal placeholder images
- **🔒 Content Masking**: Replace sensitive images with neutral placeholders
- **⚡ Performance Testing**: Test application behavior with minimal image data
- **🚫 Broken Link Handling**: Replace missing images with valid 1x1 alternatives

## 📋 Requirements

- Python 3.6+
- [pypng](https://pypi.org/project/pypng/) library

## 🛠️ Technical Details

The utility creates a 1x1 pixel PNG with:
- **Dimensions**: 1×1 pixel
- **Color**: White (RGB: 255, 255, 255)
- **Format**: PNG with lossless compression
- **Transparency**: Alpha channel supported

## 📁 Project Structure

```
replace-png/
├── app.py              # Main application logic
├── setup.py           # Package setup configuration
├── requirements.txt   # Python dependencies
├── bin/
│   └── replace-png    # Executable script with environment setup
└── README.md          # This file
```

## ⚠️ Disclaimer

⚠️ **This tool permanently replaces PNG files.** Always backup your original files before processing. The replaced images cannot be restored to their original content.
