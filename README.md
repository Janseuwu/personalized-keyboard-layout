# personalized-keyboard-layout
Creates a personalized keyboard layout for the user. It only looks at the letters and not any special characters.

The idea is to see how many times the user uses each letter and create a keyboard layout, that puts the most frequent letters on the easiest to reach keys. This will optimize writing speed a lot.

The idea was stolen from a friend, [linnnus](github.com/linnnus). He will probably make a proper version of this sometime in the future so keep an eye out in case you're interested. 

# Installation and usage
## Installation
Simply clone the repo with `git clone https://github.com/Janseuwu/personalized-keyboard-layout.git`

## Usage
The program takes samples from .txt files. Therefore, in order for the script to work properly, you need to put your .txt in the `samples` directory.

The .txt files should contain the text you want the program to create your personalized keyboard layout from.
*This can be multiple .txt files*

After creating your .txt files, simply run the script with `python3 main.py`

No `requirements.txt` is needed, since the program only uses `glob`, which is a standard library

# TODO
- Customize _entire_ keyboard instead of only letters
- Take into account keys that are used together or almost never used together
- Find original ideas instead of stealing linnnus's
