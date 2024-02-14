# file: ds14_stackBracelet.py
# desc: 스택 수식 정합여부 판단

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

# 수식괄호 판단 함수
def checkBracket(expr):
    for ch in expr: # '(' 'a' '+' 'b' ')'
        if ch in '({[<':    #여는 괄호가 있으면
            push(ch)
        elif ch in ')}]>':  # 닫는 괄호가 있으면
            out = pop()
            if ch == ')' and out == '(':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == ']' and out =='[':
                pass
            elif ch == '>' and out =='<':
                pass
            else:
                return False
        else:
            continue

    if isStackEmpty() == True:
        return True
    else: 
        return False


# 전역 변수 선언
size = 50
stack = [None for _ in range(size)]
top = -1


# 메인코드

if __name__=='__main__':
    arr = ['(a+b)',')a*b(', '((a+b)-c', '(a+b]', '(<a+{a+b}/[c*d]>)']

    for expr in arr:
        top = -1
        print(f'{expr} ==> {checkBracket(expr)}')