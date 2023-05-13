import glob

def text_data():
    """ Fetch all the .txt files and create a string from the contents of every .txt file in the directory """

    sample_text_files = glob.glob("*.txt") # create a list with each .txt file in the dir
    sample_text = "" # create empty string to concatenate to later
    for file in sample_text_files: # open each .txt file in the list and concatenate the contents to sample_text
        with open(file, "r") as f:
            text = f.read().lower() # readlines and convert to lowercase
            sample_text = sample_text + text

    sample_text = sample_text.replace(" ", "").replace("\n", "") # make the string one continuous line of characters
    return sample_text

def find_frequencies():
    """ Finds the frequencies of each letter """

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sample_text = text_data()
    frequencies = {
            'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
            'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
            }
    
    # count letters and update dict
    for letter in sample_text:
        if letter not in alphabet:
            continue
        else:
            frequencies[letter] += 1

    frequencies = [(l, f) for l, f in frequencies.items()] # convert the dict to a list of tuples
    frequencies = sorted(frequencies, key=lambda x: x[1], reverse=True) # sort the tuples from high to low
    return frequencies

def create_layout():
    """ Creates the optimized layout with the gathered data """

    letters_freq = find_frequencies()
    # represent the keyboard layout as a 1d array
    kb = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             '10', '11', '12', '13', '14', '15', '16', '17', '18',
               '19', '20', '21', '22', '23', '24', '25'
        ]
    # (totally not accurate but not far off ig :D)
    best_keys_order = [10, 11, 12, 13, 15, 16, 17, 18, 14, 6, 2, 3, 22, 23, 24, 21, 1, 7, 25, 4, 5, 20, 8, 9, 19, 0]
    # replace the indexes in 'kb' with the corresponding letters
    for i, num in enumerate(best_keys_order):
        kb[num] = letters_freq[i][0]

    # prints the keyboard layout in a pretty format :3 (💀)
    kb_layout = ""
    for i, letter in enumerate(kb):
        match i:
            case 9:
                kb_layout = kb_layout + f"[{letter}]\n "
            case 18:
                kb_layout = kb_layout + f"[{letter}]\n  "
            case _:
                kb_layout = kb_layout + f"[{letter}]"

    print(kb_layout)

if __name__ == "__main__":
    create_layout()
