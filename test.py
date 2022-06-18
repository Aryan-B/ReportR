
# import tweepy
import pymongo

# CONSUMER_KEY='gzQvSTImxHd45JpiKWmmSKKr7'
# CONSUMER_SECRET='DfnCsOYl6nZBxhzMyBsBJft4eICYpdGLzxHzc9JVTvRHx1wQSI'
# BEARER_TOKEN='AAAAAAAAAAAAAAAAAAAAAIlidwEAAAAA2R6oJU1A7gSSFpS1jWY7c7h9A8c%3D1He36wuiqCPfN400VyZFICHgF2jhTmvxlni6UAKOAoobrHDtm3'
# ACCESS_TOKEN='1537579747189739520-YFuyIjDDdFaiF3jMy3J6NYgPiY5ob8'
# ACCESS_TOKEN_SECRET='2Z9AdlddQcZpFqfAJgwhpIab3Z2Y2aONb2N6tez3IBJwz'

# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)

# id="https://twitter.com/DegreaseNeil/status/1537616241917034497".split('/')[-1]
# fetched=api.get_status(id)
# print(fetched.text)

client = pymongo.MongoClient("mongodb+srv://demo:test@cluster0.z1gqq09.mongodb.net/?retryWrites=true&w=majority")
db = client.test
dbname = client.get_database('sentiments')
collection_name = dbname["records"]
# collection_name.insert_one({"text": "This is a test", "report_count":0})

collection_name.update_one(
    {"id": "12345"},
    { '$inc': { 'count': 1 } },
    upsert=True
)
