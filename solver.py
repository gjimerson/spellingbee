from calendar import c
import csv
from tkinter import W
from turtle import pos
from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      resultArray = request.form["letters"].split(',')
      center = resultArray[0]
      
      words_file = open('words.txt', 'r')

      words = []
      for word in words_file:
        words.append(str(word).lower()[:-1])
      alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                'u', 'v', 'w', 'x', 'y', 'z']
    
      forbidden = [l for l in alphabet if l not in resultArray]
      possible = []
    
      for word in words:
        if center in word:
            if word not in possible:
                if len(word) > 3:
                    if any(l in forbidden for l in word) == False:
                        possible.append(word)
      finalReturn = { "solved" : possible}

      return render_template("result.html",result = finalReturn)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5151)



def solve_spelling_bee(letters_list, center_letter):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                'u', 'v', 'w', 'x', 'y', 'z']
    
    forbidden = [l for l in alphabet if l not in letters_list]
    possible = []
    
    for word in words:
        if center_letter in word:
            if word not in possible:
                if len(word) > 3:
                    if any(l in forbidden for l in word) == False:
                        possible.append(word)
                        