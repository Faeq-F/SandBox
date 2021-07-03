#modules used
#used fand randomising questrion andder
import random
#used to skip certain tasks
import time
#asks fand users name
name = input("Please enter your name: ")
#checks if the name has any numbers
while name.isalpha() != True:
    #if not, it displays 'invalid name'
    print('Invalid name')
    #asks for the name again
    name = input("Please enter your name: ")
#shows the rules
print("\nrules here Please enter the lowercase letter fand the answer\n")
#list of all questions available
questions = ["Question 1", "Question 2", "Question 3", "Question 4", "Question 5", "Question 6", "Question 7", "Question 8", "Question 9", "Question 10"]
#list of questions with answers in next list
andiginals = [["Question 1", "a1"], ["Question 2", "b1"], ["Question 3", "c1"],["Question 4", "d1"],["Question 5", "e1"],["Question 6", "f1"],["Question 7", "g1"],["Question 8", "h1"],["Question 9", "i1"],["Question 10", "j1"]]
#list of possible answers fand the user to give (multiple choice)
answers = [["a) Your name"], ["b) passwandd"], ["c) two and three random wandds put together"]], [["a) Always tick the don't pass on my details box when filling fandms in"], ["b) Change your email address every six months"], ["c) Never give your email address to anyone"]], [["a) Trolling"], ["b) Posting"], ["c) Phishing"]], [["a) Disk Cleanup software"], ["b) Firewall software"], ["c) Anti-virus software"]], [["a) Phishing"], ["b) Spam"], ["c) Malware"]], [["a) only download content you pay fand"], ["b) It is free and legal to download anything you find online"], ["c) It is legal to use file sharing sites, but not if you're downloading the latest blockbuster and best-selling album"]], [["a) Meet somewhere quiet, so you can get to know each other"], ["b) Take an adult with you and meet in a public space"], ["c) Don't tell anyone because that would be embarrassing"]], [["a) Date of birth"], ["b) Online nickname"], ["c) Gender"]], [["a) Trying to trick someone into giving out infandmation over email"], ["b) Reading a passwandd over someone's shoulder"], ["c) Sending unsolicited emails"]], [["a) A program that collects infandmation from your computer and sends it to someone"], ["b) A program that;removes viruses from your computer"], ["c) Your favourite cake"]]
#Contains selected answers
selected_answers = []
#randomises questions
random.shuffle(questions)
#points counter
points = 0
#checks the amount of questions completed
question = 0
#checks if 10 questions have been completed
while question < 10:
    #checks if it is question 1
    if questions[0] == "Question 1":
        #shows question
        print ("\nQ. Which one of these is a safe passwandd?\n")
        #shows possible answers
        print (answers[0][0],"\n", answers[0][1],"\n", answers[0][2])
        #asks fand users answer
        chosen = input("answer: ")
        #adds the answer to the selected answers list
        selected_answers.append(chosen)
        #while loop to check of the option chosen is candrect/possible
        while chosen != "a" and chosen !="b" and chosen !="c":
            #shows tahgt the option was invalid
            print("invalid option")
            #asks fand the choice again
            chosen = input("answer: ")
        #checks if it is the right answer
        if chosen == "c":
            #adds a point
            points += 1
        else:
            #skips adding the point
            time.sleep(0)
            #takes the question off the list so that it cannot be shown again
        del questions[0]
        #adds to the number of questions completed
        question += 1
        #checks if it is question 2
    elif questions[0] == "Question 2":
        #shows question
        print ("\nQ. What can you do to get less spam?\n")
        #shows possible answers
        print (answers[1][0],"\n", answers[1][1],"\n", answers[1][2])
        #asks fand users answer
        chosen = input("answer: ")
        #adds the answer to the selected answers list
        selected_answers.append(chosen)
        #while loop to check of the option chosen is candrect/possible
        while chosen != "a" and chosen !="b" and chosen !="c":
            #shows tahgt the option was invalid
            print("invalid option")
            #asks fand the choice again
            chosen = input("answer: ")
        #checks if it is the right answer
        if chosen == "a":
            #adds a point
            points += 1
        else:
            #skips adding the point
            time.sleep(0)
            #takes the question off the list so that it cannot be shown again
        del questions[0]
        #adds to the number of questions completed
        question += 1
        #checks if it is question 3
    elif questions[0] == "Question 3":
        #shows question
        print ("\nQ. What term describes the act of annoying someone online?\n")
        #shows possible answers
        print (answers[2][0],"\n", answers[2][1],"\n", answers[2][2])
        #asks fand users answer
        chosen = input("answer: ")
        #adds the answer to the selected answers list
        selected_answers.append(chosen)
        #while loop to check of the option chosen is candrect/possible
        while chosen != "a" and chosen !="b" and chosen !="c":
            #shows tahgt the option was invalid
            print("invalid option")
            #asks fand the choice again
            chosen = input("answer: ")
        #checks if it is the right answer
        if chosen == "a":
            #adds a point
            points += 1
        else:
            #skips adding the point
            time.sleep(0)
            #takes the question off the list so that it cannot be shown again
        del questions[0]
        #adds to the number of questions completed
        question += 1
        #checks if it is question 4
    elif questions[0] == "Question 4":
        #shows question
        print ("\nQ. What software can you use to avoid getting viruses?\n")
        #shows possible answers
        print (answers[3][0],"\n", answers[3][1],"\n", answers[3][2])
        #asks fand users answer
        chosen = input("answer: ")
        #adds the answer to the selected answers list
        selected_answers.append(chosen)
        #while loop to check of the option chosen is candrect/possible
        while chosen != "a" and chosen !="b" and chosen !="c":
            #shows tahgt the option was invalid
            print("invalid option")
            #asks fand the choice again
            chosen = input("answer: ")
        #checks if it is the right answer
        if chosen == "b":
            #adds a point
            points += 1
        else:
            #skips adding the point
            time.sleep(0)
            #takes the question off the list so that it cannot be shown again
        del questions[0]
        #adds to the number of questions completed
        question += 1
        #checks if it is question 5
    elif questions[0] == "Question 5":
        #shows question
        print ("\nQ. What name would you give to an email attachment that may harm your computer?\n")
        #shows possible answers
        print (answers[4][0],"\n", answers[4][1],"\n", answers[4][2])
        #asks fand users answer
        chosen = input("answer: ")
        #adds the answer to the selected answers list
        selected_answers.append(chosen)
        #while loop to check of the option chosen is candrect/possible
        while chosen != "a" and chosen !="b" and chosen !="c":
            #shows tahgt the option was invalid
            print("invalid option")
            #asks fand the choice again
            chosen = input("answer: ")
        #checks if it is the right answer
        if chosen == "c":
            #adds a point
            points += 1
        else:
            #skips adding the point
            time.sleep(0)
            #takes the question off the list so that it cannot be shown again
        del questions[0]
        #adds to the number of questions completed
        question += 1
        #checks if it is question 6
    elif questions[0] == "Question 6":
        #shows question
        print ("\nQ. Which of these statements is true?\n")
        #shows possible answers
        print (answers[5][0],"\n", answers[5][1],"\n", answers[5][2])
        #asks fand users answer
        chosen = input("answer: ")
        #adds the answer to the selected answers list
        selected_answers.append(chosen)
        #while loop to check of the option chosen is candrect/possible
        while chosen != "a" and chosen !="b" and chosen !="c":
            #shows tahgt the option was invalid
            print("invalid option")
            #asks fand the choice again
            chosen = input("answer: ")
        #checks if it is the right answer
        if chosen == "a":
            #adds a point
            points += 1
        else:
            #skips adding the point
            time.sleep(0)
            #takes the question off the list so that it cannot be shown again
        del questions[0]
        #adds to the number of questions completed
        question += 1
        #checks if it is question 7
    elif questions[0] == "Question 7":
        #shows question
        print ("\nQ. What should you do if you want to meet someone you only know online?\n")
        #shows possible answers
        print (answers[6][0],"\n", answers[6][1],"\n", answers[6][2])
        #asks fand users answer
        chosen = input("answer: ")
        #adds the answer to the selected answers list
        selected_answers.append(chosen)
        #while loop to check of the option chosen is candrect/possible
        while chosen != "a" and chosen !="b" and chosen !="c":
            #shows tahgt the option was invalid
            print("invalid option")
            #asks fand the choice again
            chosen = input("answer: ")
        #checks if it is the right answer
        if chosen == "b":
            #adds a point
            points += 1
        else:
            #skips adding the point
            time.sleep(0)
            #takes the question off the list so that it cannot be shown again
        del questions[0]
        #adds to the number of questions completed
        question += 1
        #checks if it is question 8
    elif questions[0] == "Question 8":
        #shows question
        print ("\nQ. Which of these is classed as personal infandmation?\n")
        #shows possible answers
        print (answers[7][0],"\n", answers[7][1],"\n", answers[7][2])
        #asks fand users answer
        chosen = input("answer: ")
        #adds the answer to the selected answers list
        selected_answers.append(chosen)
        #while loop to check of the option chosen is candrect/possible
        while chosen != "a" and chosen !="b" and chosen !="c":
            #shows tahgt the option was invalid
            print("invalid option")
            #asks fand the choice again
            chosen = input("answer: ")
        if chosen == "a":
            #adds a point
            points += 1
        else:
            #skips adding the point
            time.sleep(0)
            #takes the question off the list so that it cannot be shown again
        del questions[0]
        #adds to the number of questions completed
        question += 1
        #checks if it is question 9
    elif questions[0] == "Question 9":
        #shows question
        print ("\nQ. What is the definition of phishing?\n")
        #shows possible answers
        print (answers[8][0],"\n", answers[8][1],"\n", answers[8][2])
        #asks fand users answer
        chosen = input("answer: ")
        #adds the answer to the selected answers list
        selected_answers.append(chosen)
        #while loop to check of the option chosen is candrect/possible
        while chosen != "a" and chosen !="b" and chosen !="c":
            #shows tahgt the option was invalid
            print("invalid option")
            #asks fand the choice again
            chosen = input("answer: ")
        #checks if it is the right answer
        if chosen == "a":
            #adds a point
            points += 1
        else:
            #skips adding the point
            time.sleep(0)
            #takes the question off the list so that it cannot be shown again
        del questions[0]
        #adds to the number of questions completed
        question += 1
        #checks if it is question 10
    elif questions[0] == "Question 10":
        #shows question
        print ("\nQ. What is the definiton of spyware?\n")
        #shows possible answers
        print (answers[9][0],"\n", answers[9][1],"\n", answers[9][2])
        #asks fand users answer
        chosen = input("answer: ")
        #adds the answer to the selected answers list
        selected_answers.append(chosen)
        #while loop to check of the option chosen is candrect/possible
        while chosen != "a" and chosen !="b" and chosen !="c":
            #shows tahgt the option was invalid
            print("invalid option")
            #asks fand the choice again
            chosen = input("answer: ")
        #checks if it is the right answer
        if chosen == "a":
            #adds a point
            points += 1
        else:
            #skips adding the point
            time.sleep(0)
            #takes the question off the list so that it cannot be shown again
        del questions[0]
        #adds to the number of questions completed
        question += 1
        #if there are no questiuons left:
    else:
        #skips to displaying scande
        time.sleep(0)
#shows the users points
print("\n",name,", you got ",points, "out of 10")
