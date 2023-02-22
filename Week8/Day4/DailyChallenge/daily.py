class Pagination:
    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = int(pageSize)
        self.totalPages = int(len(items) / pageSize) + (1 if len(items) % pageSize > 0 else 0)
        self.currentPage = 1

    def getVisibleItems(self):
        startIndex = (self.currentPage - 1) * self.pageSize
        endIndex = startIndex + self.pageSize
        return self.items[startIndex:endIndex]

    def prevPage(self):
        self.currentPage = max(self.currentPage - 1, 1)
        return self

    def nextPage(self):
        self.currentPage = min(self.currentPage + 1, self.totalPages)
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        pageNum = int(pageNum)
        self.currentPage = max(min(pageNum, self.totalPages), 1)
        return self

    # testing
alphabetList = "abcdefghijklmnopqrstuvwxyz"
p = Pagination(alphabetList, 15)
print(p.getVisibleItems())
p.nextPage().nextPage()
print(p.getVisibleItems())
p.goToPage(10)
print(p.currentPage)
p.goToPage(-1)
print(p.currentPage)