sudo docker build . --tag iiiorg/zap-runner:0.0.1
sudo docker run --env-file ./.env iiiorg/zap-runner:0.0.1 
