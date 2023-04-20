forecast = []
for time in range(len(series) - window_size):
  forecast.append(model.predict(series[time:time + window_size][np.newaxis]))
  
# forecast = forecast[split_time-window_size:]
# results = np.array(forecast)[:, 0, 0]
