import os
import sys
import getch3

arr_2 = []
current_str = 1
will_str = 24
height = None
inp = True
words = ["line", "float"]

def define_file():
    if __name__ == '__main__':
        global arr_2
        global height
        global will_str
        File = None
        
        if len(sys.argv) == 2:
            File = sys.argv[1]
         
            with open(File) as text:
                for line in text:
                    arr_2.append(line)

            height = len(arr_2)

            if height < will_str:
                will_str = height
            
            return True 
        else:
            return False

def control():
    global current_str
    global will_str
    global inp

    key = getch3.getch()
    if ord(key) == 119:  #up
        if current_str > 1:
            current_str-=1
            will_str-=1
        
    elif ord(key) == 115:  #low
        if will_str < height:
            current_str+=1
            will_str+=1    
    
    elif ord(key) == 113:  #q
        inp = False

def back_end_black():
    print("\033[40m")

def Print_line(text):
    lenth = len(text)
    i = 0
    Print_Word = False

    while i < lenth-1 and i < 80:
        Print_Word = False
        
        for word in words:
            if text.find(word, i) == i:
                print("\033[32m%s\033[37m" % word, end='')
                i+=len(word)
                Print_Word = True
                break

        if not Print_Word:
            print("%c" % text[i], end='')
            i+=1

    print()   
    
def out_white_text():
    print("\033[37m", end='')
    

def Print():
    for i in range(current_str-1, will_str):
        out_white_text()
        Print_line(arr_2[i])

def run():
    back_end_black()

    if define_file():
        while (inp):
            os.system("clear")
            Print()
            control()
    else:
        print("Error")

#запуск
run()













