VERSION=0.1.4
sudo docker build . --tag iiiorg/zap-runner:$VERSION
sudo docker push iiiorg/zap-runner:$VERSION
