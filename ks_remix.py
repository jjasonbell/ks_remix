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
	print('\n')