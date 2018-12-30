from cardiacpedia.models import IPG
from cardiacpedia import db
import pandas as pd

file = pd.read_csv('devices/IPG LOW-VOLTAGE DEVICES.csv')
print(file.head())
