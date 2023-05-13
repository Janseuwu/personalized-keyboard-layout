# personalized-keyboard-layout
Creates a personalized keyboard layout for the user. It only looks at the letters and not any special characters.

The idea was stolen from a friend, [linnus](github.com/linnnus). He will probably make a proper version of this sometime in the future

# Installation and usage
## Installation
Simply clone the repo with `git clone https://github.com/Janseuwu/personalized-keyboard-layout.git`

## Usage
The program takes samples from .txt files. Therefore, in order for the script to work properly, you need to put your .txt in the same directory as the script.
The .txt files should contain the text you want the program to create your personalized keyboard layout for from.
This can be multiple .txt files. 
After creating your .txt files, simply run the script with `python3 main.py`

No `requirements.txt` is needed, since the program only uses `glob`, which is a standard library
