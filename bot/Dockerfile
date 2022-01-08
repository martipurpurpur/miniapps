FROM python:3.8-slim-buster
# set work directory
WORKDIR /bot
# copy project
COPY . .
# install dependencies
RUN pip install --user aiogram
# run app
CMD ["python", "Scheduler.py"]