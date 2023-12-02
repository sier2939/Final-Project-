# Final-Project-
A python program that finds what the best word to play in Wordle is and what word the user should play next.
Essentially the program does this by narrowing down to the best choices you have based on the first guest the user makes. 

How Wordle works:

Report

Instructions:
The program begins by asking the user " Enter the correct letters", assuming that the user has Wordle open then from there first guess they can simply enter all the letters that are correct. The program will then ask users to "Enter letters in the correct positions (use 'x' for unknown positions)". This is important because by knowing what words are in the correct psitions we can narrow down the choices significantly. Next it asks "Enter letters to exclude" this tells the what words to not include in the choices at all. finally it outputs the list of possible word choices for the user to try, then asks "Do you want to rerun the program?" where the user can repeat these instructions all 6 turns. 

problem/ question: you have only 6 attempts to guess the daily wordle word, with this program it will see what word might be best played next based on your first guess in a means to allow the user to find the word before the they run out of turns. 

Summary: (what the program does to arrive at the end result)
Criteria:
Working code 

1. import valid-wordle-words.txt to the main file wordle.py (you dont have to covert into anything)
        based on the users first guess whatever words are apart of the solution, the program will ask for that input with the input it will read through the file and search for words containing the letters that are for sure apart of the solution, then if non of the words are the solution it will append them to game history so each guess after 6 turns that the user inputs the program will never output the same words. 
2. Create a function first_guess that outputs a word containing 'aeiou' to give users a starting place have this print the word they should use. 

3. create a function working_words that asks users what words are apart of the final solution, thefunction will read through the file and print out all possibilities for possible final word. If none are apart of it then use the first_guess function to give them a new word to try.

4. Another function best_choice will work to narrow down the choices based off position 


