import hug
import pandas as pd
import os, random
os.chdir(os.getenv('HOME') + '/Documents/Novaline/ks_remix')


df = pd.read_csv('ks_remix.csv')
with open('targets.txt', 'r', encoding='utf-8') as f:
	targets = f.read()
targets = targets.split("\n")

names = df.name

num = 10
for i in range(0, num):
	name = random.choice(names)
	target = random.choice(targets)
	print(name, 'FOR', target)

@hug.get()
def ks_gen(hug_timer=3):
    """Generates a Kickstarter campaign idea"""
    name = random.choice(names)
    target = random.choice(targets)
    return {'message': '{0} FOR {1}!'.format(name, target),
            'took': float(hug_timer)}