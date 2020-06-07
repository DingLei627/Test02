import random


print('---------我是你大爷----------')
secret=random.randint(1,20);
temp=input("猜测女神心理想的哪个数字哟：");
guesss=int(temp);

while guess !=secret:
    temp=input("哎呀 猜错了，再猜一次:");
    guess=int(temp);
    if guess==secret:
        print("卧槽 猜对了女神的心思，得手了");
        break;
    else:
        if guess>secret:
            print("猜大了 ");
        else:
            print("猜小了 ");

print("游戏结束");