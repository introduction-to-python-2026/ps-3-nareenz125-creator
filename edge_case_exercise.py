def move(myList, direction):
    index_of_one = myList.index(1)
    myList[index_of_one] = 0  

    if direction == "right":
        if index_of_one < len(myList) - 1:  
            myList[index_of_one + 1] = 1
        else:
            myList[index_of_one] = 1  
    elif direction == "left":
        if index_of_one > 0:  
            myList[index_of_one - 1] = 1
        else:
            myList[index_of_one] = 1  

    return myList
