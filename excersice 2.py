import numpy as np
import pandas as pd

###############################################################################
#question 23

df=pd.DataFrame(np.random.random(size=(5,3)))
print(df-df.mean())


###############################################################################
#question 24

df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))
g=df.sum()
print(g.min())