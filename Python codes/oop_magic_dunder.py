# special methods
class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    # to directly print(b) we use __str__ function
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    # to find length
    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book has been deleted")

b=Book('python','jose',200)
print(b)
#OUPUT== python by jose

print(len(b))
#OUTPUT== 200

del b
#OUTPUT== a book has been deleted