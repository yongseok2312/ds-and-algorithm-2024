# file: ds17_circularqueue.py
# desc: 원형 큐 일반 구현 원형 큐에서는 rear|front % SIZE 개념이 핵심

# queue 풀 함수
def isQueueFull():
    global SIZE, rear, front, queue
    if (rear+1) % SIZE == front:
        return True
    else:
        return False
    

# queue 엠티 확인 함수
def isQueueEmpty():
    global front, rear
    if front == rear:
        return True
    else:
        return False
    
# queue 데이터 삽입 함수
def enQueue(data):
    global queue, rear,SIZE
    if isQueueFull() == True: # 큐가 꽉차서 데이터 입력 불가
        print('큐가 꽉찼습니다.')
        return # 함수 탈출
    else:
        rear = (rear+1) % SIZE
        queue[rear] = data

# queue 데이터 추출 함수
def deQueue():
    global front,queue, SIZE
    if isQueueEmpty()==True:
        print('큐가 비었습니다.')
        return
    else:
        front = (front+1) % SIZE
        data = queue[front]
        queue[data] = None
        return data
    
# 추출 데이터 확인함수
def peek():
    global queue, front,SIZE
    if isQueueEmpty() == True:
        print('큐가 비었습니다.')
        return None
    else:
        return queue[(front+1)%SIZE]
    

# 전역 변수
SIZE = int(input('큐 크기 입력하세요(정수) > '))   # 상수(constant) 대문자 사용
queue = [ None for _ in range(SIZE)]
front = rear = 0

# 메인 코드
if __name__ == '__main__':
#   queue = [None, None, '문별', '휘인', '선미']
#   front  =1
#   rear = 4 
#   print(isQueueFull())
#   print(queue)
  
  
    while True:
        select = input('삽입(e), 추출(d), 확인(p), 종료(x) > ')

        if select.lower() == 'e':
            data = input('입력 데이터 > ')
            enQueue(data)
            print(f'큐상태 : {queue}')
        elif select.lower() == 'd':
            data = deQueue()
            print(f'추출데이터: {data}')
            print(f'큐상태: {queue}')
        elif select.lower() == 'p':
            data = peek()
            print(f'확인 데이터 > {data}')
            print(f'큐상태 : {queue}')
        elif select.lower() == 'x':
            break
        else:
            continue


