from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'GET': 
        return render_template('index.html', bool1 = False, bool2 = False)
    else:
        f = request.form
        s = f['sentence']
        x = s.splitlines()
        print(x)
        b1 = 1
        if f['ch'] == "prof":
            b1 = 0
        sen = TextBlob(s).sentiment
        pol = round(sen.polarity, 2)
        polc = round(sen.polarity + 1, 2)
        obj = round(sen.subjectivity, 2)
        res = ""
        if s.find("?") != -1:
            res = res + "I guess you are asking me a question, hmm but I can't answer it."
        elif pol >= 0.8:
            res = res + "You seem to be in a jolly mood."
        elif obj > 0.65 and pol <0.8 and pol > -0.8:
            res = res + "That's completely your veiw, right?"
        elif obj < 0.1:
            res = res + "Sorry I couldn't evaluate that, but it seems like a statement."
        elif pol < -0.8:
            res = res + "Doesn't sound good! I think you should gather yourself and move-on."
        elif pol < -0.5:
            res = res + "I think you must try to be Positive."
        elif len(res) == 0:
            res = res + "Sorry, I couldn't figure that out!"
        return render_template('index copy.html', pol = pol,polc = polc, obj = obj, res = res , bool1 = b1, bool2 = True)

if __name__ == '__main__':
   app.run(debug=True)
