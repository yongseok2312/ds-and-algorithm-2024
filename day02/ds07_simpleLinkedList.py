# file: ds07_simpleLinkedList.ipynb
# desc: 단순 연결 리스트 일반 구현

memory = [] # 컴퓨터 메모리를 유사구성
# head,curr, prev 일반변수
# head = node
head, curr, prev = None, None, None

class Node():
    # data, link 두개의 멤버변수 존재
    # 생성자 추가
    def __init__(self, name) -> None:
        self.data = name
        self.link = None

def printNodes(start):
    curr = start
    if curr == None: return
    print(curr.data, end = ' -> ')
    while curr.link != None:
        curr = curr.link
        print(curr.data, end= ' -> ')
    print()


dataArray = ['다현', '정연', '쯔위', '사나', '지효'] 

if __name__ == '__main__':
    node = Node(dataArray[0])   # 다현 데이터 담은 노드 생성
    head = node # 첫번째 값을 head가 가리킴
    memory.append(node) # 가짜 메모리에 집어넣음

    for data in dataArray[1:]: # 두번째 노드부터 끝까지
        prev = node
        node = Node(data) # 정연
        prev.link = node
        memory.append(node)
    printNodes(head)