

word='HAPPINESS'
reveal=list(len(word)*'_')
print(reveal)
lives=7
gameWon=False

while gameWon==False:
    #can ask user to guess letter
    guess=input("Guess a letter or word")
    guess=guess.upper()
    
    if guess==word:
        gameWon=True
    if len(guess)==1 and guess in word:
        for i in range(0,len(word)):
            letter=word[i]
            if guess==letter:
                reveal[i]=guess
    if '_' not in reveal:
        gameWon=True
    else:
        lives-=1
        
if gameWon:
    print("welldone")
else:
    print("you failed, the word was:",word)