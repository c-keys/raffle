import csv
import random
import argparse
from random import shuffle
parser = argparse.ArgumentParser()
parser.add_argument("csv",help = "the location of the csv input")
parser.add_argument("totalWinners", type=int, help="total number of selected winners")
args = parser.parse_args()
winlist = []
csvrow = open(args.csv)
totalWinners = args.totalWinners
with open(args.csv) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        username =  row['What username do you go by online?']
        if row['What username do you go by online?'] == '-':
            username = row['Ticket First Name']
        winlist.append(row['Number'] + " " +  username)
[print(thing) for thing in random.sample(winlist, len(winlist))[0:totalWinners]]
slide = open('winners.html','w')
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
for i in random.sample(winlist, len(winlist))[0:totalWinners]:
    winner = i[:12] + (i[12:] and '...')
    slide.write("<li>"+winner+"</li>\n")
slide.write("""
</ul>
</body>
</html>
""")
slide.close()
