import sys
import argparse
import pickle

#ввод аргументов командной строки(argparse)
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-m','--mode', choices=['c', 'r', 'h'], default='h')
    parser.add_argument ('-c', '--count', default=0, type=int)
    parser.add_argument ('-f', '--fileName', default="", type=str)

    return parser
 
def CreateArgs():
    if __name__ == '__main__':
        parser = createParser()
        namespace = parser.parse_args()
 
        #print (namespace)

        Mode = namespace.mode
        Count = namespace.count 
        File_Name = namespace.fileName
        
        return Mode, Count, File_Name
#**********************************************************

class TechnicalPark:
    '''Харастеристики компьютера'''
    def __init__(self, cpu="", clock_frequency="", 
                 volume_ozu="", volume_hd="", monitor=""): 
        self.cpu = cpu 
        self.clock_frequency = clock_frequency
        self.volume_ozu = volume_ozu
        self.volume_hd = volume_hd
        self.monitor = monitor

class Read:
    '''Чтение электронной таблицы'''
    def __init__(self, count, fileName):
        #создаю двумерный  массив для считывания
        self.park = []
        #создаю переменную количества записей
        self.count = count  #количество прочитанных записей
        self.COUNT = 0  #максимальное количество записей
        #открываю файл
        self.text = open(fileName, "rb")

    def DefineFile(self):
        '''Открывает и записывает файл и считает количество строчек'''
        #определяется количество записей
        self.COUNT = pickle.load(self.text) 
        
        if self.COUNT < self.count:
            self.count = self.COUNT
        
        #создается двумерный список для записи
        for i in range(self.count):
            self.park.append(TechnicalPark())
        
        #запись двумерного списка
        for i in range(self.count):
            self.park[i] = pickle.load(self.text)
    
    def Print(self):
        '''Выводит count записей'''
        for index, obj in enumerate(self.park):
            if index+1 > self.count:
                break
            print("\n\033[4mPersonal Computer %3d:\033[0m" % (index+1))
            print("-cpu =", obj.cpu, 
                  "\n-clock_frequency =", obj.clock_frequency, 
                  "\n-volume_ozu =", obj.volume_ozu, 
                  "\n-volume_hd =", obj.volume_hd,
                  "\n-monitor =", obj.monitor)


    def CloseFile(self):
        '''закрывает файл'''
        self.text.close()

class Create:
    '''Создание электронной таблицы'''
    def __init__(self, count, fileName):
        #создаю двумерный  массив для считывания
        self.park = []
        for line in range(count):
            self.park.append(TechnicalPark())
        #создаю переменную количества записей
        self.count = count
        #открываю файл
        self.text = open(fileName, "wb")
    
    def InputData(self):
        '''Ввод и проверка данных'''
        for index, obj in enumerate(self.park):
            print("\n\033[4mPersonal Computer %3d:\033[0m" % (index+1))
            obj.cpu = input("  Enter cpu: ")
            obj.clock_frequency = input("  Enter clock_frequency: ")
            obj.volume_ozu = input("  Enter volume_ozu: ")
            obj.volume_hd = input("  Enter volume_hd: ")
            obj.monitor = input("  Enter monitor: ")
            

    def Write(self):
        '''Запись данных в двумерный массив'''
        pickle.dump(self.count, self.text)
        
        for obj in self.park:
            pickle.dump(obj, self.text)

    def CloseFile(self):
        '''Закрывет файл'''
        self.text.close()


def ModeCreate(count, fileName):
    '''Создание электронной таблицы'''
    Park = Create(count, fileName)

    Park.InputData()

    Park.Write()

    Park.CloseFile()

def ModeRead(count, fileName):
    '''чтение электронной таблицы'''
    Park = Read(count, fileName)

    Park.DefineFile()

    Park.Print()

    Park.CloseFile()


def ModeHelp():
    '''Вызов мануала'''
    print("%sПРОГРАММА ДЛЯ СОЗДАНИЯ ПАРКА КОМПЬТЕРОВ%s" % ('*'*20, '*'*21))
    print("Создание записей парка:")
    print("    python3 main.py -m(--mode) c -c(--count) <0...100> -f(--fileName) <file_name>")
    print("Чтение записей парка:")
    print("    python3 main.py -m(--mode) c -c(--count) <0...100> -f(--fileName) <file_name>")
    print("Помощь:")
    print("    python3 main.py -m(--mode) h")
    print("Author: Bubnov Evgeny 19-ivt-2")
    print("#Copyright")
    print('*'*80)
    
def run():
    '''Запуск программы
       Выбор режима
       запуск режима'''
    mode, count, fileName = CreateArgs()

    if mode == 'c' and count > 0:
        ModeCreate(count, fileName)
    elif mode == 'r' and count > 0:
        ModeRead(count, fileName)
    elif mode == 'h':
        ModeHelp()

#Запуск
run()





