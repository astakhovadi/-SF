
def binary_search(array, element, left, right):

    
    if (element > array[-2]) and element != array[-2] : # 
        return print ('Номер позиции элемента, который меньше введенного N: ', len(sort_x)-1)
    
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
    a = x.split(' ')
    b =[int(i) for i in a]
    
    b.sort()
    
    return (b)


x = input('введите последовательность чисел через пробел: ')
element = int(input('введите число N: '))
x=x+' ' + str(element)
sort_x = sort_list(x)


print(binary_search(sort_x, element, 0, len(sort_x)-1))





