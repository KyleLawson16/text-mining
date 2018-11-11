import pickle
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Load data from a file (will be part of your data processing script)
with open('bitcoin_discussions.pickle','r') as input_file:
    bitcoin_discussions = pickle.load(input_file)


def get_relevant_submissions(submissions, month):
    return [ submission for submission in submissions if month in submission.title ]

def submission_dict(submissions, lower, upper):
    return {i.title[lower:upper]: i for i in submissions}

def score_comments(comments):
    scores = []
    for i in comments:
        try:
            score = SentimentIntensityAnalyzer().polarity_scores(i.body)
            scores.append(score)
        except:
            pass


    totals = { 'neg': 0, 'neu': 0, 'pos': 0, 'compound': 0, 'count': 0 }
    for i in scores:
        totals['neg'] += i['neg']
        totals['neu'] += i['neu']
        totals['pos'] += i['pos']
        totals['compound'] += i['compound']
        totals['count'] += 1

    final_score = {
        'neg': totals['neg'] / totals['count'],
        'neu': totals['neu'] / totals['count'],
        'pos': totals['pos'] / totals['count'],
        'compound': totals['compound'] / totals['count']
    }
    return final_score


def get_final_scores(dict, submissions, month):
    for key, val in submissions.items():
        score = score_comments(val.comments)
        dict['{} {}'.format(month, key)] = score
    return dict


def main():
    dec_discussions = submission_dict(get_relevant_submissions(bitcoin_discussions, 'December'), 27, 29)
    jan_discussions = submission_dict(get_relevant_submissions(bitcoin_discussions, 'January'), 26, 28)
    feb_discussions = submission_dict(get_relevant_submissions(bitcoin_discussions, 'February'), 27, 29)
    final_scores = {}
    final_scores = get_final_scores(final_scores, dec_discussions, 'December')
    final_scores = get_final_scores(final_scores, jan_discussions, 'January')
    final_scores = get_final_scores(final_scores, feb_discussions, 'February')
    print(final_scores)

    # Save Data
    with open('final_scores.pickle','w') as f:
        pickle.dump(final_scores,f)



if __name__ == '__main__':
    main()
