"""
This program is used to generate an html file with a list of randomly-selected winners.
It can be used for giveaways, raffles, etc. so long as the input csv is properly
formatted (for now).

Todo:
    * Add args to select a specified column.
    * Improve docstrings. Some of the phrasing used in the docstrings are...bad.
    * Write a readme for easier usage.

"""
import csv
import random
import argparse
def gen_list(argcsv):
    """
    This function generates the list of possible winners to be passed into html_writer().

    Args:
        argcsv - csv file from parse_args() to read and pull the list of possible winners from
    Returns:
        inputlist - the list of possible winners. It takes in the ticketholder's
        username and ticketnumber and appends them before inserting them into
        winlist to be passed to html_writer()

    """
    banned_tix = ['CORE', 'Vendor Ticket', 'SPU Dorm Room - Friday and Saturday', 'SPU Dorm Room - Saturday ONLY',
                  'Soldering Workshop: Fourier (BYOS) 10am-11:30am', 'Soldering Workshop: Fourier 10am-11:30am',
                  'Soldering Workshop: 4x4 Handwire 1pm-3pm']

    inputlist = []
    with open(argcsv) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            username = row['What username do you go by online?']
            if row['What username do you go by online?'] == '-':
                username = "{} {}.".format(row['Ticket First Name'], row['Ticket Last Name'][0:1])
            num = row['Number']
            if row['Ticket'] not in banned_tix:
                inputlist.append({'number':num,'username':username})
    return inputlist
def html_writer(inputlist, total_winners, csvout, htmlout):
    """
    This function writes the html file to display the winners.

    Args
    inputlist - full list of entrants
        total_winners - total number of specified winners taken from command line args

    Returns:
        None. Writes an html file.

    """
    with open(htmlout, 'w') as slide:
        slide.write(
            '<!doctype html>\n'
            '<html lang=en>\n'
            '<head>\n'
            '<meta charset=utf-8>\n'
            '<title>SMKmeetup Giveaway Winners!</title>\n'
            '<link rel="stylesheet" href="raffle-style.css">\n'
            '</head>\n'
            '<body>\n'
            '<h2>SMKmeetup Giveaway Winners</h2>\n'
            '<ul class="multi-12">\n'
        )
        for winner in random.sample(inputlist, total_winners):
            slide.write("<li>{} {}</li>\n".format(winner['number'], winner['username']))
            inputlist.pop(inputlist.index(winner))
        slide.write(
            '</ul>\n'
            '</body>\n'
            '</html>\n'
        )
        with open(csvout, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['number','username'])
            writer.writerow({'number': 'Number', 'username': 'What username do you go by online?'})
            for loser in inputlist:
                writer.writerow({'number': loser['number'], 'username': loser['username']})

def parse_args():
    """
    This function parses the arguments from the command line.

    Args:
        None

    Returns:
        args object to be passed to other functions

    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', "--csvin", help="the location of the csv input",required=True)
    parser.add_argument('-w', "--total_winners", type=int, help="total number of selected winners",required=True)
    parser.add_argument('-o', "--csvout",  help="csv output file",required=True)
    parser.add_argument('-p', "--htmlout", help="html output file",required=True)
    return parser.parse_args()

def main():
    """
    This function calls all the necessary functions needed for the program to run.
    """
    args = parse_args()
    html_writer(gen_list(args.csvin), args.total_winners, args.csvout, args.htmlout)
if __name__ == "__main__":
    main()
