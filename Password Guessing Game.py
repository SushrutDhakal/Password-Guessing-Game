#written parts
#more calculations are needed

#Importing libraries
import tkinter
import random

#Getting a random 4 letter password from A-F
def generate_password (): 

     global password

     letters = 'ABCDEF' #range of the letters 
     blank_1 = random.choice (letters)
     blank_2 = random.choice (letters)
     blank_3 = random.choice (letters)
     blank_4 = random.choice (letters)
     password = [blank_1, blank_2, blank_3, blank_4] #4 letter password 

     #print (password) #printing password (un-comment for testing purposes)

#After the feedback is sent, saying bye to the user 
def goodbye_message ():

     direct_input = enter_feedback.get ()
     user_feedback = str (direct_input)
     feedback_file = "Feedback.txt"  #Saving feedback in a file for the dev team to see and fix
     writing_feedback = open (feedback_file, "a")
     writing_feedback.write (f'{user_feedback} \n')
     writing_feedback.close ()

     goodbye_frame = tkinter.Frame (main_window) #After the user sends feedback message
     goodbye_frame.grid (row = 17, column = 0)
     goodbye_label = tkinter.Label (goodbye_frame, text = 'Thanks for letting us know!' 
                                    f' Our team will fix this as soon as possible. Goodbye! 👋', font = ("Times", 13)) 
     goodbye_label.grid (row = 17, column = 0)

#Game feedback entry place
def feedback_entry ():

     #globalize
     global enter_feedback 

     feedback_frame = tkinter.Frame (main_window) #After rating is entered, they can enter feedback
     feedback_frame.grid (row = 15, column = 0)
     filler_label = tkinter.Label (feedback_frame, text = '')
     filler_label.grid (row = 15, column = 0) 
     feedback_label = tkinter.Label (feedback_frame, text = 'Thanks for letting us know! ' 
                                     f'Please enter any feedback you may have: ') #Ask user to send feedback 
     feedback_label.grid (row = 16, column = 0)

     enter_feedback = tkinter.Entry (feedback_frame, bg = "light grey", width = '60')
     enter_feedback.grid (row = 16, column = 1) 
     enter_feedback.insert (0, "Enjoyed the app!") #Default message
     submit_feedback = tkinter.Button (feedback_frame, text = "Send", command = goodbye_message) #Send the message to the dev team
     submit_feedback.grid (row = 16, column = 2 )

#After game is ended, either winner loses or wins
def game_over ():

     #globalize
     global rating_selected, display_password

     over_frame = tkinter.Frame (main_window)
     over_frame.grid (row = 10, column = 0) 

     filler_label = tkinter.Label (over_frame, text = '') #filler label for a blank row of space 
     filler_label.grid (row = 10, column = 0) 

     display_password = password[0] + password[1] + password [2] + password [3] #so the password is displayed as ABCD and not ['A', 'B', 'C', 'D'] 
     player_score = 0 #intial player score when game is started

     if (feedback == ["✅", "✅", "✅", "✅"]) and (difficulty_choice == 'H'): #points if user wins on hard mode 
          player_score = guess_limit * 150

     if (feedback == ["✅", "✅", "✅", "✅"]) and (difficulty_choice == 'M'): #points if user wins on hard mode 
          player_score = guess_limit * 100

     if (feedback == ["✅", "✅", "✅", "✅"]) and (difficulty_choice == 'E'): #points if user wins on hard mode 
          player_score = guess_limit * 50

     if (feedback == ["✅", "✅", "✅", "✅"]): #if the player wins (the feedback is all ✅)
              winner = tkinter.Label (over_frame, text = f'Congratulations, you have cracked the password..' 
                                     f'YOU WIN! You scored {player_score} points!', 
                                      font = ("Times", 15, "bold"), bg = 'lime green')
              winner.grid (row = 11, column = 0)

     green_check_score = 0 #Intial values of the 'partial scores' 
     check_score = 0 
     wrong_score = 0 
     #Even if the player loses, they get points depending on how close their feedback was to the actual password

     if ("✅" in feedback): #If feedback has a ✅
          if (difficulty_choice == 'H'):
               green_check_score = 30
          elif (difficulty_choice == 'M'):
               green_check_score = 25
          elif (difficulty_choice == 'E'):
               green_check_score = 20

     if ("✔" in feedback): #If feedback has a ✔
          if (difficulty_choice == 'H'):
               check_score = 15
          elif (difficulty_choice == 'M'):
               check_score = 10
          elif (difficulty_choice == 'E'):
               check_score = 5

     if (feedback [0] == "✖") and (feedback [1] == "✖") and (feedback [2] == "✖") and (feedback [3] == "✖"): #If feedback is just ✖'s
          wrong_score = 0

     if (guess_limit == 0): #If they run out of guesses. 
          loss_player_score = green_check_score + check_score + wrong_score #adding the 3 partial scores
          game_lost = tkinter.Label (over_frame, text = f'Sorry, you are out of guesses.. YOU LOSE! The password was ' 
                                   f'{display_password}. You scored {loss_player_score} points!', 
                                font = ("Times", 15, "bold"), bg = '#fb7b7b')
          game_lost.grid (row = 11, column = 0)

     filler = tkinter.Label (over_frame, text = '') #filler label for a blank row of space 
     filler.grid (row = 12, column = 0)

     rate_message = tkinter.Label (over_frame, text = 'Please take a quick minute and rate this app out of 5!') #Asks user to rate app 
     rate_message.grid (row = 13, column = 0)

     rating_selected = tkinter.StringVar () 

     rating_frame = tkinter.Frame (main_window)
     rating_frame.grid (row = 14, column = 0) 

     #The 5 rating options
     one_stars = tkinter.Radiobutton (rating_frame, text = '✰', value = '1', anchor = "w", 
                                        bg = "white", variable = rating_selected)
     one_stars.grid (row = 14, column = 1)

     two_stars = tkinter.Radiobutton (rating_frame, text = '✰✰', value = '2', anchor = "w", 
                                        bg = "#d2f9d2", variable = rating_selected)
     two_stars.grid (row = 14, column = 2)

     three_stars = tkinter.Radiobutton (rating_frame, text = '✰✰✰', value = '3', anchor = "w", 
                                        bg = "white", variable = rating_selected)
     three_stars.grid (row = 14, column = 3)

     four_stars = tkinter.Radiobutton (rating_frame, text = '✰✰✰✰', value = '4', anchor = "w", 
                                        bg = "#d2f9d2", variable = rating_selected)
     four_stars.grid (row = 14, column = 4)

     five_stars = tkinter.Radiobutton (rating_frame, text = '✰✰✰✰✰', value = '5', anchor = "w", 
                                        bg = "white", variable = rating_selected)
     five_stars.grid (row = 14, column = 5)

     five_stars.invoke () #Intial selected rating

     submit_frame = tkinter.Frame (main_window)
     submit_frame.grid (row = 15, column = 0)   

     rating_submit_button = tkinter.Button (submit_frame, text = "Submit", font = 'Times', 
                                             command = feedback_entry, anchor = 'center') #Submit rating 
     rating_submit_button.grid (row = 15, column = 0 )

#Playing the main game 

def play_game ():

     #globalize
     global guess_limit, feedback, player_score, difficulty_choice

     direct_input = letter1.get () #getting the user guesses
     first_letter = str (direct_input)
     direct_input = letter2.get ()
     second_letter = str (direct_input)
     direct_input = letter3.get ()
     third_letter = str (direct_input)
     direct_input = letter4.get ()
     fourth_letter = str (direct_input)

     player_guess = [first_letter, second_letter, third_letter, fourth_letter] #holds all user guesses
     feedback = ["✖", "✖", "✖", "✖"] #intial feedback 

#generating the feedback based on player guesses
     if (player_guess [0] in password) and (player_guess [0] != password [0]): 
          feedback [0] = '✔'

     if (player_guess [1] in password) and (player_guess [1] != password [1]):
          feedback [1] = '✔'

     if (player_guess [2] in password) and (player_guess [2] != password [2]):
          feedback [2] = '✔'

     if (player_guess [3] in password) and (player_guess [3] != password [3]):
          feedback [3] = '✔'
          
     if (player_guess [0] == password [0]):
          feedback [0] = '✅'

     if (player_guess [1] == password [1]):
          feedback [1] = '✅'

     if (player_guess [2] == password [2]):
          feedback [2] = '✅'

     if (player_guess [3] == password [3]):
          feedback [3] = '✅'

     feedback1 = tkinter.Label (guessing_frame, text = "", bg = "azure2") 
     feedback1.grid (row = 8 , column = 9)

     feedback1.configure (text = f'Clues: {feedback [0]} {feedback [1]} { feedback [2]} {feedback [3]}') #display feedback

     if (feedback == ["✅", "✅", "✅", "✅"]) or (guess_limit == 0): #if user guesses password
          game_over ()
     else:
          guess_limit -= 1 #Take one away from guess counter 
          retry_frame = tkinter.Frame (main_window)
          retry_frame.grid (row = 9, column = 0)
          retry_label = tkinter.Label (retry_frame, text = f'\nUse the clues and try again!' 
                                        f'You have {guess_limit} attempts left') #Tell them number of guesses left
          retry_label.grid (row = 9, column = 0)    

#Setting up the game screen with textboxes and difficulty

def game_setup ():

     #globalize
     global letter1, letter2, letter3, letter4
     global first_letter, second_letter, third_letter, fourth_letter
     global difficulty_choice, guessing_frame, guess_limit

     difficulty_choice = difficulty_selected.get () #guess limit depending on user selection
     if (difficulty_choice == 'E'):
          guess_limit = 15
     if (difficulty_choice == 'M'):
          guess_limit = 11
     if (difficulty_choice == 'H'):
          guess_limit = 7

     guessing_frame = tkinter.Frame (main_window)
     guessing_frame.grid (row = 7, column = 0)
     filler_label = tkinter.Label (guessing_frame, text = '') #filler label for an empty row 
     filler_label.grid (row = 7, column = 0) 

     #Letter entry fields 
     letter1 = tkinter.Entry (guessing_frame, bg = "light grey", fg = "black", width = 10)
     letter1.grid (row = 8, column = 0) 
     letter2 = tkinter.Entry (guessing_frame, bg = "light grey", fg = "black", width = 10)
     letter2.grid (row = 8, column = 1) 
     letter3 = tkinter.Entry (guessing_frame, bg = "light grey", fg = "black", width = 10)
     letter3.grid (row = 8, column = 2) 
     letter4 = tkinter.Entry (guessing_frame, bg = "light grey", fg = "black", width = 10)
     letter4.grid (row = 8, column = 3) 
     letter_submit = tkinter.Button (guessing_frame, text = "Enter", command = play_game)
     letter_submit.grid (row = 8, column = 5 )

     letter1.insert (0, "A") #Intial value inside of textboxes (Validation)
     letter2.insert (0, "B")
     letter3.insert (0, "C")
     letter4.insert (0, "D")

     filler_label = tkinter.Label (guessing_frame, text = '                        ') #filler label for making it centered
     filler_label.grid (row = 8, column = 6) 

#First function when game is run 

def main ():
     
     #Globalize Variables
     global main_window, difficulty_selected

     #Tkinter implementation
     main_window = tkinter.Tk () #Basic GUI outlines 
     main_window.geometry ("800x510")
     main_window.title ("Code Cracker: Password Guessing Game")

     generate_password () #generation password at start of game 

     title_frame = tkinter.Frame (main_window)
     title_frame.grid (row = 0, column = 0)

     title_label = tkinter.Label (title_frame, text = "---Code Cracker: Password Guessing Game---", #Title
                                              bg = "black", fg = 'lime green', font = ("Times", 22, "bold"))
     title_label.grid (row = 0, column = 0)

     heading_frame = tkinter.Frame (main_window) 
     heading_frame.grid (row = 1, column = 0)

     filler_label = tkinter.Label (heading_frame, text = '_____________________________________________________________________' 
                                   f'___________________________________________________________________________________________')
     filler_label.grid (row = 1, column = 0) 

     #Heading text with instructions
     heading1_label = tkinter.Label (heading_frame, text = f'Code cracker is a single player game against a generated password.' 
                                     f' A secret 4 letter code from letters A-F is generated.', 
                                     font = ("Times", 12))
     heading1_label.grid (row = 2, column = 0) 

     heading2_label = tkinter.Label (heading_frame, text = 'Your job is to crack the code by making guesses.' 
                                     f' After each guess, clues will be given:', font = ("Times", 12))
     heading2_label.grid (row = 3, column = 0) 

     heading3_label = tkinter.Label (heading_frame, bg = '#33CC32', text = '✖ = not in the code | ✔ = in the code but in the wrong position |' 
                                     f' ✅ = in the code and in the right position. \nGOOD LUCK!', font = ("Times", 12, "bold"))
     heading3_label.grid (row = 4, column = 0) 

     filler_label = tkinter.Label (heading_frame, text = '')
     filler_label.grid (row = 5, column = 0) 

     #Button to begin the game 
     play_button = tkinter.Button (heading_frame, text = "PLAY", bg = "#d2f9d2", font = 'Times', width = '30', command = game_setup) 
     play_button.grid (row = 6, column = 0 )

     difficulty_frame = tkinter.Frame (main_window) 
     difficulty_frame.grid (row = 6, column = 0)
     difficulty_selected = tkinter.StringVar ()

     selection_label = tkinter.Label (difficulty_frame, text = 'Select your difficulty: ') #Selection of difficulty 
     selection_label.grid (row = 6, column = 0) 

     #Difficulty Section
     easy = tkinter.Radiobutton (difficulty_frame, text = 'Easy [15 guesses]', width = '20', 
                                 value = 'E', anchor = "w", bg = "white", variable = difficulty_selected)
     easy.grid (row = 6, column = 1)

     medium = tkinter.Radiobutton (difficulty_frame, text = 'Medium [11 guesses]', width = '20', 
                                   value = 'M', anchor = "w", bg = "white", variable = difficulty_selected)
     medium.grid (row = 6, column = 2)

     hard = tkinter.Radiobutton (difficulty_frame, text = 'Hard [7 guesses]', width = '20', 
                                 value = 'H', anchor = "w", bg = "white", variable = difficulty_selected)
     hard.grid (row = 6, column = 3)
     easy.invoke () #Intial section

     main_window.mainloop () #Looping the main window 
main()