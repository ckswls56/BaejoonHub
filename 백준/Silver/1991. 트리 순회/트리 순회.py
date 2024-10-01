class Node:
    
    def __init__(self,item,left=0,right=0):
        self.item = item
        self.left = left
        self.right = right


def preorder(node):
    print(node.item,end="")        
    if node.left!='.':
        preorder(tree[node.left])
    if node.right!='.':
        preorder(tree[node.right])
        
def inorder(node):
            
    if node.left!='.':
        inorder(tree[node.left])
        
    print(node.item,end="")
    
    if node.right!='.':
        inorder(tree[node.right])
        
def postorder(node):
            
    if node.left!='.':
        postorder(tree[node.left])
    if node.right!='.':
        postorder(tree[node.right])
    print(node.item,end="")
    
n = int(input())

inputs = []
for _ in range(n):
    inputs.append(input().split())
    
tree = {}
    
for i,l,r in inputs:
    tree[i] = Node(i,l,r)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])