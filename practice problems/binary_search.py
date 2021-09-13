# binary search practice 
from typing import Any, Sequence

def binary_search(a: Sequence, key: Any) -> int:
    """search sequence a to find one that matches with key"""
    pl=0 #leftmost index
    pr=len(a)-1 #rightmost index

    while True:
        pc = (pl+pr)//2 #center index
        if a[pc] == key:
            return pc
        elif a[pc]>key:
            pr = pc-1
        else: 
            pl = pc+1
        if pl > pr:
            break
    return -1

if __name__ == '__main__':
    num=int(input("how many elements are in the sequence?"))
    x=[None]*num
    
    for i in range(len(x)):
        x[i]=int(input("insert an integer for the sequence: "))

    k = int(input("which number do you want to find?"))

    answer = binary_search(x, k)

    if answer != -1:
        print(f'number {k} is found at index number {answer}.')
    else:
        print(f'number {k} is not found.')

