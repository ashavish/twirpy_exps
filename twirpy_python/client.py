from twirp.context import Context
from twirp.exceptions import TwirpServerException
from generated import textprediction_twirp, textprediction_pb2

client = textprediction_twirp.SentimentPredictorClient("http://localhost:3000")

try:
    response = client.PredictSentiment(
    	ctx=Context(), request=textprediction_pb2.Content(text="its a lovely movie. i really liked it",model="CV_LOGISTIC"), server_path_prefix="/twirpy")
    print(response)
except TwirpServerException as e:
    print(e.code, e.message, e.meta, e.to_dict())
