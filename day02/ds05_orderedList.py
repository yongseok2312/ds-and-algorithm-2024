# file: ds05_orderedList.py
# desc: 선형리스트 응용\2

def printPoly(p_x):
    term = len(p_x)-1
    polyStr = 'P(x) = '

    for i in range(len(px)):
        coef = p_x[i]

        if (coef >= 0):
            polyStr += '+'
            polyStr += str(coef) + 'X^' + str(term) + ''
            term -= 1
    return polyStr

def calcPoly(xVal, p_x):
    retValue = 0
    term = len(p_x)-1

    for i in range(len(px)):
        coef = p_x[i]
        retValue += coef* xVal ** term
        term -= 1
    return retValue

px = [7, -4, 0, 5]

if __name__ == '__main__':

    pSter = printPoly(px)
    print(pSter)
    xValue = int(input('X 값 -->'))

    pxValue = calcPoly(xValue, px)
    print(pxValue)