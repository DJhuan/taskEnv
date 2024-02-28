
class Todo:
    def __init__(self, title, details, deadline=False):
        self.title = title
        self.details = details
        self.deadline = "No deadline" if deadline == False else deadline

    def info(self):
        return (self.title, self.details, self.deadline)

if __name__ == "__main__":
    new_todo = Todo("Simple task", "Nothing much")
    print(new_todo.info())

