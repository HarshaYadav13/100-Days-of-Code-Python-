import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(data_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    name = input("Enter your name: ").upper()
    try:
        nato_dict = {letter: data_dict[letter] for letter in name if letter != " "}
    except KeyError:
        print('Sorry, only write alphabets to get the result.')
        generate_phonetic()
    else:
        print(nato_dict)


generate_phonetic()
