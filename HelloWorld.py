def say_hello(a):
    if ((a % 3 == 0) and (a % 7 == 0)):
        return "Hello world"
    elif (a % 7 == 0):
        return "Hello"
    elif a % 3 == 0:
        return "world"
    else:
        return "Не делится без остатка ни на 3, ни на 7"

def validate_number(a):
    if a.isdigit():
        return int(a)
    elif len(a) < 1:
        print("Вы ничего не ввели")
        exit()
    elif (a[0] == '-') and a[1:].isdigit():
        return int(a)
    else:
        print("Это не целое число")
        exit()


a = validate_number(input('Введите целое число: '))
print(say_hello(a))

########################################################################################################################
class Node:
    def __init__(self, data):
        self.data = data  #то, что передаем в список
        self. next = None #ссылка на следующий элемент

#создает новый узел и добавляет его в конец списка, проходя его
    def append(self, value):  #добавление в список новых узлов
        n = self           #Ссылка на первый узел
        while n.next:       #проходим по списку, пока в нем есть узлы
            n = n.next
        n.next =  Node(value)        #указываем на последний узел: устанавливаем наш новый узел, если узлов больше нет

    # мой вариант с рекурсией
    def add(self, value):
        if self.next:
            self.next.add(value)
        else:
            self.next = Node(value)

    def printnode(self):
        if self.next:
            self.next.printnode()
        print(self.data)

    def printnode_while(self):
        n = self
        print(n.data)
        while n.next:
            n = n.next
            print(n.data)


ll = Node(1)
ll.add(5)
ll.add(7)
ll.append(8)
ll.printnode()
ll.printnode_while()


