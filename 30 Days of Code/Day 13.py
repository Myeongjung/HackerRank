from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook():
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price
        
    def display(self):
        print("Title: "+ title)
        print("Author: "+ author)
        print("Price: "+ str(price))
        

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()