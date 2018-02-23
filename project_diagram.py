import json
from logger import Logger
import networkx as nx
LOG = Logger()

def diagram(payload):
    data = payload['payload']
    #LOG.console(data)
    
    G = nx.DiGraph()
    for transaction in data['transactions']:
        connection = (transaction['country_from'],transaction['country_to'])
        G.add_edges_from([connection])
    data = convert2cytoscapeJSON(G)
    return data
      

# this function is used to convert networkx to Cytoscape.js JSON format
# returns string of JSON
def convert2cytoscapeJSON(G):
    # load all nodes into nodes array
    final = {}
    final["nodes"] = []
    final["edges"] = [] 
    for node in G.nodes():
        nx = {}
        nx["data"] = {}
        nx["data"]["id"] = node
        nx["data"]["name"] = node
        final["nodes"].append(nx.copy())
    #load all edges to edges array
    for edge in G.edges():
        nx = {}
        nx["data"]={}
        nx["data"]["id"]=edge[0]+edge[1]
        nx["data"]["source"]=edge[0]
        nx["data"]["target"]=edge[1]
        final["edges"].append(nx)

    return json.dumps(final)
       

