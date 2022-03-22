import matplotlib.pylab as p

s = {35, 25, 20, 10, 10}
k = ['Python', 'Java','C#', 'C', 'Go']
p.pie(s, labels=k)
p.show()