# file: ds11_stack.py
# desc: 스택 전체 구현

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
size = 5
stack = [None for _ in range(size)]
top = -1


# 메인코드

if __name__=='__main__':

    while   True: 
        select= input('push(p),pop(o),peek(e),exit(x) > ')

        if select.lower() =='p':
            data = input('입력데이터 >> ')
            push(data)
            print(f'스택상태: {stack}')
        elif select.lower() == 'o':
            data = pop()
            print(f'추출 데이터: {data}')
            print(f'스택상태: {stack}')
        elif select.lower() == 'e':
            data = peek()
            print(f'확인 데이터: {data}')
            print(f'스택상태: {stack}')
        elif select.lower() == 'x':
            exit(0)
        else:
            continue