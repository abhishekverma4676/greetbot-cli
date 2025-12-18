#!/usr/bin/env python3
"""
GreetBot - A friendly CLI tool.
"""
import argparse


def greet(name: str) -> str:
    return f"Hello, {name}! GreetBot welcomes you."


def main():
    parser = argparse.ArgumentParser(description="GreetBot CLI")
    parser.add_argument("--name", required=True, help="Name of the person to greet")
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
