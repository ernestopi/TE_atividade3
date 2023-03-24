import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt


titanic = pd.read_csv('train.csv',index_col=0, parse_dates=True)
titanic.head()
titanic.plot()
#plt.show()


#saber a idade passeiros
ages = titanic["Age"]
#ages()

#Estou interessado na idade e sexo dos passageiros do Titanic.
age_sex = titanic[["Age", "Sex"]]
age_sex.head()
#Estou interessado nos passageiros com mais de 35 anos.
above_35 = titanic[titanic["Age"] > 35]
above_35.head()

#nome dos passageiros com mais de 35 anos
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
adult_names.head()
plt.show()

#print(titanic)
#print(ages)
#print(age_sex)
#print(above_35)
print(adult_names)


