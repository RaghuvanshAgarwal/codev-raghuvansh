with open("./Input/Names/invited_names.txt") as invited_name:
    names_list = invited_name.read().split("\n")
    with open("./Input/Letters/starting_letter.txt") as letter_content:
        content = letter_content.read()
        for name in names_list:
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as output_letter:
                output_letter.write(content.replace("[name]", name))
