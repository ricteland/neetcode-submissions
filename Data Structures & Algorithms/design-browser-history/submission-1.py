class BrowserHistory:

    def __init__(self, homepage: str):

        self.history = [homepage]
        self.cursor = 0

    def visit(self, url: str) -> None:
        
        del self.history[self.cursor+1:]

        self.history.append(url)
        self.cursor += 1
        print(f"Visited {url}, history {self.history}, cursor {self.cursor}")

    def back(self, steps: int) -> str:

        steps = min(steps, self.cursor)

        self.cursor -= steps

        print(f"Went back {steps} steps, now at {self.history[self.cursor]}")
        return self.history[self.cursor]

    def forward(self, steps: int) -> str:
        
       availible = len(self.history) -1 - self.cursor

       steps = min(steps, availible)

       self.cursor += steps
       print(f"Went forward {steps} steps, now at {self.history[self.cursor]}")

       return self.history[self.cursor]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)