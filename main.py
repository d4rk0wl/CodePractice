from Structure import states, test, callsign_format
import random
import string
from UI import MainInterface


def callsign_generator():
    cs_format = callsign_format[random.randint(0, 6)]
    result = ""

    for char in cs_format:
        if char == 'S' or char == 'P':
            result += random.choice(string.ascii_letters).upper()
        else:
            result += str(random.randint(0, 9))

    return result


def generate(name, callsign, random_call):
    print(f"name - {name}")
    print(f"callsign - {callsign}")
    print(f"Random - {random_call}")

    print(callsign_generator())


def main():
    MainInterface(generate)


if __name__ == "__main__":
    main()
