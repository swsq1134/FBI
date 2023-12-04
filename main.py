import lamini
from lamini import LaminiClassifier
import GraphResolver
from flask import Flask, render_template,request,url_for
from flask_bootstrap import Bootstrap
from textblob import TextBlob,Word 
import random
import networkx
import time
import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
#lamini.api_key = "200b69251b27b0a53e622a68b4203b18a79b9cd8f1a94b526e35c41fa0447ab5"
lamini.api_key = "860b7378fb6c783394f3a6d7abea52ffcbb353da8b2b0c53f72159a1ae7a12f3" 
matplotlib.rcParams["figure.figsize"] = [7.50, 3.50]
matplotlib.rcParams["figure.autolayout"] = True
global graphx
global impactedapplications
def classify(text):
    classifier = LaminiClassifier()

    classifier = LaminiClassifier.load(r"Probabilities\my_model.lamini")

    #error = input("Enter the error encountered:")

    prediction = classifier.predict([text])[0]

    # Get the probabilities for each class
    #probabilities = classifier.predict_proba("booking error")

    print("Source of the error: %s" %prediction)
    print("\n")
    graphx = GraphResolver.Creategraph()
    impactedapplications = GraphResolver.GetImpactedApplications(prediction)
    impactedapplications.add(prediction)
    print("The impacted applications are:\n")
    for item in impactedapplications:
        print(item, end = "\n")
    return prediction, ", ".join(impactedapplications), text


app = Flask(__name__, template_folder = '')
Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/analyse',methods=['POST'])
def analyse():
	text = request.form['text']
	if request.method == 'POST':
		prediction, apps,  textx =  classify(text)

	return render_template('index.html', prediction = prediction, apps = apps, textx = textx)

@app.route('/graph',methods=['POST'])
def graph():
    networkx.draw(graphx)
    img = io.BytesIO() # file-like object for the image
    plt.savefig(img) # save the image to the stream
    img.seek(0) # writing moved the cursor to the end of the file, reset
    plt.clf() # clear pyplot

    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
	app.run(debug=True)


