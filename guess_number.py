'''
猜數字遊戲，電腦會隨機產100~999隨機一個數字，玩家可以輸入數字，
程式會根據你的答案回答幾a幾b，猜對且正確位置為a，猜對但位置錯誤為b，
如果回答超過10次就輸了
'''
import random
# Constant Setting
MAX_GUESS = 10
flag = True
ans_list = []
guess_list = []
# Define Function
def spawn_rand_number():
    print('Game Start!!')
    ans_list = list(str(random.randint(100,999)))
    return ans_list
     
def guess_round(ans_list):
    for i in range(1,MAX_GUESS):
        
        print('Round %2d'%(i))
        guess_list = list(input())
        correct = decide_stage(guess_list,
                               ans_list,len(ans_list))
        if correct == len(ans_list):
            print('Win!!!')
            return
    print('Lose!')
            

def decide_stage(guess,ans_list,length):
    a=b=0
    for i in range(length):
        if ans_list[i] == guess[i]:
            a+=1           
        elif ans_list[i] in guess:
            b+=1
    print('%dA %dB'%(a,b))
    return a
    
def restart_game():
    print('Play again?(yes or no)')    
    string = input()
    if string == 'yes':
        return True
    elif string == 'no':
        return False
    else:
        print('input error! Please type again')
        restart_game()
#Main
while flag:
    LIST = spawn_rand_number()
    guess_round(LIST)
    flag = restart_game()

