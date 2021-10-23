class TreeNode:
    """Tree node for binary tree representative"""

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.val}'


def level_order(root):
    result = []
    queue = [root]
    while not len(queue) == 0:
        queue_size = len(queue)
        # get size of current queue
        nodes = []
        for i in range(queue_size):
            node = queue.pop(0)
            nodes.append(node.val)
            # check for the children and append to the queue if it's not none
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(nodes)
    return result


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    order_list = level_order(root)
    print("level orders : ", order_list)
