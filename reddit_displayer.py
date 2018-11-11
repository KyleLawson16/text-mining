import pickle
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# Load data from a file (will be part of your data processing script)
with open('final_scores.pickle','r') as input_file:
    final_scores = pickle.load(input_file)

def create_date_list(month, num_days):
    dates = []
    for i in range(num_days + 1):
        if i < 10:
            dates.append('{} 0{}'.format(month, i))
        else:
            dates.append('{} {}'.format(month, i))
    return dates

december_dates = create_date_list('December', 31)
january_dates = create_date_list('January', 31)
february_dates = create_date_list('February', 29)



objects, sentiment = [], []
for i in december_dates:
    if i in final_scores.keys():
        objects.append('D {}'.format(i[9:]))
        sentiment.append(final_scores[i]['neu'])

y_pos = np.arange(len(objects))
plt.bar(y_pos, sentiment, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Sentiment')
plt.title('December Bitcoin Sentiment')
plt.show()



objects, sentiment = [], []
for i in january_dates:
    if i in final_scores.keys():
        objects.append('J {}'.format(i[8:]))
        sentiment.append(final_scores[i]['neu'])

y_pos = np.arange(len(objects))
plt.bar(y_pos, sentiment, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Sentiment')
plt.title('January Bitcoin Sentiment')
plt.show()



objects, sentiment = [], []
for i in february_dates:
    if i in final_scores.keys():
        objects.append('J {}'.format(i[9:]))
        sentiment.append(final_scores[i]['neu'])

y_pos = np.arange(len(objects))
plt.bar(y_pos, sentiment, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Sentiment')
plt.title('February Bitcoin Sentiment')
plt.show()
