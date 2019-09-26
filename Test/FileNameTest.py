import os

f_list = os.listdir("E:\算法精确率表计分类\油面温度控制器-[BWY-803L9A]\suzhoujjh500\负样本")
# print f_list
for i in f_list:
	# os.path.splitext():分离文件名与扩展名
	if os.path.splitext(i)[1] == '.JPG':
		print(i)