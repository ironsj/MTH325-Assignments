"""The Havel_Hakimi function takes a list as its parameter. It first checks to see if the number of
0's in the list is equal to the list. If so, the function returns True. The function then puts the list
in descending order. After this it checks to see if the last element in this list is less than 0. If so,
it returns false. Then the first element is removed. After, it checks if the first element is greater than
the length of the list and returns False if so. Then, 1 is subtracted for the next elements up to whatever
the element that was removed was equal to. Then, the first element is removed and the function is
called recursively if True or False was never returned"""


def Havel_Hakimi(seq):
    if seq.count(0) == len(seq):
        return True
    seq.sort(reverse=True)
    if seq[len(seq) - 1] < 0:
        return False
    firstElement = seq.pop(0)
    if firstElement >= len(seq):
        return False
    for i in range(firstElement):
        seq[i] = seq[i] - 1
    return Havel_Hakimi(seq)


a = [5, 5, 5, 5, 4, 4]
print(Havel_Hakimi(a))
