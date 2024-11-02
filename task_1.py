class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_max_value(root):
    # Перевіряємо, чи дерево порожнє
    if root is None:
        return None

    # Проходимо по правій гілці, поки є правий нащадок
    current_node = root
    while current_node.right is not None:
        current_node = current_node.right

    # Повертаємо значення найправішого вузла, тобто найбільше значення
    return current_node.value

# Приклад використання
# Створимо просте дерево
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(30)

# Знаходимо найбільше значення
max_value = find_max_value(root)
print("Найбільше значення в дереві:", max_value)
