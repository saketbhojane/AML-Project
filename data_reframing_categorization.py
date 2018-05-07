import tqdm
from sklearn.model_selection import train_test_split
import time
import os

description = []
caption = []

with open('parallel_corp_entertainment.desc', 'r') as f:
    for line in tqdm.tqdm(f):
        description.append(line.strip())

with open('parallel_corp_entertainment.summ', 'r') as f:
    for line in tqdm.tqdm(f):
        caption.append(line.strip())

# print("Total data size = ", len(description))

# print("Training size = ", len(X_train))
# print("Test size = ", len(X_test))
# print("Validation size = ", len(X_val))

if not os.path.exists("dataset"): os.makedirs("dataset")
if not os.path.exists("./dataset/TOI"): os.makedirs("./dataset/TOI")

article_names = []

for i, (d, c) in tqdm.tqdm(enumerate(zip(description, caption))):
    data = d + '\n\n' + "@highlight" + '\n\n' + c

    with open('./dataset/TOI/news' + str(i), 'w') as f:
        f.write(data)

    article_names.append('news' + str(i))

random_seed = int(str(time.time()).split('.')[1])
X_train, X_test, y_train, y_test = train_test_split(article_names, [0]*len(article_names), test_size=0.1, random_state=random_seed)

random_seed = int(str(time.time()).split('.')[1])
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.11, random_state=random_seed)

if not os.path.exists("url_lists"): os.makedirs("url_lists")

with open('url_lists/all_train.txt', 'w') as f:
    for file_name in X_train:
        f.write(file_name + '\n')

with open('url_lists/all_test.txt', 'w') as f:
    for file_name in X_test:
        f.write(file_name + '\n')

with open('url_lists/all_val.txt', 'w') as f:
    for file_name in X_val:
        f.write(file_name + '\n')
