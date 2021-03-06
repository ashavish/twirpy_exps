## Twirpy installation experiments

### A sentiment predictor for text. The response is 'POS' or 'NEG' and a probability.The client sends the text along with the type of model that needs to be used.

The client server communication is done using Twirpy,Twirp and Protoc. It is tested with the server running on python3 and using both Python3 client and a Go client.


Create 'models' folder under twirpy_python

[Download models from here](https://drive.google.com/file/d/18CP2gUiYXyRF3r2jhe70ESC5_1R2Q9p6/view?usp=sharing)

And place all the models in the 'models' folder 


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

```
mkdir ~/go
mkdir ~/go/bin
```

```
export GOPATH=$HOME
export GOBIN=$GOPATH/bin
```


3.Install protoc compiler

```
sudo apt-get install protobuf-compiler
```

4. Get the twirpy plugin

```
go get -u github.com/verloop/twirpy/protoc-gen-twirpy
```
or 

```
git clone https://github.com/verloop/twirpy
cd twirpy/protoc-gen-twirpy
go install 
```

If it gives a permission error, check the GOPATH and GOBIN environment variables. They should be configured correctly.

5.Install Twirp

```
pip3 install twirp
```

6.Install Uvicorn - ASGI server 

```
pip3 install uvicorn
```

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

We should get a proper response


## For Go Client

1. Get the plugins

```
go get -u github.com/twitchtv/twirp/protoc-gen-twirp
go get -u github.com/golang/protobuf/protoc-gen-go
```

```
export PATH=$PATH:$GOPATH/bin
```

2. Run protoc plugin for go

```
protoc --proto_path=$GOPATH/src:. --twirp_out=./generated --go_out=./generated textprediction.proto  --plugin=protoc-gen-twirp=$GOBIN/protoc-gen-twirp --plugin=protoc-gen-go=$GOBIN/protoc-gen-go
```

If the command doesnt run check the $GOBIN path. (ie ~/go/bin) . The protoc file should be present.


3. All Go packages should be under GOPATH / src ie. ~/go/src

For us to use example package, we create a folder called example under ~/go/src and put the two files - textprediction.pb.go and textprediction.twirp.go under example


4. Create the client.go as given 

and run it using

```
go run client.go
```

We should get a proper response


## Dockerfile

Build the docker image 

```
docker build ./ -t twirpy_exps
```

List images
```
docker image ls
```

Run it and check
```
docker run -it twirpy_exps
```

Deploy it as a service

```
docker run -p 3000:3000 twirpy_exps
```


## Deploying on Kubernetes using Google Cloud 

Clone the project on google cloud shell

```
git clone https://github.com/ashavish/twirpy_exps
```

Dont forget to download the models and place it under the model folder

Build the docker image

```
docker build -t gcr.io/<GCP_PROJECT_NAME>/twirpy_exps:v1 ./
```
Check the images
```
docker images
```

Run the docker image
```
docker run -p 3000:3000 gcr.io/<GCP_PROJECT_NAME>/twirpy_exps:v1
```

We push to docker container registries for accessing it while creating the Kubernetes Cluster

```
gcloud auth configure-docker
```

```
docker push gcr.io/<GCP_PROJECT_NAME>/twirpy_exps
```

```
gcloud container clusters create twirpy-cluster --zone us-central1-c
```

See the created cluster under Kubernetes Engine->Clusters on Google cloud console

```
kubectl create deployment twirpy-cluster --image=gcr.io/<GCP_PROJECT_NAME>/twirpy_exps:v1
```

```
kubectl get deploy
```

Expose the Kubernetes cluster to the external world
```
kubectl expose deployment twirpy-cluster --name=twirpy-service --type=LoadBalancer --port 3000 --target-port 3000
```

Check the details of the service
```
kubectl get services twirpy-service
```

Get the external ip and change it within the client.py file

And try running python3 client.py

You should get a proper response !
