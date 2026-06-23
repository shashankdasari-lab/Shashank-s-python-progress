"""2. String Analyzer ⭐
Problem Statement

Accept a string from the user and generate a complete analysis report.

Display
Total Length
First Character
Last Character
Uppercase Version
Lowercase Version
Number of vowels"""

string=str(input("Enter a string:"))
print("Length:",len(string))
print("Uppercasecase:",string.upper())
print("Lowercase:",string.lower())
print("First Character:",string[0])
print("Last Character:",string[-1])
