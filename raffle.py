import csv
import random
import sys
from random import shuffle
winlist = []
with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        username =  row['What username do you go by online?']
        if row['What username do you go by online?'] == '-':
            username = row['Ticket First Name']
        winlist.append(row['Number'] + " " +  username)
[print(thing) for thing in random.sample(winlist, len(winlist))[0:30]]
slide = open('slide.html','w')
slide.write("""
 <!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>SMK Winter Meetup 2018 Winners!</title>
    <h1>And the winners are...</h1>
  </head>
  <body>
""")
for i in random.sample(winlist, len(winlist))[0:30]:
    slide.write("<p>"+i+"</p>\n")
slide.write("""
  </body>
</html>
""")
slide.close()
