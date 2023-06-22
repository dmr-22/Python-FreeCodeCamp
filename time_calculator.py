def add_time(start, duration, day = None):

  added_hours = 0
  minutes = 0

  ########Start time split########
  start_split = start.split()
  start_hour_minutes = start_split[0].split(':')
  start_hour = start_hour_minutes[0]
  start_minutes = start_hour_minutes[1]
  print(f'start minutes: {start_minutes}')
  start_clock = start_split[1]

  #######Duration time split#######
  duration_split = duration.split(':')
  duration_hour = duration_split[0]
  duration_minutes = duration_split[1]

  sum_hour = int(start_hour) + int(duration_hour)
  sum_minutes = int(start_minutes) + int(duration_minutes)
  print(f'minutes: {sum_minutes}')

  ##########Minutes##########
  if sum_minutes > 60 :
    added_hours = int(sum_minutes / 60)
    minutes = sum_minutes % 60
    if minutes < 10:
      minutes = "0" + str(minutes)
    print(f'minutes {minutes}')
    sum_hour = sum_hour + added_hours
    print(f'sum hour {sum_hour}')
  else:
    minutes = sum_minutes
    if minutes < 10:
      minutes = "0" + str(minutes)
    print(f'minutes {minutes}')

  ##########Hour##########
  if sum_hour > 12 :
    hour = sum_hour % 12    
    if hour == 0:
      hour = 12
    print(f'hour: {hour}')
  else:
    hour = sum_hour
    print(f'Hour: {hour}')
  

  result = f'{hour}:{minutes}'
  print(result)
  
  #print(start_hour, start_minutes, start_clock)
  #print(sum_hour, sum_minutes)

  return 0

add_time("6:30 PM", "205:12")