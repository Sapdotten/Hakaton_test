FROM python

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV BOT_PASSWORD_DOCKERFILE="Dy\d0T6f"
# ENV BOT_ID=bot2

COPY . .


CMD python ./main.py 
