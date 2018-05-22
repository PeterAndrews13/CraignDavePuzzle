import numpy as np
import pytube
import cv2
from PIL import Image
from pytesser import *


def saveVideo(videoLink):
    yt = pytube.YouTube(videoLink)
    yt.streams.first().download()
    return yt.title


def saveFrame(videoName,stillName):
    cap = cv2.VideoCapture(videoName)
    cap.set(1,180);# take the 180th frame
    ret, frame = cap.read()
    cv2.imwrite(stillName,frame)

def readFrame(stillName):
    im = Image.open(stillName)
    text = image_file_to_string(stillName)
    return text


