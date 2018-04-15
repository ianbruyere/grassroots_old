from .models import Status
from django_pandas.io import read_frame
import pandas as pd
from nltk.tokenize import word_tokenize

qs = Status.objects.all()

df = read_frame(qs)
print(df.head(10))


