# TypeError Invalid comparison between datetime64[ns] and date


from datetime import date
import pandas as pd


df = pd.DataFrame({'date': ['06/12/2023', '07/15/2023', '11/16/2023'],
                   'value': [2, 3, 4]})

# ✅ Access dt.date attribute
df['date'] = pd.to_datetime(df['date']).dt.date
print(df)

print('-' * 50)

df2 = df.loc[df['date'] >= date.today()]

print(df2)