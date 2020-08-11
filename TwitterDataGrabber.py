import tweepy
import time
import sys
import twitterAPIkeys as twitKeys
import pandas as pd


#creating path to get API Keys


# *********** UPDATE KEYS WHEN USING AND CLEAR WHEN DONE *********************
CONSUMER_KEY = twitKeys.CONSUMER_KEY
CONSUMER_SECRET = twitKeys.CONSUMER_SECRET
ACCESS_KEY = twitKeys.ACCESS_KEY
ACCESS_SECRET = twitKeys.ACCESS_SECRET
# *********** UPDATE KEYS WHEN USING AND CLEAR WHEN DONE *********************

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

df = pd.read_csv('Partially_cleaned_2019_set.csv')
checkForDups = {}
df['Player'] = df['Player'].astype(str)



twitterDf = pd.DataFrame(columns=['player_name', 'screen_name', 'followers_count', 'statuses_count'])

previndex = 0

for index, row in df.iterrows():
    if(index != 0 and (index % 20 == 0)):
        s = "Retrieved players {} to {}...".format(previndex, index)
        print(s)
        time.sleep(3)
        previndex = index
    if((row['Player'] not in checkForDups) and (row['G'] > 10)):
        checkForDups[row['Player']] = 1
        try:
            player = api.search_users(str(row['Player']))
            if(len(player) == 0):
                print(row['Player'])
            if(len(player) > 0 and player[0].verified):
                twitterDf.loc[index] = [row['Player'], player[0].screen_name, player[0].followers_count, player[0].statuses_count]
        except OSError as err:
            print("ERROR: ", err)
        except:
            print("Location of error: index: {} , name: {}".format(index, row['Player']))


print(twitterDf.head(n = 10))
twitterDf.to_csv(r'twitterData.csv', index = False, header = True)
#print(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)


#TODO: store data in CSV file
