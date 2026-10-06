def chat(messe,name,count):
    if messe=="привет":
        return "как дела?"+name
        count=count+1
    elif messe=="как дела?":
        print("нормально")
        count=count+1
    elif messe=="ты супер":
        print("ты тоже супер",name)
        count=count+1
    elif messe=="мы друзья ?":
        print("конечно,",name)
        count=count+1
    elif messe=="пока":
        print(count)
    elif messe=="помощь":
        print("привет я умею: \n здороваться \n делать комплементы \n прощаться")
    else:
        print("я тебя не понимаю",name)
        count=count+1
count=0
name=input("привет как тебя зовут ? \n") 
age=int(input("сколько тебе лет ? \n"))
print("тебе", age,"лет")
if age<18: 
    print("тебе сюда нельзя")
    exit()
while True:
    messe = input("ты: ").lower()
    count=count+1
    otvet=chat (messe,name,count)
    print(otvet)