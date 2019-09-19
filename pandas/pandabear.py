#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt

excel_file = 'movies.xls'

movies = pd.read_excel(excel_file)
#print(movies.head())

movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
#print(movies_sheet1.head())

movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
#print(movies_sheet2.head())

movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)
#print(movies_sheet3.head())

movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])
#print(movies.shape)

sorted_by_gross = movies.sort_values(["Gross Earnings"], ascending=False).head(10)
sorted_by_score = movies.sort_values(['IMDB Score'], ascending=False).head(10)

print(sorted_by_gross["Gross Earnings"])
print(sorted_by_score['IMDB Score'])
#print(sorted_by_gross.keys())
for i in sorted_by_gross["Gross Earnings"]:
    print(i)

input("Press enter to continue...")

fig, ax = plt.subplots()
image, = ax.bar(sorted_by_gross['Gross Earnings'], sorted_by_gross['Year'])
plt.draw()
fig.savefig("stackedbar.png")

image, = ax.hist(sorted_by_score['IMDB Score'])
plt.draw()
fig.savefig("imdbscore.png")
plt.close(fig)
