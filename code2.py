import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction
##分别读取1/2/3.xlsx文件保存在df2中
df2_1 = pd.read_excel('C:\\Users\\Administrator\\Desktop\\Excel_Pandas\\2\\1.xlsx',sheet_name='Sheet1',header=None)
df2_2 = pd.read_excel('C:\\Users\\Administrator\\Desktop\\Excel_Pandas\\2\\2.xlsx',sheet_name='Sheet1',header=None)
df2_3 = pd.read_excel('C:\\Users\\Administrator\\Desktop\\Excel_Pandas\\2\\3.xlsx',sheet_name='Sheet1',header=None)
##将三个DataFrame进行拼接合并，整合为一个Frame
df2_all= pd.concat([df2_1,df2_2,df2_3],axis=0,ignore_index=True)
##将第二列从str变为float，并保留三位小数
for i  in range(103):             
    df2_all.iat[i,1] = round(float(Fraction(df2_all.iat[i,1])),3)
##获取前五列数据
df2_5=df2_all.iloc[:,[0,1,2,3,4]]
df2_5v=df2_5.values
##输入phase,rotor,power,voltage,rotate数据
strx = input('请依次输入phase,rotor,power,voltage,rotate 的值\n注意:以逗号隔开，rotor的值为分数)\n')
strx_list = strx.strip(',').split(',')#将str以逗号分隔为list
strx_list[1] = round(float(Fraction(strx_list[1] )),3)#第二个分数数据转float
for i in [0,2,3,4]:
    strx_list[i] = int(strx_list[i])
arr = np.array(strx_list)#输入数据list转array向量
##计算输入数据与文件数据的欧氏距离，并求解相似度
dict = {}
for j in range(103):
    dist = np.sqrt(np.sum(np.square(df2_5v[j]-arr))) #欧氏距离
    sim = 1.0 / (1.0 + dist)#归一化
    dict[j] = sim
max_key = max(dict, key=dict.get)#寻找dict中最大value，并返回对应key值
##确定相似都最大数据的文件位置
if max_key <= 37:
    ex_pos = '1.xlsx'
    max_pos = str(max_key+1)
elif max_key > 61 :
    ex_pos = '3.xlsx'
    max_pos = str(max_key - 61)
else:
    ex_pos = '2.xlsx'
    max_pos = str(max_key - 37)
##打印数据：最大相似度，对应数据，数据位置
print('最大相似度值为: %.6f'%dict[max_key])
print('相似度最大数据:',df2_all.iloc[max_key,:].values)
print('数据位置: 位于%s中第%s行'%(ex_pos,max_pos))
