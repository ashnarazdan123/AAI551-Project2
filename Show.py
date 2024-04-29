from Media import Media

class Show(Media):
    def __init__(self, id, title, avgRating, show, directors, actors, countryCode, dateAdded, releaseYear, rating, duration, genres, description):
        super().__init__(id, title, avgRating)
        self.__show = show
        self.__directors = directors
        self.__actors = actors
        self.__countryCode = countryCode
        self.__dateAdded = dateAdded
        self.__releaseYear = releaseYear
        self.__rating = rating
        self.__duration = duration
        self.__genres = genres
        self.__description = description

    def getShow(self):
        return self.__show

    def setShow(self, show):
        self.__show = show

    def getDirectors(self):
        return self.__directors

    def setDirectors(self, directors):
        self.__directors = directors

    def getActors(self):
        return self.__actors

    def setActors(self, actors):
        self.__actors = actors

    def getCountryCode(self):
        return self.__countryCode

    def setCountryCode(self, countryCode):
        self.__countryCode = countryCode

    def getDateAdded(self):
        return self.__dateAdded

    def setDateAdded(self, dateAdded):
        self.__dateAdded = dateAdded

    def getReleaseYear(self):
        return self.__releaseYear

    def setReleaseYear(self, releaseYear):
        self.__releaseYear = releaseYear

    def getRating(self):
        return self.__rating

    def setRating(self, rating):
        self.__rating = rating

    def getDuration(self):
        return self.__duration

    def setDuration(self, duration):
        self.__duration = duration

    def getGenres(self):
        return self.__genres

    def setGenres(self, genres):
        self.__genres = genres

    def getDescription(self):
        return self.__description

    def setDescription(self, description):
        self.__description = description
