import yaml
import json

fruit = {
	'pear':['seckel','bartlett'],
	'apple':['fuji','crispin']
}

cities = ['Chicago','Houston','Atlanta']

list = [1,2,3,'words']

list.append(fruit)
list.append(cities)

with open("ymltst.yml","w") as f:
	f.write(yaml.dump(list,default_flow_style=False))
f.close()

with open("jsntst.json","w") as f2:
        json.dump(list, f2)
f2.close()


