from Media import Media
class Book(Media):
    def __init__(self, id, title, avgRating, authors, isbn, isbn13, langCode, numPages, numRatings, pubDate, publisher):
        super().__init__(id, title, avgRating)
        self.__authors = authors
        self.__isbn = isbn
        self.__isbn13 = isbn13
        self.__langCode = langCode
        self.__numPages = numPages
        self.__numRatings = numRatings
        self.__pubDate = pubDate
        self.__publisher = publisher
    
    def getAuthors(self):
        return self.__authors

    def setAuthors(self, authors):
        self.__authors = authors

    def getIsbn(self):
        return self.__isbn

    def setIsbn(self, isbn):
        self.__isbn = isbn

    def getIsbn13(self):
        return self.__isbn13

    def setIsbn13(self, isbn13):
        self.__isbn13 = isbn13

    def getLangCode(self):
        return self.__langCode

    def setLangCode(self, langCode):
        self.__langCode = langCode

    def getNumPages(self):
        return self.__numPages

    def setNumPages(self, numPages):
        self.__numPages = numPages

    def getNumRatings(self):
        return self.__numRatings

    def setNumRatings(self, numRatings):
        self.__numRatings = numRatings

    def getPubDate(self):
        return self.__pubDate

    def setPubDate(self, pubDate):
        self.__pubDate = pubDate

    def getPublisher(self):
        return self.__publisher

    def setPublisher(self, publisher):
        self.__publisher = publisher