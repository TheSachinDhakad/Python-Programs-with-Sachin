import time


def searcher ():
    import datetime
    book = "this is a book from harry and code with ahrry and good"
    time.sleep(4)

    while True:
        text = (yield )
        if text in book:
         print("your  test is in the book ")

        else:
            print("your text is not in the book ")

search = searcher()
print("search started ......")
next(search)
print("next method run..")
search.send("harry")
# input("press any key")
# search.send("harry and")


