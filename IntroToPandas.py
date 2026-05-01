import pandas as pd
import numpy as np

exam_data = {'name':['anastasia','dima','katherone','james','emily',
'michael','laura','kevin','jonas','mathew'],
            'score':[12.5,9,9,16.5,np.nan,9,20,14.5,np.nan,8],
            'attempts':[1,3,2,3,2,3,1,1,2,1],
            'qualify':['yes','no','yes','no','yes','yes','no','no','yes','no']}

lable = ['a','b','c','d','e','f','g','h','i','j']

df = pd.DataFrame(exam_data , index=lable)
print('summary of the basics')
print(df.info())
