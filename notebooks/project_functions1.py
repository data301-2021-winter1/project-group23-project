import pandas as pd
import seaborn as sns
import numpy as np

# Loading the csv file and dropiing the unwanted columns.

def load_and_process(path_to_csv_file):
    data = (pd.read_csv(path_to_csv_file)
    .drop(columns =['CF','CA','SCF','SCA','TOI', 'Unnamed: 2'])
            )
    return data

# Dropping all of the teams I don't want and just getting the Vancouver Canucks, reseting the index, collecting the correct games (10 before Covid-19 outbreak).

def Canucks_Before_Data(data):
    data1 = (data.drop(data[data.Team.isin(["Arizona Coyotes", "Buffalo Sabres", "Boston Bruins", "Carolina Hurricanes", "Columbus Blue Jackets", "Calgary Flames", "Chicago Blackhawks", "Colorado Avalanche", "Dallas Stars", "Detroit Red Wings", "Florida Panthers", "Los Angeles Kings", "Minnesota Wild", "Nashville Predators", "Pittsburgh Penguins", "San Jose Sharks", "Tampa Bay Lightning", "St Louis Blues", "Vegas Golden Knights", "Edmonton Oilers", "Montreal Canadiens", "New Jersey Devils", "New York Islanders", "New York Rangers", "Ottawa Senators", "Philadelphia Flyers", "Toronto Maple Leafs", "Winnipeg Jets", "Washington Capitals", "Anaheim Ducks"])].index)
    .reset_index()
    .drop(data.index[0:27]).drop(data.index[47:56])
    .reset_index().drop(columns = "index")
    .drop(columns =['level_0'])
    .drop(data.index[10:20])
    .reset_index()
    .rename(columns={'CF%':"CF% Before",'SCF%':"SCF% Before",'SH%':"SH% Before",'SV%':"SV% Before",'PDO':"PDO Before"}).drop(columns="Team")
            )
    return data1    

# Dropping all of the teams I don't want and just getting the Vancouver Canucks, reseting the index, collecting the correct games (10 after Covid-19 outbreak).

def Canucks_After_Data(data):
    data2= (data.drop(data[data.Team.isin(["Arizona Coyotes", "Buffalo Sabres", "Boston Bruins", "Carolina Hurricanes", "Columbus Blue Jackets", "Calgary Flames", "Chicago Blackhawks", "Colorado Avalanche", "Dallas Stars", "Detroit Red Wings", "Florida Panthers", "Los Angeles Kings", "Minnesota Wild", "Nashville Predators", "Pittsburgh Penguins", "San Jose Sharks", "Tampa Bay Lightning", "St Louis Blues", "Vegas Golden Knights", "Edmonton Oilers", "Montreal Canadiens", "New Jersey Devils", "New York Islanders", "New York Rangers", "Ottawa Senators", "Philadelphia Flyers", "Toronto Maple Leafs", "Winnipeg Jets", "Washington Capitals", "Anaheim Ducks"])].index)
    .reset_index()
    .drop(data.index[0:27]).drop(data.index[47:56])
    .reset_index().drop(columns = "index")
    .drop(columns =['level_0'])
    .drop(data.index[0:10]).drop(data.index[20:20])
    .reset_index()
    .rename(columns={'CF%':"CF% After",'SCF%':"SCF% After",'SH%':"SH% After",'SV%':"SV% After",'PDO':"PDO After"}).drop(columns="Team")
            )
    return data2

# Dropping all of the teams I don't want and just getting the Buffalo Sabres, reseting the index, collecting the correct games (10 before Covid-19 outbreak).

def Sabres_Before_Data(data):
    data3 = (data.drop(data[data.Team.isin(["Arizona Coyotes", "Vancouver Canucks", "Boston Bruins", "Carolina Hurricanes", "Columbus Blue Jackets", "Calgary Flames", "Chicago Blackhawks", "Colorado Avalanche", "Dallas Stars", "Detroit Red Wings", "Florida Panthers", "Los Angeles Kings", "Minnesota Wild", "Nashville Predators", "Pittsburgh Penguins", "San Jose Sharks", "Tampa Bay Lightning", "St Louis Blues", "Vegas Golden Knights", "Edmonton Oilers", "Montreal Canadiens", "New Jersey Devils", "New York Islanders", "New York Rangers", "Ottawa Senators", "Philadelphia Flyers", "Toronto Maple Leafs", "Winnipeg Jets", "Washington Capitals", "Anaheim Ducks"])].index)
    .reset_index()
    .drop(data.index[20:56])
    .drop(data.index[10:20])
    .drop(columns = "index")
    .reset_index()
    .rename(columns={'CF%':"CF% Before",'SCF%':"SCF% Before",'SH%':"SH% Before",'SV%':"SV% Before",'PDO':"PDO Before"}).drop(columns="Team")
        )  
    return data3

# Dropping all of the teams I don't want and just getting the Buffalo Sabres, reseting the index, collecting the correct games (10 After Covid-19 outbreak).

def Sabres_After_Data(data):
    data4 = (data.drop(data[data.Team.isin(["Arizona Coyotes", "Vancouver Canucks", "Boston Bruins", "Carolina Hurricanes", "Columbus Blue Jackets", "Calgary Flames", "Chicago Blackhawks", "Colorado Avalanche", "Dallas Stars", "Detroit Red Wings", "Florida Panthers", "Los Angeles Kings", "Minnesota Wild", "Nashville Predators", "Pittsburgh Penguins", "San Jose Sharks", "Tampa Bay Lightning", "St Louis Blues", "Vegas Golden Knights", "Edmonton Oilers", "Montreal Canadiens", "New Jersey Devils", "New York Islanders", "New York Rangers", "Ottawa Senators", "Philadelphia Flyers", "Toronto Maple Leafs", "Winnipeg Jets", "Washington Capitals", "Anaheim Ducks"])].index)
    .reset_index()
    .drop(data.index[0:10])
    .drop(data.index[20:56])
    .drop(columns = "index")
    .reset_index()
    .rename(columns={'CF%':"CF% After",'SCF%':"SCF% After",'SH%':"SH% After",'SV%':"SV% After",'PDO':"PDO After"}).drop(columns="Team")
        )
    return data4

# Canucks Combined Function 

def Canucks_Before_And_After(data):
    data1 = (data.drop(data[data.Team.isin(["Arizona Coyotes", "Buffalo Sabres", "Boston Bruins", "Carolina Hurricanes", "Columbus Blue Jackets", "Calgary Flames", "Chicago Blackhawks", "Colorado Avalanche", "Dallas Stars", "Detroit Red Wings", "Florida Panthers", "Los Angeles Kings", "Minnesota Wild", "Nashville Predators", "Pittsburgh Penguins", "San Jose Sharks", "Tampa Bay Lightning", "St Louis Blues", "Vegas Golden Knights", "Edmonton Oilers", "Montreal Canadiens", "New Jersey Devils", "New York Islanders", "New York Rangers", "Ottawa Senators", "Philadelphia Flyers", "Toronto Maple Leafs", "Winnipeg Jets", "Washington Capitals", "Anaheim Ducks"])].index)
    .reset_index()
    .drop(data.index[0:27]).drop(data.index[47:56])
    .reset_index().drop(columns = "index")
    .drop(columns =['level_0'])
    .drop(data.index[10:20])
    .reset_index()
    .rename(columns={'CF%':"CF% Before",'SCF%':"SCF% Before",'SH%':"SH% Before",'SV%':"SV% Before",'PDO':"PDO Before"}).drop(columns="Team")
    .drop(columns = ["index"])
            )
    data2 = (data.drop(data[data.Team.isin(["Arizona Coyotes", "Buffalo Sabres", "Boston Bruins", "Carolina Hurricanes", "Columbus Blue Jackets", "Calgary Flames", "Chicago Blackhawks", "Colorado Avalanche", "Dallas Stars", "Detroit Red Wings", "Florida Panthers", "Los Angeles Kings", "Minnesota Wild", "Nashville Predators", "Pittsburgh Penguins", "San Jose Sharks", "Tampa Bay Lightning", "St Louis Blues", "Vegas Golden Knights", "Edmonton Oilers", "Montreal Canadiens", "New Jersey Devils", "New York Islanders", "New York Rangers", "Ottawa Senators", "Philadelphia Flyers", "Toronto Maple Leafs", "Winnipeg Jets", "Washington Capitals", "Anaheim Ducks"])].index)
    .reset_index()
    .drop(data.index[0:27]).drop(data.index[47:56])
    .reset_index().drop(columns = "index")
    .drop(columns =['level_0'])
    .drop(data.index[0:10]).drop(data.index[20:20])
    .reset_index()
    .rename(columns={'CF%':"CF% After",'SCF%':"SCF% After",'SH%':"SH% After",'SV%':"SV% After",'PDO':"PDO After"}).drop(columns="Team")
    .drop(columns = ["index"])
            )
    DataCanucksBandA = (pd.concat([data1,data2], axis=1)
                       )
    return DataCanucksBandA
    
# Sabres Combined Function 

def Sabres_Before_After(data):
    data3 = (data.drop(data[data.Team.isin(["Arizona Coyotes", "Vancouver Canucks", "Boston Bruins", "Carolina Hurricanes", "Columbus Blue Jackets", "Calgary Flames", "Chicago Blackhawks", "Colorado Avalanche", "Dallas Stars", "Detroit Red Wings", "Florida Panthers", "Los Angeles Kings", "Minnesota Wild", "Nashville Predators", "Pittsburgh Penguins", "San Jose Sharks", "Tampa Bay Lightning", "St Louis Blues", "Vegas Golden Knights", "Edmonton Oilers", "Montreal Canadiens", "New Jersey Devils", "New York Islanders", "New York Rangers", "Ottawa Senators", "Philadelphia Flyers", "Toronto Maple Leafs", "Winnipeg Jets", "Washington Capitals", "Anaheim Ducks"])].index)
    .reset_index()
    .drop(data.index[20:56])
    .drop(data.index[10:20])
    .drop(columns = "index")
    .reset_index()
    .rename(columns={'CF%':"CF% Before",'SCF%':"SCF% Before",'SH%':"SH% Before",'SV%':"SV% Before",'PDO':"PDO Before"}).drop(columns="Team")
    .drop(columns = ["index"])
        )
    data4 = (data.drop(data[data.Team.isin(["Arizona Coyotes", "Vancouver Canucks", "Boston Bruins", "Carolina Hurricanes", "Columbus Blue Jackets", "Calgary Flames", "Chicago Blackhawks", "Colorado Avalanche", "Dallas Stars", "Detroit Red Wings", "Florida Panthers", "Los Angeles Kings", "Minnesota Wild", "Nashville Predators", "Pittsburgh Penguins", "San Jose Sharks", "Tampa Bay Lightning", "St Louis Blues", "Vegas Golden Knights", "Edmonton Oilers", "Montreal Canadiens", "New Jersey Devils", "New York Islanders", "New York Rangers", "Ottawa Senators", "Philadelphia Flyers", "Toronto Maple Leafs", "Winnipeg Jets", "Washington Capitals", "Anaheim Ducks"])].index)
    .reset_index()
    .drop(data.index[0:10])
    .drop(data.index[20:56])
    .drop(columns = "index")
    .reset_index()
    .rename(columns={'CF%':"CF% After",'SCF%':"SCF% After",'SH%':"SH% After",'SV%':"SV% After",'PDO':"PDO After"}).drop(columns="Team")
    .drop(columns = ["index"])
        )
    DataSabresBandA = (pd.concat([data3,data4], axis=1)
                      )
    return DataSabresBandA
    
# A function to show the statistics of selected variables for the top four functions.

def Describe(data):
    return data.describe().T