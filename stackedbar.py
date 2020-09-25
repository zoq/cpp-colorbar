import numpy as np
import matplotlib.pyplot as plt
from PIL import Image 

def colorbar(values, colors, filename='output.png', height=10, width=3):
  plt.rcParams["figure.figsize"] = (width, height)
  plt.rcParams["savefig.pad_inches"] = 0 
  
  values = values.split(';')
  colors = colors.split(';')
  
  v = 0
  i = 0
  for value in values:
    b = plt.bar(0, float(value), 10, bottom=v, color=( \
        int(colors[i]) / 255, \
        int(colors[i + 1]) / 255,\
        int(colors[i + 2]) / 255, 1))
    v += float(value)
    i += 3
  
  plt.axis('off')
  plt.autoscale(tight=True)
  plt.savefig(filename)

  im = Image.open(filename)
  im2 = im.rotate(270, expand=True)
  im2.save(filename)

values = '10;20;40;100';
colors = '255;123;1;1;1;1;4;4;4;255;0;0'
colorbar(values, colors)
