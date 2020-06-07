import random


print('---------我是你大爷----------')
times =3

secret=random.randint(1,20);
temp=input("3次机会 猜测女神心理想的哪个数字哟：");
guesss=int(temp);

while guess !=secret and (times>0):
    temp=input("哎呀 猜错了，再猜一次:");
    guess=int(temp);
    times=times-1;
    if guess==secret:
        print("卧槽 猜对了女神的心思，得手了");
        break;
    else:
        if guess>secret:
            print("猜大了 ");
        else:
            print("猜小了 ");
        if times>0:
            print("再试一次")
        else:
            print("机会用光了")

print("游戏结束");