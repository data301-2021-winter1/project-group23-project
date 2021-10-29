import pandas as pd
import seaborn as sns
import numpy as np
#Importing processed csv file
def load_and_process(path_to_csv_file):
    datak = (pd.read_csv(path_to_csv_file)
    .drop(columns =['CF','CA','SCF','SCA','Unnamed: 2'])
    )
    return datak

#Creating north division, by dropping all teams that were not in the division, then dropping the team name and index and creating a column for the division name. 
def North_Div1(datak):
    datak1 = (datak.drop(datak[datak.Team.isin([ "Arizona Coyotes", "Buffalo Sabres", "Boston Bruins", "Carolina Hurricanes", "Columbus Blue Jackets", 
                                        "Chicago Blackhawks", "Colorado Avalanche", "Dallas Stars", "Detroit Red Wings", "Florida Panthers",
                                        "Los Angeles Kings", "Minnesota Wild", "Nashville Predators", "Pittsburgh Penguins", "San Jose Sharks", "Tampa Bay Lightning",
                                        "St Louis Blues", "Vegas Golden Knights", "New Jersey Devils", "New York Islanders", "New York Rangers", "Philadelphia Flyers", 
                                        "Washington Capitals", "Anaheim Ducks"])].index)
              .reset_index()
              .drop(columns = ['Team', 'index'])
             )
    datak1['Division']='North'
    return datak1
#Creating east division, by dropping all teams that were not in the division, then dropping the team name and index and creating a column for the division name. 
def East_Div1(datak):
    datak2 = (datak.drop(datak[datak.Team.isin(["Arizona Coyotes", "Carolina Hurricanes", "Columbus Blue Jackets", "Calgary Flames", "Chicago Blackhawks", "Colorado Avalanche", 
                                       "Dallas Stars", "Detroit Red Wings", "Florida Panthers", "Los Angeles Kings", "Minnesota Wild", "Nashville Predators", "San Jose Sharks", 
                                       "Tampa Bay Lightning", "St Louis Blues", "Vegas Golden Knights", "Edmonton Oilers", "Montreal Canadiens","Ottawa Senators",
                                       "Toronto Maple Leafs", "Winnipeg Jets", "Anaheim Ducks", "Vancouver Canucks",])].index)
               .reset_index()
               .drop(columns = ['Team', 'index'])
               
             )
    datak2['Division']='East'
    return datak2
#Creating central division, by dropping all teams that were not in the division, then dropping the team name and index and creating a column for the division name. 
def Cent_Div1(datak):
    datak3 = (datak.drop(datak[datak.Team.isin(["Arizona Coyotes", "Buffalo Sabres", "Boston Bruins", "Calgary Flames","Colorado Avalanche"
                                        ,"Los Angeles Kings", "Minnesota Wild","Pittsburgh Penguins", "San Jose Sharks", "St Louis Blues", "Vegas Golden Knights",
                                        "Edmonton Oilers", "Montreal Canadiens", "New Jersey Devils", "New York Islanders", 
                                        "New York Rangers", "Ottawa Senators", "Philadelphia Flyers", "Toronto Maple Leafs",
                                        "Winnipeg Jets", "Washington Capitals", "Anaheim Ducks", "Vancouver Canucks"])].index)
              .reset_index()
              .drop(columns = ['Team', 'index'])
              
             )
    datak3['Division']='Central'
    return datak3
#Creating west division, by dropping all teams that were not in the division, then dropping the team name and index and creating a column for the division name. 
def West_Div1(datak):
    datak4 = (datak.drop(datak[datak.Team.isin(["Buffalo Sabres", "Boston Bruins", "Carolina Hurricanes", 
                                        "Columbus Blue Jackets", "Calgary Flames", "Chicago Blackhawks",  "Dallas Stars", "Detroit Red Wings", "Florida Panthers",
                                       "Nashville Predators", "Pittsburgh Penguins","Tampa Bay Lightning","Edmonton Oilers", "Montreal Canadiens",
                                        "New Jersey Devils", "New York Islanders", "New York Rangers", "Ottawa Senators", 
                                        "Philadelphia Flyers", "Toronto Maple Leafs", "Winnipeg Jets", "Washington Capitals","Vancouver Canucks"])].index)
              .reset_index()
              .drop(columns = ['Team', 'index'])
            
             )
    datak4['Division']='West'
    return datak4
# Creating all divisons as a concat of all of above divisions to compare. 
def all_divisions_describe(datak):
    
    datak1 = (datak.drop(datak[datak.Team.isin([ "Arizona Coyotes", "Buffalo Sabres", "Boston Bruins", "Carolina Hurricanes", "Columbus Blue Jackets", 
                                        "Chicago Blackhawks", "Colorado Avalanche", "Dallas Stars", "Detroit Red Wings", "Florida Panthers",
                                        "Los Angeles Kings", "Minnesota Wild", "Nashville Predators", "Pittsburgh Penguins", "San Jose Sharks", "Tampa Bay Lightning",
                                        "St Louis Blues", "Vegas Golden Knights", "New Jersey Devils", "New York Islanders", "New York Rangers", "Philadelphia Flyers", 
                                        "Washington Capitals", "Anaheim Ducks"])].index)
              .reset_index()
              .drop(columns = ['Team', 'index'])
             )
    datak1['Division']='North'
    
    datak2 = (datak.drop(datak[datak.Team.isin(["Arizona Coyotes", "Carolina Hurricanes", "Columbus Blue Jackets", "Calgary Flames", "Chicago Blackhawks", "Colorado Avalanche", 
                                       "Dallas Stars", "Detroit Red Wings", "Florida Panthers", "Los Angeles Kings", "Minnesota Wild", "Nashville Predators", "San Jose Sharks", 
                                       "Tampa Bay Lightning", "St Louis Blues", "Vegas Golden Knights", "Edmonton Oilers", "Montreal Canadiens","Ottawa Senators",
                                       "Toronto Maple Leafs", "Winnipeg Jets", "Anaheim Ducks", "Vancouver Canucks",])].index)
               .reset_index()
               .drop(columns = ['Team', 'index'])
               
             )
    datak2['Division']='East'
    
    datak3 = (datak.drop(datak[datak.Team.isin(["Arizona Coyotes", "Buffalo Sabres", "Boston Bruins", "Calgary Flames","Colorado Avalanche"
                                        ,"Los Angeles Kings", "Minnesota Wild","Pittsburgh Penguins", "San Jose Sharks", "St Louis Blues", "Vegas Golden Knights",
                                        "Edmonton Oilers", "Montreal Canadiens", "New Jersey Devils", "New York Islanders", 
                                        "New York Rangers", "Ottawa Senators", "Philadelphia Flyers", "Toronto Maple Leafs",
                                        "Winnipeg Jets", "Washington Capitals", "Anaheim Ducks", "Vancouver Canucks"])].index)
              .reset_index()
              .drop(columns = ['Team', 'index'])
              
             )
    datak3['Division']='Central'
    
    datak4 = (datak.drop(datak[datak.Team.isin(["Buffalo Sabres", "Boston Bruins", "Carolina Hurricanes", 
                                        "Columbus Blue Jackets", "Calgary Flames", "Chicago Blackhawks",  "Dallas Stars", "Detroit Red Wings", "Florida Panthers",
                                       "Nashville Predators", "Pittsburgh Penguins","Tampa Bay Lightning","Edmonton Oilers", "Montreal Canadiens",
                                        "New Jersey Devils", "New York Islanders", "New York Rangers", "Ottawa Senators", 
                                        "Philadelphia Flyers", "Toronto Maple Leafs", "Winnipeg Jets", "Washington Capitals","Vancouver Canucks"])].index)
              .reset_index()
              .drop(columns = ['Team', 'index'])
            
             )
    datak4['Division']='West'
    
   
    
    all_div = (pd.concat([datak1, datak2, datak3, datak4], axis=0)
              )
    return all_div