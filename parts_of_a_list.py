a = ["az", "toto", "picaro", "zone", "kiwi"] 

def partlist(arr):
    left = arr.pop(0)
    right = arr.pop(-1)
    while i > (len(arr) + 1):
        if i <= 1:
            arr.pop(0)
    return (left, right)

print(partlist(a))