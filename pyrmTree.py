# Pyrm binary tree
# searched bottom up

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def evaluate_bottom_up(node):
    # Base Case: If we hit a leaf (a number), return it
    if isinstance(node.value, int):
        print(f"  Reached Leaf: {node.value}")
        return node.value

    # THE DIVE: Recursively solve the left and right sides first
    left_val = evaluate_bottom_up(node.left)
    right_val = evaluate_bottom_up(node.right)

    # THE BOTTOM-UP ACTION: Now that we have child values, solve the parent
    print(f"Calculating: {left_val} {node.value} {right_val}")
    
    if node.value == '+': return left_val + right_val
    if node.value == '-': return left_val - right_val
    if node.value == '*': return left_val * right_val
    if node.value == '/': return left_val / right_val

# --- Building the Tree Structure ---
# (3 + 5) * (10 - 2)
left_side = Node('+', Node(3), Node(5))
right_side = Node('-', Node(10), Node(2))
root = Node('*', left_side, right_side)

# --- Running the Algorithm ---
print("Starting Recursive Bottom-Up Search...")
final_result = evaluate_bottom_up(root)
print(f"\nFinal Result at the Root: {final_result}")
