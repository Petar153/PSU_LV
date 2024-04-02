import pandas as pd
import numpy as np

mtcars = pd.read_csv('mtcars.csv')

#1
print(mtcars.sort_values(by=['mpg']).head(5))
#2

print(mtcars[mtcars.cyl == 8].sort_values(by=['mpg'], ascending=False).head(3))

#3
print(mtcars[mtcars.cyl == 6].mpg.mean())

#4
print(mtcars[(mtcars.cyl==4) & (mtcars.wt>2) & (mtcars.wt<2.2)].mpg.mean())

#5
print(mtcars.am.value_counts())

#6
print(len(mtcars[(mtcars.am==0) & (mtcars.hp>100)]))

#7
mtcars['kg'] = mtcars.wt*1000*0.453
print(mtcars[['car','kg']])