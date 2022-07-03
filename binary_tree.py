class Node:
    INDENT = '\n'

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def inverted(self):
        result = Node(self.data)
        result.left = self.right.inverted() if self.right else None
        result.right = self.left.inverted() if self.left else None
        return result

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def __str__(self):
        Node.INDENT += '\t'
        result = str(self.data)
        if self.left:
            result += f"{Node.INDENT}left: {str(self.left)}"
        if self.right:
            result += f"{Node.INDENT}right: {str(self.right)}"
        Node.INDENT = Node.INDENT[:-1]
        return result


def are_asymmetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif (root1 is None) != (root2 is None) or root1.data != root2.data:
        return False
    else:
        return are_asymmetric(root1.left, root2.right) and \
            are_asymmetric(root1.right, root2.left)


def get_temp_tree():
    root = Node(27)
    root.insert(14)
    root.insert(16)
    root.insert(12)
    root.insert(35)
    root.insert(38)
    root.insert(31)
    root.insert(15)
    return root


def main():
    root = get_temp_tree()
    print(root)
    root_invert = root.inverted()
    print(root_invert)
    print(f"are_asymmetric?={are_asymmetric(root, root_invert)}")
    root.insert(555)
    print(f"are_asymmetric?={are_asymmetric(root, root_invert)}")


if __name__ == "__main__":
    main()
