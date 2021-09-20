import pandas as pd

def lambda_handler(event, context):
    d = "test.xlsx"
    df = pd.DataFrame(data=d)
    print(df)
    print('done x1.1')
