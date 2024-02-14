# file: ds13_stack.py
# desc: 스택 전체 구현

import webbrowser
import time
def isStackFull():
    global size, stack, top
    if top == (size -1):
        return True #스택이 꽉 찼음
    else:
        return False
    
def push(data): 
    global size, stack, top
    if isStackFull() == True:
        print('스택이 꽉찼습니다.')
        return
    else:
        top+=1
        stack[top] = data

def isStackEmpty():
    global size, stack, top
    if top <= -1:
        return True # 스택이 비었음
    else:
        return False
    
def pop():
    global size, stack, top
    if isStackEmpty() == True:
        print('스택이 비었습니다.')
        return 
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data
    
def peek():
    global stack, top
    if isStackEmpty() == True:
        print('스택이 비어있습니다.')
        return None
    else:
        return stack[top]


# 전역 변수 선언
size = 10
stack = [None for _ in range(size)]
top = -1


# 메인코드

if __name__=='__main__':
    urls = ['naver.com', 'daum.net', 'nate.com','bing.com','github.com']
    for url in urls:
        push(url)
        webbrowser.open(f'https://www.{url}')
        print(url, end=' --> ')
        time.sleep(1)

    print('방문종료')
    time.sleep(5) # 5초 동안 아무것도 하지 않고 대기

    print(stack)
    while True:
        url = pop()
        if url == None: break

        webbrowser.open(f'https://www.{url}')
        print(url,end=' -> ')
        time.sleep(1)
print('방문 종료')
    