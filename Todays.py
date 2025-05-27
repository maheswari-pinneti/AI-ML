import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#create an array
arr=np.array([1,2,3,5,6,7,9])

#Basic Operations
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Squaredd:", arr ** 2)

#create a DataFrame
data={'Name': ['Harshith', 'Bhavya', 'Sinchu'],
      'Age': [25, 20, 23],
      'City': ['New York', 'Atlanta', 'Chicago']
      }
df=pd.DataFrame(data)

#Basic Operations
print("DataFrame:\n", df)
print("Average Age:", df['Age'].mean())
print("People in New York:\n", df[df['City']=='New York'])

#sample data
X=[1,2,3,4,5,6]
Y=[10,12,17,19,9,7]

#plot
plt.plot(X,Y, marker='o', color='blue', linestyle='--')
plt.title('Sample Line Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.show()

