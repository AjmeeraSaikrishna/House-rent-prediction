import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
rent_df = pd.read_csv("../input/house-rent-prediction-dataset/House_Rent_Dataset.csv")
rent_df.sample(5)
rent_df.shape
rent_df.columns
rent_df.info()
rent_df.describe()
rent_df.isnull().sum()
rent_df.duplicated().sum()
print("Mean House Rent:", round(rent_df["Rent"].mean()))
print("Median House Rent:", round(rent_df["Rent"].median()))
print("Highest House Rent:", round(rent_df["Rent"].max()))
print("Lowest House Rent:", round(rent_df["Rent"].min()))
rent_df["Rent"].sort_values(ascending = False)[:5]
rent_df["Rent"].sort_values()[:5]
sns.set_context("poster", font_scale = .8)
plt.figure(figsize = (20, 6))
ax = rent_df["City"].value_counts().plot(kind = 'bar', color = "crimson", rot = 0)

for p in ax.patches:
    ax.annotate(int(p.get_height()), (p.get_x() + 0.25, p.get_height() - 100), ha = 'center', va = 'bottom', color = 'white')
sns.set_context("poster", font_scale = .8)
plt.figure(figsize = (20, 6))
ax = rent_df["Furnishing Status"].value_counts().plot(kind = 'bar', color = "Orange", rot = 0)

for p in ax.patches:
    ax.annotate(int(p.get_height()), (p.get_x() + 0.25, p.get_height() - 250), ha = 'center', va = 'bottom', color = 'Black')
sns.set_context("poster", font_scale = .8)
plt.figure(figsize = (20, 6))
ax = rent_df["Tenant Preferred"].value_counts().plot(kind = 'bar', color = "Green", rot = 0)

for p in ax.patches:
    ax.annotate(int(p.get_height()), (p.get_x() + 0.25, p.get_height() - 300), ha = 'center', va = 'bottom', color = 'White')
plt.figure(figsize = (20, 8))
counts = rent_df["City"].value_counts()
explode = (0, 0, 0, 0, 0, 0.1)
colors = ['#FF1E00', '#A66CFF', '#EAE509', '#D61C4E', '#3CCF4E', '#3AB4F2']

counts.plot(kind = 'pie', colors = colors, explode = explode, autopct = '%1.1f%%')
plt.axis('equal')
plt.legend(labels = counts.index, loc = "best")
plt.show()
plt.figure(figsize = (20, 6))
plt.ticklabel_format(style = 'plain')
plt.scatter(rent_df["Size"], rent_df["Rent"])
plt.xlabel("Size")
plt.ylabel("Rent");
x = rent_df["Rent"]
y = rent_df["Size"]
colors = rent_df["Size"]
sizes = rent_df["Size"]
plt.figure(figsize = (25, 8))
plt.ticklabel_format(style = 'plain')
plt.scatter(x, y, c = colors, s = sizes, alpha = 0.3, cmap = 'viridis')
plt.colorbar();
plt.figure(figsize = (20, 7))
sns.barplot(x = rent_df["City"], y = rent_df["Rent"], palette = "nipy_spectral");
n_bins = 20
plt.figure(figsize = (20, 6))
rent_df["Size"].hist(bins = n_bins);
sns.set_context("poster", font_scale = .8)
plt.figure(figsize = (30, 10))
ax = rent_df["BHK"].value_counts().plot(kind = 'bar', color = "Blue", rot = 0)

for p in ax.patches:
    ax.annotate(int(p.get_height()), (p.get_x() + 0.25, p.get_height() + 1), ha = 'center', va = 'bottom', color = 'Black')
sns.set_context("poster", font_scale = .8)
plt.figure(figsize = (30, 10))
ax = rent_df["Bathroom"].value_counts().plot(kind = 'bar', color = "Green", rot = 0)

for p in ax.patches:
    ax.annotate(int(p.get_height()), (p.get_x() + 0.25, p.get_height() + 1), ha = 'center', va = 'bottom', color = 'Black')
plt.figure(figsize = (20, 5))
colormap = plt.cm.plasma
sns.heatmap(pd.crosstab(rent_df["Area Type"], rent_df["BHK"]), cmap = colormap)
from wordcloud import WordCloud, STOPWORDS

text = " ".join(Company for Company in rent_df["Area Locality"])
word_cloud = WordCloud(width = 1600,
                       height = 800,
                       colormap = 'prism',
                       background_color = "white").generate(text)
plt.figure(figsize = (30, 6))
plt.imshow(word_cloud, interpolation="gaussian")
plt.axis("off")
plt.show()from wordcloud import WordCloud, STOPWORDS

text = " ".join(Company for Company in rent_df["Area Locality"])
word_cloud = WordCloud(width = 1600,
                       height = 800,
                       colormap = 'prism',
                       background_color = "white").generate(text)
plt.figure(figsize = (30, 6))
plt.imshow(word_cloud, interpolation="gaussian")
plt.axis("off")
plt.show()
from wordcloud import WordCloud, STOPWORDS

text = " ".join(Company for Company in rent_df["Area Locality"])
word_cloud = WordCloud(width = 1600,
                       height = 800,
                       colormap = 'prism',
                       background_color = "white").generate(text)
plt.figure(figsize = (30, 6))
plt.imshow(word_cloud, interpolation="gaussian")
plt.axis("off")
plt.show()
from wordcloud import WordCloud, STOPWORDS

text = " ".join(Company for Company in rent_df["Area Locality"])
word_cloud = WordCloud(width = 1600,
                       height = 800,
                       colormap = 'prism',
                       background_color = "white").generate(text)
plt.figure(figsize = (30, 6))
plt.imshow(word_cloud, interpolation="gaussian")
plt.axis("off")
plt.show()
from wordcloud import WordCloud, STOPWORDS

text = " ".join(Company for Company in rent_df["Area Locality"])
word_cloud = WordCloud(width = 1600,
                       height = 800,
                       colormap = 'prism',
                       background_color = "white").generate(text)
plt.figure(figsize = (30, 6))
plt.imshow(word_cloud, interpolation="gaussian")
plt.axis("off")
plt.show()
from wordcloud import WordCloud, STOPWORDS

text = " ".join(Company for Company in rent_df["Area Locality"])
word_cloud = WordCloud(width = 1600,
                       height = 800,
                       colormap = 'prism',
                       background_color = "white").generate(text)
plt.figure(figsize = (30, 6))
plt.imshow(word_cloud, interpolation="gaussian")
plt.axis("off")
plt.show()
from wordcloud import WordCloud, STOPWORDS

text = " ".join(Company for Company in rent_df["Area Locality"])
word_cloud = WordCloud(width = 1600,
                       height = 800,
                       colormap = 'prism',
                       background_color = "white").generate(text)
plt.figure(figsize = (30, 6))
plt.imshow(word_cloud, interpolation="gaussian")
plt.axis("off")
plt.show()
from wordcloud import WordCloud, STOPWORDS

text = " ".join(Company for Company in rent_df["Area Locality"])
word_cloud = WordCloud(width = 1600,
                       height = 800,
                       colormap = 'prism',
                       background_color = "white").generate(text)
plt.figure(figsize = (30, 6))
plt.imshow(word_cloud, interpolation="gaussian")
plt.axis("off")
plt.show()
