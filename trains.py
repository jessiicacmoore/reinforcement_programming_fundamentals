trains = [
  {'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
  {'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
  {'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
  {'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
  {'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
  {'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
  {'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
  {'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]

train_111_dir = trains[7]['direction']
train_80B_freq = trains[5]['frequency_in_minutes']
train_610_dir = trains[2]['direction']

print(train_111_dir)
print(train_80B_freq)
print(train_610_dir)

def list_by_direction(direction):
  new_list = []
  for train in trains:
    if train['direction'] == direction:
     new_list.append(train['train'])

  print(new_list)

list_by_direction('north')
list_by_direction('east')

trains[0]['first_departure_time'] = 6
print(trains[0])

trains = [
  {'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
  {'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
  {'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
  {'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
  {'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
  {'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
  {'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
  {'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]


trains_by_frequency = {}

for train in trains:
  name = train['train']
  freq = train['frequency_in_minutes']
  if freq in trains_by_frequency:
    trains_by_frequency[freq].append(name)
  else:
    trains_by_frequency[freq] = [name]

print(trains_by_frequency)

