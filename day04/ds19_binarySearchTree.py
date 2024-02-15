# file: ds19_binarySearchTree.py
# desc: 이진검색트리 구현

class TreeNode():
    left= None
    data= None
    right= None

    def __init__(self) -> None:
        self.left = self.right = self.data = None

# def preorder(node):
#     if node == None:
#         return
#     print (node.data, end = ' -> ')
#     preorder(node.left)
#     preorder(node.right)

def inorder(node):
    if node == None: return
    inorder(node.left)
    print(node.data, end = ' -> ')
    inorder(node.right)

# def postorder(node):
#     if node == None: return

#     postorder(node.left)
#     postorder(node.right)
#     print(node.data, end = ' -> ')

# 전역 변수
root = None
grouplist = ['블랙핑크', '레드벨벳', '마마무','에이핑크','걸스데이','트와이스']

# 메인
node = TreeNode()
node.data = grouplist[0]
root = node

for name in grouplist[1:]:
    node = TreeNode()
    node.data = name
    
    curr = root
    while True:
        if name < curr.data:
            if curr.left == None:
                curr.left = node
                break
            else:
                curr = curr.left
        else:
            if curr.right == None:
                curr.right = node
                break
            else:
                curr = curr.right

curr = root
print('중위 순회: ', end = ' ')
inorder(curr)
print('끝')

deleteName = '마마무'
curr = root
parent = None

while True:
    if deleteName == curr.data:
        if curr.left == None and curr.right == None:
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None

            del(curr) # 연결이 끊어진 노드를 완전 삭제
        elif curr.left != None and curr.right == None: # 내노드 왼쪽에 자식 노드가 있으면
            if parent.left == curr:
                parent.left = curr.left
            else:
                parent.right = curr.left
            
            del(curr)
        elif curr.left == None and curr.right != None: # 내 노드 오른쪽에 자식 노드가 있으면
            if parent.left == curr:
                parent.left = curr.right
            else:
                parent.right = curr.right

            del(curr)
        
        print(f'{deleteName}이 삭제됨')
        break

    elif deleteName < curr.data:
        if curr.left == None:
            print(f'{deleteName}이 트리에 없음')
            break
        else:
            parent = curr
            curr = curr.left
    else:
        if curr.right == None:
            print(f'{deleteName}이 트리에 없음')
            break
        else:
            parent = curr
            curr = curr.right

curr = root
print('중위 순회: ', end = ' ')
inorder(curr)
print('끝')
