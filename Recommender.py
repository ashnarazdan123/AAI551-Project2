import tkinter
from Book import Book
from Show import Show
class Recommender():
    def __init__(self):
         self.__bookDict = {}
         self.__showDict = {}
         self.__associationsDict = {}

    def loadBooks(self):
        root = tkinter.Tk()
        root.withdraw()
        
        while True:
            path = tkinter.filedialog.askopenfilename(title = 'Select books file') 

            if not path:
                print("No file selected")
            else:
                try:
                    with open(path, 'r') as file:
                        for line in file:
                            line = line.strip().split()
                            newBook = Book(line[0], line[1], line[3], line[2], line[4], line[5], line[6], line[7], line[8], line[9], line[10])
                            self.__bookDict[newBook.getId()] = newBook
                    file.close()
                except FileNotFoundError:
                    print("File not found.")
                    continue
                    
    def loadShows(self):
        root = tkinter.Tk()
        root.withdraw()
        
        while True:
            path = tkinter.filedialog.askopenfilename(title = 'Select shows file') 

            if not path:
                print("No file selected")
            else:
                try:
                    with open(path, 'r') as file:
                        for line in file:
                            line = line.strip().split()
                            #show_id,type,title,director,cast,average_rating,country,date_added,release_year,rating,duration,listed_in,description
                            newShow = Show(line[0], line[2], line[5], line[1], line[3], line[4], line[6], line[7], line[8], line[9], line[10], line[11], line[12])  
                            self.__showDict[newShow.getId()] = newShow
                    file.close()
                except FileNotFoundError:
                    print("File not found.")
                    continue
    
    def loadAssociations(self):
        root = tkinter.Tk()
        root.withdraw()
        
        while True:
            path = tkinter.filedialog.askopenfilename(title = 'Select associations file') 

            if not path:
                print("No file selected")
            else:
                try:
                    with open(path, 'r') as file:
                        for line in file:
                            id0, id1 = line.strip().split(',')
                            #line[0] = ID 1, line[1] = ID 2
                            
                            # ===== USING ID0 AS OUTER DICT =====
                            if id0 not in self.__associationsDict:
                                # ID 0 not in dictionary
                                self.__associationsDict[id0] = {}
                                self.__associationsDict[id0][id1] = 1
                            else:
                                # ID 0 is already in dictionary
                                if id1 in self.__associationsDict[id0]:
                                    # ID1 already key in inner dictionary, increment count
                                    self.__associationsDict[id0][id1] += 1
                                else:
                                    # ID1 not key in inner dictionary
                                    self.__associationsDict[id0][id1] = 1
                            
                            # ===== USING ID1 AS OUTER DICT =====
                            if id1 not in self.__associationsDict:
                                # ID 1 not in dictionary
                                self.__associationsDict[id1] = {}
                                self.__associationsDict[id1][id0] = 1
                            else:
                                # ID 1 is already in dictionary
                                if id0 in self.__associationsDict[id1]:
                                    # ID2 already key in inner dictionary, increment count
                                    self.__associationsDict[id1][id0] += 1
                                else:
                                    # ID2 not key in inner dictionary
                                    self.__associationsDict[id1][id0] = 1
                    file.close()
                except FileNotFoundError:
                    print("File not found.")
                    continue
                
    def getMovieList(self):
        # Return title and runtime of movies
        for item in self.__showDict:
            if item.getShow() == "Movie":
                print(item.getTitle(), item.getDuration())
            
    def getTVList(self):
        # Return title and number of seasons of all shows
        for item in self.__showDict:
            if item.getShow() == "TV Show":
                print(item.getTitle(), item.getDuration())
    def getBookList(self):
        # Return Title and author of all books
        for item in self.__bookDict:
            print(item.getTitle(), item.getAuthors())
            
    def getMovieStats(self):
        # Return Ratings, percentage of ratings, (2 decimals)
        # Avg movie duration, (2 decimals)
        # Director of most movies
        # Actor of most movies
        # Most frequent movie genre
    def getTVStats(self):
        
    def getBookStats(self):
        
    def searchTVMovies(self):
        
    def searchBooks(self):
        
    def getRecommendations(self):
           