#question 1 ieee (COMPLETE)
S = input("Enter a string of even length : ")
L = len(S)
def func_breaker():
    P = S[:int(L/2)]
    Q = S[int(L/2):]

    if P==Q :
        print('yes')
    else:
        print('no')
if L%2 == 0:
    func_breaker()
else:
    print("Retry!")