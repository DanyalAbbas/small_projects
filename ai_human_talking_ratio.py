import json
import os

def calculate_talking_ratio(transcript_file):
    with open(transcript_file, 'r') as f:
        json_thing = json.load(f)

    human_words = 0
    ai_words = 0

    transcript = json_thing.get('transcript', [])
    speaker = "AI:"
    for word in transcript.split():
        if word == "AI:":
            speaker = word
        elif word == "User:":
            speaker = word
        
        human_words += 1 if speaker == "User:" else 0
        ai_words += 1 if speaker == "AI:" else 0        
        
    total_words = human_words + ai_words
    if total_words == 0:
        return 0.0

    return ai_words / total_words


print(calculate_talking_ratio("smt.json"))