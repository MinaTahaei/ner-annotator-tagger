import nltk 
import json 
import redis 
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
        os.mkdir('../InputFiles/%s' % (name))
    except:
        print('none')
    f = open('../InputFiles/%s/%s.json' % (name, fname), 'w')
    json.dump(request.json, f)
    f.close()
    with open("../database.txt", 'a') as myFile:
        myFile.write(fname + '.txt\n')
    return "True"


@app.route("/files", methods=["GET"])
@cross_origin()
def files():
    used = []
    def sor(x):
        first = x.find('_')+1
        second = x[first:].find('_')+first
        return int(x[first:second])
    def sor_2(x):
        index = x.find('.')
        name = x[0:index]
        try:
            num = int(name)
        except:
            num = int(x[0:index-1])
        return num
    r = redis.Redis()
    try:
        with open("../database.txt", "r") as myFile:
            used = myFile.read().splitlines()
    except:
        pass
    files_names = []
    #dic = {}
    #list = sorted(os.listdir('../segFiles'))
    #for item in list:
    files = sorted(os.listdir('../segFilesOnServer'))
    for fileItem in files:
        #dic[fileItem] = item
        if(fileItem not in used):
            files_names.append(fileItem)
    #r.hmset("FilesList",dic)
    files_names = sorted(files_names, key = sor_2)
    return jsonify(files_names)


@app.route("/files/<name>", methods=["GET"])
@cross_origin()
def fileData(name):
    #r = redis.Redis()
    #dic = r.hgetall("FilesList")
    #path = dic[name.encode('utf-8')].decode('utf-8')
    f = open('../segFilesOnServer/%s' % (name), 'r')
    data = f.read()
    f.close()
    return jsonify(data)
if __name__ == "__main__":
    app.run(port=5555, debug=True)
