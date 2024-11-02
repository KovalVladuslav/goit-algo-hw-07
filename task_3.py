class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_tree_values(root):
    # Якщо дерево порожнє, повертаємо 0
    if root is None:
        return 0

    # Рекурсивно знаходимо суму лівого та правого піддерев і додаємо значення поточного вузла
    return root.value + sum_tree_values(root.left) + sum_tree_values(root.right)

# Приклад використання
# Створимо просте дерево
root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right = TreeNode(15)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

# Знаходимо суму всіх значень
total_sum = sum_tree_values(root)
print("Сума всіх значень у дереві:", total_sum)
