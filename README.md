# tempconv
A simple, smart CLI temperature conversion utility written in Python. 

## Dependencies
Python 3

## Purpose
Provide a simple command-line utility to quickly convert temperatures between Celsius and Fahrenheit units based upon semi-natural language input.

## Description
This is a simple CLI utility for conversion of temperatures between Celsius and Fahrenheit units. It features rudimentary natural language intelligence:
- The program understands that Celsius input is to be converted to Fahrenheit output and vice versa
- The program cares not whether the unit input is uppercase or lowercase (10c = 10C)
- The program is unbothered by spaces in the input ("50  F " = "50F")
- The program accepts both integer and floating-point inputs

Similarly, the program, which presents its output as an integer, is aware of precision:
- If the program must round the output, it presents the result as "approximate."
- If the program sees no remainder (no non-zero digits in the decimal places), it presents the result as a precise integer.

Finally, the program returns a proper error message for bad input instead of crashing.

## Installation and Use
Simply run the **tempconv.py** file:

`python3 tempconv.py`

## Future Development
- Streamline the code a bit more.
- Dress up the output with color or other formatting.
- Potentially, add Kelvin conversion
