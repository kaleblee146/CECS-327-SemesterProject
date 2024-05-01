import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

read_in = pd.read_csv('taylormusicdata.csv')
read_in.head()

encoder = OneHotEncoder()
encoded_titles = encoder.fit_transform(read_in[['title']])
encoded_titles_df = pd.DataFrame(encoded_titles.toarray(), columns=encoder.get_feature_names_out(['title']))

# Combine the encoded titles with the original dataframe
read_in_encoded = pd.concat([read_in, encoded_titles_df], axis=1)

# Define X and y
x = encoded_titles_df
y = read_in['peak_position']

pred = LinearRegression()
pred.fit(x, y)

plt.figure(figsize=(10, 6))
bars_actual = plt.bar(read_in['title'], read_in['peak_position'] - 60, bottom=60, align='center', alpha=0.5, label='Actual Peak Position')

# Reverse the y-axis values
plt.title('Taylor Swift')
plt.xlabel('Title')
plt.ylabel('Album Peak Position on Billboard')
plt.xticks(rotation=90)
plt.ylim(60,0)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
bars_pred = plt.bar(read_in['title'], pred.predict(x) - 60, bottom=60, color='red', alpha=0.5, label='Predicted Peak Position')

plt.title('Taylor Swift')
plt.xlabel('Title')
plt.ylabel('Album Peak Position on Billboard')
plt.xticks(rotation=90)
plt.ylim(60,0)
plt.legend()
plt.tight_layout()
plt.show()
'''
album_peak_position = read_in.groupby('title').agg({'peak_position': ['min', 'max']}).reset_index()

plt.figure(figsize=(10, 6))
plt.scatter(album_peak_position['title'], album_peak_position['peak_position']['min'], color='red', label='Lowest Peak')
plt.scatter(album_peak_position['title'], album_peak_position['peak_position']['max'], color='blue', label='Highest Peak')
plt.title('Taylor Swift Albums: Lowest and Highest Peak Positions on Billboard 200')
plt.xlabel('Album')
plt.ylabel('Peak Position')
plt.xticks(rotation=90)  
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
'''

