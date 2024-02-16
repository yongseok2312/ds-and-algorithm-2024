# file: ds21_dfs.py
# desc: 그래프 깊이 우선 탐색 구현

# 그래프 클래스 선언, 인접 행렬을 담고 있는 객체
class Graph():
    SIZE = graph = None     # 멤버 변수

    def __init__(self,size) -> None:
        self.SIZE = size
        self.graph = [ [0 for _ in range(self.SIZE)] for _ in range(self.SIZE)]

# 전역 변수 선언
G1 = None
stack = visited =  list()

# 메인 코드
G1 = Graph(4)
G1.graph[0][2] = G1.graph[2][0] = 1 
G1.graph[0][3] = G1.graph[3][0] = 1 
G1.graph[1][2] = G1.graph[2][1] = 1 
G1.graph[2][3] = G1.graph[3][2] = 1 

print('무방향 그래프 > ')
for row in range(4):
    for col in range(4):
        print(G1.graph[row][col], end = ' ')
    print()


