# main file for the code


def main():
    rerun = "yes"

    excluded_letters= ""

    while rerun.lower() == "yes":
        with open("wordle-words.txt", "r") as f:
            words_list_string = f.read().strip('[]')
            words = [word.strip(" '") for word in words_list_string.split(',')]

    

        # Finds the matching words containing all the letters

        correct_letters = input("Enter the correct letters: ").lower()
        matching_words = [word for word in words if all(letter in word.lower() for letter in correct_letters)]
        
        #  Finds words with letters in the correct positions using enumerate to checks if the letters in the specified positions match the  letters in the word. The built in enumerate function can iterate over the string while keeping track of the elements which make it possible.
        
        letter_positions = input("Enter letters in the correct positions (use '*' for unknown positions): ").lower()
        matching_words = [word for word in matching_words if all(letter_positions[i] == '*' or letter_positions[i] == letter.lower() for i, letter in enumerate(word) if i < len(letter_positions))]

        # print(matching_words)

        #  Ignores words with the specifified letters
        
        excluded_lettersNew = input("Enter letters to exclude: ").lower()
        excluded_letters += excluded_lettersNew
        print(excluded_letters)
        matching_words = [word for word in matching_words if not any(letter in word.lower() for letter in excluded_letters)]

        # Displays the matching words...

        if matching_words:
            print("Words in the file:", ", ".join(matching_words))
        else:
            print("No matching words found.")

        rerun = input("Do you want to rerun the program? (yes/no): ")


main()
