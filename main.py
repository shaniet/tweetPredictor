import tweepy
import requests
import random
from classes import Node

# Variables that contains the credentials to access Twitter API
consumer_key = 'jtnq7r8NH4B9fxjpjtOu4mZl1'
consumer_secret = 'EMDzjKC6hsImKCLrlKhYswHPGky6VTxMfZaPjZ45iVNSfa3An7'
access_token= '984110343218712576-3A6UjAtd4oGyxxyF0SCeXJt923Y2Nn1'
access_token_secret = 'D4cPbLCJjGByBcKkDqNYrACP0DEVchCSB7D4l13EJHoSl'
bearer_token = "AAAAAAAAAAAAAAAAAAAAALpRaAEAAAAAzh1DP%2Fl8Ugr19nVjjzJutY51zUo%3DATDOjFuYTw1e2ay5ltgtm3VZzJB9Ii9vLNGGct1mqd31klvcnA"

# bearer token: AAAAAAAAAAAAAAAAAAAAALpRaAEAAAAAJz0Zi8RMYPn4hqOVA20mirLDFgs%3D9bGeDNja9hzIXnM19w0puDYQFIEXfciJvrbePhlKKBxTW9hsnm

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

print(tweets)
tweets_dict = tweets.json()
tweets_data = tweets_dict['data']
node_lookup = {}
root_nodes = {}

# for each entry in the tweet data
for entry in tweets_data:
	print(entry['text'])

	# split the sentence into words
	words = entry['text'].split()
	if words:
		rootie = Node(words[0])
		node_lookup[words[0]] = rootie
		root_nodes[words[0]] = rootie
	# for every word besides the last, do something
	for i in range(len(words)-1):
		print("PROCESSING: ", words[i])
		# if this is the last word in the sentence, either continue if we already added the node or add the node
		if i == len(words) - 1:
			print('this should be the last word above ^')
			if words[i] in node_lookup.keys():
				continue
			else:
				node_lookup[words[i]] = Node(words[i])

		# if this word is already found, add the next word to its next_nodes, else, create a new node with the next node as its next
		if words[i] in node_lookup.keys():
			# if the next word is found, just add it to update_nodes

			print("WORDS[i] IS ALREADY IN NODE_LOOKUP. HERE'S ITS PRINT DATA")
			node_lookup[words[i]].print_data()
			if words[i+1] in node_lookup.keys():
				print('in the first if')
				# confusing, basically, get the node at words[i] from our dictionary, and update its next nodes with the node from our dictionary
				node_lookup[words[i]].update_node(node_lookup[words[i+1]])
			else:
				print("in the first else")
				nextie = Node(words[i+1])
				node_lookup[words[i+1]] = nextie
				node_lookup[words[i]].update_node(nextie)
		else:
			this_node = Node(words[i+1])
			node_lookup[words[i]] = this_node
			if words[i+1] in node_lookup.keys():
				print('in the second if')
				# confusing, basically, get the node at words[i] from our dictionary, and update its next nodes with the node from our dictionary
				node_lookup[words[i]].update_node(node_lookup[words[i+1]])
			else:
				print('in the second else')
				nextie = Node(words[i+1])
				node_lookup[words[i+1]] = nextie
				node_lookup[words[i]].update_node(nextie)

print(node_lookup)
# print(tweets_data)


# HERE GOES NOTHING MEOWWWW
root_node = random.choice(list(root_nodes.values()))
user = root_node
LENGTH_OF_SENTENCE = 5
sentence = ""
for i in range(LENGTH_OF_SENTENCE):
	sentence = sentence + " " + user.val
	# user.print_data()
	next_node = user.rand_node()
	if next_node:
		user = next_node
	else:
		user = random.choice(list(node_lookup.values()))

print("THIS IS THE SENTENCE GENERATED: ")
print(sentence)








