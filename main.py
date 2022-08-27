import tweepy
import requests
import random
from classes import Node

# Variables that contains the credentials to access Twitter API
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token= ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET
bearer_token = BARER_TOKEN


client = tweepy.Client( bearer_token=bearer_token, 
                        consumer_key=consumer_key, 
                        consumer_secret=consumer_secret, 
                        access_token=access_token, 
                        access_token_secret=access_token_secret, 
                        return_type = requests.Response,
                        wait_on_rate_limit=True)

# Define query
query = 'from:elonmusk -is:retweet'

# get max. 10 tweets
tweets = client.search_recent_tweets(query=query, 
                                    tweet_fields=['author_id', 'created_at'],
                                     max_results=10)

tweets_dict = tweets.json()
tweets_data = tweets_dict['data']
node_lookup = {}
root_nodes = {}

# for each entry in the tweet data
for entry in tweets_data:

	# split the sentence into words
	words = entry['text'].split()
	if words:
		rootie = Node(words[0])
		node_lookup[words[0]] = rootie
		root_nodes[words[0]] = rootie
	# for every word besides the last, do something
	for i in range(len(words)-1):
		# if this is the last word in the sentence, either continue if we already added the node or add the node
		if i == len(words) - 1:
			if words[i] in node_lookup.keys():
				continue
			else:
				node_lookup[words[i]] = Node(words[i])

		# if this word is already found, add the next word to its next_nodes, else, create a new node with the next node as its next
		if words[i] in node_lookup.keys():
			# if the next word is found, just add it to update_nodes

			node_lookup[words[i]].look_up()
			if words[i+1] in node_lookup.keys():
				# get the node at words[i] from our dictionary, and update its next nodes with the node from our dictionary
				node_lookup[words[i]].update_node(node_lookup[words[i+1]])
			else:
				nextie = Node(words[i+1])
				node_lookup[words[i+1]] = nextie
				node_lookup[words[i]].update_node(nextie)
		else:
			this_node = Node(words[i+1])
			node_lookup[words[i]] = this_node
			if words[i+1] in node_lookup.keys():
				# get the node at words[i] from our dictionary, and update its next nodes with the node from our dictionary
				node_lookup[words[i]].update_node(node_lookup[words[i+1]])
			else:
				nextie = Node(words[i+1])
				node_lookup[words[i+1]] = nextie
				node_lookup[words[i]].update_node(nextie)





root_node = random.choice(list(root_nodes.values()))
user = root_node
LENGTH_OF_SENTENCE = 5
sentence = ""
for i in range(LENGTH_OF_SENTENCE):
	sentence = sentence + " " + user.val
	next_node = user.rand_node()
	if next_node:
		user = next_node
	else:
		user = random.choice(list(node_lookup.values()))



print("THIS IS THE SENTENCE GENERATED: ")
print(sentence)








