import pandas as pd

df = pd.read_csv('us-population-2010-2019.csv')
df

#reshape
df = pd.melt(df, id_vars = ['states', 'id'], var_name = 'year', value_name = 'population')
df

# chuyen doi kieu du lieu
df['states'] = df['states'].astype(str)
df['id'] = df['id'].astype(int)
df['year'] = df['year'].astype(int)
df['population'] = df['population'].str.replace(',', '').astype(int)
df

#Phan tich co ban - Loc theo nam 
selected_year = 2014
df_selected_year = df[df['year'] == selected_year]
df_selected_year

# Sap xep du lieu 
df_selected_year = df_selected_year.sort_values(by = 'population', ascending = False)
df_selected_year

# so sánh dân số với năm trước đó
def diff_population_previous(input_df, input_year):
  df_selected_year = input_df[input_df['year'] == input_year].reset_index()
  df_previous_year = input_df[input_df['year'] == input_year - 1].reset_index()

  df_selected_year['diff_population'] = df_selected_year.population.sub(df_previous_year.population, fill_value = 0)
  return df_selected_year

diff_population_previous(df, 2014)

# loc ra nhung danh sach : bang bi giam

df_diff_2014_2013 = diff_population_previous(df, 2014)
df_decrease_2014_2013 = df_diff_2014_2013[df_diff_2014_2013.diff_population<0]

df_decrease_2014_2013

# tinh phan tramm tren tong so cac bang 
len(df_decrease_2014_2013)/len(df_diff_2014_2013) * 100


alt.themes.enable('dark')

heatmap = alt.Chart(df).mark_rect().encode(
    x = alt.X('states:O'),
    y = alt.Y('year: O'),
    color = alt.Color('max(population): Q')
)

heatmap
