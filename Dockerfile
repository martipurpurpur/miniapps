FROM python:3.8-slim-buster
# set work directory
WORKDIR /multiapp/sheduler/
# copy project
COPY . /multiapp/sheduler/
# install dependencies
RUN pip install --user aiogram
# run app
CMD ["python", "sheduler\Sheduler.py"]