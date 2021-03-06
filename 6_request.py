import pandas as pd
import os.path as path
import json
import requests

df = pd.read_csv(path.join('3_X_fitted_dataframe', 'X_test_scaled.csv'))

# POST request method API, at the endpoint of mlflow /invocations, with data converted to json
response = requests.post("http://127.0.0.1:1234/invocations", data=df[:].to_json(orient="split"), headers={"Content-Type": "application/json; format=pandas-split"})
print(str(response.content))
