import streamlit




streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast')
streamlit.text(':) Omega 3 & Blueberry Oatmeal')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('Your smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#List to pick fruit to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


#display the table on page
streamlit.dataframe(fruits_to_show)
