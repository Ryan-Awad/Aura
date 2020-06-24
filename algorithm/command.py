import json

class Command:
    def __init__(self, cmd):
        self.cmd = cmd.lower() # Assigns the users input for the command to "self.cmd"
        self.database = json.load(open("dataset/database.json", "r"))
    
    def get_response(self):
        pattern_found = False
        for obj in self.database:
            for pattern in obj["Patterns"]:
                if pattern in self.cmd: # work on how you handle the patterns!
                    pattern_found = True
                    return obj["Responses"], obj["Script"]
        
        if not pattern_found:
            return "Pardon?"