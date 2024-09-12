import json
import os
import re

class ScoreService:
    
    def __init__(self, level):
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.level = level
        self.file_path = os.path.join(script_dir, f'best_scores-{level}.json')
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'a') as file:
                file.write('[]')


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

    def get_top_scores(self):
        scores = self.load_scores()
        sorted_scores = [x['time'] for x in sorted(scores, key=lambda x: self.time_to_milliseconds(x['time']))[:10]]
        return sorted_scores