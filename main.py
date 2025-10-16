import moviepy
import tkinter as tk
from youtube import *

#-----inputs for testing-----
AUDIO = "testData/Human_Music.mp3"
IMAGE = "testData/frog.jpg"

#----------------------------



def makeVid(image, audio):
    sound = moviepy.AudioFileClip(audio, fps = 44100)
    visual = moviepy.ImageClip(image, duration=sound.duration).resized(height= 1080)
    visual = visual.with_audio(sound) 
    visual.write_videofile("testOutput/test.mp4",fps = 30)



#makeVid(IMAGE,AUDIO)


ytRun()










# --- upload ---
# call youtube.videos().insert(...) here
