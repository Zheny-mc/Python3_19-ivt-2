
#*******************базовый элемент***************************
class Circuit_Element:
    '''Элемент цепи '''
    def info(self):
        print("Элемент цепи")
#*************************************************************
class Passive_Electric_Element(Circuit_Element):
    '''Пассивный электрический элемент'''
    def info(self):
        print("Пассивный электрический элемент")
#*****************child********************************************
class Resistance(Passive_Electric_Element):
    '''Сопротивлние'''
    def info(self):
        print("Сопротивлние")

class Power_Supply(Passive_Electric_Element):
    '''Источник питания'''
    def info(self):
        print("Источник питания")

class Conductor(Passive_Electric_Element):
    '''Проводник'''
    def info(self):
        print("Проводник")

#*************************************************************
class Active_Electric_Element(Circuit_Element):
    '''Активный электричекий элемент '''
    def info(self):
        print("Активный электрический элемент")
#*****************child********************************************
class Capacity_Capacitor(Active_Electric_Element):
    '''Емкость конденсатора'''
    def info(self):
        print("Емкость конденсатора")

class Inductance(Active_Electric_Element):
    '''Индкуктивность'''
    def info(self):
        print("Индкуктивность")

class Triode(Passive_Electric_Element):
    '''Триод(Биполярный транзистор)'''
    def info(self):
        print("Триод(Биполярный транзистор)")
#********************************************************************

def help():
    print("СИСТЕМА УЧЕТА РАДИОДЕТАЛЕЙ")
    print("************************************")
    print("Элемент цепи|")
    print("            |1.Пассивный")
    print("                 |1.Сопротивление")
    print("                 |2.Источник питания")
    print("                 |3.Проводник")
    print("            |2.Активный")
    print("                 |1.Емкость")
    print("                 |2.Индуктивность")
    print("                 |3.Триод")
    print("************************************")
    print("******организация полиморфизма******")
    print("***Автор: Бубнов Евгений 19-ивт-2***")

def create():
    """Создание списка и количества радиодеталей"""
    #ввод количества радиодеталей
    count = int(input("ВВедите количество радиодеталей: "))    
    Elememts = []
    
    return count, Elememts

def Input(count, Element):
    """Заполнение исходных данных"""
    #manual
    help()
    
    #выбор элемента
    for i in range(count):
        print("Create #%d" % (i+1))
        
        change_element = int(input("Введите номер детали: "))
        
        if change_element == 11:
            Element.append(Resistance())
        elif change_element == 12:
            Element.append(Power_Supply())
        elif change_element == 13:
            Element.append(Conductor())
        elif change_element == 21:
            Element.append(Capacity_Capacitor())
        elif change_element == 22:
            Element.append(Inductance())
        elif change_element == 23: 
            Element.append(Triode())
    
    return Element
    
    
def Output(Element=[]):
    """Вывод заполненых данных"""
    for index, obj in enumerate(Element):
        print("#%2d."%(index+1), end='') 
        obj.info()

def run():
    #создание исходых данных
    count, element = create()
    #ввод данных
    element = Input(count, element)    
    #вывод
    Output(element)

#запуск
run()
