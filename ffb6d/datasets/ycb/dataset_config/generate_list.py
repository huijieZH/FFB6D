import glob
import os
import numpy as np
f = open("train_data_list.txt", "w+")
model_path = "/home/huijie/research/progresslabeller/FFB6D/ffb6d/datasets/ycb/YCB_Video_Dataset/data"
sensor = "D435"
template_path = os.path.join(sensor, "train_scene*")



def all_select(f):
   for data_package in sorted(glob.glob(os.path.join(model_path, template_path + "*"))):
      for filepath in sorted(glob.glob(os.path.join(data_package, "*-box.txt"))):
         idx = os.path.basename(filepath)[:6]
         f.write(os.path.join("data/primesense/", os.path.basename(data_package), idx) + "\n")

   f.close()

def random_select(f, ratio):
   for data_package in sorted(glob.glob(os.path.join(model_path, template_path + "*"))):
      for filepath in sorted(glob.glob(os.path.join(data_package, "*-box.txt"))):
         if np.random.random() < ratio:
            idx = os.path.basename(filepath)[:6]
            f.write(os.path.join("data", sensor ,os.path.basename(data_package), idx) + "\n")
   f.close()   

if __name__ == "__main__":
   random_select(f, 0.33)
   #all_select(f)
