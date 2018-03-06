import json
from logger import Logger
import networkx as nx
LOG = Logger()

def diagram(payload):
    project_data = payload['payload']
    #LOG.console(project_data)
    
    G = nx.DiGraph()
    for transaction in project_data['transactions']:
        connection = (transaction['country_from'],transaction['country_to'])
        G.add_edges_from([connection])
    data = convert2cytoscapeJSON(G)

    #Adding what type of transaction it is.'
    for i,d in enumerate(data["edges"]):
        d['data']['type'] = project_data['transactions'][i]["type"]
        d['data']['pair'] = project_data['transactions'][i]["currency_from"]+project_data['transactions'][i]["currency_to"]
    
    
    return json.dumps(data)
      

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

    return final
       

