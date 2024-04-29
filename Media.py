class Media:
    def __init__(self, id, title, avgRating):
        self.__id = id
        self.__title = title
        self.__avgRating = avgRating

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def getAvgRating(self):
        return self.__avgRating

    def setAvgRating(self, avgRating):
        self.__avgRating = avgRating
