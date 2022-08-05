import os
from urllib import request

data_dirname = "data"

data_meta = [
    {
        "url": "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2021-01.parquet",
        "local_path": os.path.join(data_dirname, "green_tripdata_2021-01.parquet"),
    },
    {
        "url": "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2021-02.parquet",
        "local_path": os.path.join(data_dirname, "green_tripdata_2021-02.parquet"),
    },
    {
        "url": "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2021-03.parquet",
        "local_path": os.path.join(data_dirname, "green_tripdata_2021-03.parquet"),
    },
]

if not os.path.exists(data_dirname):
    os.mkdir(data_dirname)
    
for dm in data_meta:
    if not os.path.exists(dm['local_path']):
        request.urlretrieve(dm['url'], dm['local_path'])
