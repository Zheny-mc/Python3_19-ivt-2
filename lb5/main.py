def punctuation_mark(ch):
    '''Определяет является ли символ знаком препинания'''
    if   (ch >= '!' and ch <= '/'):
        return True
    elif (ch >= ':' and ch <= '@'):
        return True
    elif (ch >= '{' and ch <= '~'):
        return True
    elif (ch == ' '):
        return True
    else:
        return False


Str = input("Input: ")
words = []  #слова текста
word = ""   #слово
n = 1  #кол-во слов у которых первая и последняя буква совпадает

for i in range(0, len(Str)):
    if not punctuation_mark(Str[i]):
        word += Str[i]
        print("find", word)
    else:
        if len(word) != 0:
            print("add", word)
            words.append(word)
            print("words", words)
            word = ""
        print()

if len(word) != 0:
    print("add", word)
    words.append(word)
    print("words ", words)
    word = ""

print('\n', words)

#поиск слов с одинаковыми первыми и последними символами
i = 0
j = 1
while i < len(words)-1:
    len_current = len(words[i]) - 1
    len_next = len(words[j]) - 1

    if ((words[i][0] == words[j][0]) and 
        (words[i][len_current] == words[j][len_next])):
        n+=1
        j+=1
    else:
        h = 0


