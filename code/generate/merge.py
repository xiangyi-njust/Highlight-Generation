import pandas as pd
import json

df_abstract = pd.read_excel('../../data/Elesivr-crawl-for-abstract.xlsx')
df_highlight = pd.read_excel('../../data/TFSC-highlight.xlsx')
with open('../../data/full_page_info.json', 'r') as f:
    full_page_infos = json.load(f)

titles = df_abstract['title'].tolist()
abstracts = df_abstract['abstract'].tolist()
all_titles = df_highlight['title'].tolist()
highlights = df_highlight['highlight'].tolist()

datasets = {}

for i in range(len(highlights)):
    title = all_titles[i]
    highlight = highlights[i]

    if title in datasets.keys():
        datasets[title]['highlight'] += '\n'
        datasets[title]['highlight'] += highlight
    else:
        datasets[title] = {}
        datasets[title]['highlight'] = highlight

for i in range(len(abstracts)):
    title = titles[i]
    abstract = abstracts[i]

    datasets[title]['abstract'] = abstract

for title in full_page_infos.keys():
    datasets[title]['full_page'] = full_page_infos[title]

with open('../../data/dataset.json', 'w') as f:
    json.dump(datasets, f)
