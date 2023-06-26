import pandas as pd
import networkx as nx
from sklearn.neighbors import kneighbors_graph

 
# read in excel file and specified sheet
dataframe1 = pd.read_excel("PutFilePathToExcelHere", "PutSheetToOpenHere")
df1 = dataframe1.values
knGraph1 = kneighbors_graph(df1, 4) #Create KNN graph (produced in CSR format)
g1 = nx.Graph(knGraph1) #Use NetworkX to create the graphical representation so that it can be exported in a format Gephi can use
nx.write_gexf(g1, "knGraphFin30GEXF.gexf") #Export final graph in a format gephi can use (In this case GEXF)
