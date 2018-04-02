# AML-Project
How the preprocessing works:
1. Picks up category of the article through URL mentioned in the first line, makes directory for that category if not made already and copies the article in that folder.
2. After the categorisation is done, the bash script runs through all the category folders made and sees if the number of articles in that folder is less than 10K.
If so, it'll delete that folder as it's just not enough data to run our model on.

I found that, after doing this on our TOI dataset, 10 categories are left with almost every category having > 50K articles.

How to run?

Place both the scripts (preprocess.sh and categorise_news_article.py) files in the same folder.

$./preprocess.sh <Destination folder path eg ./Dataset/ > <Source folder i.e Dataset folder path eg./TOI/ >   
#Don't forget to put '/' at the end of path ;)

Try not to give invalid inputs, as I didn't make the script robust enough :D

Dependency:
1. Python2 should be installed on your machine.
2. Also install tqdm package: pip2 install tqdm
