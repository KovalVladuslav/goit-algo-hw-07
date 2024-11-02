class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_min_value(root):
    # Перевіряємо, чи дерево порожнє
    if root is None:
        return None

    # Проходимо по лівій гілці, поки є лівий нащадок
    current_node = root
    while current_node.left is not None:
        current_node = current_node.left

    # Повертаємо значення найлівішого вузла, тобто найменше значення
    return current_node.value

# Приклад використання
# Створимо просте дерево
root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right = TreeNode(15)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

# Знаходимо найменше значення
min_value = find_min_value(root)
print("Найменше значення в дереві:", min_value)
