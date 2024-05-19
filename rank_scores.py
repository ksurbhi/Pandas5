import pandas as pd

# using pyhton solution
def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    score_list = []
    if len(scores) == 0:
        return pd.DataFrame([], columns = ['score','rank'])
    for i in range(len(scores)):
        score = scores['score'][i]
        score_list.append(score)
    score_list.sort(reverse = True)
    rnk = 1
    final_result  = [[score_list[0], rnk]]
    for i in range(1, len(score_list)):
        if score_list[i] == score_list[i-1]:
            final_result.append([score_list[i], rnk])
        else:
            rnk = rnk +1
            final_result.append([score_list[i], rnk])
    df = pd.DataFrame(final_result, columns = ['score','rank'])
    return df

# Using Pandas Solution
def order_scores(scores: pd.DataFrame) -> pd.DataFrame:   
    scores['rank'] = scores['score'].rank(method = 'dense', ascending = False)
    return scores.sort_values('rank')[['score','rank']]
