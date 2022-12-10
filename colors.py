# MEAN AND MEDIAN OF COLORS ON HTML PAGE
from bs4 import BeautifulSoup
import pandas as pd

with open("python_class_question.html") as file:
    contents = file.read()
soup = BeautifulSoup(contents, "html.parser")
table_columns = soup.select("td")
table_columns_text = [column.getText() for column in table_columns]
table_columns_text = list(filter(lambda a: "DAY" not in a, table_columns_text))
table_dict = {
    "Monday": table_columns_text[0].split(", "),
    "Tuesday": table_columns_text[1].split(", "),
    "Wednesday": table_columns_text[2].split(", "),
    "Thursday": table_columns_text[3].split(", "),
    "Friday": table_columns_text[4].split(", ")
}
monday_frequency = {}
tuesday_frequency = {}
wednesday_frequency = {}
thursday_frequency = {}
friday_frequency = {}
colors = list(set(
    table_dict["Monday"] + table_dict["Tuesday"] + table_dict["Wednesday"] + table_dict["Thursday"] + table_dict[
        "Friday"]))
for color in colors:
    monday_frequency[color] = table_dict["Monday"].count(color)
    tuesday_frequency[color] = table_dict["Tuesday"].count(color)
    wednesday_frequency[color] = table_dict["Wednesday"].count(color)
    thursday_frequency[color] = table_dict["Thursday"].count(color)
    friday_frequency[color] = table_dict["Friday"].count(color)
frequency_dict = {
    "Monday": monday_frequency,
    "Tuesday": tuesday_frequency,
    "Wednesday": wednesday_frequency,
    "Thursday": thursday_frequency,
    "Friday": friday_frequency
}
df = pd.DataFrame(frequency_dict).transpose().sum()
total_sum = 0
for color in colors:
    total_sum += df[color]
total_sum /= 5
for color in colors:
    if df[color] > total_sum:
        mean = color
        break
print(f"1. The mean is {mean}")

max_color = colors[0]
for color in colors:
    if df[color] > df[max_color]:
        max_color = color
print(f"2. The color worn mostly is {max_color}")

median_list = table_dict["Monday"] + table_dict["Tuesday"] + table_dict["Wednesday"] + table_dict["Thursday"] + table_dict[
        "Friday"]
middle_index = int((len(median_list) - 1)/2)
print(f"3. Median colour is {median_list[middle_index]}")

prob_red = median_list.count("RED")/len(median_list)
print(f"5. If a color is chosen at random, the probability it is RED is {round(prob_red, 6)}")

