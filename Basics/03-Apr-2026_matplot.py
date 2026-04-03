# matplotlib --> graphs, charts
# matplotlib --> numpy & pandas

# Line Plot
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("Book1.csv")
x = df["Age"]
y = df["Salary"]
# x = [1,2,3,4,5]
# y = [10,20,30,40,50]
# plt.plot(x,y) 
# plt.plot(x, y, color='red')
# plt.plot(x,y,color='green',linestyle='--')
# plt.plot(x,y,color="blue",linestyle='--', marker='o')
plt.plot(x,y,color="blue",linestyle='--', marker='X')
plt.title("Line Plot")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()

