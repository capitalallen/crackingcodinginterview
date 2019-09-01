class Node:

    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item

    def __str__(self):
        return '('+str(self.left)+':L ' + "V:" + str(self.val) + " R:" + str(self.right)+')'


# def initiateArrayToBinary(array):
#     return initArrayToBinaryHelper(array, 0, len(array) - 1)


def initArrayToBinary(arr):
    return initArrayToBinaryHelper(arr,0,len(arr)-1)
def initArrayToBinaryHelper(arr,start,end):
    #middle of start and end
    #if middle equals to 0 return ''
    #root: node of arr[middle]
    #recursion: left start to middle -1
    #recursion: right middle to end
    #return root
    if start > end:
        return ''
    middle = (start+end)//2
    root = Node(arr[middle])
    root.left = initArrayToBinaryHelper(arr,start,middle-1)
    root.right = initArrayToBinaryHelper(arr,middle+1,end)
    return root

# class Node:

#     def __init__(self, item):
#         self.right = None
#         self.left = None
#         self.val = item

#     def __str__(self):
#         return '('+str(self.left)+':L ' + "V:" + str(self.val) + " R:" + str(self.right)+')'


# def initiateArrayToBinary(array):
#     return arrayToBinary(array, 0, len(array) - 1)


# def arrayToBinary(array, start, end):
#     if start > end:
#         return ''
#     mid = (start + end) // 2
#     print(start,end,mid)
#     root = Node(array[mid])
#     root.left = arrayToBinary(array, start, mid - 1)
#     root.right = arrayToBinary(array, mid + 1, end)
#     return root

testArray = [0,1,2,3,4,5]
print(initArrayToBinary(testArray))
