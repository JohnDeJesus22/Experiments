import pydub

import os

file_path=os.getcwd()
#'C:\\Users\\Sabal\\OneDrive\\Desktop\\Audiobook files\\ffmpeg-20180723-0bb5cd8-win64-static\\bin\\ffprobe'

pydub.AudioSegment.ffmpeg=file_path
sound = pydub.AudioSegment.from_file('christmasmiscellany2018_02_various_128kb.mp3')

halfway_point = len(sound) // 2
first_half = sound[:halfway_point]

# create a new file "first_half.mp3":
first_half.export("C:\\Users\\Sabal\\OneDrive\\Desktop\\Audiobook files\\ffmpeg-20180723-0bb5cd8-win64-static\\bin\\first_half.mp3", format="mp3")