#pip install 'us'
#pip install 'pandas'

import us  # The 'US' package contains information of states in USA
import pandas as pd  # The Pandas package is used to create data frames

list = us.states.mapping('abbr','name') 

# Creating a list of states that will be in upper & lower case

uppercase_states = ['UpperCase']
for i in list:
    state_name = list[i].upper()  
    uppercase_states += [state_name]


lowercase_states = ['LowerCase']
for i in list:
    state_name = list[i].lower()  
    lowercase_states += [state_name]

# This will create a dataframe for the list
data_frame = pd.DataFrame(uppercase_states,lowercase_states)

# Creating a csv file for dataframe
data_frame.to_csv('file1.csv', header = True) 