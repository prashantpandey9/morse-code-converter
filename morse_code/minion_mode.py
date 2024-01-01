# morse_code/minion_mode.py
import argparse
from morse_code.converter import text_to_morse, play_morse_code
from morse_code.constants import DOT_SOUND_FILE, DASH_SOUND_FILE


def text_to_morse_cli():
    parser = argparse.ArgumentParser(
        description="Convert text to Morse code and play it in Minion style."
    )
    parser.add_argument("text", help="The text to convert to Morse code")

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--play", action="store_true", help="Play the Morse code as sound"
    )

    args = parser.parse_args()

    text = args.text
    morse_code = text_to_morse(text)

    print(f"Text: {text}")
    print(f"Morse Code: {morse_code}")

    if args.play:
        play_morse_code(morse_code, DOT_SOUND_FILE, DASH_SOUND_FILE)


if __name__ == "__main__":
    text_to_morse_cli()
