#!/usr/bin/python3

# This is a tutorial how to fix pandas' SettingWithCopyWarning.
# Source: https://www.dataquest.io/blog/settingwithcopywarning/

import pandas as pd

# File can be downloaded from: http://www.modelingonlineauctions.com/datasets
data = pd.read_csv('/home/balint/workspace/tmp/useful_python_scripts/data/xbox-3-day-auctions.csv')
data.head()

#%%
# It can be tempting to ignore the warning if your code still works as expected.
# This is bad practice and SettingWithCopyWarning should _never_ be ignored.


# Assignment
data = pd.read_csv('xbox-3-day-auctions.csv')
# Access
data.get('auctionid')
# Indexing
data[1:15]
# Chaining
data[1:5][1:3]

#%%
# E.g. user 'parakeet2004'’s bidder rating is incorrect and we must update it.
data[data.bidder == 'parakeet2004']

data[data.bidder == 'parakeet2004']['bidderrate'] = 100

# Oh no! We’ve mysteriously stumbled upon the SettingWithCopyWarning!

# Values were not changed!
data[data.bidder == 'parakeet2004']

# It's caused by chaining two indexing operations together.

# Setting the new value correctly
data.loc[data.bidder == 'parakeet2004', 'bidderrate'] = 100

# Taking a look at the result
data[data.bidder == 'parakeet2004']['bidderrate']

#%%
# Hidden chaining

winners = data.loc[data.bid == data.price]
winners.head(n=100)

# Woohoo, something is missing!
winners.loc[304, 'bidder']
# Let's fix it!
winners.loc[304, 'bidder'] = 'therealname'

# Oh, no! Not again, SettingWithCopyWarning! 

# The correct way: 
winners = data.loc[data.bid == data.price].copy()
winners.loc[304, 'bidder'] = 'therealname'
print(winners.loc[304, 'bidder'])
print(data.loc[304, 'bidder'])

# And if you want to change the original, use a single assignment operation!

#%%
# Turning off the warning (this is usually bad practice!)

#'raise' - to raise an exception instead of a warning.
#'warn' - to generate a warning (default).
#None - to switch off the warning entirely.

pd.set_option('mode.chained_assignment', None)
data[data.bidder == 'parakeet2004']['bidderrate'] = 100

pd.set_option('mode.chained_assignment', 'raise')
data[data.bidder == 'parakeet2004']['bidderrate'] = 100


# A more precise way to use this setting is by using a context manager:
    
# resets the option we set in the previous code segment
pd.reset_option('mode.chained_assignment')
              
with pd.option_context('mode.chained_assignment', None):
    data[data.bidder == 'parakeet2004']['bidderrate'] = 100



















