import pandas as pd
import json

d = json.loads(open("farmers-protest-tweets-2021-03-5.json").read())
df = pd.json_normalize(d)

def most_retweeted():
    print('Top Tweets')