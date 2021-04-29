VERSION=0.2.0
sudo docker build . --tag iiiorg/zap-runner:$VERSION
sudo docker push iiiorg/zap-runner:$VERSION
