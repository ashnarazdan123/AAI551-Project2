import tkinter
from Book import Book
from Show import Show
from Media import Media
from tkinter import filedialog
class Recommender():
    def __init__(self):
         self.__bookDict = {}
         self.__showDict = {}
         self.__associationsDict = {}

    def loadBooks(self):
        root = tkinter.Tk()
        root.withdraw()
        
        while True:
            path = tkinter.filedialog.askopenfilename(title='Select books file')

            if not path:
                print("No file selected")
            else:
                try:
                    with open(path, 'r') as file:
                        for line in file:
                            line = line.strip().split(',')
                            if len(line) != 11:
                                print("Invalid format in line:", line)
                                tkinter.messagebox.showerror("Error", "Invalid Books File")
                                break
                            newBook = Book(line[0], line[1], line[3], line[2], line[4], line[5], line[6], line[7], line[8], line[9], line[10])
                            self.__bookDict[newBook.getId()] = newBook
                    file.close()
                    break
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
                            line = line.strip().split(',')
                            if len(line) != 13:
                                tkinter.messagebox.showerror("Error", "Invalid Shows File")
                                break
                            #show_id,type,title,director,cast,average_rating,country,date_added,release_year,rating,duration,listed_in,description
                            newShow = Show(line[0], line[2], line[5], line[1], line[3], line[4], line[6], line[7], line[8], line[9], line[10], line[11], line[12])  
                            self.__showDict[newShow.getId()] = newShow
                    file.close()
                    break
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
                            
                            if len(line.strip().split(',')) != 2:
                                tkinter.messagebox.showerror("Error", "Invalid Associations File")
                                break
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
                    break
                    
                except FileNotFoundError:
                    print("File not found.")
                
    def getMovieList(self):
        # Return title and runtime of movies
        maxTitleLen = 0
        maxDurationLen = 0
        
        movies = []
        for item in self.__showDict.values():
            if item.getShow() == "Movie":
                movies.append(item)
        
        for movie in movies:
            titleLen = len(movie.getTitle())
            durationLen = len(movie.getDuration())
            
            maxTitleLen = max(maxTitleLen, titleLen)
            maxDurationLen = max(maxDurationLen, durationLen)
        movieStr = f"{'Title':<{maxTitleLen}}  {'Duration':<{maxDurationLen}}\n" 
        
        for movie in movies:
            movieStr += f"{movie.getTitle():<{maxTitleLen}}  {movie.getDuration():<{maxDurationLen}}\n"
        return movieStr
            
    def getTVList(self):
        # Return title and number of seasons of all shows
        
        maxTitleLen = 0
        maxDurationLen = 0
        
        shows = []
        for item in self.__showDict.values():
            if item.getShow() == "TV Show":
                shows.append(item)
        
        for show in shows:
            titleLen = len(show.getTitle())
            durationLen = len(show.getDuration())
            
            maxTitleLen = max(maxTitleLen, titleLen)
            maxDurationLen = max(maxDurationLen, durationLen)
        showStr = f"{'Title':<{maxTitleLen}}  {'Seasons:':<{maxDurationLen}}\n" 
        
        for show in shows:
            showStr += f"{show.getTitle():<{maxTitleLen}}  {show.getDuration():<{maxDurationLen}}\n"
        return showStr

    def getBookList(self):
        maxTitleLen = 0
        maxAuthorLen = 0
        # Return Title and author of all books
        
        books = []
        for item in self.__bookDict.values():
            if item.getId() != "bookID":
                books.append(item)
        
        for book in books:
            titleLen = len(book.getTitle())
            authorLen = len(book.getAuthors())
            
            maxTitleLen = max(maxTitleLen, titleLen)
            maxAuthorLen = max(maxAuthorLen, authorLen)
        
        bookStr = f"{'Title':<{maxTitleLen}}  {'Author:':<{maxAuthorLen}}\n" 
        
        for book in books:
            bookStr += f"{book.getTitle():<{maxTitleLen}}  {book.getAuthors():<{maxAuthorLen}}\n"
        return bookStr
    
    def getMovieRatings(self):
        ratingDict = {}
        ratingPercentages ={}
        
    # Code to calculate movie ratings percentages
        for show in self.__showDict.values():
                    # add ratings to rating dict
                    if show.getShow() == "Movie":
                        rating = show.getRating()
                        if rating not in ratingDict:
                            ratingDict[rating] = 1
                        else:
                            ratingDict[rating] += 1

        totalShows = sum(ratingDict.values())
                #calculate rating percentages
        for rating, count in ratingDict.items():
            percentage = (count / totalShows) * 100
            ratingPercentages[rating] = "{:.2f}".format(percentage)
        return ratingPercentages

    def getTVRatings(self):
        ratingDict = {}
        ratingPercentages = {}

        # add ratings to rating dict
        for show in self.__showDict.values():
            if show.getShow() == "TV Show":
                rating = show.getRating()
                if rating not in ratingDict:
                    ratingDict[rating] = 1
                else:
                    ratingDict[rating] += 1
        totalShows = sum(ratingDict.values())
         #calculate rating percentages
        for rating, count in ratingDict.items():
            percentage = (count / totalShows) * 100
            ratingPercentages[rating] = "{:.2f}".format(percentage)
        return ratingPercentages

            
    def getMovieStats(self):
        ratingDict = {}
        totalMovies = 0
        directorsDict = {}
        actorsDict = {}
        genreDict = {}
        ratingPercentages = {}
        totalDuration = 0

        for show in self.__showDict.values():
            # add ratings to rating dict
            if show.getShow() == "Movie":
                rating = show.getRating()
                if rating not in ratingDict:
                    ratingDict[rating] = 1
                else:
                    ratingDict[rating] += 1

                duration = show.getDuration().split(" ")
               # verify the show has a duration and add to total
                if len(duration) == 2 and "min" in duration[1]:
                    try:
                        totalDuration += int(duration[0])
                        totalMovies += 1
                    except ValueError:
                        pass
                # iterate through directors, actors, and genres and add to the dict and increment value
                director = show.getDirectors()
                if director.strip():
                    if director not in directorsDict:
                        directorsDict[director] = 1
                    else:
                        directorsDict[director] += 1

                actors = show.getActors().split("\\")
                for actor in actors:
                    if actor.strip():
                        if actor not in actorsDict:
                            actorsDict[actor] = 1
                        else:
                            actorsDict[actor] += 1

                genres = show.getGenres().split(",")
                for genre in genres:
                    if genre.strip():
                        if genre not in genreDict:
                            genreDict[genre] = 1
                        else:
                            genreDict[genre] += 1

        totalShows = sum(ratingDict.values())

        #calculate rating percentages
        for rating, count in ratingDict.items():
            percentage = (count / totalShows) * 100
            ratingPercentages[rating] = "{:.2f}".format(percentage)
        #avergae movie duration
        if totalMovies > 0:
            avgDuration = totalDuration / totalMovies
        else:
            avgDuration = 0
        #most frequent director
        maxDirector = None
        if directorsDict:
            maxDirector = max(directorsDict, key=directorsDict.get)
        #most frequent actor
        maxActor = None
        if actorsDict:
            maxActor = max(actorsDict, key=actorsDict.get)
        #most frequent genre
        maxGenre = None
        if genreDict:
            maxGenre = max(genreDict, key=genreDict.get)
        movieStats = "Ratings: \n"
        for rating, percentage in ratingPercentages.items():
            movieStats += f"{rating}: {percentage}%\n"

        movieStats += f"Avg Duration:{avgDuration:.2f} minutes \nMax Director: {maxDirector}\nMax Actor: {maxActor}\nMax Genre: {maxGenre}"

        return movieStats

    def getTVStats(self):
        ratingDict = {}
        totalSeasons = 0
        actorsDict = {}
        ratingPercentages = {}
        genreDict={}
        # add ratings to rating dict
        for show in self.__showDict.values():
            if show.getShow() == "TV Show":
                rating = show.getRating()
                if rating not in ratingDict:
                    ratingDict[rating] = 1
                else:
                    ratingDict[rating] += 1
                # calculate total num of seasons
                duration = show.getDuration().split(" ")
                if len(duration) == 2 and "Season" in duration[1]:
                    try:
                        num_seasons = int(duration[0])
                        totalSeasons += num_seasons
                    except ValueError:
                        pass
                # add and increment the actors into dict
                actors = show.getActors().split("\\")
                for actor in actors:
                    if actor.strip():
                        if actor not in actorsDict:
                            actorsDict[actor] = 1
                        else:
                            actorsDict[actor] += 1
                # calculate genres
                genres = show.getGenres().split("\\")
                for genre in genres:
                    genre = genre.strip()
                    if genre:
                        if genre not in genreDict:
                            genreDict[genre] = 1
                        else:
                            genreDict[genre] += 1

        totalShows = sum(ratingDict.values())
       # calulate rating percentages
        for rating, count in ratingDict.items():
            percentage = (count / totalShows) * 100
            ratingPercentages[rating] = "{:.2f}".format(percentage)
        #average seasons
        if totalShows > 0:
            avgSeasons = totalSeasons / totalShows
        else:
            avgSeasons = 0
        #most frequent actor
        maxActor = None
        if actorsDict:
            maxActor = max(actorsDict, key=actorsDict.get)
        
        #most frequent genre
        maxGenre = None
        if genreDict:
            maxGenre = max(genreDict, key=genreDict.get)

        tvStats = "Ratings:\n"
        for rating, percentage in ratingPercentages.items():
            tvStats += f"{rating}: {percentage}%\n"

        tvStats += f"Average Number of Seasons: {avgSeasons:.2f} seasons \nMost Frequent Actor: {maxActor}\nMost Frequent Genre: {maxGenre}"

        return tvStats

    
    def getBookStats(self):
        pageCountTotal = 0
        authorsDict = {}
        publishersDict = {}

        for book in self.__bookDict.values():
            #total num of pages
            pageCount = book.getNumPages()
            try:
                pageCountTotal += int(pageCount)
            except ValueError:
                pass
            #add authors to author dict
            authors = book.getAuthors().split("\\")  
            for author in authors:
                if author.strip():
                    if author not in authorsDict:
                        authorsDict[author] = 1
                    else:
                        authorsDict[author] += 1
            #add publishes to publisher dict
            publisher = book.getPublisher()  
            if publisher:  
                if publisher not in publishersDict:
                    publishersDict[publisher] = 1
                else:
                    publishersDict[publisher] += 1


        totalBooks = len(self.__bookDict)
        #average num of pages
        if totalBooks > 0:
            avgPageCount = pageCountTotal / totalBooks  
        else:
            avgPageCount = 0
        #most frequent author
        maxAuthor = None
        if authorsDict:
            maxAuthor = max(authorsDict, key=authorsDict.get)
        #most frequent publisher
        maxPublisher = None
        if publishersDict:
            maxPublisher = max(publishersDict, key=publishersDict.get)
        bookStats = ""
        bookStats += f"Average number of pages: {avgPageCount:.2f} pages\nMost Frequent Author: {maxAuthor}\nMost Frequent Publisher: {maxPublisher}"
        return bookStats

    def searchTVMovies(self, typeOf, title, director, actor, genre):
        maxTitleLen = 0
        maxDirectorLen = 8
        maxActorLen = 0
        maxGenreLen = 0
        #check for type
        if typeOf not in ["Movie", "TV Show"]:
            tkinter.messagebox.showerror("Error", "This is not a valid type. Pick TV Show or Movie.")
            return "No Results"
        # generate error in no info entered
        if not (title or director or actor or genre):
            tkinter.messagebox.showerror("Error", "No valid information entered. Please enter information for Title, Director, Actor, and/or Genre.")
            return "No Results"
        
        shows = []
        #add matching shows to dict
        for show in self.__showDict.values():
            if (typeOf == "Movie" and show.getShow() == "Movie") or (typeOf == "TV Show" and show.getShow() == "TV Show"):
                if (title.lower() in show.getTitle().lower()) and (director.lower() in show.getDirectors().lower()) and (actor.lower() in show.getActors().lower()) and (genre.lower() in show.getGenres().lower()):
                    shows.append(show)
        
        if len(shows) ==0:
            return "No Results"
        
        #formatting
        for show in shows:
            titleLen = len(show.getTitle())
            directorLen = len(show.getDirectors())
            actorLen = len(show.getActors())
            genreLen = len(show.getGenres())

            maxTitleLen = max(maxTitleLen, titleLen)
            maxDirectorLen = max(maxDirectorLen, directorLen)
            maxActorLen = max(maxActorLen, actorLen)
            maxGenreLen = max(maxGenreLen, genreLen)

        showStr = f"{'Title':<{maxTitleLen}}  {'Director':<{maxDirectorLen}}  {'Actors':<{maxActorLen}}  {'Genre':<{maxGenreLen}}\n"
        #add to output string
        for show in shows:
            showStr += f"{show.getTitle():<{maxTitleLen}}  {show.getDirectors():<{maxDirectorLen}}  {show.getActors():<{maxActorLen}}  {show.getGenres():<{maxGenreLen}}\n"
        return showStr
        
    def searchBooks(self, title, author, publisher):
        maxTitleLen = 0
        maxAuthorLen = 0
        maxPublisherLen = 0
        # throw error for no info
        if not (title or author or publisher):
            tkinter.messagebox.showerror("Error", "No valid information entered. Please enter information for Title, Author, and/or Publisher.")
            return "No Results"

        books = []
        #append matching books
        for book in self.__bookDict.values():
            if (title.lower() in book.getTitle().lower()) and (author.lower() in book.getAuthors().lower()) and (publisher.lower() in book.getPublisher().lower()):
                books.append(book)

        if len(books) == 0:
            return "No Results"
        
        #formatting 
        for book in books:
            titleLen = len(book.getTitle())
            authorLen = len(book.getAuthors())
            publisherLen = len(book.getPublisher())

            maxTitleLen = max(maxTitleLen, titleLen)
            maxAuthorLen = max(maxAuthorLen, authorLen)
            maxPublisherLen = max(maxPublisherLen, publisherLen)

        bookStr = f"{'Title':<{maxTitleLen}}  {'Author':<{maxAuthorLen}}  {'Publisher':<{maxPublisherLen}}\n"
        #book string to output
        for book in books:
            bookStr += f"{book.getTitle():<{maxTitleLen}}  {book.getAuthors():<{maxAuthorLen}}  {book.getPublisher():<{maxPublisherLen}}\n"

        return bookStr

        
    def getRecommendations(self, typeOf, title):
        
        assocList = []
        itemID = 0
        showID = 0 
       
        if typeOf in ["Movie", "TV Show"]:
           maxTitleLen = 0
           maxAuthorLen = 0
           showTitleList = []
           # search show dictionary
           for show in self.__showDict.values():
               showTitleList.append(show.getTitle().lower())
               if title.lower() in show.getTitle().lower():
                # title is in dictionary
                # get title ID
                    showID = show.getId().lower() # set showID to id of desired show
           #Title not in list
           if title.lower() not in showTitleList:
                tkinter.messagebox.showerror("Error", "No recommendations for that title")
                return "No Results"   
        # go through associations dictionary
        
        # Associations Dictionary -> (ID {KEY} -> (ID {KEY} -> Count{VALUE}) {VALUE})
           for item in self.__associationsDict.keys(): #Iterate through associations Keys
               if showID == item:                       # if showID found in associationDict 
                   assocID = self.__associationsDict[item]    # assoc ID set to dictionary
            
        # Find associated books with assocID
           for item in assocID.keys(): # Item referring to associated book object ID
               for book in self.__bookDict.values():  # Iterate through bookDict
                   if book.getId() == item:  # If bookDict ID matches associated book objectID
                       assocList.append(book) # append assocList with associated book objects
                       
           for item in assocList:
                titleLen = len(item.getTitle())
                authorLen = len(item.getAuthors())

                maxTitleLen = max(maxTitleLen, titleLen)
                maxAuthorLen = max(maxAuthorLen, authorLen)
                
           bookRec = f"{'Title':<{maxTitleLen}}  {'Author':<{maxAuthorLen}}\n"
           for book in assocList:
                bookRec += f"{book.getTitle():<{maxTitleLen}}  {book.getAuthors():<{maxAuthorLen}}\n"    
           return bookRec
           
        elif typeOf in ["Book"]:
           maxTitleLen = 0
           maxDirectorLen = 0
           maxActorLen = 0
           maxGenreLen = 0
           bookID = 0
           bookTitleList = []
           # search book dictionary for desired book 
           for book in self.__bookDict.values():
               bookTitleList.append(book.getTitle().lower())
               if title.lower() in book.getTitle().lower():
                    bookID = book.getId().lower() #store bookID to search association dict
                
           if title.lower() not in bookTitleList: # title not in dictionary
                tkinter.messagebox.showerror("Error", "No recommendations for that title")
                return "No Results"    
                
           # search association dict for desired association ID     
           for item in self.__associationsDict.keys():
                if bookID == item:
                    # if bookID matches ID of item access dictionary containing the associations to book ID
                    assocID = self.__associationsDict[item] # assocID given the dictionary containing the associated IDs and their values
                    # assocID -> contains ID's of shows and movies associated with given book
            
        # Find associated shows with assocID
           for item in assocID.keys():
               for show in self.__showDict.values():
                   if show.getId() == item: #item (associated shows ID) found in showDict
                       assocList.append(show) #append assocList with associated show object
           
           for show in assocList:
               # Find max length for all object lines
                titleLen = len(show.getTitle())
                directorLen = len(show.getDirectors())
                actorLen = len(show.getActors())
                genreLen = len(show.getGenres())

                maxTitleLen = max(maxTitleLen, titleLen)
                maxDirectorLen = max(maxDirectorLen, directorLen)
                maxActorLen = max(maxActorLen, actorLen)
                maxGenreLen = max(maxGenreLen, genreLen)
                       
           showRec = f"{'Title':<{maxTitleLen}}  {'Director':<{maxDirectorLen}}  {'Actors':<{maxActorLen}}  {'Genre':<{maxGenreLen}}\n"
           for show in assocList:
                showRec += f"{show.getTitle():<{maxTitleLen}}  {show.getDirectors():<{maxDirectorLen}}  {show.getActors():<{maxActorLen}}  {show.getGenres():<{maxGenreLen}}\n"    
           return showRec
               

