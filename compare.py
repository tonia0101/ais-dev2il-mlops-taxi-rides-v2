import pandas as pd

df_csv = pd.read_csv('example-data/2025-01-01.taxi-rides.csv')
print(df_csv.dtypes)



df_pq = pd.read_parquet('example-data/2025-01-01.taxi-rides.parquet')
print(df_pq.dtypes)


import os

csv_size = os.path.getsize('example-data/2025-01-01.taxi-rides.csv')
pq_size  = os.path.getsize('example-data/2025-01-01.taxi-rides.parquet')

print(f'CSV:     {csv_size / 1024 / 1024:.1f} MB')
print(f'Parquet: {pq_size  / 1024 / 1024:.1f} MB')
print(f'Parquet is {csv_size / pq_size:.1f}x smaller')



import time

t = time.time()
pd.read_csv('example-data/2025-01-01.taxi-rides.csv')
csv_time = time.time() - t

t = time.time()
pd.read_parquet('example-data/2025-01-01.taxi-rides.parquet')
pq_time = time.time() - t

print(f'CSV:     {csv_time:.3f}s')
print(f'Parquet: {pq_time:.3f}s')




df_csv = pd.read_csv('example-data/2025-01-01.taxi-rides.csv')
df_csv['tpep_pickup_datetime']  = pd.to_datetime(df_csv['tpep_pickup_datetime'])
df_csv['tpep_dropoff_datetime'] = pd.to_datetime(df_csv['tpep_dropoff_datetime'])
print(df_csv.dtypes)

"""
tpep_pickup_datetime     datetime64[ns]
tpep_dropoff_datetime    datetime64[ns]
trip_distance                   float64
ride_time                        object
outlier                            bool
dtype: object
"""

#df_csv['ride_time'] = pd.to_numeric(df_csv['ride_time'])
#print(df_csv.dtypes)

"""
Traceback (most recent call last):
  File "lib.pyx", line 2391, in pandas._libs.lib.maybe_convert_numeric
ValueError: Unable to parse string "unknown"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/antoniasturm/Documents/AIS_SS_26/DevOps and MLOps/MLOps_exercise/compare.py", line 53, in <module>
    df_csv['ride_time'] = pd.to_numeric(df_csv['ride_time'])
                          ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "/Users/antoniasturm/Documents/AIS_SS_26/DevOps and MLOps/MLOps_exercise/.venv/lib/python3.13/site-packages/pandas/core/tools/numeric.py", line 232, in to_numeric
    values, new_mask = lib.maybe_convert_numeric(  # type: ignore[call-overload]
                       ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        values,
        ^^^^^^^
    ...<4 lines>...
        and not values_dtype.storage == "pyarrow_numpy",
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "lib.pyx", line 2433, in pandas._libs.lib.maybe_convert_numeric
ValueError: Unable to parse string "unknown" at position 0
"""

import time
import pandas as pd

t = time.time()
for _ in range(365):
    pd.read_csv('example-data/2025-01-01.taxi-rides.csv')
csv_time = time.time() - t

t = time.time()
for _ in range(365):
    pd.read_parquet('example-data/2025-01-01.taxi-rides.parquet')
pq_time = time.time() - t

print(f'CSV:     {csv_time:.1f}s')
print(f'Parquet: {pq_time:.2f}s')
print(f'Parquet is {csv_time / pq_time:.0f}x faster')

"""
CSV:     12.8s
Parquet: 0.33s
Parquet is 39x faster
"""

