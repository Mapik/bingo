
import os
import numpy as np
import random
from PIL import Image

path = os.getcwd() + '/otp3/'

#-------------------------------------------
# Reading images' files' names
#-------------------------------------------

list_im = []
for file in os.listdir(path):
  filename = os.fsdecode(file)
  img_path = path + filename
  list_im.append(img_path)

#-------------------------------------------
# Opening images 
#-------------------------------------------

imgs = [ Image.open(i) for i in list_im ]

#-------------------------------------------
# Creating random lists
#-------------------------------------------

global_list = []

for k in range(1,11):
  full_list = []
  local_list = []
  random.shuffle(imgs)
  for i, img in enumerate(imgs):
    file_name = img.filename
    full_list.append(file_name)
    if len(local_list)<25:
      local_list.append(file_name)
  global_list.append(local_list)

#-------------------------------------------
# Producing Bingo cards
#-------------------------------------------

n = 0

for l_one in global_list:
  chunks = [l_one[x:x+5] for x in range(0, len(l_one), 5)]
  n += 1
  img_comb_list = []
  for list_im in chunks:
    n += 1
    imgs = [ Image.open(i) for i in list_im ]
    x = (np.asarray( i ) for i in imgs )
    imgs_comb = np.hstack( x )
    img_comb_list.append(imgs_comb)

  imgs_comb = np.vstack( (i for i in img_comb_list ) )
  imgs_comb = Image.fromarray( imgs_comb)
  imgs_comb.save( 'bingo_{}.jpg'.format(n) )    

#-------------------------------------------
# Producing caller
#-------------------------------------------

print(len(full_list))
chunks = [full_list[x:x+3] for x in range(0, len(full_list), 3)]
print(len(chunks))
n += 1
img_comb_list = []
for list_im in chunks:
  n += 1
  imgs = [ Image.open(i) for i in list_im ]
  x = (np.asarray( i ) for i in imgs )
  imgs_comb = np.hstack( x )
  img_comb_list.append(imgs_comb)

imgs_comb = np.vstack( (i for i in img_comb_list ) )
imgs_comb = Image.fromarray( imgs_comb)

#-------------------------------------------
# Saving
#-------------------------------------------

imgs_comb.save( 'caller_{}.jpg'.format(n) )    


