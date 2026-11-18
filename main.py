from pathlib import Path

import osmnx as ox
from mesa import Model

Lviv_Coord = (49.8418, 24.0321) 
Range = 1000 #м
Output = Path(__file__).resolve().parent/"output"

class Model(Model):
    def __init__(self, network):
        super().__init__()
        self.network = network
        
def main():
    Output.mkdir(exist_ok=True)
    ox.settings.cashe_folder = Output / "caсhe"
    
    network = ox.graph_from_point(
        Lviv_Coord,
        dist = Range,
        network_type = "walk",
    )
    model = Model(network)
    
    ox.save_graphml(model.network, filepath=Output/"network.graphml")
    ox.save_graph_geopackage(model.network, filepath=Output/"network.gpkg", directed=True)        

if __name__ == "__main__":                    
    main()