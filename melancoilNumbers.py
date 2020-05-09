#Going to take the base of happy numbers
#we are going to have a group for known happy numbers
#we are also going to have a group for known melancoil numbers
#if the number we are testing is in the group we are going to continue to the next number
#WE are going to graph the numbers using nodes (hopefully)

import networkx as nx
from matplotlib import pyplot as plt

def getNextHappyNumber(y):
    y = str(y)
    total = 0
    for i in range(len(y)):
        total += int(y[i])**2 
    return total

print(getNextHappyNumber(7))

G = nx.Graph()

for x in range(1,200): #we are only doing positive integers over 0 
    G.add_edge(x,getNextHappyNumber(x)) #it would be cool if there where arrows

nx.draw(G, node_color='red', with_labels=True)
plt.show()
