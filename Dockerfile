# # init a base image (Alpine is small Linux distro)
# FROM Python 3.9.5 -alpine
# # define the present working directory
# WORKDIR /Banglore_Houseprice_prediction
# # copy the contents into the working dir
# ADD . /Banglore_Houseprice_prediction
# # run pip to install the dependencies of the flask app
# RUN pip install -r requirements.txt
# # define the command to start the container
# CMD ["python","app.py"]

FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/
EXPOSE 8000
WORKDIR  /usr/app/
RUN pip install -r requirements.txt
CMD streamlit run App.py