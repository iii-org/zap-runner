export TARGET_URL=http://demo.iiidevops.org/
sudo docker build . --tag iiiorg/zap-runner:0.0.1
sudo docker run -e TARGET_URL=$TARGET_URL iiiorg/zap-runner:0.0.1 
