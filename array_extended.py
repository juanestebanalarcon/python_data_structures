from random import randint as rdint
class Array:
    def __init__(self,capacity,fill_value=None):
        self.items=list()
        for item in range(capacity):
            self.items.append(fill_value)
    def __len__(self):
        return len(self.items)
    def __str__(self) -> str:
        return str(self.items)
    def __iter__(self):
        return iter(self.items)
    def __getItem__(self,index):
        return self.items[index]
    def __setitem__(self,index,new_item):
        self.items[index]=new_item
    def __setRandomItems__(self):
        for i in range(rdint(1,10)):
            self.items[i]=rdint(20,100)
        return self.items
    def __sumItems__(self):
        sum_items=sum(self.__setRandomItems__())
        print(sum_items)
    