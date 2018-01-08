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
[print(thing) for thing in random.sample(winlist, len(winlist))[0:48]]
slide = open('slide.html','w')
slide.write("""
<!doctype html>
<html lang=en>
<head>
<meta charset=utf-8>
<title>SMKmeetup Giveaway Winners!</title>
<link rel="stylesheet" href="raffle-style.css">
</head>
<body>
<h2>SMKmeetup Giveaway Winners</h2>
<ul class="multi-12">
""")
for i in random.sample(winlist, len(winlist))[0:48]:
    winner = i[:18] + (i[18:] and '...')
    slide.write("<li>"+winner+"</li>\n")
slide.write("""
</ul>
</body>
</html>
""")
slide.close()
