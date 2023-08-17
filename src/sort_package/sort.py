class Sort:
    def __init__(self, list):
        self.list = list

    def selection_sort(self):
        for i in range(len(self.list)):
            min_index = self.__select_min(self.list, i, len(self.list))
            self.list = self.__swap_elements(self.list, i, min_index)
        return self.list
    
    def __select_min(self, list, init, end):
        print(list, init, end)
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