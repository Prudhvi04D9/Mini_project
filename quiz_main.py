import json
import random
qnum = 1
total_points = 0
e_read = []
d_read = []
def eliminate_option(ques, level):
    if level == 'easy':
        possible_options = ['a', 'b', 'c', 'd']
        possible_options.remove(e_read[0]['Question' + str(ques)]['correct_answer'])
        any_two_to_remove = random.sample(possible_options, 2)
        two_to_keep = list(set(['a', 'b', 'c', 'd']) - set(any_two_to_remove)) + list(set(any_two_to_remove) - set(['a', 'b', 'c', 'd']))
        two_to_keep.sort()
        print("Options after elimination are : ")
        print("{}: ".format(two_to_keep[0]) + e_read[0]['Question' + str(ques)][two_to_keep[0]])
        print("{}: ".format(two_to_keep[1]) + e_read[0]['Question' + str(ques)][two_to_keep[1]])
    else:
        possible_options = ['a', 'b', 'c', 'd']
        possible_options.remove(d_read[0]['Question' + str(ques)]['correct_answer'])
        any_two_to_remove = random.sample(possible_options, 2)
        two_to_keep = list(set(['a', 'b', 'c', 'd']) - set(any_two_to_remove)) + list(set(any_two_to_remove) - set(['a', 'b', 'c', 'd']))
        two_to_keep.sort()
        print("Options after elimination are : ")
        print("{}: ".format(two_to_keep[0]) + d_read[0]['Question' + str(ques)][two_to_keep[0]])
        print("{}: ".format(two_to_keep[1]) + d_read[0]['Question' + str(ques)][two_to_keep[1]])
    return two_to_keep
def rule_print():
    print("Welcome to the quiz!")
    print("Rule 1 : There will be a total of 5 questions")
    print("Rule 2 : The points are counted as follows : ")
    print(" You answered an easy question correctly : 5 points")
    print(" You answered a difficult question correctly : 10 points")
    print("Rule 3 : There will be 2 easy questions and then 3 difficult questions")
    print("Okay, so let's get started")
def point_display(total):
    print("Your total points are ", total)
    if total <= 10:
        print("You can do better!")
    elif total <= 20:
        print("Good job! Keep improving")
    elif total <= 30:
        print("Nice! You seem smart")
    elif total <= 35:
        print("Great job! That was a nice game")
    else:
        print("You cracked the quiz! Brilliant!")
def ask_easy_ques():
    global qnum
    global total_points
    easy_ques = random.sample(range(1, 6), 2)
    for i in easy_ques:
        print("Question {}".format(qnum))
        print(e_read[0]["Question" + str(i)]['Ques'])
        print("a: " + e_read[0]['Question' + str(i)]['a'])
        print("b: " + e_read[0]['Question' + str(i)]['b'])
        print("c: " + e_read[0]['Question' + str(i)]['c'])
        print("d: " + e_read[0]['Question' + str(i)]['d'])
        c3 = input("Answer :  ")
        while c3.lower() not in ['a', 'b', 'c','d']:
            print("Choose correctly")
            c3 = input("Answer :  ")   
        if c3.lower() == e_read[0]['Question' + str(i)]['correct_answer'].lower():
            print("Your answer is correct! Let's go to the next question!")
            total_points += 5
        else:
            print("Sorry, wrong answer! Let's go to the next question!")
        qnum += 1
def ask_diff_ques():
    global qnum
    global total_points
    diff_ques = random.sample(range(1, 6), 3)
    for i in diff_ques:
        print("Question {}".format(qnum))
        print(d_read[0]["Question" + str(i)]['Ques'])
        print("a: " + d_read[0]['Question' + str(i)]['a'])
        print("b: " + d_read[0]['Question' + str(i)]['b'])
        print("c: " + d_read[0]['Question' + str(i)]['c'])
        print("d: " + d_read[0]['Question' + str(i)]['d'])
        c3 = input("Answer : ")
        while c3.lower() not in ['a', 'b', 'c','d']:
            print("Choose correctly")
            c3 = input("Answer : ")        
        if c3.lower() == d_read[0]['Question' + str(i)]['correct_answer'].lower():
            print("Your answer is correct! Let's go to the next question!")
            total_points += 10
        else:
            if qnum == 4:
                print("Sorry! Wrong answer")
            else:
                print("Sorry, wrong answer! Let's go to the next question!")
        qnum += 1    
def read_all_ques():
    global e_read
    global d_read
    with open("easy_ques.json") as fileobj:
        e_read = json.load(fileobj)    
    with open("difficult_ques.json") as fileobj:
        d_read = json.load(fileobj)
if __name__ == '__main__':
    read_all_ques()  
    print("Welcome to the 5 question quiz!")   
    c2 = input("Do you need me to tell you the rules? (Enter y/n)")
    if c2.lower() == 'y':
        rule_print()
    else:
        print("Okay, so let's get started")   
    choice = input("Are you ready to start? (Enter y/n)")   
    if choice.lower() == 'y':
        ask_easy_ques()
        ask_diff_ques()
        point_display(total_points)
        print("Thank you for playing the quiz!")                
    else:
        print("Okay! Do come back when you are ready! Bye :)")
