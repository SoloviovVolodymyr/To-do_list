import os
import argparse
import sys
import base_functions
import commands

def input_todo():
    todos = base_functions.view_todos()
    while True:
        user_action = input("Введіть допомога, для довідки: ")
        if not commands.dispatch(todos, user_action):
            break

def build_parser():
    parser = argparse.ArgumentParser(
        prog="cli.py", description="Todo: діалог або команда під час запуску."
    )
    return parser

def main():
    os.makedirs("data", exist_ok = True)
    if not os.path.exists(base_functions.FILEPATH):
        with open(base_functions.FILEPATH, "w", encoding="utf-8"):
            pass

    input_todo()

if __name__ == "__main__":
    main()

