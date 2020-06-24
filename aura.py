from algorithm.command import Command
from algorithm.input_and_output import speak, listen_input, yes_or_no
import random as rnd
import importlib

while True:
    speak("How can I help you?", True)
    cmd = listen_input()
    responses = Command(cmd).get_response()

    if responses != "Pardon?":
        response_index = rnd.randint(0, len(responses) - 1)
        response = responses[0][response_index]
        command_script = responses[1]

        speak(response, True)

        if command_script != None:
            importlib.import_module("command_scripts." + command_script)
    else:
        speak(responses, True) # Says "Pardon?"
        continue
    
    speak("Can I help you with anything else?", True)
    retry = listen_input()
    yes = yes_or_no(retry)
    if yes:
        continue
    else:
        speak("Goodbye then!", True)
        break