# twitjudge.py
#
# parses the tweet archive file and presents it tweet by tweet, allowing the
# user to generate a list of IDs to exclude from deletion.
#
# usage: savetwit.py /path/to/tweet.js exclusionsfile.txt
# the output is saved as keep.txt

# we need the following libraries:
from sys import argv
import json # to parse the file

# the user needs to tell us which files they want us to use. we'll open them
# later, but let's just get the filenames for now
srcfn = argv[1]
keepfn = argv[2]
retfn = argv[3]

tweetcount = 0
tweettotal = 0
keepcount = 0
killcount = 0

# functions

def ynprompt():
    ReplyValid = False
    while ReplyValid == False:
        reply = input("Does it spark joy? (y/n)")
        if reply == "y":
            ReplyValid = True
            return True
        if reply == "n":
            ReplyValid = True
            return False
        else:
            ReplyValid = False
            print("Please enter y or n.")
    print()

def keeptweet():
    global keepcount
    keepcount = keepcount + 1
    print("This tweet sparks joy. We'll keep it.")
    print(str(keepcount) + " tweets kept so far.\n")
    drawline(5,"- ")
    print("\n")
    keepfile.write("    " + "'" + idstr + "'" + ",\n")

def killtweet():
    global killcount
    killcount = killcount + 1
    print("This tweet doesn't inspire joy. We'll get rid of it.")
    print(str(killcount) + " tweets let go so far.")
    drawline(5,"- ")
    print("\n")
    shamefile.write(idstr + "\n")

def askuser():
    keep = ynprompt()
    if keep == True: keeptweet()
    else: killtweet()

def drawline(len,cha):
    for i in range (0,len):
        print(cha, end = "")
        i += 1

# execution

drawline(15,"=")
print("\n")

print("twitjudge.py by leland rolofson\n")

drawline(15,"=")
print("\n")

with open(srcfn,"r",encoding="utf-8") as sourcefile:

    # skipping the first 25 characters because we don't need them
    sourcefile.seek(25)

    # reads the file
    archive_data = sourcefile.read()
    json_data = json.loads(archive_data)

    for tweet in json_data:
        tweettotal += 1

    with open(keepfn,"a",encoding="utf-8") as keepfile, open(retfn,"a") as shamefile:

        for tweet in json_data:
            tweetcount += 1
            print(str(tweetcount) + " of " + str(tweettotal) + "\n")
            # we'll use these to handle the relevant parts of the tweet
            created_date = tweet["created_at"]
            text = tweet["full_text"]
            idstr = tweet["id_str"]
            favcount = tweet["favorite_count"]

            # prints the tweet along with the date and the time
            print("On " + "\x1b[2;30;47m" + created_date + "\x1b[37;0;0m you tweeted:")
            print()
            print('"' + text + '"')
            if (int(favcount) > 0):
                if int(favcount) == 1:
                    peopleform = " person "
                if int(favcount) > 1:
                    peopleform = " people "
                print("\n❤️ " + favcount + peopleform + "liked it.\n")
            else:
                print("</3")
            askuser()

print("Considered " + str(tweetcount) + " tweets.")
print("Decided to keep " + str(keepcount) + " of them.")
print("Let go of " + str(killcount) + " of them.")
print()
print("8",end="")
drawline(10,"=")
print("D",end="")
drawline(5,"~")
