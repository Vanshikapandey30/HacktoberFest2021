
from tkinter import *
from PIL import ImageTk,Image
import tkinter.font as font
import mysql.connector
import requests
import json

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MongoDB_2",
    database="movie"
)

root=Tk()
root.title("The House of Cinema")
root.iconbitmap("C:/Users/RAJAT/Desktop/Programming/Programming/Python learning for projects/garlic.ico")
root.geometry("590x260")
root.configure(bg='#fafafa')

img1 = ImageTk.PhotoImage(Image.open("images/posters/suggestions/memento.jpg"))


def submit():
    root.state('zoomed')
    imageLabel.destroy()
    passwordLabel.destroy()
    nameLabel.destroy()
    nameEntry.destroy()
    passwordEntry.destroy()
    page1btn.destroy()
    headlabel.destroy()

    title = Label(root,text="The House of Cinema",bg="#fafafa")
    title['font']=headFont2
    title.grid(row=0,column=0,columnspan=3,padx=4,sticky=W)
    
    global SearchBox
    SearchBox = Entry(root,width=30)
    SearchBox.grid(row=1,column=0,pady=(60,0),padx=10,sticky=W)

    #delete line below 
    SearchBox.insert(0,"Blade Runner")
    search = Button(root,text="Search",command=Search)
    b1 = Button(root,text="Trending Movies",bg="silver",command=trending)
    b2 = Button(root,text="Highest Rated",bg="silver",command=ratings)
    b3 = Button(root,text="Movie of the Month",bg="silver",command=motm)
    b4 = Button(root,text="Latest Released",bg="silver",command=latest)
    b5 = Button(root,text="Liked Movies ",bg="silver",command=likeitoff)
    b6 = Button(root,text="Watchlist ",bg="silver",command=watchitoff)
    
    search.grid(row=2,column=0,padx=10,sticky=W,pady=(5,10),ipadx=69)
    b1.grid(row=3,column=0,sticky=W,padx=10,pady=(30,0),ipadx=41)
    b2.grid(row=4,column=0,sticky=W,padx=10,ipadx=48)
    b3.grid(row=5,column=0,sticky=W,padx=10,ipadx=32)
    b4.grid(row=6,column=0,sticky=W,padx=10,ipadx=45)
    b5.grid(row=7,column=0,sticky=W,padx=10,ipadx=49)
    b6.grid(row=8,column=0,sticky=W,padx=10,ipadx=59)

    imglabel = Label(root,image=img1)
    imglabel.grid(row=9,column=0,sticky=W,padx=10,pady=(20,0))
    caption = Label(root,text="Movie of the day",bg="#fafafa")
    caption['font']=myfont
    caption.grid(row=10,column=0,padx=19,pady=2,sticky=W)

    global frame
    frame=LabelFrame(root,width=1145,height=710)
    frame.grid(row=1,column=1,rowspan=50,pady=(40,0),columnspan=20)
    frame.grid_propagate(0)

    ### empty space
    a="  "
    empty = Label(frame,text=a*108)
    empty.grid(row=0,column=1,columnspan=2)
 
def Search():
    global frame
    frame=LabelFrame(root,width=1145,height=710)
    frame.grid(row=1,column=1,rowspan=50,pady=(40,0),columnspan=20)
    frame.grid_propagate(0)

    a="  "
    empty = Label(frame,text=a*108)
    empty.grid(row=0,column=1,columnspan=2)
    name = SearchBox.get()

    #DBMS
    b=SearchBox.get()
    mycursor= mydb.cursor()
    query = "SELECT ID,NAME FROM MOVIE_ID WHERE NAME = %s"
    add = (b,)
    mycursor.execute(query,add)
    result=mycursor.fetchone()
    
    #MOVIE POSTER
    global poster
    poster = ImageTk.PhotoImage(Image.open("images/posters/"+name+".jpg"))
    posterLabel = Label(frame,image=poster)
    posterLabel.grid(row=1,column=3,rowspan=10,sticky=N,pady=(60,0))

    askReview = Label(frame,text="Watched it already??")
    askReview['font']=normal
    askReview.grid(row=8,column=3,sticky=NW,padx=(8,0))

    askReview2 = Label(frame,text="Give a review")
    askReview2['font']=normal
    askReview2.grid(row=8,column=3,padx=(8,0),sticky=SW)

    reviewd = Button(frame,text="Done")
    reviewd.grid(row=8,column=3,sticky=SE,padx=(0,5),ipadx=20)
    
    review = Entry(frame,width=43)
    review.grid(row=9,column=3,columnspan=2,padx=(8.5,0),sticky=W)

    ### MOVIE ID
    global ID,MOVIE
    ID=str(result[0])
    MOVIE=result[1]

    #STREAMING POSTER & LABEL
    stream = Label(frame,text="Streaming Now")
    stream['font']=streamfont
    stream.grid(row=1,column=0,padx=(11),pady=(30,0),sticky=S)

    global streaming
    query2 = "SELECT PLATFORM FROM MOVIE_ID WHERE ID=%s"
    val2 = (ID,)
    mycursor.execute(query2,val2)
    streampic = mycursor.fetchall()
    stream = streampic[0]
    streaming = ImageTk.PhotoImage(Image.open("images/stream/"+streampic[0][0]+".jpeg"))
    streamingLabel = Label(frame,image=streaming)
    streamingLabel.grid(row=2,column=0,sticky=NSEW,padx=(2,0),rowspan=2)

    search = Button(root,text="Search",command=Search)
    search.grid(row=2,column=0,padx=10,sticky=W,pady=(5,10),ipadx=69)

    # API
    api_request = requests.get("https://api.themoviedb.org/3/movie/"+ID+"?api_key=1d1059419394733b62f2b378982c8522&language=en-US")
    api = json.loads(api_request.content)

    ## MOVIE DATA
    mname = Label(frame,text=result[1])
    mname['font']=posterfont
    mname.grid(row=1,column=1,sticky=N,columnspan=2)

    taglength = len(api['tagline'])
    tagline = Label(frame,text="\""+api['tagline']+"\"")
    if taglength>55:
        tagline['font']=taglinefont
    else:
        tagline['font']=myfont
    tagline.grid(row=2,column=1,sticky=N,columnspan=2)
    
    genre = Label(frame,text=" Genre: " +api['genres'][0]['name'],font=("Courier",13))
    genre.grid(row=2,column=1,sticky=SW)
    
    date = api['release_date']
    year=date[0:4]
    month=date[5:7]
    day=date[8:10]
    release_date = " Release Date: "+day+"."+month+"."+year
    dateLabel = Label(frame,text=release_date,font=("Courier",13))
    dateLabel.grid(row=3,column=1,sticky=NW)

    runtime = Label(frame,text=" Runtime: "+str(api['runtime'])+"m",font=("Courier",13))
    runtime.grid(row=3,column=1,sticky=W)

    query3 = "SELECT DIRECTOR FROM MOVIE_ID WHERE ID = %s"
    val3 = (ID,)
    mycursor.execute(query3,val3)
    resultDirector = mycursor.fetchall()
    director = Label(frame,text="Director: "+resultDirector[0][0],font=("Courier",13))
    director.grid(row=2,column=2,sticky=SW)

    IMDb = Label(frame,text="IMDb: "+str(api["vote_average"]),font=("Courier",13))
    IMDb.grid(row=3,column=2,sticky=NW)

    #overview = api['overview']
    if SearchBox.get()=="forrest gump":
        overview="Forrest, a man with low IQ, recounts the early years of\n his life when he found himself in the middle of key historical\n events. All he wants now is to be reunited with his\n childhood sweetheart, Jenny."
        description = Label(frame,text=overview,font=("Courier",13))
        description.grid(row=4,column=1,sticky=S,columnspan=2)
    elif SearchBox.get()=="titanic":
        overview="Seventeen-year-old Rose hails from an aristocratic family\n and is set to be married. When she boards the Titanic, she \nmeets Jack Dawson, an artist, and falls in love with \nhim."
        description = Label(frame,text=overview,font=("Courier",13))
        description.grid(row=4,column=1,sticky=S,columnspan=2)
    else:    
        overview="In the smog-choked dystopian Los Angeles of 2019,blade\n runner Rick Deckard is called out of retirement to terminate\n a quartet of replicants who have escaped to Earth seeking\n their creator for a way to extend their short life spans."
        description = Label(frame,text=overview,font=("Courier",13))
        description.grid(row=4,column=1,sticky=S,columnspan=2)

    review = Label(frame,text="Reviews",font=("Georgia",14,"bold"))
    review.grid(row=5,column=1,sticky=W)
    #review
    if SearchBox.get()=="titanic":
        review1 = "You won’t mind seeing the Titanic sink all over \nagain - in 3D exactly a hundred years from the\n moment it actually happened."
        review1label = Label(frame,text=review1,font=("Courier",13,"italic"))
        review1label.grid(row=6,column=1,columnspan=2,sticky=N)

        reviewBy = Label(frame,text="- The Times",font=("Georgia",10,"bold"))
        reviewBy.grid(row=6,column=2,sticky=SE,padx=(0,10))
    else:
        review1 = "HODOR HODOR HODOR dystopian Los Angeles of 2019,blade\n runner Rick Deckard is called out of retirement to terminate\n a quartet of replicants who have escaped to Earth seeking\n their creator for a way to extend their short life spans."
        review1label = Label(frame,text=review1,font=("Courier",13,"italic"))
        review1label.grid(row=6,column=1,columnspan=2,sticky=N)

        reviewBy = Label(frame,text="- Chetan Sharma",font=("Georgia",10,"bold"))
        reviewBy.grid(row=6,column=2,sticky=SE,padx=(0,10))

    review2 = "GROOT GROOT GROOT dystopian Los Angeles of 2019,blade\n runner Rick Deckard is called out of retirement to terminate\n a quartet of replicants who have escaped to Earth seeking\n their creator for a way to extend their short life spans."
    review2label = Label(frame,text=review2,font=("Courier",13,"italic"))
    review2label.grid(row=7,column=1,columnspan=2,rowspan=3,sticky=N)

    reviewBy2 = Label(frame,text="- Suyash Johri",font=("Georgia",10,"bold"))
    reviewBy2.grid(row=9,column=2,sticky=NE,padx=(0,10))

    #watchlist
    global white
    white = ImageTk.PhotoImage(Image.open("images/watchlist.png"))
    global imagebutton
    imagebutton = Button(frame,image=white,command=saved)
    imagebutton.grid(row=4,column=0,sticky=NW,padx=(16,0),pady=(10,0))

    #like
    global like
    global likebutton
    like = ImageTk.PhotoImage(Image.open("images/white heart2.jpeg"))
    likebutton = Button(frame,image=like,command=voted)
    likebutton.grid(row=4,column=0,sticky=NE,padx=(0,30),pady=(10,0))

    featuring = Label(frame,text="Featuring",font=("Courier",15,"bold"))
    featuring.grid(row=4,column=0,sticky=SW,padx=(15,0))

    #cast
    global cast1
    if SearchBox.get()=="forrest gump":
        cast1 = ImageTk.PhotoImage(Image.open("images/actors/tomhanks.jpg"))
        cast1label = Label(frame,image=cast1)
        cast1label.grid(row=5,column=0,sticky=N,rowspan=4)

        cast1name = Label(frame,text="Tom Hanks",font=("Courier",13))
        cast1name.grid(row=9,column=0,sticky=S)
    elif SearchBox.get() == "titanic":
        cast1 = ImageTk.PhotoImage(Image.open("images/actors/leonardo.jpg"))
        cast1label = Label(frame,image=cast1)
        cast1label.grid(row=5,column=0,sticky=N,rowspan=4)

        cast1name = Label(frame,text="Leo DiCaprio",font=("Courier",13))
        cast1name.grid(row=9,column=0,sticky=S)
        
    else:
        cast1 = ImageTk.PhotoImage(Image.open("images/actors/ryan gosling.jpg"))
        cast1label = Label(frame,image=cast1)
        cast1label.grid(row=5,column=0,sticky=N,rowspan=4)

        cast1name = Label(frame,text="Ryan Gosling",font=("Courier",13))
        cast1name.grid(row=9,column=0,sticky=S)
    
    SearchBox.delete(0,END)

def vote():
    global like
    global likebutton
    like = ImageTk.PhotoImage(Image.open("images/white heart2.jpeg"))
    likebutton = Button(frame,image=like,command=voted)
    likebutton.grid(row=4,column=0,sticky=NE,padx=(0,30),pady=(10,0))

    mycursor = mydb.cursor()
    query="DELETE FROM LIKELIST WHERE LID = %s"
    val=(int(ID),)
    mycursor.execute(query,val)
    mydb.commit()
    
def voted():
    global liked
    global likedbutton
    liked = ImageTk.PhotoImage(Image.open("images/red heart2.jpeg"))
    likedbutton = Button(frame,image=liked,command=vote)
    likedbutton.grid(row=4,column=0,sticky=NE,padx=(0,30),pady=(10,0))

    mycursor = mydb.cursor()
    query="INSERT INTO LIKELIST (LID,LNAME) VALUES (%s,%s)"
    val=(int(ID),MOVIE)
    mycursor.execute(query,val)
    mydb.commit()

def watchlist():
    global white
    global imagebutton
    white = ImageTk.PhotoImage(Image.open("images/watchlist.png"))
    imagebutton = Button(frame,image=white,command=saved)
    imagebutton.grid(row=4,column=0,sticky=NW,padx=(16,0),pady=(10,0))

    mycursor = mydb.cursor()
    query="DELETE FROM WATCHLIST WHERE WID = %s"
    val=(int(ID),)
    mycursor.execute(query,val)
    mydb.commit()
    
def saved():
    global black
    global savedbutton
    black = ImageTk.PhotoImage(Image.open("images/watchlist2.png"))
    savedbutton = Button(frame,image=black,command=watchlist)
    savedbutton.grid(row=4,column=0,sticky=NW,padx=(16,0),pady=(10,0))

    mycursor = mydb.cursor()
    query="INSERT INTO watchlist (WID,WNAME) VALUES (%s,%s)"
    val=(int(ID),MOVIE)
    mycursor.execute(query,val)
    mydb.commit()

def ratings():
    frame.destroy()
    global frame2
    frame2=LabelFrame(root,width=1145,height=710)
    frame2.grid(row=1,column=1,rowspan=50,pady=(40,0),columnspan=20)
    frame2.grid_propagate(0)

    ranklist=["rank1","rank2","rank3","rank4","rank5","rank6","rank7","rank8"]
    global imagelist
    imagelist=["rank1image","rank2image","rank3image","rank4image","rank5image","rank6image","rank7image","rank8image"]
    genrelist=["152min | Action,Adventure","151min | Drama,Thriller","178min | Crime,Comedy","120min | Action,Sci-fi","142min | Drama","142min | Drama,Crime","150min | Action,Sci-Fi","210min | Romance"]

    mycursor=mydb.cursor()
    query="SELECT VOTES FROM MOVIE_ID WHERE NAME = %s"
    query1="SELECT NAME,VOTES FROM MOVIE_ID ORDER BY VOTES DESC LIMIT 8"
    mycursor.execute(query1)
    result=mycursor.fetchall()
    namelist=[]
    for i in result:
        namelist.append(i)

    for i in range(8):
        ranklist[i] = LabelFrame(frame2,width=565,height=145)
        ranklist[i].grid(row=i%4,column=i//4,padx=(5,0),pady=(5,0))
        ranklist[i].grid_propagate(0)
        imagelist[i] = ImageTk.PhotoImage(Image.open("images/posters/ranking/"+namelist[i][0]+".jpg"))
        rank1imagelb = Label(ranklist[i],image=imagelist[i])
        rank1imagelb.grid(row=0,column=0,rowspan=4)

        nameText = Label(ranklist[i],text=str(i+1)+". "+namelist[i][0],font=("Georgia",16,"bold"))
        nameText.grid(row=0,column=1,padx=10,sticky=W)
        genreText = Label(ranklist[i],text=genrelist[i])
        genreText['font']=myfont
        genreText.grid(row=1,column=1,padx=10,sticky=W)
        votesText = Label(ranklist[i],text="Votes: "+ str(namelist[i][1]))
        votesText['font']=myfont
        votesText.grid(row=2,column=1,padx=10,sticky=W)
     
def trending():
    frame.destroy()
    global frame2
    frame2=LabelFrame(root,width=1145,height=710)
    frame2.grid(row=1,column=1,rowspan=50,pady=(40,0),columnspan=20)
    frame2.grid_propagate(0)

    api_request = requests.get("https://api.themoviedb.org/3/trending/movie/week?api_key=1d1059419394733b62f2b378982c8522")
    api = json.loads(api_request.content)


    tlist=["trend1","trend2","trend3","trend4"]
    global timage
    timage=["timage1","timage2","timage3","timage4"]
    ab=" "


    for i in range(4):
        tmovie_name = api['results'][i]['title']
        TID = api['results'][i]['id']
        api_request2 = requests.get("https://api.themoviedb.org/3/movie/"+str(TID)+"?api_key=1d1059419394733b62f2b378982c8522&language=en-US")
        api2 = json.loads(api_request2.content)
        line2 = str(api2['runtime']) + "min | " + api2['genres'][0]['name'] + "," + api2['genres'][1]['name']

        tlist[i] = LabelFrame(frame2,width=1130,height=145)
        tlist[i]['font']=myfont
        tlist[i].grid(row=i,column=0,padx=5,pady=(5,0))
        tlist[i].grid_propagate(0)


        
        timage[i] = ImageTk.PhotoImage(Image.open("images/posters/trending/"+tmovie_name+".jpg"))
        timageLabel = Label(tlist[i],image=timage[i])
        timageLabel.grid(row=0,column=0,rowspan=4)

        tmovie_details = Label(tlist[i],text=line2)
        tmovie_details['font']=myfont
        tmovie_details.grid(row=1,column=1,sticky=SW,padx=10,pady=(10,0))

        t_imdb = Label(tlist[i],text="IMDb: " + str(api2['vote_average']))
        t_imdb['font']=myfont
        t_imdb.grid(row=2,column=1,padx=10,sticky=SW)

        date = api2['release_date']
        year=date[0:4]
        month=date[5:7]
        day=date[8:10]
        release_date = "Releasing on: "+day+"."+month+"."+year
        
        t_release = Label(tlist[i],text=release_date)
        t_release['font']=myfont
        t_release.grid(row=3,column=1,padx=10,sticky=NW,pady=(0,10))

        tname = Label(tlist[i],text=tmovie_name,font=("Georgia",16,"bold"))
        tname.grid(row=0,column=1,padx=10,sticky=W)

        #empty2 = Label(tlist[i],text=ab*190,bg="red")
        #empty2.grid(row=0,column=2,sticky=E)


    trending_no1 = Label(frame2,text="#1 ON TRENDING",font=("Georgia",10,"bold"),fg="#167ac6")
    trending_no1.grid(row=0,column=0,sticky=NE,padx=(0,13),pady=(13,0))

    trending_no2 = Label(frame2,text="#2 ON TRENDING",font=("Georgia",10,"bold"),fg="#167ac6")
    trending_no2.grid(row=1,column=0,sticky=NE,padx=(0,13),pady=(13,0))

    trending_no3 = Label(frame2,text="#3 ON TRENDING",font=("Georgia",10,"bold"),fg="#167ac6")
    trending_no3.grid(row=2,column=0,sticky=NE,padx=(0,13),pady=(13,0))

    trending_no4 = Label(frame2,text="#4 ON TRENDING",font=("Georgia",10,"bold"),fg="#167ac6")
    trending_no4.grid(row=3,column=0,sticky=NE,padx=(0,13),pady=(13,0))
    
def likeitoff():
    frame.destroy()
    global frame2
    frame2=LabelFrame(root,width=1145,height=710)
    frame2.grid(row=1,column=1,rowspan=50,pady=(40,0),columnspan=20)
    frame2.grid_propagate(0)

    mycursor = mydb.cursor()
    query="SELECT COUNT(LID) FROM LIKELIST"
    mycursor.execute(query)
    result=mycursor.fetchone()

    query2="SELECT LNAME FROM LIKELIST"
    mycursor.execute(query2)
    result2=mycursor.fetchall()
    movie=[]
    for i in range(len(result2)):
        movie.append(result2[i][0])

    count=result[0]
    list=["watchframe","watchframe2","watchframe3","watchframe4","watchframe5","watchframe6","watchframe7","watchframe8","watchframe9","watchframe10"]
    global imglist
    imglist=["image1","image2","image3","image4","image5","image6","image7","image8","image9","image10","image11"]
    for i in range(count):
        list[i]=LabelFrame(frame2,width=1000,height=100)
        list[i].grid(row=0,column=i,pady=(15,0),padx=(10,0))
        list[i].grid_propagate(0)

        imglist[i]=ImageTk.PhotoImage(Image.open("images/posters/watchlist/"+movie[i]+".jpg"))
        image = Label(list[i],image=imglist[i])
        image.pack()
    
def watchitoff():
    frame.destroy()
    global frame2
    frame2=LabelFrame(root,width=1145,height=710)
    frame2.grid(row=1,column=1,rowspan=50,pady=(40,0),columnspan=20)
    frame2.grid_propagate(0)

    mycursor = mydb.cursor()
    query="SELECT COUNT(WID) FROM WATCHLIST"
    mycursor.execute(query)
    result=mycursor.fetchone()

    query2="SELECT WNAME FROM WATCHLIST"
    mycursor.execute(query2)
    result2=mycursor.fetchall()
    movie=[]
    for i in range(len(result2)):
        movie.append(result2[i][0])

    count=result[0]
    list=["watchframe","watchframe2","watchframe3","watchframe4","watchframe5","watchframe6","watchframe7","watchframe8","watchframe9","watchframe10"]
    global imglist
    imglist=["image1","image2","image3","image4","image5","image6","image7","image8","image9","image10","image11"]
    for i in range(count):
        list[i]=LabelFrame(frame2,width=1000,height=100)
        list[i].grid(row=0,column=i,pady=(15,0),padx=(10,0))
        list[i].grid_propagate(0)

        imglist[i]=ImageTk.PhotoImage(Image.open("images/posters/watchlist/"+movie[i]+".jpg"))
        image = Label(list[i],image=imglist[i])
        image.pack()

def motm():
    frame.destroy()
    global frame2
    frame2 = LabelFrame(root,width=1145,height=710)
    frame2.grid(row=1,column=1,rowspan=50,pady=(40,0),columnspan=20)
    frame2.grid_propagate(0)

    error = Label(frame2,text="Sorry!!!!",font=("Franklin Gothic Book",16,"bold"),fg="silver")
    error.grid(row=0,column=0,padx=500,pady=(250,0))

    error2 = Label(frame2,text="The feature is currently unavailable",font=("Franklin Gothic Book",15,"bold"),fg="silver")
    error2.grid(row=1,column=0)

def latest():
    frame.destroy()
    global frame2
    frame2 = LabelFrame(root,width=1145,height=710)
    frame2.grid(row=1,column=1,rowspan=50,pady=(40,0),columnspan=20)
    frame2.grid_propagate(0)

    error = Label(frame2,text="Sorry!!!!",font=("Franklin Gothic Book",16,"bold"),fg="silver")
    error.grid(row=0,column=0,padx=500,pady=(250,0))

    error2 = Label(frame2,text="The feature is currently unavailable",font=("Franklin Gothic Book",15,"bold"),fg="silver")
    error2.grid(row=1,column=0)
    
       
### FONT
logo = ImageTk.PhotoImage(Image.open("garlic.ico"))
headFont = font.Font(family='Georgia',size=20, weight='bold')
headFont2= font.Font(family='Georgia',size=27, weight='bold')
myfont = font.Font(family='Courier', size=12)
normal = font.Font(family='Courier')
streamfont = font.Font(family='Courier', size=17)
posterfont = font.Font(family='Georgia',size=20,weight='bold')
taglinefont = font.Font(family='Courier',size=10)

btnFont = font.Font(family='Calibri',size=10)

headlabel = Label(root,text="The House of Cinema",bg="#fafafa")
headlabel['font']=headFont
headlabel.grid(row=0,column=0,columnspan=2) #end
nameLabel = Label(root,text="Username",bg="#fafafa")
nameLabel['font']=myfont
nameLabel.grid(row=1,column=0,pady=(60,0),sticky=W) #end
passwordLabel = Label(root,text="Password",bg="#fafafa")
passwordLabel['font']=myfont
passwordLabel.grid(row=2,column=0,sticky=W) #end
imageLabel = Label(root,image=logo)
imageLabel.grid(row=0,column=2,rowspan=100,padx=(10,0))

nameEntry = Entry(root,width=30)
nameEntry.grid(row=1,column=1,pady=(60,0),sticky=W) #end
passwordEntry = Entry(root,show='*',width=30)
passwordEntry.grid(row=2,column=1,sticky=W)

page1btn = Button(root,text="Submit",command=submit)
page1btn['font']=btnFont
page1btn.grid(row=3,column=0,padx=4,pady=5,ipadx=40,sticky=W)

root.mainloop()
