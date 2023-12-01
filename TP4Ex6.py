def custom_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                print(arr)
    print(arr)

my_list = [5, 2, 4, 8, 1, 3]

custom_sort(my_list)
print(sorted(my_list))
print(my_list)
my_list.sort()
print(my_list)
