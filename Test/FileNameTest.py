import os

f_list = os.listdir("E:\算法精确率表计分类\绕组温度控制器-[BWR-6]\suzhoujjh499\负样本")
# print f_list
for i in f_list:
	# os.path.splitext():分离文件名与扩展名
	if os.path.splitext(i)[1] == '.JPG':
		print(i)