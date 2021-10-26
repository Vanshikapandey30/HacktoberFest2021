import pandas as pd


myfile = pd.read_excel('C://Users//Wolverine//Desktop//book1.xlsx',index_col=0)

myfile.to_csv('yo it worked')
