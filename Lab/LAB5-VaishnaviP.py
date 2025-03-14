from collections import defaultdict
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def buildTree(elements):
    if len(elements) == 0:
        return None
    root_node = TreeNode(elements[0])
    nodes = [root_node]
    for i, x in enumerate(elements[1:]):
        if x is None:
            continue
        parent_node = nodes[i // 2]
        is_left = (i % 2 == 0)
        node = TreeNode(x)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)
    return root_node

def verticalOrder(mylist):
    if len(elements) == 0:
        return None
    root = buildTree(mylist)
    column_map = defaultdict(list)
    min_col, max_col = 0, 0
    queue = deque([(root, 0)])

    while queue:
        node, col = queue.popleft()
        column_map[col].append(node.val)
        min_col = min(min_col, col)
        max_col = max(max_col, col)

        if node.left:
            queue.append((node.left, col - 1))
        if node.right:
            queue.append((node.right, col + 1))

    result = []
    for col in range(min_col, max_col + 1):
        result.append(column_map[col])

    return result

if __name__ == "__main__":
    elements1 = [3, 9, 8, 4, 0, 1, 7, None, None, None, 2, 5]
    print(verticalOrder(elements1))  

