# Goal of this file, teaching you how to:
# - read .csv-file from url into pandas dataframe
# - read .csv-file from local path to pandas dataframe

import io
import requests
import pandas as pd

# This URL is from the Stanford Statweb, - Datasets for "The Elements of Statistical Learning"
url    = "https://statweb.stanford.edu/~tibs/ElemStatLearn/datasets/SAheart.data"
source = requests.get(url).content
data   = pd.read_csv(io.StringIO(source.decode('utf-8')))


# Reading the data into pandas dataframe from local folder, this is the same dataset as the one above
data = pd.read_csv('data/SAheart.csv')
data
