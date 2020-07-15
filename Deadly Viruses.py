#Comparison between deadly viruses
#Author Nishant Kaushik
#Date: 2020-07-15

#comparison between Covid-19 & the Bubonic plague that killed nearly half of europe in the 14th Century
import numpy as np
from covid import Covid
from matplotlib import pyplot as plt 

covid = Covid()

total_deaths = [covid.get_total_deaths(), 4000000] #Total Deaths are 40% of the Total people infected
total_confirmed_cases = [covid.get_total_confirmed_cases(),10000000] #Total Confirmed case reduced by a factor of 10 to accomodate the graph
diseases = ['Covid19',' Bubonic Plague - 14th Century']
pos = np.arange(len(diseases))

bar_width = 0.35

print(total_deaths)
print(total_confirmed_cases)

plt.bar(pos,total_deaths,color='red',edgecolor='black')
plt.bar(pos,total_confirmed_cases,color='blue',edgecolor='black',bottom=total_deaths)
plt.xticks(pos, diseases)
plt.xlabel('diseases', fontsize=16)
plt.ylabel('in Millions', fontsize=16)
plt.title('Stacked Barchart - Comparing deadly Viruses',fontsize=18)
#plt.legend(total_deaths,total_confirmed_cases,loc=2)
plt.show()
