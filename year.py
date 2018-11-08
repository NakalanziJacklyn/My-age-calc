userage = int(input('In which year where you born?'))
age = 2018 - userage
if age <0:
  print('Invalid')
elif age < 18:
  print('You are a minor')
elif age < 36:
  print('You are a Youth')
elif age > 36:
  print('You are an elder')
