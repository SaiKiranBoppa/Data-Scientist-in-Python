trip_distance_miles = taxi[:,7]
trip_length_seconds = taxi[:,8]

trip_length_hours = trip_length_seconds / 3600 # 3600 seconds is one hour

trip_mph = trip_distance_miles/trip_length_hours
