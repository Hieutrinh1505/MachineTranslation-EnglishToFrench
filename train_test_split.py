import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("eng_french.csv")
df = df.rename(columns = {"English words/sentences":"English","French words/sentences":"French"})

train, test = train_test_split(df,test_size=0.1, random_state=42)
train, valid = train_test_split(df,test_size=0.1, random_state=50)

train.to_csv(r'C:\Users\hieut\MachineTranslation\MachineTranslation-EnglishToFrench\train.csv', index=False)
test.to_csv(r'C:\Users\hieut\MachineTranslation\MachineTranslation-EnglishToFrench\test.csv', index=False)
valid.to_csv(r'C:\Users\hieut\MachineTranslation\MachineTranslation-EnglishToFrench\valid.csv', index=False)

