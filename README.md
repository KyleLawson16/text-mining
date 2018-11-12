# Text Mining Project

### MIS3640 - Problem Solving & Software Design

## Table of Contents:

- [Project Overview](#Overview)
- [Implementation](#Implementation)
- [Results](#Results)
- [Reflection](#Reflection)

## Packages Used:

- [config](https://pypi.org/project/config/)
- [matplotlib](https://matplotlib.org/)
- [nltk](https://www.nltk.org/)
- [numpy](http://www.numpy.org/)
- [pickle](https://docs.python.org/3/library/pickle.html)
- [praw](https://praw.readthedocs.io/en/latest/)

## <a name="Project">Project Overview:</a>

The goal of this project was to analyze the change in sentiment of Reddit's Bitcoin Daily Discussion Threads throughout the months of December 2017, January 2018, and February 2018. These three months were when Bitcoin drastically increased and decreased in value, so I was expecting to see a strong correlation between sentiment and price. In order to test this theory I decided to gather the top 100 comments on every Daily Discussion thread and run them through a sentiment analysis, ultimately plotting the results on bar charts.

## <a name="Implementation">Implementation:</a>

I broke up this project into three files that each served their own purpose. The first file, reddit_miner.py, was used to pull data from reddit and store it using pickle. The difficult part was pulling the correct submissions from Reddit's Bitcoin subreddit. However, using praw's search feature I was able to search for 'Daily Discussion, December' to pull all of the December discussions, and so on for each month.

With a list of submission objects stored using pickle I then created a file, reddit_analyzer.py, which was used to reformat the submission data and run a sentiment analysis. First, I filtered out a few irrelevant submissions and then converted the list to a dictionary for each month that included a key for each day of the month and a value of the associated submission for that day. With these dictionaries, I was then able to analyze all of the comments for each Daily Discussion using nltk and average their sentiment scores. This process ran for a few minutes, but once finished I stored the data using pickle once again.

In the final file, reddit_displayer.py, I took the sentiment scores for each day and visualized them on bar charts for each month. Building the charts was made easy by matplotlib, but I had to make 12 total, positive, negative, neutral, and compound for each month.

## <a name="Results">Results:</a>

### Positive Sentiment

![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/December_pos.png)
![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/January_pos.png)
![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/February_pos.png)

### Negative Sentiment

![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/December_neg.png)
![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/January_neg.png)
![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/February_neg.png)

### Neutral Sentiment

![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/December_neu.png)
![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/January_neu.png)
![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/February_neu.png)

### Compound Sentiment

![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/December_comp.png)
![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/January_comp.png)
![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/February_comp.png)
