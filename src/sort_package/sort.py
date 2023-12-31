class Sort:
    def __init__(self, list):
        self.list = list

    def selection_sort(self):
        for i in range(len(self.list)):
            min_index = self.__select_min(self.list, i, len(self.list))
            self.list = self.__swap_elements(self.list, i, min_index)
        return self.list
    
    def __select_min(self, list, init, end):
        min = list[init]
        for i in range(init, end):
            if list[i] < min:
                min = list[i]
        return list.index(min)
    
    def __swap_elements(self, list, i, j):
        aux_i = list[i]
        aux_j = list[j]
        list.pop(i)
        list.insert(i, aux_j)
        list.pop(j)
        list.insert(j, aux_i)
        return list
    
    def insertion_sort(self):
        sorted_list = []
        for element in self.list:
            self.__insert(sorted_list, element)
        self.list = sorted_list
        return self.list
    
    def __insert(self, list, element):
        pos = self.__find_position(list, element)
        list.insert(pos, element)
        return list

    def __find_position(self, list, element):
        for i, e in enumerate(list):
            if element < e:
                return i
        return len(list)
        
    def merge_sort(self, array):
        # Divide the unsorted list into n sublists, 
        # each containing one element (a list of one element is considered sorted).
        # Repeatedly merge sublists to produce new sorted sublists until there is 
        # only one sublist remaining. This will be the sorted list.
        if len(array) == 1:
            return array
        else:
            cut = len(array)/2
            return self.__merge(self.merge_sort(array[:cut]), self.merge_sort(array[cut:]))

    def merge_sort_2(self):
        divided_list = []
        merged_list = []
        for e in self.list:
            divided_list.append([e])
        
        while(len(divided_list) > 1):
            merged_list = []
            for i in range(0, len(divided_list), 2):
                if i == len(divided_list)-1:
                    merged = divided_list[i]
                else:
                    merged = self.__merge(divided_list[i], divided_list[i+1])
                merged_list.append(merged)
            divided_list = merged_list
        return divided_list[0]
            
    def __merge(self, list1, list2):
        # Given two sorted lists, merge then into a sorted list
        index1 = 0
        index2 = 0
        sorted_list = []

        while (index1 < len(list1) and index2 < len(list2)):
            if list1[index1] < list2[index2]:
                sorted_list.append(list1[index1])
                index1 += 1
            else:
                sorted_list.append(list2[index2])
                index2 += 1

        if index1 < len(list1):
            sorted_list.extend(list1[index1:])
        if index2 < len(list2):
            sorted_list.extend(list2[index2:])
        return sorted_list
    
    def bubble_sort(self):
        swap = True
        aux = 0
        while(swap):
            swap = False
            for i in range(0, len(self.list) - 1 - aux):
                if self.list[i] > self.list[i+1]:
                    swap = True
                    self.__swap_elements(self.list, i, i+1)
            aux += 1
        return self.list
    
    def quick_sort(self, array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            array.pop(0)
            min = filter(lambda x: x <= pivot, array)
            max = filter(lambda x: x > pivot, array)
            return self.quick_sort(min) + [pivot] + self.quick_sort(max)




# 2 4 6
# 3 5 7
# 2 3 4 5 6 7
# compara os 2 menores. o menor vai pra lista final.
# compara 

# 2 4 6
# 3 5 7 9


# 2 4 6 8
# 3 5 9

