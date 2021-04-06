VERSION=0.1.1-debug
sudo docker build . --tag iiiorg/zap-runner:$VERSION
sudo docker push iiiorg/zap-runner:$VERSION
sudo docker run -v $(pwd):/zap/wrk/:rw --env-file ./.env iiiorg/zap-runner:$VERSION
