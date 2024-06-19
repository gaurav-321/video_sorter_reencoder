# Video Sorter & Re-encoder

This repository contains Python scripts to sort and re-encode video files efficiently.

## sorter.py

**Key Features**

*   Sorts video files based on:
    *   **Orientation:** Landscape or portrait
    *   **Resolution:** 144p, 240p, 360p, 480p, 720p, 1080p, 2160p
*   Organizes files into folders within "E:\final_file\" based on the above criteria
*   Handles errors by moving problematic files to an "error" subdirectory
*   Uses `tqdm` library for a visual progress bar during sorting

## reencode.py

**Key Features**

*   Re-encodes video files to optimize their bitrates based on resolution and orientation
*   Uses `ffmpeg` with HEVC (h.265) codec for video and AAC for audio
*   Utilizes NVIDIA GPU acceleration (`hevc_nvenc`) if available
*   Prioritizes larger files for processing
*   Handles errors during re-encoding
*   Provides a progress bar for monitoring the process

## duplicate.py

**Key Features**

*   Identifies and deletes duplicate video files within a specified folder.
*   Uses file size as the primary criteria for detecting duplicates.

## Requirements

*   Python 3.x
*   Libraries: `av`, `tqdm`, `moviepy`, `shutil`, `shlex`, `traceback`

## Installation

1.  Clone this repository.
2.  Install the required libraries using `pip`:

```bash
pip install av tqdm moviepy
```

## Usage

1.  Place your unsorted video files in the desired directory (e.g., "E:\final_file\all").
2.  Run `sorter.py` to sort the files based on resolution and orientation.
3.  Run `reencode.py` to re-encode the sorted videos (located in the "error" folder after sorting).
4.  Run `duplicate.py` to remove any duplicate videos in the specified folder.

## Contributing

Feel free to submit pull requests for enhancements or bug fixes.

## License

This project is licensed under the MIT License.
