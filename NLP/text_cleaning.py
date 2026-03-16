import contractions
import re
from string import punctuation

text = " I like to play  Games and paint pictures . , its very good ! "
def cleaning(text):
    #convert into lower case
    text = text.lower()
    # install library called contractions for expanding contractions
    text = contractions.fix(text)
    # remove punctuations
    #punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    text = re.sub('[%s]' % re.escape(punctuation), '', text)

    #remove extra spaces
    text = " ".join.text.split()
    return text





