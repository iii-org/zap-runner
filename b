VERSION=1.0.0
sudo docker build . --tag iiiorg/zap-runner:$VERSION
sudo docker push iiiorg/zap-runner:$VERSION
