def load_and_process(path_to_csv_file):
    import pandas as pd
    import seaborn as sns
    import numpy as np
    datak = (pd.read_csv(path_to_csv_file)
    .drop(columns =['CF','CA','SCF','SCA','Unnamed: 2'])
    )
    return datak

dframe= load_and_process("../data/raw/Games - Natural Stat TrickTeam Season Totals - Natural Stat Trick.csv")
dframe

def North_Div1(datak):
    import pandas as pd
    import seaborn as sns
    import numpy as np
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

def East_Div1(datak):
    import pandas as pd
    import seaborn as sns
    import numpy as np
    datak2 = (datak.drop(datak[datak.Team.isin(["Arizona Coyotes", "Carolina Hurricanes", "Columbus Blue Jackets", "Calgary Flames", "Chicago Blackhawks", "Colorado Avalanche", 
                                       "Dallas Stars", "Detroit Red Wings", "Florida Panthers", "Los Angeles Kings", "Minnesota Wild", "Nashville Predators", "San Jose Sharks", 
                                       "Tampa Bay Lightning", "St Louis Blues", "Vegas Golden Knights", "Edmonton Oilers", "Montreal Canadiens","Ottawa Senators",
                                       "Toronto Maple Leafs", "Winnipeg Jets", "Anaheim Ducks", "Vancouver Canucks",])].index)
               .reset_index()
               .drop(columns = ['Team', 'index'])
               
             )
    datak2['Division']='East'
    return datak2

def Cent_Div1(datak):
    import pandas as pd
    import seaborn as sns
    import numpy as np
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

def West_Div1(datak):
    import pandas as pd
    import seaborn as sns
    import numpy as np
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

def all_divisions_describe(datak):
    import pandas as pd
    import seaborn as sns
    import numpy as np
    
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