#!C:\Program Files\Git\bin\sh.exe
# Andy Theriault - 10.16.2024
# ISS 212 CS Scripting - WK 5 - Bash Review
# Bash Script that takes input from the user and outputs a string using 2 inputs
# Takes input from the user and assigns to variables.

echo "What is your first name?"
read -r firstname #user input

echo "What is your last name?"
read -r lastname #user input
#echo the captured data that is stored in the variables
echo "Your first name is ${firstname} and your last name is ${lastname}"

