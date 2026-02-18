import json
import networkx as nx
from pyvis.network import Network


input_path = "data/processed/concepts.json"
output_path = "graph_embed.html"

with open(input_path, 'r') as f:
    course_data = json.load(f)

G = nx.Graph()

for course_id in course_data.keys():
    G.add_node(course_id,
               label=course_id,
               color="#5ca4a9",
               size=25,
               font={'color': 'white'})

course_ids = list(course_data.keys())
for i in range(len(course_ids)):
    for j in range(i + 1, len(course_ids)):
        c1, c2 = course_ids[i], course_ids[j]
        shared = set(course_data[c1]).intersection(set(course_data[c2]))
        
        if len(shared) >= 1:
            G.add_edge(c1, c2, 
                       value=len(shared), 
                       title=f"Shared: {', '.join(shared)}",
                       color="#666666")

net = Network(height="100vh", width="100%", bgcolor="#222222", font_color="white")


net.from_nx(G)

net.toggle_physics(True)

net.show(output_path, notebook=False)
print("Graph created successfully :)")