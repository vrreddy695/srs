
import pandas as pd
import numpy as np
df=pd.read_sas('~/Downloads/hsb2-1.sas7bdat')
df.head()
freq=df.groupby(['race']).size().reset_index(name='counts')
freq['pct']=(freq['counts']/df.shape[0])*100
print('populaiton race praportions:', "\n", freq)
import srs
sample=srs.samp(df, 'race', 0.25)

freq=sample.groupby(['race']).size().reset_index(name='counts')
freq['pct']=(freq['counts']/sample.shape[0])*100
print('populaiton race praportions:', "\n", freq)
df.shape
sample.shape
