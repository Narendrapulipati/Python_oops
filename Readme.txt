Laptop Shop Customer Program: without using Framwork
This Python program demonstrates inheritance by having a Customer class inherit from a shop class. It allows users to select a laptop brand (HP, Lenovo, or Dell) and input details like price, warranty, color, and RAM size. The program validates the brand and handles invalid price inputs by setting the price to 0. If the brand is unavailable, the program exits with an error message.

The Customer class collects user input, then calls the parent shop class constructor to initialize and later display the laptop details via show_details().

Usage:

Run the program.

Enter a valid brand.

Provide price range, warranty, color, and RAM size.

View the laptop details.

Requirements:

Python 3.x

A defined shop class with __init__ and show_details() methods.
