# Convert categorical variable into dummy/indicator variables

import pandas as pd
s = pd.Series(list('abca'))
df = pd.get_dummies(s)


df = pd.get_dummies(df, columns=['director', 'actor'])