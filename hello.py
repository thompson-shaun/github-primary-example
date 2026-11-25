"""A tiny application for the Torii GitHub-primary walkthrough."""
import argparse


def greet(name):
    return f"Hello, {name}!"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", nargs="?", default="world")
    print(greet(parser.parse_args().name))


if __name__ == "__main__":
    main()
