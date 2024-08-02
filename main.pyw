from Structure import first_greeting, second_greeting, ota_phrases, states, ending_templates, parks, callsign_format, \
    ragchew_phrases, names
from random import randint, choice, shuffle
import string
from UI import MainInterface


def callsign_generator():
    cs_format = callsign_format[randint(0, 6)]
    callsign = ""

    for char in cs_format:
        if char == 'S' or char == 'P':
            callsign += choice(string.ascii_letters).upper()
        else:
            callsign += str(randint(0, 9))

    return callsign


def generate_ending(ending_callsign, ending_randsign, name):
    def generate_7x():
        if randint(0, 1) == 0:
            return '72'
        else:
            return '73'

    return ending_templates[randint(0, len(ending_templates) - 1)].format(
        callsign=ending_callsign,
        br=generate_7x(),
        randsign=ending_randsign,
        name=name
    )


def ragchew_generator(params):
    phrase_list = []

    if params['mode'] == "All":
        array_length = 50
    else:
        array_length = 100

    for item in range(array_length):
        if params['random']:
            callsign = callsign_generator()
        else:
            callsign = params['callsign']

        randsign = callsign_generator()

        selected_phrase = ragchew_phrases[randint(0, len(ragchew_phrases) - 1)]

        phrase_list.append(selected_phrase.format(
            callsign=callsign,
            randsign=randsign,
            state=states[randint(0, len(states) - 1)],
            sig=f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}",
            randname=names[randint(0, len(names) - 1)],
            name=names[randint(0, len(names) - 1)],
            ending=generate_ending(callsign, randsign, params['name'])
        ).upper())

    return phrase_list


def ota_phrase_generator(params):
    phrase_list = []

    def generate_greeting1(greeting_callsign):
        return first_greeting[randint(0, len(first_greeting) - 1)].format(callsign=greeting_callsign,
                                                                          name=params['name'],
                                                                          randsign=callsign_generator())

    def generate_greeting2(greeting2_call, greeting2_rand):
        return second_greeting[randint(0, len(second_greeting) - 1)].format(callsign=greeting2_call,
                                                                            randsign=greeting2_rand)

    def generate_ota():
        if randint(0, 1) == 0:
            return f"at {parks[randint(0, len(parks) - 1)]}"
        else:
            return ""

    if params['mode'] == "All":
        array_length = 50
    else:
        array_length = 100

    for item in range(array_length):
        if params['random']:
            callsign = callsign_generator()
        else:
            callsign = params['callsign']

        randsign = callsign_generator()

        selected_phrase = ota_phrases[randint(0, len(ota_phrases) - 1)]

        phrase_list.append(selected_phrase.format(
            greeting1=generate_greeting1(callsign),
            greeting2=generate_greeting2(callsign, randsign),
            sig=f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}",
            ota=generate_ota(),
            randsign=randsign,
            callsign=callsign,
            state=states[randint(0, len(states) - 1)],
            ending=generate_ending(callsign, randsign, params['name'])
        ).upper())

    return phrase_list


def main():
    def all_generator(params, callback):
        phrases = []
        match params['mode']:
            case "All":
                phrases.extend(ota_phrase_generator(params))
                phrases.extend(ragchew_generator(params))
            case "POTA/SOTA":
                phrases.extend(ota_phrase_generator(params))
            case "Ragchew":
                phrases.extend(ragchew_generator(params))

        shuffle(phrases)

        with open(f"{params['save_location']}/output.txt", 'w') as file:
            if params['separated']:
                result = ','.join(phrases)
                print(result, file=file)
            else:
                result = ""
                for element in phrases:
                    result += f"{element} "
                print(result, file=file)

        callback()

    MainInterface(all_generator)


if __name__ == "__main__":
    main()
