import random


print('---------�������ү----------')
times =3

secret=random.randint(1,20);
temp=input("3�λ��� �²�Ů����������ĸ�����Ӵ��");
guesss=int(temp);

while guess !=secret and (times>0):
    temp=input("��ѽ �´��ˣ��ٲ�һ��:");
    guess=int(temp);
    times=times-1;
    if guess==secret:
        print("�Բ� �¶���Ů�����˼��������");
        break;
    else:
        if guess>secret:
            print("�´��� ");
        else:
            print("��С�� ");
        if times>0:
            print("����һ��")
        else:
            print("�����ù���")

print("��Ϸ����");