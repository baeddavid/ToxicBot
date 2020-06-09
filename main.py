import discord
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator

client = discord.Client()
analyzer = SentimentIntensityAnalyzer()
translator = Translator()

def sentiment_analyzer_scores(text):
	trans = translator.translate(text).text
	score = analyzer.polarity_scores(trans)
	lb = score['compound']
	if lb > 0.5:
		return 'simpy ' + str(lb)
	elif (lb >= 0.05) and (lb < 0.5):
		return 'wholesome ' + str(lb)
	elif(lb > -0.05) and (lb < 0.05):
		return 'okay I guess ' + str(lb)
	elif lb < 0.05:
		return 'toxic and problematic. Check yourself ' + str(lb)
	else:
		return 'toady ' + str(lb)
@client.event
async def on_ready():
	print('We haev loggen in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith("!analyze"):
		sentiment = sentiment_analyzer_scores(message.content)
		print('sentiment: ' + str(sentiment))
		await message.channel.send('Your message was ' + str(sentiment))

client.run('key')