def chat(messe):
    count=0
    if messe=="привет":
        return "как дела?"
        count=count+1
    elif messe=="как дела?":
        return "нормально"
        count=count+1
    elif messe=="ты супер":
        return "ты тоже супер"
        count=count+1
    elif messe=="мы друзья ?":
        return "конечно,"
        count=count+1
    elif messe=="пока":
        return str(count)
    elif messe=="помощь":
        return "привет я умею: \n здороваться \n делать комплементы \n прощаться"
    else:
        return "я тебя не понимаю"
        count=count+1