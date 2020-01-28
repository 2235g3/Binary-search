import random

def BS():
    def Binary_search(List, mid, trgt, hi_indx):
        found = False
        multi = 2
        while found == False:
            if trgt == List[mid]:
                print("Target found!")
                print("The target:", trgt)
                print("Its index position is:", mid)
                found = True
            multi = int(multi * 2)
            if trgt < List[mid]:
                mid = int((len(List) - 1) // multi)
            elif trgt > List[mid]:
                new = hi_indx - mid
                l = new // 2
                mid = int(new + l)

    def Bubble(List):
        i = 0
        for i in range(len(List) - 1, 0, -1):
            for i in range(i):
                first = List[i]
                second = List[i + 1]
                if first > second:
                    List[i] = second
                    List[i + 1] = first
                i = i + 1
                if i == len(List) - 1:
                    break
        return List
    
    lst = []
    num = 0
    number = 0
    loop = False
    choice = int(input("Do you want to choose the numbers in the list (1) or have them randomly generated (2)? "))
    size = int(input("How big do you want the list? "))
    if choice == 1:
        while num < size:
            ask = int(input("Enter a value: "))
            lst.append(ask)
            num = num + 1
        while loop == False:
            trgt = int(input("What is the target? "))
            for i in lst:
                if i != trgt:
                    number = number + 1
            if number < len(lst):
                loop = True
            else:
                print("Value is not in the list")
    elif choice == 2:
        bgvl = int(input("What do you want the biggest value to be? "))
        while num < size:
            rnum = random.randint(0, bgvl)
            lst.append(rnum)
            num = num + 1
        trgt = lst[random.randint(0, bgvl)]
    Bubble(lst)
    mid = int((len(lst) - 1) // 2)
    Len = len(lst) - 1
    Binary_search(lst, mid, trgt, Len)
            
BS()

