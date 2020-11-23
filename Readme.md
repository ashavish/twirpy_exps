## Twirpy installation experiments

### A sentiment predictor for text and gives response of 'POS' or 'NEG' and a probability.The client sends the text along with the type of model that needs to be used.

The client server communication using Twirpy,Twirp and Protoc is tested with the server running on python3 and using both Python3 client and a Go client.


Create a virtual environment

1. Install Golang from https://golang.org/doc/install?download=go1.15.5.linux-amd64.tar.gz
Follow all instructions

Check out the go version by typing
```
go version
```

Check the location of installation
```
which go
```

2. Create GO environment variables

mkdir ~/go
mkdir ~/go/bin

export GOPATH=$HOME
export GOBIN=$GOPATH/bin



3.Install protoc compiler

```
sudo apt-get install protobuf-compiler
```

4. Get the twirpy plugin

go get -u github.com/verloop/twirpy/protoc-gen-twirpy

or 

git clone https://github.com/verloop/twirpy
Navigate to twirpy/protoc-gen-twirpy and run 

```
go install 
```

If it gives a permission error, check the GOPATH and GOBIN environment variables. They should be configured correctly.

5.Install Twirp

pip3 install twirp

6.Install Uvicorn - ASGI server 

pip3 install uvicorn


7. Navigate to twirpy/example

```
protoc --python_out=./generated --twirpy_out=./generated textprediction.proto
```

if it gives this error

```
--twirpy_out: protoc-gen-twirpy: Plugin failed with status code 1.
```

Then include this 

```
protoc --python_out=./generated --twirpy_out=./generated textprediction.proto --plugin=protoc-gen-twirpy=$GOBIN/protoc-gen-twirpy
```

8.Once its done you should see the below files in the output directories

textprediction_pb2.py
textprediction_twirp.py

using the specification in textprediction.proto

9. Create server.py and client.py as given in the example folder

10. Run the server by running

```
uvicorn server:app --port=3000
```

11. In another terminal run the client

```
python3 client.py
```

We should see a proper response


## For Go Client

1. Get the plugins

go get -u github.com/twitchtv/twirp/protoc-gen-twirp
go get -u github.com/golang/protobuf/protoc-gen-go

export PATH=$PATH:$GOPATH/bin

2. Run protoc plugin for go

protoc --proto_path=$GOPATH/src:. --twirp_out=./generated --go_out=./generated textprediction.proto  --plugin=protoc-gen-twirp=$GOBIN/protoc-gen-twirp --plugin=protoc-gen-go=$GOBIN/protoc-gen-go

If the command doesnt run check the $GOBIN path. (ie ~/go/bin) . The protoc file should be present.


3. All Go packages should be under GOPATH / src ie. ~/go/src

For us to use example package, we create a folder called example under ~/go/src and put the two files - textprediction.pb.go and textprediction.twirp.go under example


4. Create the client.go as given 

and run it using

```
go run client.go
```

We should see a proper response
