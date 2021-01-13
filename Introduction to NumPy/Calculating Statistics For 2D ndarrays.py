# we'll compare against the first 5 rows only
taxi_first_five = taxi[:5]
# select these columns: fare_amount, fees_amount, tolls_amount, tip_amount
fare_components = taxi_first_five[:,9:13]
fare_sums = fare_components.sum(axis = 1)
fare_totals = taxi_first_five[:,13]
print(fare_totals)
print(fare_sums)
