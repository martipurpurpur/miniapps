class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert_in_neariest(self, val):
        visited = []
        visited.append(self)
        while visited:
            item = visited.pop(0)
            if item.val:
                if item.left is None:
                    item.left = TreeNode(val)
                    return
                if item.right is None:
                    item.right = TreeNode(val)
                    return
                visited.append(item.left)
                visited.append(item.right)
            else:
                item.val = val

    def preorder(self):
        print(str(self.val) + "->", end=' ')  # отображаем корень
        if self.left:
            self.left.preorder()              # рекурсивная функция для левого поддерева
        if self.right:
            self.right.preorder()

t = TreeNode(None)
t.insert_in_neariest(1)
t.insert_in_neariest(3)
t.insert_in_neariest(45)
t.insert_in_neariest(6)
t.insert_in_neariest(7)
t.insert_in_neariest(45)
t.insert_in_neariest(14)
t.insert_in_neariest(4)
t.preorder()