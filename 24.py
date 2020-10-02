
arr = [9,7,6,8,5,3,2,4,1,0]
def kSmallest(arr):
    arr.sort(reverse=False)
    for i in arr:
        print (arr[i])
kSmallest(arr)
