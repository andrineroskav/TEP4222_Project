# Authors: Andrine Roska Vallestad, Ida Bertine Rambøl, Kristian L. Karstensen
# Mail:
# Version stuff
# something 
# header stuff
#Tester her 123


#%%
# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#%%
# Making a new DataFrame
    # Import finished dataset here instead 
    # Ex: CBi = pd.read_excel(r"CBi_NOR_test.xlsx", header=[0], index_col=[0])

Category =  pd.read_excel(r"Data/Test_product_categories.xlsx", header=[0,1])#.fillna(0)

COICOP = Category.columns.get_level_values(0)
COICOP

#%%

#CBi_Urb = pd.DataFrame(index=Category.columns, columns=['CB En FP','City','Town','Rural'])
CBi_Urb = pd.DataFrame(columns=COICOP, index=['City','Town','Rural'])
CBi_Urb


# .pivot flip dataframe
#%%
Random = np.random.randint(low=0, high=100, size=(CBi_Urb.shape))
df = pd.DataFrame(Random, index=CBi_Urb.index, columns=CBi_Urb.columns)

#%%
df


#%%
from matplotlib import colormaps
list(colormaps)

#%%


ax = df.plot.bar(stacked=True, title='Consumption Based Energy Footprint - Norway')

#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], title='Line', loc='upper left')

###############################################
######      Plotting with Seaborn        ######

#%%
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a visualization
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)

#%%
penguins = sns.load_dataset("penguins")
sns.histplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")

#%%

sns.histplot(data=df, x=df.index, hue="species", multiple="stack")

#%%




# colorblind
# Spectral


ax = df.plot(kind = 'bar', stacked = True, color= sns.color_palette('Spectral', n_colors=12))
#plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0, fontsize=14)


handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], title='COICOP', bbox_to_anchor=(1, 1), loc=2, borderaxespad=0, fontsize=14)

#plt.ylabel('UNIT')
#plt.xlabel('Urbaization')
plt.title('Consumption Based Energy Eootprint', fontsize=14) #fontstyle ='TNR'

