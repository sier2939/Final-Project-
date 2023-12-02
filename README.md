# Final-Project-
A python program that finds what the best word to play in Wordle is and what word the user should play next.
Essentially the program does this by narrowing down to the best choices you have based on the first guest the user makes. 

How Wordle works:

Report

Instructions:
The program begins by asking the user " Enter the correct letters", assuming that the user has Wordle open then from there first guess they can simply enter all the letters that are correct. The program will then ask users to "Enter letters in the correct positions (use 'x' for unknown positions)". This is important because by knowing what words are in the correct psitions we can narrow down the choices significantly. Next it asks "Enter letters to exclude" this tells the what words to not include in the choices at all. finally it outputs the list of possible word choices for the user to try, then asks "Do you want to rerun the program?" where the user can repeat these instructions all 6 turns. 

problem/ question: 
You have only 6 attempts to guess the daily wordle word, with this program it will see what word might be best played next based on your first guess in a means to allow the user to find the word before the they run out of turns. 

Summary: (what the program does to arrive at the end result)
The program uses the function main that uses a while loop, to go through the txt file wordle-words and display the best choices to the user based on filtering questions asked for input. I started by initializing rerun to be equal to the value "yes" and the function excluded_letters to be " " which initializes an empty string to store letters that should be excluded. This came before the while loop. Inside the while loop I have code that reads the txt file and essentially cleans it. The while loop is so that the program will rerun if the user types yes, this allows them to keep using the program until they have run out of turns. Within the while loop I use multiple for loops and assign the variables correct_letters, matching_words, letter_positions, and excluded_words to certain inputs and created for loops for each of those that uses the function 'all' to create an argument that checks if the elements in the list is 'True' or 'False'. Then I was able to display the outputs using the variable names I created and the text file, as well as the initialization I did in the beginning with rerun. 







