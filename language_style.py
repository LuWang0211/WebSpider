import jieba
import jieba.analyse
import jieba.posseg as pseg

# #
# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式

# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

# seg_list = jieba.cut("他来到了网易杭研大厦", cut_all=True)
# print(", ".join(seg_list))

# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print(", ".join(seg_list))

# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))

# # seg_list = jieba.cut("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
# # print(", ".join(seg_list))

# seg_list = jieba.analyse.extract_tags("新年伊始，不少食品登上抽检“黑榜”。昨日本报从国家食品药品监督管理总局官网获悉，其公布的2015年第二期食品安全监督抽检信息显示，共抽检肉及肉制品样品2473批次，合格率为95%，55批次产品不合格；在被检测的食用油、油脂及制品中,21批次品牌产品被检出不合格，一线食用油品牌基本检查过关。", 5)
# print("/".join(seg_list))

# seg_list = pseg.cut("我爱北京天安门")
# for w in seg_list:
#     print(w.word, w.flag)


def texts_simplified(files):
    pass

