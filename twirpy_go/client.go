package main

import (
    "context"
    "net/http"
    "os"
    "fmt"
    "example"
    "github.com/twitchtv/twirp"    
    // textprediction_pb "twirpy_go/example/textprediction.pb"
)

func main() {
    var (
        sentiment *example.Sentiment
        err error
    )    
    client := example.NewSentimentPredictorProtobufClient("http://localhost:3000", &http.Client{}, twirp.WithClientPathPrefix("/twirpy"))

    sentiment, err = client.PredictSentiment(context.Background(), &example.Content{Text:"its a lovely movie. i really liked it",Model:"CV_LOGISTIC"})
    if err != nil {
        fmt.Printf("oh no: %v", err)
        os.Exit(1)
    }
    fmt.Printf("%+v",sentiment)
}
