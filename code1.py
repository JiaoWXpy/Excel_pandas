import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
##构造函数生成topol不同类型的频数汇总DataFrame表
##函数说明：输入文件路径生成topol频数表
def topol_bar(a):                           #a:文件路径,注意:'\'都要使用‘\\’
    df = pd.read_excel(a,sheet_name='Sheet1')#读取整张表格
    dft = df.pivot_table(values = ['phase'],index = ['topol'],aggfunc = 'count')#Pivot.table
    dft.rename(columns={'phase':'Fred'}, inplace = True)
    return dft
##使用topol_bar函数将两个表格中topol例数据分类汇总
df1 = topol_bar('C:\\Users\\Administrator\\Desktop\\Excel_Pandas\\1\\3.xls')
df2 = topol_bar('C:\\Users\\Administrator\\Desktop\\Excel_Pandas\\1\\4.xls')
##绘制直方图并显示
df1.plot(kind='bar',width = 0.35).get_figure()#直方图，宽度0.35
plt.title('3.xls Topol-Frequency')#设置标题
pl.xticks(rotation=360)#旋转xlable到水平位置
plt.ylabel('Frequency')#设置y轴lable
plt.yticks(np.arange(-0, 60, 5))#设置y轴范围，下同

df2.plot(kind='bar',width = 0.23).get_figure()
plt.title('4.xls Topol-Frequency')
pl.xticks(rotation=360)
plt.ylabel('Frequency')
plt.yticks(np.arange(-0, 60, 5))
plt.show()#显示图表



