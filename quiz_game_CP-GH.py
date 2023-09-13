'''
PROGRAM DESCRIPTION

PLAYER MANAGEMENT
------------------
1. Track player score in the Scoreboard
2. If player name is not provided, program will create a guest player, concatinated with 2 digit number
3. Keep track of player last score and show it when the quiz started
4. At the end of each game, program shows the number of correct and incorrect answers.
5. Update scoreboard with current score.
6. If same player play again, program will update his/her score


GAME LEVELS
------------
1. Program maintain two levels that is beginner and Expert Level.
2. For beginner level, question appears in order every time and no time limit.
3. For expert level, program shuffle question orders and there is a time limit to answer the questions.

GENERAL FEATURES
----------------
1. Program continues until players select no to close the program
2. Multiple players can play the game and progam keep track the each player score in a session.
3. One player can play at a time.
4. After each question, program give the feedback message for correct and incorrect answer with smily or sad face.
5. Dynamic question bank, more questions can be added in a questions list object with muliple choices, 
   score per question and correct answer
'''

import os
import random
import time
from inputimeout import inputimeout, TimeoutOccurred

questions=[[1,'What is the capital of united kingdom? ',
            ['A. London','B. Manchester','C. Leeds','D. Birmingham '],'A',10],
            [2,'How many constituencies in total in the UK',
            ['A. 300','B. 700','C. 650','D. 800'],'C',20],
            [3,'Where was Robert Burns from?',
            ['A. Wales','B. Scotland','C. Northern Ireland','D. England'],'B', 10],
            [4,'Who was Queen Elizabeth II married to?',
            ['A. Prince Philip','B. King Charles III','C. Prince Harry','D. Prince William'],'A',20],
            [5,'Which flag has a white cross on a blue background?',
            ['A. Irish','B. Scottish','C. English','D. Wales'],'B',30],
            [6,'Where is the Cenotaph located?',
            ['A. Dorset','B. Trafalgar Sq','C. Whitehall','D. Wiltshire'],'C',40],
            [7,'Who built the Tower of London?',
            ['A. Henry VII','B. Henry VIII','C. William the Conqueror','D. Oliver Cromwell'],'C',50],
            [8,'Roast beef is a traditional food of which country?',
            ['A. England','B. Scotland','C. Wales','D. Northern Ireland'],'A',40],
            [9,'Which of these UK landmarks is in Wales?',
            ['A. The Lake District','B. The Giant Causeway','C. Snowdonia','D. Loch Lomond'],'C',30],
            [10,'When is St David day?',
            ['A. 30th of Nov','B. 23rd April','C. 17th March','D. 1st March'],'D',60]
      ]


players = []

Loop = True

Player_Name=''
Player_Score = 0
level = 'B'
TIME_LIMIT = 5


def updateScore(player, score=0):
      x = ''
      for i in range(len(players)):
           x = players[i]['Name'].upper()
           if x == player.upper():
                players[i]['Score'] = score
                break
      if x != player.upper():
           l = {'Name':player,'Score':score}
           players.append(l)


def lastScore(player):      # Function to get Player Last Score
     last_score = 0
     for i in range(len(players)):
           x = players[i]['Name'].upper()
           if x == player.upper():
                last_score = players[i]['Score']
                break
     
     return last_score


def positions():
     nlist = sorted(players, key=lambda d: d['Score'],reverse=True) 
     if len(nlist) >= 2:
          print('\n\tFirst Position: ',nlist[0]['Name'])
          print('\tSecond Position: ',nlist[1]['Name'])
     if len(nlist) > 2:
          print('\tThird Position: ',nlist[2]['Name'])


def start_quize():
    print(f'\n\n\tWelcome {Player_Name} to the Game')
    print(f'\tYour Last score is {lastScore(Player_Name)}')
    playGame = True
    questionNo = 0
    qsn =0
    Answer = ''
    correctAnswers = 0
    incorrectAnswers = 0
    questionPoint = 0
    score = 0
    
    # Make a copy of original list of questions to shuffle randomly for Option E
    q =  questions.copy()
    if level.upper() == 'E':
        random.shuffle(q)
    

    while questionNo <= len(q)-1:
        qsn = q[questionNo][0]
        
        Answer = q[questionNo][3]
        questionPoint = q[questionNo][4]
        print('\n\tQuestion: '+str(qsn))
        print('\t',q[questionNo][1])
        for op in range(len(q[questionNo][2])):
                print('\t',q[questionNo][2][op])
        
        # Checking for the Game Level
        if level.upper() == 'E':    # Expert Level
            #  timeout = 5            # timelimit approx 5 sec
            #  t = Timer(TIME_LIMIT, print, [", Sorry Time's up!, Enter to move to next Question"])
            #  Start Timer
            #  t.start()
             print("\n\tYou have", str(TIME_LIMIT), " seconds")
             try:
                  ans=inputimeout('\tChoose the Correct Option: ',timeout= TIME_LIMIT).upper()
             except TimeoutOccurred:
                  print('\tTimeout')
                  ans=''
            #  ans = input('\tChoose the Correct Option: ').upper()
            #  t.cancel()

        else:
             ans = input('\tChoose the Correct Option: ').upper()   # Beginner level
        questionNo += 1
        if ans == Answer:
            print("\tCorrect (^◡^)")
            score = score + questionPoint
            correctAnswers = correctAnswers + 1
        else:
            print("\tIncorrect (◡︵◡)")
            incorrectAnswers = incorrectAnswers + 1
    print('\n\t------ F E E D  B A C K -------------')
    print(f'\n\tCorrect Answers {correctAnswers}')
    print(f'\tIncorrect Answers {incorrectAnswers}')
    Player_Score = score
    updateScore(Player_Name, Player_Score)
    time.sleep(5)


while Loop:
    os.system('cls')
    print("\n\tW E L C O M E  T O  Q U I Z  G A M E \n ")
    print("\tSCOREBOARD \n")
    print("\tPlayer\t","Latest Score")
    print("\t----------------------------------")
    for i in range(len(players)):
        print('\t',players[i]['Name'],'\t',players[i]['Score'])


    positions()
    play =input("\n\tDo you want to Play another Game (Y/N): ").upper()
    if play == 'Y':
        lvl = """
                L E V E L S

                B. Beginner level
                   Player will be allowed to take as much time to answer.
                   Questions will be presented in Order

                E. Expert Level
                   Each question will allow to answer in a limited time.
                   Each time the order of questions will be shuffled.
              """
        print(lvl)
        level=input("\tEnter Game Level (B/E) Default(B): ")
        Player_Name=input("\tEnter Player Name: ")

        if level.upper() == 'E':
             TIME_LIMIT = int(input('\tEnter time limit in seconds: '))

        if len(Player_Name) <=0 :
            Player_Name = 'Guest'+str(random.randint(0,99))
        start_quize()

    else:
        Loop = False

print("\tThank you to Play with us..")
