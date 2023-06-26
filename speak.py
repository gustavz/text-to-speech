import argparse
import os

import pyttsx3
from gtts import gTTS
from playsound import playsound
from voices import PYTTSX3_VOICES

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
    parser.add_argument("-e", "--engine", default="gtts", choices=["gtts", "pyttsx3"])
    parser.add_argument("-v", "--voice", default="Good News", choices=PYTTSX3_VOICES.keys())
    parser.add_argument("-r", "--rate", default=150)
    args = parser.parse_args()

    # read file if it is a path
    if os.path.isfile(args.text):
        with open(args.text, "r") as file:
            args.text = file.read()

    if args.engine == "gtts":
        tts = gTTS(args.text, lang="de")
        tts.save(args.speech)
        if not args.mute:
            playsound(args.speech)
    elif args.engine == "pyttsx3":
        # pyttsx3 is buggy and can't save to file on macOS
        engine = pyttsx3.init()
        engine.setProperty('voice', PYTTSX3_VOICES[args.voice])
        engine.setProperty('rate', int(args.rate))
        if not args.mute:
            engine.say(args.text)
            engine.runAndWait()
        engine.save_to_file(args.text, args.speech)
