#https://www.youtube.com/watch?v=_DpzAvb3Vk4 #Numberphile Video
#https://networkx.github.io/documentation/stable/tutorial.html
#https://stackoverflow.com/questions/27030473/how-to-set-colors-for-nodes-in-networkx

import networkx as nx
from matplotlib import pyplot as plt

def getNextHappyNumber(y):
    y = str(y)
    total = 0
    for i in range(len(y)):
        total += int(y[i])**2 
    return total

G = nx.Graph()

for x in range(1,200): #we are only doing positive integers over 0 
    G.add_edge(x,getNextHappyNumber(x)) #it would be cool if there where arrows

nx.draw(G, node_color='red', with_labels=True)
plt.show()
