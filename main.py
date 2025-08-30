#!/usr/bin/env python3
"""
Simple command-line temperature converter.

Usage examples:
  python main.py c2f 100
  python main.py f2c 212
"""

import argparse
from temp_utils import c_to_f, f_to_c, c_to_k, k_to_c

# Build the argument parser
def build_parser() -> argparse.ArgumentParser:
    # Create the top-level parser
    parser = argparse.ArgumentParser(
        description="Convert temperatures between Celsius and Fahrenheit."
    )
    # Add subparsers for the two conversion commands
    sub = parser.add_subparsers(dest="command", required=True)
    
    # Subparser for Celsius to Fahrenheit
    p1 = sub.add_parser("c2f", help="Convert Celsius to Fahrenheit")
    p1.add_argument("value", type=float, help="Temperature in Celsius")

    # Subparser for Fahrenheit to Celsius
    p2 = sub.add_parser("f2c", help="Convert Fahrenheit to Celsius")
    p2.add_argument("value", type=float, help="Temperature in Fahrenheit")

    # Subparser for Celsius to Kelvin
    p3 = sub.add_parser("c2k", help="Convert Celsius to Kelvin")
    p3.add_argument("value", type=float, help="Temperature in Celsius")

    # Subparser for Kelvin to Celsius
    p4 = sub.add_parser("k2c", help="Convert Kelvin to Celsius")
    p4.add_argument("value", type=float, help="Temperature in Kelvin")

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
    elif args.command == "c2k":
        result = c_to_k(args.value)
        print(f"{args.value} °C is {result:.2f} K")
    elif args.command == "k2c":
        result = k_to_c(args.value)
        print(f"{args.value} K is {result:.2f} °C")

if __name__ == "__main__":
    main()