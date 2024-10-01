# Image Processing Project: Blurred Background with Sharp Subject

This project demonstrates how to use OpenCV and NumPy to create a blurred background effect while keeping the subject of an image in sharp focus. The code leverages OpenCV's `grabCut` algorithm for foreground-background segmentation and applies Gaussian blur to the background for a depth-of-field effect.

## Features

- Loads an image from a file.
- Applies foreground-background segmentation using the `grabCut` algorithm.
- Blurs the background while keeping the subject sharp.
- Displays the final image with a sharp subject and a blurred background.
- Saves the output image to a file.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy (`numpy`)

You can install the required libraries using pip:

```bash
pip install opencv-python-headless numpy
