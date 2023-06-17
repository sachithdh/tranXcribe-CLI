import argparse
import os
import openai
from dotenv import load_dotenv

load_dotenv() # load environment variables from a .env file

parser = argparse.ArgumentParser(description="Audio transcriber")

parser.add_argument("-a", "--audio", type=str, help="Path to audio file")

args = parser.parse_args()

# Transcribe audio file
def transcribe(audio_file):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    audio = open(audio_file, 'rb') #open audio file with given path

    transcript = openai.Audio.transcribe("whisper-1", audio)

    return transcript.text

# print result
if args.audio:
    audio = args.audio
    result = transcribe(audio)
    print(result)

else:
    print("Invalid Audio path")
