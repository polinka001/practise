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
#
# color_dataframe = pd.DataFrame.from_dict(fur_color, orient="index")
# color_dataframe.columns = ['color', 'squireel_number']

color_dataframe = pd.DataFrame(fur_color.items(), columns = ['color', 'squireel_number'])




color_dataframe.to_csv('squirrel_count.csv')






# with open('weather_data.csv', 'r') as weather_data_file:
#     data = csv.reader(weather_data_file)
#     # print(data)
#     # [print(row) for row in data]
#     temperatures = []
#     next(data)
#     for row in data:
#         temperatures.append(int(row[1]))
#     print(temperatures)
# data = pandas.read_csv('weather_data.csv')
# print(data['temp'])
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)
#
# print(sum(temp_list) / len(temp_list))
#
# maximum = data['temp'].max()
# print(data[data.temp == maximum])

# monday = (data[data.day == 'Monday'])
#
# temp_monday = monday.temp * 1.8 + 32


# print(temp_monday)

# print(data.temp)

# elements_num = data['temp'].size()
# print(elements_num)
#
