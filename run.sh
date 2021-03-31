echo target=$TARGET_URL
zap-baseline.py -t $TARGET_URL | python /usr/src/app/upload.py
#zap-full-scan.py -t $TARGET_URL | python /usr/src/app/upload.py 
