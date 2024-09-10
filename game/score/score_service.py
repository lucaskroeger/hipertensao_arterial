import json
import os
import re

class ScoreService:
    
    def __init__(self):
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        self.file_path = os.path.join(script_dir, 'best_scores.json')

    def register(self, score):

        scores = self.load_scores()

        scores.append({'name': score.name, 'time':score.time})

        sorted_scores = sorted(scores, key=lambda x: self.time_to_milliseconds(x['time']))[:10]

        self.save_scores(sorted_scores)

    def load_scores(self):

        with open(self.file_path, 'r') as file:
            return json.load(file)
        
    def time_to_milliseconds(self, time_str):

        match = re.match(r'(\d{2}):(\d{2})\.(\d{2})', time_str)

        if match:
            minutes = int(match.group(1))
            seconds = int(match.group(2))
            milliseconds = int(match.group(3)) * 10 

            return (minutes * 60 * 1000) + (seconds * 1000) + milliseconds

        return 0

    def save_scores(self, scores):
        with open(self.file_path, 'w') as file:
            json.dump(scores, file, indent=4)