# main file for the code
# A python program that finds what the best word to play in Wordle is and what word the user should play next.

# rerun: It is set to the string "yes". This variable seems to be used to control a loop later in the code.
# excluded_letters: It is initialized as an empty string. The purpose of this variable is not clear from the provided code snippet.



def main():
    rerun = "yes"

    excluded_letters= ""

    while rerun.lower() == "yes":
        with open("wordle-words.txt", "r") as f:
            words_list_string = f.read().strip('[]')
            words = [word.strip(" '") for word in words_list_string.split(',')]

       # words_list_strin  this reads the content of the file, removes leading and trailing square brackets
       # words splits the modified string into a list of words. Each word is then stripped of leading and trailing spaces and single quotes 

        # Finds the matching words containing all the letters using all by filtering a list of words based on the user-input correct letters, and it creates a new list matching_words containing only the words that contain all the correct letters

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

        #  excluded_lettersNew are added to the existing excluded_letters string. This allows the program to make a list of letters excluded from matching words.
       
        # For each word in matching_words, it checks if any of the letters in excluded_letters are present in the word (ignoring case)
        # Words containing any excluded letters are excluded from the matching_words list.

        # Displays the matching words...

        if matching_words:
            print("Words in the file:", ", ".join(matching_words))
        else:
            print("No matching words found.")

        rerun = input("Do you want to rerun the program? (yes/no): ")

    print("congratulations on finding the word!")
main()


#  The interesting component of my program is that it is in a while loop so its just repeating the same task over and over again until it finds the best choice for the users wordle guesses. Also the use of all and enumerate to be selective with the words 

# for future improvements I can add a feature that would exclude the words with correct letters that are in the wrong positions so the user wouldnt have to think about it. 
# Also to further improve it the program would simply provide a one possible answer. 