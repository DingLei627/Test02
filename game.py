import random


print('---------�������ү----------')
secret=random.randint(1,20);
temp=input("�²�Ů����������ĸ�����Ӵ��");
guesss=int(temp);

while guess !=secret:
    temp=input("��ѽ �´��ˣ��ٲ�һ��:");
    guess=int(temp);
    if guess==secret:
        print("�Բ� �¶���Ů�����˼��������");
        break;
    else:
        if guess>secret:
            print("�´��� ");
        else:
            print("��С�� ");

print("��Ϸ����");