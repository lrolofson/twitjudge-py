# twitjudge.py
reads your twitter archive tweet-by-tweet, asks if you want to keep them, and dumps the id strings into a whitelist file for your tweet deleter. written in python 3.7.

##usage
savetwit.py is intended to be run from inside your twitter archive folder, but you can run it from anywhere you wish, i'm not your boss

`python savetwit.py /path/to/tweet.js /path/to/whitelist.txt`

a list of ids for deleted tweets is saved to bodied.txt in the directory the script is run from.
