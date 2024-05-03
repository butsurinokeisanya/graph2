#!/usr/bin/env python
# -*- coding: utf-8 -*-

#--------------------------------------------------------------
# モジュール
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#--------------------------------------------------------------
# 定数
WIDTH = 24.5 # width [cm] of the graph
HEIGHT =15.0 # Height [cm] of the graph

XMIN = 20.0 # Minimum value for the x axis
XMAX = 130.0 # Maximum value for the x axis
XTMIN = 20.0 # Minimum value for the x axis ticks
XTMAX = 130.0 # Maximum value for the x axis ticks
XINC = 10 # Increment for ticks on the x axis

YMIN=-5000 #Minimum value for the y axis
YMAX=20000 # Maximum value for the y axis
YTMIN =0.0 # Minimum value for the y axis ticks
YTMAX = 20000 # Maximum value for the y axis ticks
YINC = 5000 # Increment for ticks on the y axis

Y2MIN=-5000 #Minimum value for the y axis
Y2MAX=20000 # Maximum value for the y axis
Y2TMIN =0.0 # Minimum value for the y axis ticks
Y2TMAX = 20000 # Maximum value for the y axis ticks
Y2INC = 5000 # Increment for ticks on the y axis

IVSIZE=40 #Size of numerical values for the x and y axes
ILSIZE=50 #Size of labels for the x and y axes
LGSIZE=50 #Size of Legend
SYLBL=20 #Shift of the y label (Intensity) along the x axis in the unit of a character

PSIZE=10 #Size of '+' marks representing observed intensities
TSIZE=10 #Length (in percent of the y-axis lenght) of tick marks to show peak positions

OFFSETD=-2800 #Offset for the residual curve
OFFSET1=-700 #Offset for tick marks (peak positions) for phase No. 1

DLW=2.0 # Default linewidth
BLW=2.0 # Linewidth of graph borders


LEN_BAR=0.001*TSIZE*(YMAX-YMIN)

#--------------------------------------------------------------
#
#                      MAIN
#
#--------------------------------------------------------------

# S 読み込み
df=pd.read_csv("FapatiteJ.csv")
header=df.columns
x=df.iloc[:,0]
y1=df.iloc[:,1]
y2=df.iloc[:,2]
y3=df.iloc[:,3]
y4=df.iloc[:,4]

df2=pd.read_csv("hkl.csv")
header2=df2.columns
x2=df2.iloc[:,4]

#--------------------------------------------------------------
# T  変換
# フォント, 図枠
plt.rcParams["font.family"]="Times New Roman" # 全体のフォントを設定
plt.rcParams["mathtext.fontset"]='stix' # 数式フォント
plt.rcParams["font.size"] =IVSIZE # フォントの大きさ
plt.rcParams["axes.labelsize"] =ILSIZE
plt.rcParams["legend.fontsize"]=LGSIZE
plt.rcParams["xtick.direction"]="in" #x内向き目盛り
plt.rcParams["ytick.direction"]="in" #y内向き目盛り
plt.rcParams["xtick.minor.visible"]=True
plt.rcParams["ytick.minor.visible"]=True
# 目盛り幅
plt.rcParams["xtick.major.width"]=2.0
plt.rcParams["ytick.major.width"]=2.0
plt.rcParams["xtick.minor.width"]=2.0
plt.rcParams["ytick.minor.width"]=2.0
# 目盛りサイズ
plt.rcParams["xtick.major.size"]=20
plt.rcParams["ytick.major.size"]=20
plt.rcParams["xtick.minor.size"]=10
plt.rcParams["ytick.minor.size"]=10
plt.rcParams["xtick.top"]=True #対岸軸ON
plt.rcParams["ytick.right"]=True #対岸軸ON
plt.rcParams["axes.linewidth"]=BLW
plt.rcParams["axes.xmargin"]=0 # x軸のmax, minを交点とする. 余白を作らない.
plt.rcParams["axes.ymargin"]=0 # y軸のmax, minを交点とする. 余白を作らない.

# 軸
fig=plt.figure(figsize=(WIDTH, HEIGHT))
ax=fig.add_subplot(111)
ax.set_xlim(XMIN,XMAX)
ax.set_ylim(YMIN, YMAX)
ax2 = ax.twinx()  # 同じX軸を共有する2番めの軸のインスタンスを作成
ax2.set_ylim(Y2MIN, Y2MAX)
plt.locator_params(axis='y', nbins=6) # y軸, 6個以内

# 目盛り間隔
plt.xticks(np.arange(XTMIN, XTMAX+1, step=XINC))
ax.set_yticks(np.arange(YTMIN, YTMAX+1, step=YINC))
ax2.set_yticks(np.arange(Y2TMIN, Y2TMAX+1, step=Y2INC))

#--------------------------------------------------------------
# xdata, ydata, linewidth, color, marker, markersize,
# markeredgewidth, markeredgecolor, markerfacecolor, fillstyle,
# label, zorder
#--------------------------------------------------------------
# line
# linewidth
# ":"点線, "-."一点鎖線, "--"破線, "-"実線
#--------------------------------------------------------------
# marker
# markersize,markeredgewidth, markeredgecolor, markerfacecolor
# ".",点,"*",星",",ピクセル,"1",Y"o",丸,"2",Y(上下反転)
# "v",下三角形,"3",Y(90度時計回り)"^",三角形,"4",Y(90度反時計周り)
# "<",左三角形,"+",+">",右三角形,"x",x
# "s",四角形,"X",x(filled)"p",五角形,"D",ひし形
# "h",六角形,"d",細いひし形"8",八角形,"",マーカー無し
#--------------------------------------------------------------
# fillstyle
# none, top, bottom, right, left, full
#--------------------------------------------------------------
# color
# b, g, r, c, m, y, k

ax.plot(x, y1,         "+", color="r",  markersize=PSIZE, label=header[1])
ax.plot(x, y2,         "-", color="c",  linewidth=DLW,    label=header[2], zorder=-1)



ax2.plot(x, y3+OFFSETD, "-", color="b",  linewidth=DLW,    label=header[3])
ax2.plot(x, y4,         "-", color="k",  linewidth=DLW,    label=header[4])
ax2.errorbar(x2,[OFFSET1]*len(x2),fmt="none", color="g", yerr=LEN_BAR, label="Expected Reflection")


# タイトル
plt.title("Fluorapatite, Ca$_5$(PO$_4$)$_3$", y=1.05)
ax.legend(frameon=False) #フレームなし
ax.set_ylabel("Intensity [arb.units]", labelpad=SYLBL)
ax2.set_ylabel("Intensity [arb.units]", labelpad=SYLBL*3,rotation=270)
plt.xlabel("2$\u03b8$"+"[$\mathregular{\degree}$]", labelpad=SYLBL)

#plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.3f')) # y軸小数点3桁表示

#plt.gca().xaxis.get_major_formatter().set_useOffset(False) #  軸　の数字にオフセット (+1.05e9 など)を使わずに表現する.

#--------------------------------------------------------------
#  出力
plt.tight_layout() # グラフが重ならず設定した図のサイズ内に収まる.
plt.savefig('output.pdf', transparent=True)
plt.savefig('output.png', transparent=True, dpi=300)
