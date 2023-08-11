import pandas as pd

data = pd.read_excel('data/data.xlsx')

unuseful = [
    'Quantity of client\'s dependents',
    'Education level',
    'loan_currency'
]
data.drop(unuseful,axis=1,inplace=True)

for i in data.columns :
    new = i.lower()
    new = new.replace('\'','').replace(' ','_').replace('-','').replace('(','').replace(')','').replace('__','_')
    data.rename({i:new},axis=1,inplace=True)
	
data.to_excel('data/data.xlsx',index=False)