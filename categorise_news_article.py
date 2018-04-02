import os
import sys
import shutil
import tqdm

def pywalker(source, destination):
    domains = ['articles/', 'www.gadgetsnow.com', 'mf-news', 'recipes.timesofindia.com', 'timesofindia.indiatimes.com']
    destination = destination.rstrip('/') + '/'
    for root, dirs, files in tqdm.tqdm(os.walk(source)):
        for file_ in files:
            if file_[0] == ".":         #To not consider hidden files
                # print file_
                continue

            # print( os.path.join(root, file_) )
            with open(os.path.join(root, file_),'r') as f:
                first_line = f.readline().strip()
                if (not any(domain in first_line for domain in domains)) or ("\\" in first_line):
                    continue
                # if first_line.split("=")[0] != "url" and "timesofindia.indiatimes.com/" in first_line[1]:
                # op = ""
                try:
                    if "recipes" in first_line:
                        # op = "Recipes " + first_line
                        cat = "recipe"
                    elif "mf-news" in first_line:
                        # op = "Finance mf-news " + first_line
                        cat = "finance"
                    elif "www.gadgetsnow.com" in first_line:
                        # op = "Tech " + first_line
                        cat = "tech"
                    elif "articles/" in first_line:
                        # op = "Finance articles " + first_line
                        cat = "finance"
                    else:
                        cat = first_line.split("indiatimes.com")[1].lstrip('/').split('/')[0]
                        # category = (os.path.join(root, file_)), cat
                        # op = cat + " " + first_line
                    folder = destination + cat + '/'
                    if not os.path.exists(folder):
                		os.mkdir(folder)
                    shutil.copy(os.path.join(root, file_), folder)
                except IndexError:              #Just in case
                    print "Not parsed", (os.path.join(root, file_)), first_line

pywalker(sys.argv[1], sys.argv[2])
