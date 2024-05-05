import tkinter
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import *
from tkinter import messagebox
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from Recommender import Recommender

class RecommenderGUI:
    def __init__(self):
        #recommender object
        self.__rec = Recommender()
        self.__main_window = tkinter.Tk()
        self.__main_window.title("Media Recommender")
        self.__main_window.geometry("1200x800")
        #notebook
        self.__nb = ttk.Notebook(self.__main_window)
        self.__nb.pack(expand=1 , fill=tkinter.BOTH)
        #tabs
        self.__defaultText = "No data has been loaded yet"

        #movies
        self.__movies = ttk.Frame(self.__nb)
        self.__nb.add(self.__movies, text = "Movies")
        self.__textM = scrolledtext.ScrolledText(self.__movies, wrap=tkinter.WORD, height=25)
        self.__textM.grid(row=0, column=0, sticky="nsew")
        self.__textMavg = tkinter.Text(self.__movies, wrap=tkinter.WORD, height=10)
        self.__textMavg.grid(row=1, column=0, sticky="nsew")
        self.__movies.grid_columnconfigure(0, weight=1)
        self.__movies.grid_rowconfigure(1, weight=1)


        #tv
        self.__tv = ttk.Frame(self.__nb)
        self.__nb.add(self.__tv, text = "TV Shows")
        self.__textTV = scrolledtext.ScrolledText(self.__tv, wrap=tkinter.WORD, height=25)
        self.__textTV.grid(row=0, column=0, sticky="nsew")
        self.__textTVavg = tkinter.Text(self.__tv, wrap=tkinter.WORD, height=10)
        self.__textTVavg.grid(row=1, column=0, sticky="nsew")
        self.__tv.grid_columnconfigure(0, weight=1)
        self.__tv.grid_rowconfigure(1, weight=1)

        #books
        self.__books = ttk.Frame(self.__nb)
        self.__nb.add(self.__books, text = "Books")
        self.__textB = scrolledtext.ScrolledText(self.__books, wrap=tkinter.WORD, height=25)
        self.__textB.grid(row=0, column=0, sticky="nsew")
        self.__textBavg = tkinter.Text(self.__books, wrap=tkinter.WORD, height=10)
        self.__textBavg.grid(row=1, column=0, sticky="nsew")
        self.__books.grid_columnconfigure(0, weight=1)
        self.__books.grid_rowconfigure(1, weight=1)

        #search tv/movies
        self.__searchTVM = ttk.Frame(self.__nb)
        self.__nb.add(self.__searchTVM, text = "Search Movies / TV")
        self.__textTVM = scrolledtext.ScrolledText(self.__searchTVM, wrap=tkinter.WORD)
        self.__optionsTVM = ["Movie" , "TV Show"]
        self.__cbTVM = ttk.Combobox(self.__searchTVM, values=self.__optionsTVM)
        self.__typeLabel = tkinter.Label(self.__searchTVM,text="Type:")
        self.__titleLabel = tkinter.Label(self.__searchTVM,text="Title:")
        self.__entryTitleTVM = tkinter.Entry(self.__searchTVM, width=50)
        self.__directorLabel = tkinter.Label(self.__searchTVM, text="Director:")
        self.__entryDirector = tkinter.Entry(self.__searchTVM, width=50)
        self.__actorLabel = tkinter.Label(self.__searchTVM, text="Actor:")
        self.__entryActor = tkinter.Entry(self.__searchTVM, width=50)
        self.__genreLabel = tkinter.Label(self.__searchTVM, text="Genre:")
        self.__entryGenreTVM = tkinter.Entry(self.__searchTVM, width=50)
        self.__buttonTVM = tkinter.Button(self.__searchTVM, text="Search", padx=7,command=self.searchShows)

        #packing for search tv/movies
        self.__typeLabel.grid(row=0, column=0, sticky=tkinter.W)
        self.__cbTVM.grid(row=0, column=1, sticky=tkinter.W)
        self.__titleLabel.grid(row=1, column=0, sticky=tkinter.W)
        self.__entryTitleTVM.grid(row=1,column=1, sticky=tkinter.W)
        self.__directorLabel.grid(row=2,column=0, sticky=tkinter.W)
        self.__entryDirector.grid(row=2,column=1, sticky=tkinter.W)
        self.__actorLabel.grid(row=3,column=0, sticky=tkinter.W)
        self.__entryActor.grid(row=3,column=1, sticky=tkinter.W)
        self.__genreLabel.grid(row=4,column=0, sticky=tkinter.W)
        self.__entryGenreTVM.grid(row=4,column=1, sticky=tkinter.W)
        self.__buttonTVM.grid(row=5,column=1, sticky=tkinter.W)
        self.__textTVM.grid(row=6, column=1, sticky="nsew")
        self.__searchTVM.grid_rowconfigure(6,weight=1)
        self.__searchTVM.grid_columnconfigure(1, weight=1)


        #search books
        self.__searchB = ttk.Frame(self.__nb)
        self.__nb.add(self.__searchB, text = "Search Books")
        self.__stextB = scrolledtext.ScrolledText(self.__searchB, wrap=tkinter.WORD)
        self.__titleLabelB = tkinter.Label(self.__searchB, text="Title:")
        self.__entryTitleB = tkinter.Entry(self.__searchB, width=50)
        self.__authorLabel = tkinter.Label(self.__searchB, text="Author:")
        self.__entryAuthor = tkinter.Entry(self.__searchB, width=50)
        self.__publisherLabel = tkinter.Label(self.__searchB, text="Publisher:")
        self.__entryPublisher = tkinter.Entry(self.__searchB, width=50)
        self.__buttonB = tkinter.Button(self.__searchB, text="Search", padx=7, command=self.searchBooks)

        #packing for search books
        self.__titleLabelB.grid(row=0, column=0, sticky=tkinter.W)
        self.__entryTitleB.grid(row=0, column=1, sticky=tkinter.W)
        self.__authorLabel.grid(row=1, column=0, sticky=tkinter.W)
        self.__entryAuthor.grid(row=1, column=1, sticky=tkinter.W)
        self.__publisherLabel.grid(row=2, column=0, sticky=tkinter.W)
        self.__entryPublisher.grid(row=2, column=1, sticky=tkinter.W)
        self.__buttonB.grid(row=3, column=1, sticky=tkinter.W)
        self.__stextB.grid(row=4, column=1, sticky="nsew")
        self.__searchB.grid_rowconfigure(4, weight=1)
        self.__searchB.grid_columnconfigure(1, weight=1)


        #recommendations
        self.__recTab = ttk.Frame(self.__nb)
        self.__nb.add(self.__recTab, text = "Recommendations")
        self.__textR = scrolledtext.ScrolledText(self.__recTab, wrap=tkinter.WORD)
        self.__typeLabelR = tkinter.Label(self.__recTab, text="Type:")
        self.__optionsR = ["Movie", "TV Show", "Book"]
        self.__cbR = ttk.Combobox(self.__recTab, values=self.__optionsR)
        self.__titleLabelR = tkinter.Label(self.__recTab, text="Title:")
        self.__entryTitleR = tkinter.Entry(self.__recTab, width=50)
        self.__buttonR = tkinter.Button(self.__recTab, text="Get Recommendation", command=self.getRecommendations)

        self.__typeLabelR.grid(row=0, column=0, sticky=tkinter.W)
        self.__cbR.grid(row=0, column=1, sticky=tkinter.W)
        self.__titleLabelR.grid(row=1, column=0, sticky=tkinter.W)
        self.__entryTitleR.grid(row=1, column=1, sticky=tkinter.W)
        self.__buttonR.grid(row=2, column=1, sticky=tkinter.W)
        self.__textR.grid(row=3, column=1, sticky="nsew")
        self.__recTab.grid_rowconfigure(3, weight=1)
        self.__recTab.grid_columnconfigure(1, weight=1)

       #ratings
        self.__ratingsTab = ttk.Frame(self.__nb)
        self.__nb.add(self.__ratingsTab, text="Ratings")

        #function buttons
        self.__buttonFrame = tkinter.Frame(self.__main_window)
        self.__buttonFrame.pack(side=tkinter.BOTTOM,pady=10)
        self.__buttonLS = tkinter.Button(self.__buttonFrame, text="Load Shows", command=self.loadShows) 
        self.__buttonLS.pack(side=tkinter.LEFT,padx=80)
        self.__buttonLB = tkinter.Button(self.__buttonFrame, text="Load Books", command=self.loadBooks)
        self.__buttonLB.pack(side=tkinter.LEFT, padx=80)
        self.__buttonLR = tkinter.Button(self.__buttonFrame, text="Load Recommendations", command=self.loadAssociations)
        self.__buttonLR.pack(side=tkinter.LEFT,padx=80)
        self.__buttonInfo = tkinter.Button(self.__buttonFrame, text="Information", command=self.creditInfoBox)
        self.__buttonInfo.pack(side=tkinter.LEFT, padx=80)
        self.__buttonQ = tkinter.Button(self.__buttonFrame, text="Quit", command=self.quitButton)
        self.__buttonQ.pack(side=tkinter.LEFT, padx=80)

        #default text and configure state of text
        self.__textWidgets = [self.__textM, self.__textMavg, self.__textTVavg, self.__textBavg, self.__stextB,
                              self.__textTV, self.__textTVM, self.__textB, self.__textR]
        for widget in self.__textWidgets:
            widget.insert("1.0", self.__defaultText)
            widget.configure(state=tkinter.DISABLED)

    def quitButton(self):
        self.__main_window.destroy()
        exit()

    def loadShows(self):
        self.__rec.loadShows()
        movieList = self.__rec.getMovieList()
        tvList = self.__rec.getTVList()
        movieRatings = self.__rec.getMovieRatings()
        tvRatings = self.__rec.getTVRatings()
        self.createMovieRatings(movieRatings)
        self.createTVRatings(tvRatings)

        #movies
        
        self.__textM.configure(state=NORMAL)
        self.__textM.delete("1.0", tkinter.END)
        self.__textM.insert(tkinter.END, movieList)
        movieStats = self.__rec.getMovieStats()
        self.__textMavg.configure(state=NORMAL)
        self.__textMavg.delete("1.0", tkinter.END)
        self.__textMavg.insert(tkinter.END, movieStats)
        self.__textMavg.configure(state=DISABLED)

        #TV Shows
        self.__textTV.configure(state=NORMAL)
        self.__textTV.delete("1.0", tkinter.END)
        self.__textTV.insert(tkinter.END, tvList)
        self.__textTV.configure(state=DISABLED)
        tvStats = self.__rec.getTVStats()
        self.__textTVavg.configure(state=NORMAL)
        self.__textTVavg.delete("1.0", tkinter.END)
        self.__textTVavg.insert(tkinter.END, tvStats)
        self.__textTVavg.configure(state=DISABLED)
    
    def createMovieRatings(self, movieRatings):
        #create the pie chart for movie ratings
        if movieRatings:
            labels = list(movieRatings.keys())
            values = list(movieRatings.values())
            
            fig, ax = plt.subplots(figsize=(5, 5))
            ax.pie(values, labels=labels, autopct='%1.2f%%')
            ax.axis('equal')
            ax.set_title('Movie Ratings')
            
            canvas = FigureCanvasTkAgg(fig, master=self.__ratingsTab)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tkinter.LEFT, padx=80)
        else:
            print("No movie ratings data available.")

    def createTVRatings(self, TVratings):
        #create pie chart for tv ratings
        if TVratings:
            labels = list(TVratings.keys())
            values = list(TVratings.values())
            
            fig, ax = plt.subplots(figsize=(5, 5))
            ax.pie(values, labels=labels, autopct='%1.2f%%')
            ax.axis('equal')
            ax.set_title('TV Show Ratings')
            
            canvas = FigureCanvasTkAgg(fig, master=self.__ratingsTab)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tkinter.LEFT, padx=80)

            
        else:
            print("No TV show ratings data available.")

    def loadBooks(self):
        books = self.__rec.loadBooks()
        bookList = self.__rec.getBookList()
        self.__textB.configure(state=NORMAL)
        self.__textB.delete("1.0",tkinter.END)
        self.__textB.insert(tkinter.END, bookList)
        self.__textB.configure(state=DISABLED)
        bookStats = self.__rec.getBookStats()
        self.__textBavg.configure(state=NORMAL)
        self.__textBavg.delete("1.0",tkinter.END)
        self.__textBavg.insert(tkinter.END, bookStats)
        self.__textBavg.configure(state=DISABLED)

    def loadAssociations(self):
       recs = self.__rec.loadAssociations()


    def creditInfoBox(self):
        messagebox.showinfo(title="Credit Information", message="""Created by
Teddy Nueva Espana, Ashna Razdan, and Jacob Bower.
Completed on 5/5/2024.""")


    def searchShows(self):
        type = self.__cbTVM.get()
        title = self.__entryTitleTVM.get()
        director = self.__entryDirector.get()
        actor = self.__entryActor.get()
        genre = self.__entryGenreTVM.get()
        tvmovieSearchList = self.__rec.searchTVMovies(type,title,director,actor,genre)
        self.__textTVM.configure(state=NORMAL)
        self.__textTVM.delete("1.0",tkinter.END)
        self.__textTVM.insert(tkinter.END,tvmovieSearchList)
        self.__textTVM.configure(state=DISABLED)

    def searchBooks(self):
        title = self.__entryTitleB.get()
        author = self.__entryAuthor.get()
        pub = self.__entryPublisher.get()
        bookSearchList = self.__rec.searchBooks(title,author,pub)
        self.__stextB.configure(state=NORMAL)
        self.__stextB.delete("1.0",tkinter.END)
        self.__stextB.insert(tkinter.END,bookSearchList)
        self.__stextB.configure(state=DISABLED)


    def getRecommendations(self):
        title = self.__entryTitleR.get()
        typeOf = self.__cbR.get() 
        recString = self.__rec.getRecommendations(typeOf = typeOf, title = title)
        self.__textR.configure(state=NORMAL)
        self.__textR.delete("1.0",tkinter.END)
        self.__textR.insert(tkinter.END, recString)
        self.__textR.configure(state=DISABLED)


def main():
    gui = RecommenderGUI()
    tkinter.mainloop()

main()