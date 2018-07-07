
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import itertools as it



from sklearn.cluster import KMeans

sns.set_context('talk')

# originally from https://github.com/woodnathan/MarioKart8-Stats, added DLC and fixed a few typos
bodies = pd.read_csv('mariokart/bodies.csv')
chars = pd.read_csv('mariokart/characters.csv')
gliders = pd.read_csv('mariokart/gliders.csv')
tires = pd.read_csv('mariokart/tires.csv')

# use only stock (non-DLC) characters / karts / tires
chars = chars.loc[chars['DLC']==0]
bodies = bodies.loc[bodies['DLC']==0]
tires = tires.loc[tires['DLC']==0]
gliders = gliders.loc[gliders['DLC']==0]

stat_cols = bodies.columns[2:-1]
main_cols = ['Weight','Speed','Acceleration','Handling','Traction']

# lots of characters/karts/tires are exactly the same. here we just want one from each stat type
chars_unique = chars.drop_duplicates(subset=stat_cols).set_index('Character')[stat_cols]
bodies_unique = bodies.drop_duplicates(subset=stat_cols).set_index('Body')[stat_cols]
tires_unique = tires.drop_duplicates(subset=stat_cols).set_index('Tire')[stat_cols]



# only two types of gliders, one of which is pretty clearly just better
glider_best = gliders.loc[gliders['Glider']=='Flower']


# In[19]:


combos=[]

body_names=bodies_unique.index

tire_names=tires_unique.index

char_names=chars_unique.index

for body in body_names:
    for tire in tire_names:
        for char in char_names: 
            thiscombo=(char,body,tire)
            combos.append(thiscombo)

stats=pd.DataFrame(columns=['speed','accel','hand'], index=combos)


for combo in combos:
    #print(combo)
    char=combo[0]
    body=combo[1]
    tire=combo[2]
    speed=sum([bodies_unique.loc[body,'Speed'],tires_unique.loc[tire,'Speed'],chars_unique.loc[char,'Speed']] )
    accel= sum([bodies_unique.loc[body,'Acceleration'],tires_unique.loc[tire,'Acceleration'],chars_unique.loc[char,'Acceleration'] ])
    hand= sum([bodies_unique.loc[body,'Handling'],tires_unique.loc[tire,'Handling'],chars_unique.loc[char,'Handling'] ])
    
    index=combo
    print(index)
    stats.loc[(index),'speed':'hand']= [speed, accel, hand]
#    stats.loc[(index),'accel']=accel
 #   stats.loc[(index),'hand']=hand
    print(speed, accel, hand)


# In[3]:


stats

