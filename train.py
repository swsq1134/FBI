import lamini
from lamini import LaminiClassifier
lamini.api_key = "200b69251b27b0a53e622a68b4203b18a79b9cd8f1a94b526e35c41fa0447ab5"
# Create a new classifier
classifier = LaminiClassifier()

classes = { "XONE" : "Trade booking error occured" , "RED" : "Regulatory eligibilies not found", "RiskONE" : "Did not manage to compute Risk Indicators"}
classes["Effcom"] = "Template not found"
classes["RDWS"] = "EvalPayOff Error. The given key was not found in dictionary"
classes["Orchestrator"] = "Bad application ID"
classes["SGDocs"] = "SgDocs endpoint not responding"
classes["PricingView"] = "Market curves not found"
classes["KidWebsite"] = "Error 404: Page not found"

classifier.prompt_train(classes)

classifier.save(r"Probabilities\my_model.lamini")