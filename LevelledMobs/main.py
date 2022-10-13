import math
import matplotlib.pyplot as plt

x = list(range(1,451))
y = []
anno = [ 8,24,48,80,120,169,226,291,364,445]

for lvl in x:
    r = max(1,(lvl/2))*max(1,(lvl/27)*math.log10(max(1,lvl))/math.log10(27*4))
    y.append(r)

plt.plot(x,y)

for k in anno:
  plt.annotate(int(y[k]), [k, y[k]])