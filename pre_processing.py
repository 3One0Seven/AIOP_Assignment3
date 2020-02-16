"""This code take a string of raw text as input
and produce an array of int as an output.
"""
import csv
import re
import json
import pandas as pd
from nltk.tokenize import TweetTokenizer



class PreProc:
    """Pre Processing class used to convert json file into index list"""
    DATA_DIR = "data/"
    TWEET_GLOVE_DIR = "glove.twitter.27B/glove.twitter.27B.25d.txt"

    def __init__(self, string, max_length_tweet=100, max_length_dictionary=100):
        self.max_length_tweet = max_length_tweet
        self.max_length_dictionary = max_length_dictionary
        self.index_dict = dict()
        self.main(string)

    def main(self, string):
        """Main method used to handle run through whole precedure"""
        data = self.read_json(string)
        data = self.clean_data(data)
        data = self.tokenize_text(data)

        self.generate_dict(self.TWEET_GLOVE_DIR)
        self.word_index = self.replace_token_with_index(data)
        self.word_index = self.pad_sequence(self.word_index)

    @staticmethod
    def read_json(string):
        """Read json text and return raw text"""
        data_raw = json.loads(string)
        return data_raw["text"]

    @staticmethod
    def clean_data(string):
        """Step 1 Clean Data"""
        string = re.sub(r'@\w* ', '', string)
        string = re.sub(r"http://[\w.]+", '', string)
        return string

    @staticmethod
    def tokenize_text(data):
        """Step 2 tokenize_text"""
        tknzr = TweetTokenizer()
        data_token = tknzr.tokenize(data)
        return data_token

    def generate_dict(self, tweet_glove_dir):
        """Step 3 replace_token_with_index"""
        data = pd.read_csv(self.DATA_DIR + tweet_glove_dir,
                           sep=" ", quoting=csv.QUOTE_NONE, header=None)
        for index, token in data[0].items():
            self.index_dict[token] = index

    def replace_token_with_index(self, data_token):
        """Convert text into index"""
        index = list(map(lambda x: self.index_dict[x], data_token))
        return index

    def pad_sequence(self, index):
        """Step 4 pad_sequence"""
        index = index+[0]*(self.max_length_tweet - len(index))
        return index

# Read_data
S = '{"text": "@my_handler here is my tweet http://www.columbia.com"}'
print(S)
# with open(data_dir+'text.json') as f:
    # data_raw = json.load(f)

# Main function
print(PreProc(S).word_index)
