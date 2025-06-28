# Traffic Violation Detection System

## Description

This project uses OpenCV to process traffic video footage and detect vehicles that violate traffic rules by crossing a defined virtual line. Violating vehicles are highlighted with a red rectangle and label, while others are marked in green.

## Features

- Enhanced video preprocessing for clearer vehicle detection
- Violation detection based on line crossing
- Visual alerts for violations with colored overlays

## Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy

## Usage

1. Place a traffic video file named `traffic.mp4` in the project directory.
2. Run `app.py` using Python.
3. Press `q` to quit the detection window.

## How It Works

- The code uses background subtraction and contour detection to identify moving vehicles.
- It draws a red line on the frame; any vehicle crossing the line triggers a violation alert.

## License

This project is for educational and research purposes only.
