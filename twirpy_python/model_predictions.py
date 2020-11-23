# Sentiment Prediction for Text

import pickle
import numpy as np
import re
import os

def clean_data(data):
    # Remove <br />
    data = data.replace("<br />","")
    # Change Numbers to XX
    data = re.sub('[0-9]', 'X', data)
    # Remove punctuations
    data = re.sub(r"[,.;@#?!&$/]+"," ",data)
    data = re.sub(r"[-'\"´]+","",data)
    data = data.replace("\'","")
    # lower case
    data = data.lower()
    return data

path = "./models"
class ModelPredict():   
    def load_models(self):
        # Load all the models
        self.subword_tokenizer = pickle.load(open(os.path.join(path,"subword_tokenizer.p"),"rb"))
        self.cv_vect = pickle.load(open(os.path.join(path,"cv_vect.p"),"rb"))
        self.tfidf_vect = pickle.load(open(os.path.join(path,"tfidf_vect.p"),"rb"))
        self.cv_model = pickle.load(open(os.path.join(path,"cv_model.p"),"rb"))
        self.tfidf_model = pickle.load(open(os.path.join(path,"tfidf_model.p"),"rb"))
        self.nbsvm_cv_model = pickle.load(open(os.path.join(path,"nbsvm_cv_model.p"),"rb"))
        self.nbsvm_tfidf_model = pickle.load(open(os.path.join(path,"nbsvm_tfidf_model.p"),"rb"))
        self.log_rat_cv = np.load(os.path.join(path,"log_rat_cv.npy"))
        self.log_rat_tfidf = np.load(os.path.join(path,"log_rat_tfidf.npy"))
        print("Loaded all models")      
    def predict_nbsvm_cv(self,text):        
        dtm_test = self.cv_vect.transform([text])
        y_prob = self.nbsvm_cv_model.predict_proba(dtm_test)
        y_pred = np.argmax(y_prob,axis=1)
        return y_pred[0],np.max(y_prob)
    def predict_nbsvm_tfidf(self,text):
        dtm_test = self.tfidf_vect.transform([text])
        y_prob = self.nbsvm_tfidf_model.predict_proba(dtm_test)
        y_pred = np.argmax(y_prob,axis=1)
        return y_pred[0],np.max(y_prob)
    def predict_cv_logistic(self,text):
        dtm_test = self.cv_vect.transform([text])
        y_prob = self.cv_model.predict_proba(dtm_test)
        y_pred = np.argmax(y_prob,axis=1)
        return y_pred[0],np.max(y_prob)
    def predict_tfidf_logistic(self,text):
        dtm_test = self.tfidf_vect.transform([text])
        y_prob = self.tfidf_model.predict_proba(dtm_test)
        y_pred = np.argmax(y_prob,axis=1)
        return y_pred[0],np.max(y_prob)
    def decode_sentiment(self,sentiment):
        return "POS" if sentiment == 1 else "NEG"
    def predict(self,text,model_type):
        text = clean_data(text)
        text = " ".join(self.subword_tokenizer.encode(str(text)).tokens)
        sentiment = -1
        probability = 0        
        if model_type == "NBSVM_CV":
            sentiment,probability = self.predict_nbsvm_cv(text)
        elif model_type == "NBSVM_TFIDF":
            sentiment,probability = self.predict_nbsvm_tfidf(text)
        elif model_type == "CV_LOGISTIC":
            sentiment,probability = self.predict_cv_logistic(text)
        elif model_type == "TFIDF_LOGISTIC":
            sentiment,probability = self.predict_tfidf_logistic(text)
        else:
            return None,None
        if sentiment != -1:
            sentiment = self.decode_sentiment(sentiment)
        return sentiment,probability


#modelpredict = ModelPredict()
#modelpredict.load_models()
#modelpredict.predict("This is 3236 a test.lovely movie","TFIDF_LOGISTIC")