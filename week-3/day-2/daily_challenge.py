import math
class Pagination():
    current_page = 1
    def __init__(self, items: list, page_size: int):
        self.items = items
        self.page_size = page_size
    def firstPage(self):
        self.current_page = 1
        return self.items[0:self.page_size]
    def lastPage(self):
        self.current_page = math.ceil(len(self.items)/self.page_size)
        return self.items[0 - self.page_size:]
    def goToPage(self, page_num):
        if page_num > math.ceil(len(self.items)/self.page_size):
            self.current_page = math.ceil(len(self.items)/self.page_size)
        elif page_num < 1:
            self.current_page = 1
        else:
            self.current_page = page_num
        print(self.items[(self.current_page - 1)*self.page_size:self.current_page*self.page_size])
    def getVisibleItems(self):
        print(self.items[(self.current_page - 1)*self.page_size:self.current_page*self.page_size])
    def prevPage(self):
        if self.current_page > 1:
            self.current_page = self.current_page - 1
        return self
    def nextPage(self):
        if self.current_page < math.ceil(len(self.items)/self.page_size):
            self.current_page = self.current_page + 1
        return self

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
p.getVisibleItems() 
# ["a", "b", "c", "d"]

p.nextPage()

p.getVisibleItems()
# ["e", "f", "g", "h"]

p.lastPage()

p.getVisibleItems()
# ["y", "z"]