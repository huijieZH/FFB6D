import glob
import os
f = open("train_data_list.txt", "w+")
model_path = "/home/huijie/research/FFB6D/ffb6d/datasets/ycb/YCB_Video_Dataset/data"
template_path = "train_scene"

for data_package in glob.glob(os.path.join(model_path, template_path + "*")):
   for filepath in glob.glob(os.path.join(data_package, "*-box.txt")):
      idx = os.path.basename(filepath)[:6]
      f.write(os.path.join("data", os.path.basename(data_package), idx) + "\n")

f.close()
