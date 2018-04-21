from .models import Status
from django_pandas.io import read_frame
import pandas as pd
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
import string
import nltk
import re
from ppcwrapper.models import Bill

''' I think I neeed to shelve this for right now
good ideas for another time but I need to actually launch this thing
it's only version 1.0 anyway'''
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', '...']
 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
bill_subjects = list(Bill.get_primary_subjects())
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

def make_df(congress_member_id):
    qs = Status.get_congress_member_statuses(congress_member_id)
    return read_frame(qs)

def count_term_frequencies(df):
    count_all = Counter()
    for i in df.text:
        terms_stop = [term for term in preprocess(i) if term not in stop and term in bill_subjects]
        count_all.update(terms_stop)
    return count_all

def term_co_occurennces(df):
    pass

def sentiment_analysis(df):
    # I am hoping I can apply this to bills so that I can analyze the text of
    # a bill and determine whether it is "for" or "against" a topic and
    # than I can make assumptions about a person when they vote "yay" or "nay"
    # for that topic. That way a pattern can be shown
    pass

df = make_df('B001230')
print(count_term_frequencies(df))