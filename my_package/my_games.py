import random

def game1():  # 石头剪刀布
    player_score = computer_score = 0
    for i in range(3):
        player = input("玩家(石头剪刀布): ")
        computer = random.choice(["石头", "剪刀", "布"])
        print('电脑出的是 %s' % computer)
        if player == computer:
            player_score += 1
            computer_score += 1
        elif (player == '剪刀' and computer == "布") or (player == '石头' and computer == "剪刀") or (player == '布' and computer == "石头"):
            player_score += 1
        else:
            computer_score += 1
        print('你的得分是%d，电脑得分是%d' % (player_score, computer_score))
    if player_score > computer_score:
        print("Player wins!")
    elif player_score < computer_score:
        print("Computer wins!")
    else:
        print("Draw!Nobody wins!")

def guess_num(start,end):
    num = random.randint(start, end)
    while True:
        guess = int(input('请输入你输入的数字：'))
        if guess > num:
            print("数字大了")
        elif guess < num:
            print('数字小了')
        else:
            print('恭喜你猜对了！')
            break
