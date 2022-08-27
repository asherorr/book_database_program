from models import (Base, session,
                    Book, engine)

# main menu (add, search, analysis, exit, view options)
# add books to the database
# edit books
# delete them
# search function
# data cleaning function
# loop to run the program
# when the user decides to exit, the program stops.

if __name__ == "__main__":
    Base.metadata.create_all(engine)