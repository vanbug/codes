import feedparser
def facefeed():
	FACEBOOKFEED="http://www.facebook.com/feeds/notifications.php?id=1442653315&viewer=1442653315&key=471db49804&format=rss20" 
	feeds=feedparser.parse(FACEBOOKFEED)
	t=len(feeds['entries']) #Total number of feeds
	f=t-1 					#Practical feed number
	#print feeds['feed']['title'] # Prints 'Sukhdeep Singh's Facebook Notifications'
	#print feeds.feed.title		  # Prints 'Sukhdeep Singh's Facebook Notifications'
	#print feeds.feed.subtitle	  # Prints 'Sukhdeep Singh's Facebook Notifications'
	#print feeds.feed.link		  # Prints http://www.facebook.com/notifications.php
	#print feeds['entries'][t-1]['title'] # Total Feed Number
	#print e=feeds.entries[i] #Prints the url of the receiver receiving action and the corresponding action, i is a increasing number
	for i in range(0,f):
		e=feeds.entries[i] #Prints the url of the receiver receiving action and the corresponding action.
		print e.link
		#print e.links[0].rel  #Prints alternate
		#print e.links[0].href #Prints the urls
		#print e.updated_parsed #Prints the time of feed.



