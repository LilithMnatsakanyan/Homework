def bubble_sort(l):

    for i in range(len(l)):
        swapped = False
        for j in range(0, len(l) - i - 1):

            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True

        if not swapped:
            break


l = [77, 24, 25, 72, 90, 90]
print("List:", l)

bubble_sort(l)

print("Sorted list:", l)
