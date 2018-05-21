# CraignDavePuzzle
A project that scrapes YouTube for CraignDave videos that uses Optical Character Recognition (OCR) to make converting binary to ASCII more efficient.

CraignDave are a Youtube channel that hides binary messages in their videos. When converted to ASCII, a partial message in English is uncovered. You can find these messages at around the 6-second mark in the videos in this playlist (https://www.youtube.com/playlist?list=PLCiOXwirraUDUYF_qDYcZV8Hce8dsE_Ho)  

This project is dedicated to taking the YouTube videos in the playlist, downloading them and capturing the frame at around the 6 second mark. This output is then to be cropped and run through Tesseract, an OCR algorithm, scanned for errors and then converted to ASCII. The data from this is then to be stored in a flat file database for easier viewing.

## Prerequisites
For this project, a few dependencies are needed.
- Pytube (A YouTube video downloading library) 
- Pytesser (A wrapper for Tesseract)
- PIL (An imaging library for Python)
- CV2 (Used for saving still frames from the video)
- numpy (Used for converting images to multi-dimentional arrays)

### TODO
- [x] Create a function to download specified YouTube videos
- [x] Create a function to capture the specific frame where the binary message is present
- [x] Create a function to implement Tesseract's OCR algorithm
- [ ] Create a function to crop the image so it fits just around the binary digits.
- [ ] Create a function that corrects for any errors the OCR may have made and convert the output to ASCII
- [ ] Use the first and second function to create another function that can iterate through the videos in the playlist. It should download a video, caputure the desired frame and save the output, and then delete the original video
- [ ] Create a function that iterates through the images in the folder and uses the third and fourth functions to convert it into text.
- [ ] Create a function that takes the cropped image, video name, original text, and corrected text and store it in a flat file database. 
