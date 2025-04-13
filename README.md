# Video Sorter, Re-Encoder, & Duplicate Finder

## Description

Welcome to **Video Sorter, Re-Encoder, & Duplicate Finder**! This Python program is designed to help you manage your video files efficiently. It includes features for sorting videos based on resolution, re-encoding them using HEVC codec with optional GPU acceleration, and identifying duplicate files by comparing file size.

## Features

- **Video Sorting**: Sorts videos into folders based on their resolution.
- **Re-Encoding**: Re-encodes videos using the HEVC codec for better efficiency.
- **Duplicate Detection and Removal**: Identifies and deletes duplicate video files by comparing file sizes.

## Installation

To get started, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/gag3301v/video_sorter_reencoder.git
   cd video_sorter_reencoder
   ```

2. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Sorting Videos

To sort videos based on resolution, run:
```python
# sorter.py
python sorter.py /path/to/videos
```

### Re-Encoding Videos

To re-encode videos using HEVC codec, run:
```python
# reencode.py
python reencode.py /path/to/source /path/to/destination
```

### Deleting Duplicate Files

To identify and delete duplicate files by size, run:
```python
# duplicate.py
python duplicate.py /path/to/videos
```

## Configuration (if applicable)

No specific configuration is required for this script. Ensure you have the necessary permissions to read/write in the specified directories.

## Tests

Tests are currently not available for this project. We recommend manually testing each script as needed.

## Project Structure

```
video_sorter_reencoder/
├── sorter.py
├── reencode.py
├── duplicate.py
├── requirements.txt
└── README.md
```

## Contributing

Contributions are welcome! Please read our [CONTRIBUTING](CONTRIBUTING.md) guidelines before submitting a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Owner:** gag3301v  
**Repository URL:** [https://github.com/gag3301v/video_sorter_reencoder](https://github.com/gag3301v/video_sorter_reencoder)

Thank you for using Video Sorter, Re-Encoder, & Duplicate Finder! 🎥🚀