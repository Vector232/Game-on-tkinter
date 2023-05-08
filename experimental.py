from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file("NewComposition1.wav", format="wav")
play(sound)