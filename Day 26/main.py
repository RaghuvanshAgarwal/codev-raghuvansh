import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

user_input = input("What is your Name?\t")
user_input_nato_form = [nato_dict[letter] for letter in user_input.upper() if letter in nato_dict]
print(user_input_nato_form)
