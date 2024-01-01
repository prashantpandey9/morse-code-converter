# morse_code/converter.py

import pygame
import time
from morse_code.constants import DOT_SOUND_FILE, DASH_SOUND_FILE

MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",
}


def text_to_morse(text):
    morse_code = ""
    for char in text.upper():
        if char == " ":
            morse_code += " "
        else:
            morse_code += MORSE_CODE_DICT[char] + " "
    return morse_code


def play_morse_code(morse_code):
    pygame.init()
    pygame.mixer.init()

    dot_duration = 0.2  # Duration of a dot
    dash_duration = 3 * dot_duration  # Duration of a dash
    space_duration = dot_duration  # Duration of space between words

    sound_speed = 20  # Speed of Morse code playback

    for symbol in morse_code:
        print(symbol)
        if symbol == ".":
            pygame.mixer.Sound(DOT_SOUND_FILE).play()
            time.sleep(dot_duration / sound_speed)
        elif symbol == "-":
            pygame.mixer.Sound(DASH_SOUND_FILE).play()
            time.sleep(dash_duration / sound_speed)
        elif symbol == " ":
            time.sleep(space_duration / sound_speed)

    pygame.mixer.quit()
