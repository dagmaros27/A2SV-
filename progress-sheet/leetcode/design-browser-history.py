class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homePage = Node(homepage)
        self.currentPage = self.homePage
        
    def visit(self, url: str) -> None:
        newPage = Node(url)
        newPage.prev = self.currentPage
        self.currentPage.next = newPage
        self.currentPage = newPage

        

    def back(self, steps: int) -> str:
        while self.currentPage.prev and steps > 0:
            self.currentPage = self.currentPage.prev
            steps -= 1
        return self.currentPage.val

        

    def forward(self, steps: int) -> str:
        while self.currentPage.next and steps > 0:
            self.currentPage = self.currentPage.next
            steps -= 1
        
        return self.currentPage.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)