# A Personal Tracing
# [16, 17, 4, 3, 5, 2]
# [17, 17, 4, 3, 5, 2]
# [17, 5, 4, 3, 5, 2]
# [17, 5, 5, 5, 5, 2]
# [17, 5, 5, 5, 2, -1]
while 0 == 0 :
    list = ['1) Array index switch' , '2) Little numbers counter','3) Symmetrical matrixs' , '4) Sparse matrix' , '5) Spiral matrix']
    for i in list :
        print()
        print(i)
    print()
    choose = int(input('Choose once:'))
    print()
    if choose == 1 :
        list2 = []
        choose2 = int(input('How many indexs you want to enter to your array:'))
        for i in range(choose2) :
            index = int(input('enter the Number:'))
            list2.append(index)
        for j in range(len(list2)) :
            pass