class DynamicArray:
    def __init__(self):
        self.size=0
        self.capacity=4
        self.array=[None]*self.capacity

    def append(self,item):
        if(self.size == self.capacity):
            self._resize()
        self.array[self.size]=item
        self.size+=1

    def _resize(self):
        new_capacity= 2*(self.capacity)
        new_arr=[None]*new_capacity
        for i in range(self.size):
            new_arr[i]=self.array[i]

        self.array=new_arr
        self.capacity=new_capacity


    def get(self,index):
        if index < 0 or index >= self.capacity:
            raise IndexError("Out Of Bounds")
        return self.array[index]

    def pop(self):
        if (self.size==0):
             raise IndexError("Empty Error")

        self.size=self.size-1
        item=self.array[self.size]
        self.array[self.size]=None

        if self.size > 0 and  self.size <= self.capacity//4:
            self._shrink()
        return item

    def _shrink(self):
        self.capacity=max(4,self.capacity//2)
        new_arr=[ None]*self.capacity
        for i in range(self.capacity):
            new_arr[i]=self.array[i]
        self.array=new_arr

    def __str__(self):
        # Only show the active items, ignore the None padding at the end
        active_items = self.array[:self.size]
        return f"Array: {active_items} (Size: {self.size}, Capacity: {self.capacity})"


da = DynamicArray()
da.append("A")
da.append("B")
da.append("C")
da.append("D")
da.append("E") # This triggers the resize!

print("Array contents:", da)
print("Item at index 1:", da.get(1))
print("Popped item:", da.pop())
print("Array after pop:", da)








        