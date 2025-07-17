import csv
from tarfile import data_filter

import pandas as pd

squirrel_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
color_list = squirrel_data["Primary Fur Color"]
gray = color_list.str.count('Gray').sum()
cinnamon = color_list.str.count('Cinnamon').sum()
black = color_list.str.count('Black').sum()
print(black, gray, cinnamon)


fur_color = {
    'gray': [gray],
    'black': [black],
    'cinammon': [cinnamon]
}

color_dataframe = pd.DataFrame(fur_color.items(), columns = ['color', 'squireel_number'])

color_dataframe.to_csv('squirrel_count.csv')
