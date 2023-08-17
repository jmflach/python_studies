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
        print(f'inserindo elemento {element} em {list} na posição {pos}')
        list.insert(pos, element)
        return list

    def __find_position(self, list, element):
        for i, e in enumerate(list):
            if element < e:
                return i
        return len(list)
        