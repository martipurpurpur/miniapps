
#Класс для создания дерева
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    # Вставка нового значение в свободном месте в зависимости от велечины
    def insert(self, val):
        if self.val:         # Если существует корневой узел
            if val < self.val:  # Если значение меньше корневого узла
                if self.left is None:  # и левый узел отсутствует
                    self.left = TreeNode(val)  # формируем на месте левого узла узел с переданным для вставки значением
                else:                   # Если узел уже есть, то делаем всю проверку снова уже для левого узла
                    self.left.insert(val)
            elif val > self.val:               # Если значение больше нашего узла, то пытаемся вставить его справа
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:               # Если значения у корневого узла нет, добавляем его
            self.val = val

    # прямой обход
    def preorder(self):
        print(str(self.val) + "->", end=' ')  # отображаем корень
        if self.left:
            self.left.preorder()              # рекурсивная функция для левого поддерева
        if self.right:
            self.right.preorder()             # рекурсивная функция для правого поддерева

    # центрированный обход (отсортированный обход)
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(str(self.val) + "->", end=' ')
        if self.right:
            self.right.inorder()

    # обратный обход
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(str(self.val) + "->", end=' ')

t = TreeNode(None)
t.insert(8)
t.insert(3)
t.insert(1)
t.insert(6)
t.insert(7)
t.insert(10)
t.insert(14)
t.insert(4)
t.preorder()  # 8 3 1 6 4 7 10 14
print('\n')
t.inorder()   # 1 3 4 6 7 8 10 14
print('\n')
t.postorder() # 1 4 7 6 3 14 10 8













