FROM python 3.6
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requriments.txt 
ENTRYPOINT [/user/local/bin/python3, app.py]
COPY . . 

