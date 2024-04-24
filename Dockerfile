FROM  python    
WORKDIR /untitled2
COPY . /untitled2
RUN pip install numpy
RUN pip install pandas
RUN pip install nltk
CMD [ "python3","untitled2.py" ]