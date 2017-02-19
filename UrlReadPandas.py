# Reading csv file from url into pandas dataframe
# Reading csv file from local path to pandas dataframe

import io
import requests
import pandas as pd

# url - the path to you data
url    = "https://statweb.stanford.edu/~tibs/ElemStatLearn/datasets/SAheart.data"
source = requests.get(url).content
data   = pd.read_csv(io.StringIO(source.decode('utf-8')))

# Reading the data into pandas dataframe from local folder
data = pd.read_csv('data/SAheart.csv')
data
