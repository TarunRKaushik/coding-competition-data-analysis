%matlplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as st

from pandas.tools.plotting import scatter_matrix

df = pd.read_csv('/home/sush/Desktop/Datathon1.csv')#This path needs to be chamged if you want to test this code.

print(df.describe())



print(df.info())

df = df.dropna()
print(df.isnull().any())
df.to_csv('Cleaned1.csv')
#removing null values 



df['graduationyear'].hist()
plt.xlabel('year of graduation')
plt.ylabel('ferequency')
plt.show()

df[df.graduationyear<2012]['graduationyear'].hist()
plt.xlabel('year of graduation')
plt.ylabel('ferequency')
plt.show()

df[df.graduationyear>2012]['graduationyear'].hist()
plt.xlabel('year of graduation')
plt.ylabel('frequency')
plt.show()

#CONCLUSION:Most of the people who took the test are young people
#Among the young people, students were the greatest participators in this exam
#However, there were some veterans indicated by the histogram(plotted between years 1950 and 2010)

#The graph is left-skewed because there are people who arent student who took the test



grid = sns.FacetGrid(df[df.profession != 'student'],col='profession')
grid.map(plt.hist, 'q1')
plt.show()
grid = sns.FacetGrid(df[df.profession != 'student'],col='profession')
grid.map(plt.hist, 'q2')
plt.show()
grid = sns.FacetGrid(df[df.profession != 'student'],col='profession')
grid.map(plt.hist, 'q3')
plt.show()
grid = sns.FacetGrid(df[df.profession != 'student'],col='profession')
grid.map(plt.hist, 'q4')
plt.show()
grid = sns.FacetGrid(df[df.profession != 'student'],col='profession')
grid.map(plt.hist, 'q5')
plt.show()
grid = sns.FacetGrid(df[df.profession != 'student'],col='profession')
grid.map(plt.hist, 'q6')
plt.show()
grid = sns.FacetGrid(df[df.profession != 'student'],col='profession')
grid.map(plt.hist, 'q7')
plt.show()
grid = sns.FacetGrid(df[df.profession != 'student'],col='profession')
grid.map(plt.hist, 'q8')
plt.show()




Total = df.q1 + df.q2 + df.q3 + df.q4 + df.q5 + df.q6 + df.q7 +df.q8 
df = df.assign(Questions = Total)

grid = sns.FacetGrid(df[df.profession != 'student'],col='profession')
grid.map(plt.hist, 'Questions')
plt.show()

df[df.profession == 'student'].Questions.hist()
plt.xlabel('Marks')
plt.ylabel('frequency')
plt.show()

#CONCLUSION:
#The Faculty members were those that performed relatively better compared to 'other' and 'employed' people, but performed  
#worse than students



print(df[df.Questions == 800])

x = df.profession.value_counts()
plt.pie(x.get_values(), labels = x.index, autopct='%1.1f%%')
plt.axis("equal")
plt.show()



df['state_of_residence'].value_counts().plot(kind='bar')
plt.title('Particpants from each State')
plt.show()

df[df.Questions==800]['state_of_residence'].value_counts().plot(kind='bar')
plt.title('Toppers')
plt.show()
#CONCLUSION:The toppers are mostly from Tamil Nadu(Tamil Nadu also has the most number of particpants) as shown by the 
##barplots



#df[df.profession == 800]['state_of_residence'].value_counts().plot(kind='bar')
#plt.show()
means = []
x=np.mean(df[df.profession == 'student'].Questions)
means.append(x)

y=np.mean(df[df.profession == 'other'].Questions)
means.append(y)

w=np.mean(df[df.profession == 'faculty'].Questions)
means.append(w)

z=np.mean(df[df.profession == 'employed'].Questions)
means.append(z)



new_df = pd.DataFrame()
pro=['student','other','faculty','employed']
new_df = new_df.assign(Pro = pro)
new_df = new_df.assign(Means=means)
sns.barplot(data=new_df,x='Pro',y='Means')
plt.show()

#CONCLUSION: Students perform better than faculty,who perform better than the remaining two professions as shown by the 
##bar plot between profession and mean scores obtained by them





df[df.Questions == 800].graduationyear.hist()
plt.title('Toppers')
plt.xlabel('year of graduation')
plt.ylabel('ferequency')
plt.show()

x = df.profession.value_counts()

plt.pie(x.get_values(), labels = x.index, autopct='%1.1f%%')
plt.axis("equal")
plt.show()

#CONCLUSION:Most of the toppers were students as indicated by the pie chart and the histogram(year of graduation~2020)



diff=pd.DataFrame()
m1=np.mean(df.q1)
m2=np.mean(df.q2)
m3=np.mean(df.q3)
m4=np.mean(df.q4)
m5=np.mean(df.q5)
m6=np.mean(df.q6)
m7=np.mean(df.q7)
m8=np.mean(df.q8)
m=[]
m.append(m1)
m.append(m2)
m.append(m3)
m.append(m4)
m.append(m5)
m.append(m6)
m.append(m7)
m.append(m8)
diff=diff.assign(Mean=m)

q=['q1','q2','q3','q4','q5','q6','q7','q8']
diff=diff.assign(Question=q)
sns.barplot(x='Question', y='Mean',data=diff)
plt.show()

#CONCLUSION:Questions 4 and 1 were the easiest, while questions 7 and 8 were the hardest as shown by the barplot between
##questions and the mean marks for that question



interested = []
for index,row in df.Questions.iteritems():
    if(row == -8):
        interested.append('no')
    else:
        interested.append('yes')
df = df.assign(Interested=interested)


df[df.Interested=='no']['state_of_residence'].value_counts().plot(kind='bar')
plt.title('Not-Interested people')
plt.show()



sns.FacetGrid(df, hue="profession", size=6) \
 .map(sns.kdeplot, "graduationyear") \
 .add_legend()
plt.show()

#CONCLUSION : The following distribution shows that the 'other' people weren't very old, they were almost of the same age 
#as the employed people
#The faculty were the oldest of the people who took the test.
