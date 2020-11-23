import random

from twirp.asgi import TwirpASGIApp
from twirp.exceptions import InvalidArgument
from generated import textprediction_twirp, textprediction_pb2
from model_predictions import ModelPredict

class SentimentPredictorService(object):    
    def __init__(self):
        self.model_predict = ModelPredict()
        self.model_predict.load_models()
    def PredictSentiment(self, context, content):
        if len(content.text.strip()) == 0:
            raise InvalidArgument(argument="text", error="Text is empty!")
        sentiment,probability = self.model_predict.predict(content.text,content.model)
        return textprediction_pb2.Sentiment(
            sentiment=sentiment,
            probability= probability
        )


service = textprediction_twirp.SentimentPredictorServer(
    service=SentimentPredictorService(), server_path_prefix="/twirpy")
app = TwirpASGIApp()
app.add_service(service)
