
def binary_search(array, element, left, right):

    if left > right: # если левая граница превысила правую,
        return False #
    
   
    middle = (right+left) // 2 # находим середину
    if array[middle] == element: # если элемент в середине,
        return print ('Номер позиции элемента, который меньше введенного N: ', middle-1, 'Номер позиции элемента, который больше/равен введенному N: ',  middle)
    # возвращаем этот индекс
    elif element < array[middle]: # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle-1)
    else: # иначе в правой
        return binary_search(array, element, middle+1, right)




def sort_list (x): # создаем и сортируем список
   
    b.sort()
    return (b)


x = input('введите последовательность чисел через пробел: ')
element = int(input('введите число N: '))
a = x.split(' ')
b =[int(i) for i in a]

while element <= min(b) or element >= max(b):
    print ('N находится вне границ последовательности. Пожалуйста, введите другое число: ')
    element = int(input('введите число N: '))
    

b.append(element)
sort_x = sort_list(b)
print(binary_search(sort_x, element, 0, len(sort_x)-1))

