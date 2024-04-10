import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ucitavanje ociscenih podataka
df = pd.read_csv('cars_processed.csv')
print(df.info())

# razliciti prikazi
sns.pairplot(df, hue='fuel')

sns.relplot(data=df, x='km_driven', y='selling_price', hue='fuel')
df = df.drop(['name','mileage'], axis=1)

obj_cols = df.select_dtypes(object).columns.values.tolist()
num_cols = df.select_dtypes(np.number).columns.values.tolist()

fig = plt.figure(figsize=[15,8])
for col in range(len(obj_cols)):
    plt.subplot(2,2,col+1)
    sns.countplot(x=obj_cols[col], data=df)

df.boxplot(by ='fuel', column =['selling_price'], grid = False)

df.hist(['selling_price'], grid = False)

tabcorr = df.corr()
sns.heatmap(df.corr(), annot=True, linewidths=2, cmap= 'coolwarm') 

plt.show()

#1. Koliko mjerenja (automobila) je dostupno u datasetu? - oko 6800
#2. Kakav je tip pojedinog stupca u dataframeu? - 
#3. Koji automobil ima najveću cijenu, a koji najmanju? - dizel najveću, petrol najmanju
#4. Koliko automobila je proizvedeno 2012. godine? - 
#5. Koji automobil je prešao najviše kilometara, a koji najmanje? - petrol ima najviše, a cng najmanje
#6. Koliko najčešće automobili imaju sjedala? - 5
#7. Kolika je prosječna prijeđena kilometraža za automobile s dizel motorom, a koliko za automobile s benzinskim motorom?