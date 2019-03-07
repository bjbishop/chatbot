#!/usr/bin/env python3

import random
from name_game import name_game_printer

name = None


def get_name(n):
    global name
    global responses
    print(f"Hello {n}, nice to meet you!  I won't remember your name though...")
    name = n
    i = responses.index({"What is your name?": get_name})
    del responses[i]


def affirmative_responses(answer):
    answer = answer.lower()
    try:
        if [
                "yes",
                "ok",
                "sure",
                "fine",
        ].index(answer) is not None:
            return True
    except ValueError:
        return False


def get_color(color):
    print(f"{color} is a pretty color")


def get_job(job):
    print(f"Being a {job} is really in demand right now")


def get_marriage(marriage):
    if affirmative_responses(marriage):
        print("Congratulations!")
    else:
        print("Neither am I!")


def get_only_child(response):
    if affirmative_responses(response):
        print("no way, me too!")
    else:
        print("yeah I wish I were an only child")


def get_siblings(response):
    if not affirmative_responses(response):
        print("no way, me too!")
    else:
        print("Ah, so much drama around Christmas time")


def chat_prompts():
    global responses
    return(random.choice(responses))


responses = [
    {"What is your name?": get_name},
    {"What is your favorite color?": get_color},
    {"So what is your occupation?": get_job},
    {"Are you married?": get_marriage},
    {"Are you an only child?": get_only_child},
    {"Let's play the name game!  What name should I use?": name_game_printer},
    {"Do you have any brothers or sisters?": get_siblings},
]


def exit_messages():
    responses = [
        "\nFINE fine... jeez",
        "\nI'm outta here",
        "\nOk be that way",
        "\nSame to you, pal",
        "\nI didn't want to talk to you anyway",
        "\nFine, I'm bored",
    ]
    return(random.choice(responses))


answer = ""

if __name__ == "__main__":
    while answer != 'exit' and answer != 'quit':
        prompt = chat_prompts()
        print(list(prompt.keys())[0])
        try:
            if name is None:
                answer = input('--> ').lower()
            else:
                answer = input(f"{name}--> ").lower()
            list(prompt.values())[0].__call__(answer)
        except EOFError:
            print(exit_messages())
            break
        except KeyboardInterrupt:
            print(exit_messages())
            break
        if answer == "":
            print("Come on.")
            print(answer)
    else:
        print("See you later!")
