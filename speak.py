import argparse
import os

from gtts import gTTS
from playsound import playsound

TEXT = "text.txt"
SPEECH = "speech.mp3"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="text-to-speech",
        description="A simple tool to create speech from text",
    )
    parser.add_argument("-t", "--text", default=TEXT)
    parser.add_argument("-s", "--speech", default=SPEECH)
    parser.add_argument("-m", "--mute", action="store_true")
    args = parser.parse_args()

    # read file if it is a path
    if os.path.isfile(args.text):
        with open(args.text, "r") as file:
            args.text = file.read()

    tts = gTTS(args.text, lang="en")
    tts.save(args.speech)
    if not args.mute:
        playsound(args.speech)

    # pyttsx3 is buggy and can't save to file on macOS
    # import pyttsx3
    # engine = pyttsx3.init()
    # engine.say(args.text)
    # engine.runAndWait()
    # engine.save_to_file(args.text, args.speech)
