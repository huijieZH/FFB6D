f = open("test_data_list.txt", "w+")
path = "data/1111/"
num = 100
for idx in range(1, num):
   print(path + "{0:06d}\n".format(idx))
   f.write(path + "{0:06d}\n".format(idx))
f.close()
