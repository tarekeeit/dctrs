from flask import Flask
from flask import request
from nltk.tokenize import TweetTokenizer, sent_tokenize
import nltk

wrdtknzr = nltk.word_tokenize("Show me doctors near 20 km")
posTagging = nltk.pos_tag(wrdtknzr)
print(wrdtknzr)
print(posTagging)

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    query=request.args.get('query')
    tknzr = TweetTokenizer()
    tokenized=tknzr.tokenize(query)
    wrdtknzr=nltk.word_tokenize(query)
    posTagging=nltk.pos_tag(wrdtknzr)
    strpst = repr(posTagging) #converting list into sequence



    print(sent_tokenize(example_text))
    return strpst   #Just showing one value

if __name__ =="__main__":
    app.run(debug=True)

