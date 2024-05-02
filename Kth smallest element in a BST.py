class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize an empty stack to perform in-order traversal
        stack = []
        # Initialize a variable to count the number of visited nodes
        n = 0
        # Start with the root node
        temp = root

        # Perform in-order traversal
        while temp or stack:
            # Traverse as far left as possible, pushing each node onto the stack
            while temp:
                stack.append(temp)
                temp = temp.left
            # Once we reach the leftmost node, start popping nodes from the stack
            temp = stack.pop()
            # Increment the count of visited nodes
            n += 1
            # If count becomes equal to k, return the value of the current node
            if n == k:
                return temp.val
            # Move to the right subtree and continue traversal
            temp = temp.right

        # Return 0 if kth smallest element not found (shouldn't happen in a valid BST)
        return 0