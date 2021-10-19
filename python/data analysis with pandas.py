import pandas as pd

web_data = {"Day":[1,2,3,4,5,6],"visitors": [2000,400,4000,7000,5000,4444],"Bounce_rate":[20,20,23,15,10,34]}
Df = pd.DataFrame(web_data) #Framing data into tablular format
print(Df)


#Slicing
print(Df.head(2)) #Getting first 2 rows only
print(Df.tail(2)) #Getting last 2 rows only

#Merging two data frames
df1 = pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},
                   index = [2001,2002,2003,2004])


df2 = pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},
                   index = [2005,2006,2007,2008])
merge = pd.merge(df1,df2, on="HPI") #on means keeping only HPI common
print(merge)


#Joining of two data frames
df3 = pd.DataFrame({"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},
                   index = [2001,2002,2003,2004])


df4 = pd.DataFrame({"Low_Tier_HPI":[50,45,67,34],"Unemployment":[1,3,5,6]},
                   index = [2001,2003,2004,2004])

join = df3.join(df4)
print(join)
