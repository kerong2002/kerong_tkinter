from tkinter import *  #載入函式庫
root = Tk() #建立視窗
s = Scrollbar(root) #建立Scrollbar
t = Text(root, height=5, width=20) #建立Text且設定高和寬
s.pack(side=RIGHT) #Scrollbar放置在右邊
t.pack(side=LEFT) #Text放置在左邊
s.config(command=t.yview) #設定Scrollbar捲動軸可調
t.config(yscrollcommand=s.set) #設定Scrollbar與Text結合
#字串
string= """南臺灣的8月，不同於其他學校還沈浸在暑期寧靜氣氛中，
國立高雄應用科技大學正醞釀一股引導學術研發、連結產業創新的高速氣流，
蓄勢待發。高應大研發長許進忠教授表示「『產學』、『技轉』、『生產力4.0』，
是本校目前正積極在推動的研發主軸。」，以日前與中鋼合作成立「鍛造輥軋工程研究中心」為例，
這項針對國內扣件與汽車產業的技術發展規劃的產學合作案，透過技術移轉及研發，
即使面對全球工業4.0的浪潮，也必能為臺灣用鋼產業的高值化做出更大的貢獻。"""
t.insert("1.0", string)#插入在第一列
mainloop()
