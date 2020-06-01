import queue
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None: return root
        processor = queue.Queue()
        processor.put([root])
        
        while not processor.empty(): # So I had been running nonsense since by using queue
            current = processor.get()
            nextNodes = []
            for node in current:
                if node:
                    nextNodes.append(node.left)
                    nextNodes.append(node.right)
            i = len(nextNodes) - 1
            # processor.put(nextNodes)
            
            # nextNodes.reverse()
            current.reverse() # ?? evaluated and returns None, so I cant implicitly put in for loop
            for node in current:
                if node:
                    node.left = nextNodes[i]
                    i -= 1
                    node.right = nextNodes[i]
                    i -= 1
            if len(nextNodes) > 1: processor.put(nextNodes)
                    
        return root

# Questions:
# 1. So its an acyclic connected graph, parent child relationship, no BST invariant.
# 2. What about subtree roots with null children. How to invert at that stage? * Give my own example, and other edge cases

# Use Clean Code principles, readable/simple code, good variable names, no line mizing, DRY, SRP, patterns
# Start talking out loud, asking questions then thinking through doing it, initial ideas
# Talk about space and time and how you could possibly improve, say it loud
# No paper practicing for now/whiteboard
# use a queue, also considering a stack
# Resulting to writing in a notebook and thinking out loud

# Space complexity is O(n): n/2 elements in queue and in nextNodes list max at any point in time
# Time complexity is O(n): process every node. Appends is constant time, put is O(1), reverse?? repointing?? No more reverse, we now use i and decrement.

# Another idea, use a deque as reverse and repointing seems it would take lots of time.
# I get a Time Limit Exceeded
# NOTE: 
# 1. Use an explicit is empty check, no over cleverness. while not processor.empty():
# 2. Look at variable names. I'm happy I did not run this in an IDE.