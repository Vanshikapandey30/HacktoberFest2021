import pandas as pd

myfile = pd.read_csv("C:\\Users\\Wolverine\\Desktop\\Data(csv).csv", index_col=0)

myfile.to_html('big data.html')
