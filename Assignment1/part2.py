def partition_list(numbers):
    def inner(numbers, start=0, stop=len(numbers)-1, forward=True):
        mini = 99999999
        maxi = 0
        if forward:
            if numbers[start] < numbers[start+1]:
                return inner(numbers, start=start+1, forward=True)
            else:
                x = start+1
                while x<len(numbers):
                    if mini>numbers[x]:
                        mini = numbers[x]
                    x+=1
                while start>0:
                    if numbers[start]<=mini:
                        return numbers[:start+1]
                    start-=1
        else:
            if numbers[stop] > numbers[stop-1]:
                return inner(numbers, stop=stop-1, forward=False)
            else:
                x = stop-1
                while x>0:
                    if maxi<numbers[x]:
                        maxi = numbers[x]
                    x-=1
                while stop<len(numbers):
                    if numbers[stop]>=maxi:
                        return numbers[stop:]
                    stop+=1
    num_left = inner(numbers=numbers, forward=True)
    num_right= inner(numbers=numbers, forward=False)
    num_mid = numbers[len(num_left):len(numbers)-len(num_right)]
    return num_left, num_mid, num_right

NUMBERS= [1,3,4,6,8,10,13,15,11,9,12,13,15,17,20,25]
print partition_list (NUMBERS)