def dirReduc(arr):
    ns = {"NORTH", "SOUTH"}
    ew = {"EAST", "WEST"}
    i = 0
    l = len(arr)

    while len(arr) > i+1:
        if len(arr)>1 and({arr[i], arr[i+1]} == ns or {arr[i], arr[i+1]} == ew):
            arr.pop(i)
            arr.pop(i)
            if i > 0:
                i -=1

        else:
            i += 1
    return arr