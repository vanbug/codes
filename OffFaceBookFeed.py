## Draft code for facelet

# Importing modules
import feedparser,re

# Pattern match for extracting sender (X) and receiver (Y)
# Parsing facebook feed via feedparser
#http://www.facebook.com/feeds/notifications.php?id=1257268369&viewer=1257268369&key=7f1afbf543&format=rss20 : Jelmer's Feed
#http://www.facebook.com/feeds/notifications.php?id=529438568&viewer=529438568&key=b8c11d0c44&format=rss20   : Mithu's Feed
#http://www.facebook.com/feeds/notifications.php?id=1442653315&viewer=1442653315&key=471db49804&format=rss20 : My Feed
FACEBOOKFEED="http://www.facebook.com/feeds/notifications.php?id=1442653315&viewer=1442653315&key=471db49804&format=rss20" 
feeds=feedparser.parse(FACEBOOKFEED)

# Declaring Variables
#MAXCOUNT=25
feed=[] # creating empty erray for storing feeds
t=len(feeds['entries']) #Total number of feeds
f=t-1 					#Practical feed number

print "Total Number of Feeds :"+str(t)
# Printing the feeds in the terminal
for i in range(0,f) :
	feed.append(feeds['items'][i].title) # Appending all feeds in an array.
	e=feeds.entries[i]	#Fetching feed entries in a variable
	feedRawData=str(e.updated_parsed)	#Parsing the time of feed
	feedTimeParsed=re.match('.+year\=(\d+).+mon\=(\d+).+mday\=(\d+).+hour\=(\d+).+min\=(\d+).+sec\=(\d+)',feedRawData)
	fyear=feedTimeParsed.group(1)
	fmonth=feedTimeParsed.group(2)
	fday=feedTimeParsed.group(3)
	fhour=feedTimeParsed.group(4)
	fmin=feedTimeParsed.group(5)
	fsec=feedTimeParsed.group(6)
	feedDate=str(fday)+'.'+str(fmonth)+'.'+str(fyear)
	feedTime=str(fhour)+'.'+str(fmin)+'.'+str(fsec)
	senderName=re.match('\w+\s+\w+',feed[i])
	receiverName=re.match('\w+\s+\w+\s+\w+\s+\w+\s+(\w+\s+\w+)',feed[i])
	actionName=re.match('\w+\s+\w+\s+(\w+)',feed[i])
#	print feeds.updated_parsed
	print "Message Number "+str(i+1)
	print "Date of feed = "+feedDate
	print "Time of feed = "+feedTime
	print "Sender="+senderName.group()
	print "Receiver="+receiverName.group(1)
#	print feed[i]
#	if senderName.group()=="Abhijeet Bhatia":
#		print "yahoo"
	if actionName.group(1)=="commented":
		print "Action = A comment"+'\n'
	elif actionName.group(1)=="posted":
		print "Action = A post"+'\n'
	elif actionName.group(1)=="likes":
		print "Action = A linking"+'\n'



## Feed results
# XX' commented on your link
# XX' commented on his photo
# XX' commented on her photo
# XX' commented on your wall post. -- Posted to some body's else's wall
# XX' commented on your post.  -- Posted to own profile like results of an app.
# XX' commented on your status
# XX' commented on YY' photo
# XX' commented on YY' status
# XX' posted something on your wall.
# XX' likes your link
