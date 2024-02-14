# file: ds09_simpleLinkedList.py
# desc: 단순 연결리스트 전체 구현

# 노드 클래스 선언
class Node():
    data = None # 실제 데이터 변수
    link = None

    def __init__(self) -> None:
        self.data = None    # 클래스 자신이 self이므로 클래스의 변수에 접근하려면 반드시 self.
        self.link = None    

# start부터 시작해서 끝까지 노드.data 출력
def printNode(start):   
    curr = start    # start == head
    if curr == None: return # break, continue는 반복문일 때만 가능
    while True:
        if curr.link == None:   # 연결할 노드가 더이상 없으며
            print(curr.data)    # 자기 데이터만 출력하고    
            break               # 반복문 탈출
        else:
            print(curr.data, end=' -> ')    
            curr = curr.link
    print()

# 노드 삽입 함수
def insertNode(find, data):
    global head, prev, curr

    if head.data == find:   # 맨 처음 노드
        node = Node()
        node.data = data
        node.link = head 
        head = node
        return
    
    curr = head
    while curr.link != None:
        prev = curr 
        curr = curr.link   
        if curr.data == find:
            node = Node()
            node.data = data
            node.link = curr
            prev.link = node
            return

    node = Node()
    node.data = data
    curr.link = node
    return

# 노드 삭제 함수
def deleteNode(data):
    global head, prev, curr

    if head.data == data:
        curr = head
        head = head.link
        del(curr)
        return
    
    curr = head
    while curr.link != None:
        prev = curr
        curr = curr.link
        if curr.data == data:
            prev.link = curr.link
            del(curr)
            return

# 노드 검색 함수
def findNode(find):
    global head, curr
    curr = head
    if curr.data == find:
        return curr
    while curr.link != None:
        curr = curr.link
        if curr.data == find:
            
            return curr
    return print('없음')        


# 전역 변수
head, prev, curr = None,None,None
originData = ['다현','정연','쯔위','사나','지효']

# 메인 코드 영역
if __name__ == '__main__':
    node = Node()
    node.data = originData[0]
    head = node
    for name in originData[1:]: # 1번 인덱스부터 리스트 끝까지 반복
        prev = node
        node = Node()
        node.data = name
        prev.link = node

    print('최초 구성된 연결리스트')
    printNode(head)

    print('맨앞 노드 삽입')
    insertNode('다현','정국')
    printNode(head)

    print('중간 노드 삽입')
    insertNode('사나','미미')
    printNode(head)

    print('마지막 노드 삽입')
    insertNode('재남','알엠')
    printNode(head)

deleteNode('정국')
printNode(head)

deleteNode('쯔위')
printNode(head)

deleteNode('재남')
printNode(head)

fNode = findNode('정연')
print(f'찾은 노드 : {fNode.data}')