from pprint import pprint
import matplotlib.pyplot as plt
ls1 = [[{"sensor": 'induct'}, {"sensor": 'camera1'}],[{"sensor": 'camera2'}, {"sensor": 'sensor3'}]]
ls2 = [[{"sensor": 'sorter'}, {"sensor": 'camera1'}],[{"sensor": 'camera2'}, {"sensor": 'sensor3'}]]
ls3 = [[{"sensor": 'sorter'}, {"sensor": 'camera1'}],[{"sensor": 'camera2'}, {"sensor": 'sensor3'}]]
ls4 = [[{'sensor': 'RNDM'}, {'sensor': 'jjm'}]]

messy_list = ls1 + ls2 + ls3 + ls4

key_list = []

for i in messy_list:
    for j in i:
        key_list.append(j["sensor"])

sensor_count = {sensor: 0 for sensor in key_list}

for i in key_list:
    if i in key_list:
        sensor_count[i] += 1

sensor_sorted = dict(sorted(sensor_count.items(), key=lambda item: item[1], reverse=True))
top_two = (dict(list(sensor_sorted.items())[:2]))

keys = top_two.keys()
values = top_two.values()

plt.bar(range(len(top_two)), list(top_two.values()), align='center')
plt.xticks(range(len(top_two)), list(top_two.keys()))
plt.show()