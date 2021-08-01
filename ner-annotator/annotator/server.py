import nltk
import json
import os
from flask import Flask, request, jsonify
from flask_cors import cross_origin

from nltk.tokenize.treebank import TreebankWordTokenizer, TreebankWordDetokenizer

app = Flask(__name__)


@app.route("/tokenize", methods=["POST"])
@cross_origin()
def tokenize():
    text = request.json["text"]
    try:
        spans = list(TreebankWordTokenizer().span_tokenize(text))
    except LookupError:
        nltk.download('punkt')
        spans = list(TreebankWordTokenizer().span_tokenize(text))
    return {"tokens": [(s[0], s[1], text[s[0]:s[1]]) for s in spans]}


@app.route("/detokenize", methods=["POST"])
@cross_origin()
def detokenize():
    tokens = request.json["tokens"]
    return {"text": TreebankWordDetokenizer().detokenize(tokens)}

@app.route("/files/<fname>", methods=["POST"])
@cross_origin()
def save(fname):
    name = request.json["taggerName"]
    try:
        os.mkdir('./InputFiles/%s' % (name))
    except:
        print('none')
    f = open('./InputFiles/%s/%s.json' % (name,fname),'w')
    json.dump(request.json, f)
    f.close()
    return 'True'

@app.route("/files", methods=["GET"])
@cross_origin()
def files():
    files_names = []
    list = os.listdir('./Data')
    for item in list:
        files = os.listdir('./Data/%s' %(1))
        for fileItem in files:
            files_names.append(fileItem)
    return jsonify(files_names)

@app.route("/files/<name>", methods=["GET"])
@cross_origin()
def fileData(name):
    path = ''
    try: 
        int(name[4:6])
        path = name[4:6]
    except ValueError:
        path = int(name[4:5])
    # f = open('./Data/%s' % (name),'r')
    # data = f.read()
    # f.close()
    # return jsonify(data)   
    return 'salam'
    
if __name__ == "__main__":
    app.run(port=5555, debug=True)
