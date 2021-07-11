import speech_recognition as sr
import pywhatkit
import pyttsx3
import wikipedia
import serial
try:
    port = serial.Serial('COM3', 9600)
    print("Physical body, connected.")
except:
    print("Unable to connect to my physical body")
#robot name = Fury
robot_name = ['siri', 'furi', 'uri', 'curie', 'theory']
r = sr.Recognizer()
mic = sr.Microphone()
engine = pyttsx3.init()


def listen_for_command():
    print(22)
    with mic as source:
        print('Listening  ...')
        audio = r.listen(source, phrase_time_limit=7)
        print('End')
    try:
        command = r.recognize_google(audio)
        print('You said ',command)
        perform_task(command)
    except:
        engine.say(' please try again ')

def perform_task(command):
    command = command.split(' ')
    command = [x.lower() for x in command]
    print(command)

    if command[0] in robot_name:
        if command[1] == 'play':
            video = ' '.join(command[2:])
            port.write(b'1')
            engine.say(f'Sure playing {video}')
            pywhatkit.playonyt(video)

        elif command[1] == 'search':
            query = ' '.join(command[2:])
            port.write(b'1')
            engine.say('Searching on google ')
            pywhatkit.search(query)

        elif len(command)>3 and (command[1] == 'give' or command[1] == 'gave') and (command[2] == 'info' or command[2] == 'in'):
            query = ' '.join(command[3:])
            try :
                info = wikipedia.summary(query,sentences=3)
                engine.say(info)
                print(info)
            except:
                engine.say('Sorry coudnt find what you were looking for ')
        elif command[1] == 'hands':
            port.write(b'3')
        elif command[1] == 'weight':
            port.write(b'6')
        elif command[1] == 'smash':
            port.write(b'5')
        elif command[1] == 'confused':
            port.write(b'4')
        elif command[1] == 'stop':
            port.write(b'4')
            global running
            engine.say('Shutting down ')
            running = False
        else:
            engine.say('Hey How  you doing ')
    else:
        engine.say('hey please Give an valid command ')
        print_current_commands()

def print_current_commands():
    print('1. fury play (video name) ')
    print('2. fury search (search query name)')
    print('3. fury give info (wikipedia topic)')
    print('4. fury stop')

running = True
while running:
    listen_for_command()
    engine.runAndWait()