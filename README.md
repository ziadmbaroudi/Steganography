# Hiding Messages in PNG files
This project is a demonstration of steganography. It uses Black and White PNG files to "hide" a text message. A new file is created with an image that, to the human eye, looks identical to the original.

## Code authors
Ziad Baroudi, as teacher, provided a scaffold
Students Sarah Ang, Rachel Botros and Lauren Karipidis completed the code
in 2017.

## Limitations of the code
This code is a result of a Year 10 (Grade 10) classroom project.
The code is not meant to be examplary and only allows messages made up
of lowercase letters in the standard English alphabet as well as spaces.
No punctuation can be included.

## What you need to run this project
You need to have Python 3 installed on your computer. Simply download the files provided here.

## Sample execution
At the command prompt, type the following:

  $python3 Bob.py
  $What message do you want to encode? (140 character limit): i want to see you
  $What is the name of the image file you want to use? bw_slippers.png

To read the messsage hidden in the new file "new_bw_slippers.png":
  $python3 Alice.py
  $How many characters are there to decode? 17
  $What is the name of the image file you want to use? new_bw_slippers.png
  i want to see you
