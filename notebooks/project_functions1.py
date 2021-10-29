import pandas as pd
import seaborn as sns
import numpy as np

def load_and_process(path_to_csv_file):
    data = (pd.read_csv(path_to_csv_file)
    .drop(columns =['CF','CA','SCF','SCA','TOI', 'Unnamed: 2'])
    )
    return data

df = load_and_process("../data/raw/Games - Natural Stat TrickTeam Season Totals - Natural Stat Trick.csv")
df

def Canucks_Before_Data(data):
    data1= (data.drop(data[data.Team.isin(["Arizona Coyotes", "Buffalo Sabres", "Boston Bruins", "Carolina Hurricanes", "Columbus Blue Jackets", "Calgary Flames", "Chicago Blackhawks", "Colorado Avalanche", "Dallas Stars", "Detroit Red Wings", "Florida Panthers", "Los Angeles Kings", "Minnesota Wild", "Nashville Predators", "Pittsburgh Penguins", "San Jose Sharks", "Tampa Bay Lightning", "St Louis Blues", "Vegas Golden Knights", "Edmonton Oilers", "Montreal Canadiens", "New Jersey Devils", "New York Islanders", "New York Rangers", "Ottawa Senators", "Philadelphia Flyers", "Toronto Maple Leafs", "Winnipeg Jets", "Washington Capitals", "Anaheim Ducks"])].index)
    .reset_index()
    .drop(data.index[0:27]).drop(data.index[47:56])
    .reset_index().drop(columns = "index")
    .drop(columns =['level_0'])
    .drop(data.index[10:20])
           )
    return data1

Canucks_Before = Canucks_Before_Data(df)

def Canucks_After_Data(data):
    data2= (data.drop(data[data.Team.isin(["Arizona Coyotes", "Buffalo Sabres", "Boston Bruins", "Carolina Hurricanes", "Columbus Blue Jackets", "Calgary Flames", "Chicago Blackhawks", "Colorado Avalanche", "Dallas Stars", "Detroit Red Wings", "Florida Panthers", "Los Angeles Kings", "Minnesota Wild", "Nashville Predators", "Pittsburgh Penguins", "San Jose Sharks", "Tampa Bay Lightning", "St Louis Blues", "Vegas Golden Knights", "Edmonton Oilers", "Montreal Canadiens", "New Jersey Devils", "New York Islanders", "New York Rangers", "Ottawa Senators", "Philadelphia Flyers", "Toronto Maple Leafs", "Winnipeg Jets", "Washington Capitals", "Anaheim Ducks"])].index)
    .reset_index()
    .drop(data.index[0:27]).drop(data.index[47:56])
    .reset_index().drop(columns = "index")
    .drop(columns =['level_0'])
    .drop(data.index[0:10]).drop(data.index[20:20])
           )
    return data2

Canucks_After = Canucks_After_Data(df)

def Sabres_Before_Data(data):
    data3 = (data.drop(data[data.Team.isin(["Arizona Coyotes", "Vancouver Canucks", "Boston Bruins", "Carolina Hurricanes", "Columbus Blue Jackets", "Calgary Flames", "Chicago Blackhawks", "Colorado Avalanche", "Dallas Stars", "Detroit Red Wings", "Florida Panthers", "Los Angeles Kings", "Minnesota Wild", "Nashville Predators", "Pittsburgh Penguins", "San Jose Sharks", "Tampa Bay Lightning", "St Louis Blues", "Vegas Golden Knights", "Edmonton Oilers", "Montreal Canadiens", "New Jersey Devils", "New York Islanders", "New York Rangers", "Ottawa Senators", "Philadelphia Flyers", "Toronto Maple Leafs", "Winnipeg Jets", "Washington Capitals", "Anaheim Ducks"])].index)
    .reset_index()
    .drop(data.index[20:56])
    .drop(data.index[10:20])
    .drop(columns = "index")
    )
    
    return data3

Sabres_Before = Sabres_Before_Data(df)

def Sabres_After_Data(data):
    data4 = (data.drop(data[data.Team.isin(["Arizona Coyotes", "Vancouver Canucks", "Boston Bruins", "Carolina Hurricanes", "Columbus Blue Jackets", "Calgary Flames", "Chicago Blackhawks", "Colorado Avalanche", "Dallas Stars", "Detroit Red Wings", "Florida Panthers", "Los Angeles Kings", "Minnesota Wild", "Nashville Predators", "Pittsburgh Penguins", "San Jose Sharks", "Tampa Bay Lightning", "St Louis Blues", "Vegas Golden Knights", "Edmonton Oilers", "Montreal Canadiens", "New Jersey Devils", "New York Islanders", "New York Rangers", "Ottawa Senators", "Philadelphia Flyers", "Toronto Maple Leafs", "Winnipeg Jets", "Washington Capitals", "Anaheim Ducks"])].index)
.reset_index()
.drop(data.index[0:10])
.drop(data.index[20:56])
.drop(columns = "index")
            )
    return data4

Sabres_After = Sabres_After_Data(df)

def Describe(data):
    return data.describe().T