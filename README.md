# google-protobuf
distributed systems class exercises  
> use of google [ptotocol buffers](https://developers.google.com/protocol-buffers/?hl=es-419) to solve several tasks specified by the teacher - [uclm](https://www.uclm.es/) computer science  

## installation
### task1
**protobuf compiler** available in all major distributions and the one for python3 in my case
```
sudo apt-get install protobuf-compiler python3-protobuf
```
it can also be installed from the [official googles' repository](https://github.com/protocolbuffers/protobuf)    
in ordet to generate the stubs from a .proto file we use
```
protoc -I . --python_out=path file.proto
```
### task2
[**gRPC**](https://grpc.io/) remote procedure call system initially developed at Google
```
pip3 install grpcio grpcio-tools
```
