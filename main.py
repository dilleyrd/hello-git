#!/usr/bin/env python3
"""
Simple command-line temperature converter.

Usage examples:
  python main.py c2f 100
  python main.py f2c 212
"""
import argparse
from temp_utils import c_to_f, f_to_c

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert temperatures between Celsius and Fahrenheit."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p1 = sub.add_parser("c2f", help="Convert Celsius to Fahrenheit")
    p1.add_argument("value", type=float, help="Temperature in Celsius")

    p2 = sub.add_parser("f2c", help="Convert Fahrenheit to Celsius")
    p2.add_argument("value", type=float, help="Temperature in Fahrenheit")

    return parser

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "c2f":
        result = c_to_f(args.value)
        print(f"{args.value} °C is {result:.2f} °F")
    elif args.command == "f2c":
        result = f_to_c(args.value)
        print(f"{args.value} °F is {result:.2f} °C")

if __name__ == "__main__":
    main()