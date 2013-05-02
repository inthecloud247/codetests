# standard

from pprint import pprint

#list
fav_colors = [['tim', 'blue'], ['mary', 'green'], ['mary', 'blue'], ['steve', 'red']]
color_ordered = {}

for i in fav_colors:
  if i[-1] in color_ordered.keys():
    color_ordered[i[-1]].append(i[0])
  else:
    color_ordered[i[-1]]=[i[0]]

print 'color_ordered: '
pprint(color_ordered)

# RESULTS:
color_ordered:
{'blue': ['tim', 'mary'], 'green': ['mary'], 'red': ['steve']}

#------------------

# fancier

from pprint import pprint

#list
fav_colors = [['tim', 'blue'], ['mary', 'green'], ['mary', 'blue'], ['steve', 'red']]
color_ordered = {}

for i in fav_colors:
  color_ordered.setdefault(i[-1],[]).append(i[0])

print 'color_ordered: '
pprint(color_ordered)

# RESULTS:
color_ordered:
{'blue': ['tim', 'mary'], 'green': ['mary'], 'red': ['steve']}

#------------------
