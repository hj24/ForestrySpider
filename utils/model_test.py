from config.db.settings import DATABASE
from peewee import *
from peewee import chunked
from playhouse.mysql_ext import JSONField
from utils.decorators.db import auto_connect
from utils.decorators.counter import counter

db = DATABASE['mysqldb']

class Test3(Model):

    title = CharField(max_length=100, unique=True)
    type = IntegerField()
    tag = CharField(max_length=20)
    content = JSONField()

    class Meta:
        database = db

# def create_table():
#     with db:
#         db.create_tables([Test2])


class Save:

    def __init__(self, content):
        self.content = content

    @db.atomic()
    def mock_save_many(self, *, batch=None):
        try:
            if batch is None:
                Test3.insert_many(self.content).on_conflict_ignore().execute()
            else:
                for bat in chunked(self.content, batch):
                    Test3.insert_many(bat).on_conflict_ignore().execute()
        except Exception as e:
            print(e)
            db.rollback()
        else:
            print('save: %s records success!', len(self.content))



@counter
def save(json_obj):
    # Test3.create_table()
    # person, created = Test3.get_or_create(name='嘿嘿', defaults={'content': json_obj})
    # person1, created1 = Test3.get_or_create(name='爸爸', defaults={'content': json_obj})
    data = [{'title': str(i), 'type': 1, 'tag': '媒体报道', 'content': '{"title": "银杏叶也能做枕头了？好处还不少 ", "summary": "\\n<p>\u3000\u3000银杏树，又叫白果树，是一种古老的植物", "detail": "\\n<p>\u3000\u3000银杏树，又叫白果树，是一种古老的植物，银杏树不仅是一种观赏价值很高的植物，而且它的果实和叶子都有很高的药用价值。但是你知道吗?银杏的叶子也可以用来制作枕头了，而且还有独到的好处，我们平时使用的枕头几乎没有听说过用银杏叶做枕头，是不是觉得很神奇?接下来我们就一起看看用银杏叶做的枕头都有哪些好处吧。</p><p>\u3000\u30001. \\r\\n银杏叶枕头有一股天然的清香，对于年轻人来说，银杏叶枕头最大的好处就在于能帮助人们提高睡眠质量。这对于压力山大而难以入眠的都市白领而言，无疑是一道福音。</p><p>\u3000\u30002.银杏叶枕头还能避免成年人因血管老化惹起的高血压、脑中风、糖尿病等，可使成年人特别在中老年时期维持正常的心脏输出量以及正常的神经系统功用的自然物质,使人尽可能坚持正常的细胞生命周期，坚持梦寐以求的青春生机。</p><p>\u3000\u3000值得注意的是，做银杏叶枕头时，又或是存放时，银杏叶需要保持干燥，不然容易发霉，枕在发霉的枕头上，自然对人身体是无益处的。知道银杏叶枕头的好处后大家可以尝试去做一个，给自己的生活增添不一样的景色。</p><p><br/></p>\\n", "creator": "新闻类型：媒体报道", "date": "2019年5月31日", "link": "http://m.cnyxs.com/news_type.asp?id=34948"}'}
            for i in range(40000, 40101)]
    type_2 = [
        {'title': '<em class="textred">银杏<\\/em>达莫并用奥扎格雷静滴治疗脑梗塞疗效观察', 'type': 2, 'tag': None,
         'content': '{"type": "CJFD", "typech": "期刊", "id": "JKXS201419364", "source": "大家健康(学术版)", "contributor": "山西省晋城市泽州县人民医院神经内科", "creator": "琚长虹", "titlecopy": "银杏达莫并用奥扎格雷静滴治疗脑梗塞疗效观察", "title": "<em class=\\"textred\\">银杏<\\\\/em>达莫并用奥扎格雷静滴治疗脑梗塞疗效观察", "updatedate": "2014-12-04", "subjectcode": "E070", "subjectsubcolumncode": "E070_3", "citedtimes": "3", "downloadedtimes": "17", "date": "2014-10-20", "summary": "目的:探讨分析银杏达莫并用奥扎格雷静滴治疗脑梗塞的临床疗效。方法:选取2012年6月至2013年6月在我院神经内科进行治疗的104例脑梗塞患者作为研究对象,随机分成观察组与对照组,每组52例,对照组单纯应用银杏达莫进行治疗,观察组在对照组治疗基础上应用奥扎格雷静滴定进行治疗,两个疗程后观察两组患者的临床疗效及不良反应发生率。结果:观察组治疗的总有效率为96.15%,对照组治疗的总有效率为84.62%,观察组的总有效率明显高于对照组(P<0.05),差异有统计学意义;对照组不良反应发生率为9.62%,...", "ispublishahead": "", "year": "2014", "issue": "19", "corejournal": "", "sourcecode": "JKXS", "filetype": "111;39561"}'},
        {'title': '<em class="textred">银杏<\\/em>叶提取物阻断N-亚硝基化合物合成的研究', 'type': 2, 'tag': None,
         'content': '{"type": "CJFD", "typech": "期刊", "id": "QQHB201420005", "source": "齐齐哈尔医学院学报", "contributor": "安徽蚌埠医学院预防医学系;河南质量工程职业学院", "creator": "束莉;闫泽华;王力;张玉媛;申玲", "titlecopy": "银杏叶提取物阻断N-亚硝基化合物合成的研究", "title": "<em class=\\"textred\\">银杏<\\\\/em>叶提取物阻断N-亚硝基化合物合成的研究", "updatedate": "2014-12-08", "subjectcode": "E057", "subjectsubcolumncode": "E057_6", "citedtimes": "0", "downloadedtimes": "59", "date": "2014-10-28", "summary": "目的探讨银杏叶提取物阻断小鼠体内N-亚硝基化合物合成的作用,为银杏叶提取物的抗氧化能力和免疫抑制作用提供实验依据。方法灌胃给予小鼠生理盐水、亚硝酸钠、亚硝酸钠+低浓度EGb、亚硝酸钠+中浓度EGb、亚硝酸钠+高浓度EGb,所有小鼠分笼饲养,2周实验后提取各组小鼠血清和肝脏,-20℃保存,检测小鼠MDA、SOD及GSH等指标。结果 Na NO2组的平均肝重及肝/体重比均明显高于对照组(P<0.01);Low EGb、Middle EGb组的平均肝重及肝/体重比高于对照组,差异有统计学意义(P<0.05...", "ispublishahead": "", "year": "2014", "issue": "20", "corejournal": "", "sourcecode": "QQHB", "filetype": "XML;EPUB"}'},
        {'title': '<em class="textred">银杏<\\/em>达莫对脑出血微创碎吸术后残余血肿及脑水肿的影响', 'type': 2, 'tag': None,
         'content': '{"type": "CJFD", "typech": "期刊", "id": "QQHB201419046", "source": "齐齐哈尔医学院学报", "contributor": "深圳市龙岗区人民医院", "creator": "黄翔;兰周华;杨谦;董广宇;吴春波;杨亚敏", "titlecopy": "银杏达莫对脑出血微创碎吸术后残余血肿及脑水肿的影响", "title": "<em class=\\"textred\\">银杏<\\\\/em>达莫对脑出血微创碎吸术后残余血肿及脑水肿的影响", "updatedate": "2014-12-08", "subjectcode": "E066", "subjectsubcolumncode": "E066_61", "citedtimes": "2", "downloadedtimes": "22", "date": "2014-10-15", "summary": "目的观察银杏达莫对脑出血微创碎吸术后患者的疗效。方法将75例脑出血患者随机分为治疗组(n=37)和对照组(n=38),两组患者入院后常规给予脱水、止血治疗,并给予微创颅内血肿碎吸术。治疗组给予银杏达莫加入葡萄糖液中静滴,对照组除不用银杏达莫外余治疗与治疗组相同。观察两组患者残余血肿和脑水肿吸收、神经功能康复疗效。结果治疗组术后残余血肿的吸收、脑水肿的改善、神经功能的康复明显好于对照组(P均<0.05)。结论银杏达莫能促进脑出血微创碎吸术后患者的残余血肿的吸收及神经功能的改善。", "ispublishahead": "", "year": "2014", "issue": "19", "corejournal": "", "sourcecode": "QQHB", "filetype": "7;3893416"}'},
        {'title': '<em class="textred">银杏<\\/em>达莫注射液治疗急性脑梗死的疗效分析', 'type': 2, 'tag': None,
         'content': '{"type": "CJFD", "typech": "期刊", "id": "PLHY201430033", "source": "临床合理用药杂志", "contributor": "河北省保定市第三中心医院", "creator": "李晓卿", "titlecopy": "银杏达莫注射液治疗急性脑梗死的疗效分析", "title": "<em class=\\"textred\\">银杏<\\\\/em>达莫注射液治疗急性脑梗死的疗效分析", "updatedate": "2014-11-20", "subjectcode": "E070;E077", "subjectsubcolumncode": "E070_3;E077_3H", "citedtimes": "0", "downloadedtimes": "27", "date": "2014-10-25", "summary": "目的研究银杏达莫注射液治疗急性脑梗死的临床疗效。方法选取2012—2013年我院收治的急性脑梗死患者104例,随机分成观察组和对照组,观察组采用银杏达莫注射液治疗,对照组采用丹参注射液治疗,两组患者治疗30d后,分别从临床疗效、血流变学等方面进行比较。结果观察组治疗总有效率〔96.2%(50/52)〕高于对照组〔94.2%(49/52)〕,差异有统计学意义(P<0.05);两组患者治疗后血流变学等指标比较,差异有统计学意义(P<0.05)。结论银杏达莫注射液治疗脑梗死急性期患者的疗效显著,可有效改善...", "ispublishahead": "", "year": "2014", "issue": "30", "corejournal": "", "sourcecode": "PLHY", "filetype": "XML;EPUB;"}'},
        {'title': '药物联合臭氧疗法治疗脑供血不足的临床疗效观察', 'type': 2, 'tag': None,
         'content': '{"type": "CJFD", "typech": "期刊", "id": "PLHY201432042", "source": "临床合理用药杂志", "contributor": "河南省淅川县第二人民医院神经内科", "creator": "王灵敏", "titlecopy": "药物联合臭氧疗法治疗脑供血不足的临床疗效观察", "title": "药物联合臭氧疗法治疗脑供血不足的临床疗效观察", "updatedate": "2014-12-05", "subjectcode": "E070", "subjectsubcolumncode": "E070_3", "citedtimes": "4", "downloadedtimes": "36", "date": "2014-11-20", "summary": "目的观察药物联合臭氧疗法治疗脑供血不足的临床疗效。方法选取来医院进行治疗的脑供血不足患者314例,随机分为治疗组与对照组各157例。2组患者入院后均给予银杏达莫、甲磺酸倍他司汀、阿司匹林等改善脑供血的药物进行治疗,治疗组在此基础上加用臭氧治疗,比较2组临床效果及不良反应。结果治疗组患者临床治疗总有效率为88.54%,对照组患者临床治疗总有效率为67.52%,比较差异具有统计学意义(P<0.01)。治疗组患者治疗后的MCA、BA及VA平均血流速度均显著高于对照组患者,差异具有统计学意义(P<0.01)...", "ispublishahead": "", "year": "2014", "issue": "32", "corejournal": "", "sourcecode": "PLHY", "filetype": "0419121;0"}'},
        {'title': '联合应用杏灵分散片和调脂药治疗血脂异常的临床疗效观察', 'type': 2, 'tag': None,
         'content': '{"type": "CJFD", "typech": "期刊", "id": "QYWA201417127", "source": "当代医药论丛", "contributor": "山西省109医院", "creator": "常炜", "titlecopy": "联合应用杏灵分散片和调脂药治疗血脂异常的临床疗效观察", "title": "联合应用杏灵分散片和调脂药治疗血脂异常的临床疗效观察", "updatedate": "2014-12-12", "subjectcode": "E079", "subjectsubcolumncode": "E079_6", "citedtimes": "0", "downloadedtimes": "28", "date": "2014-10-15", "summary": "目的 :观察联合应用杏灵分散片和调脂药治疗血脂异常的临床疗效及预后。方法 :对60例血脂异常患者的临床资料进行回顾性分析,将其分为观察组和对照组。为对照组患者单用调脂药进行治疗,为观察组患者联合应用调脂药和杏灵分散片进行治疗,并对比分析其进行治疗后的血脂达标率。结果 :观察组患者的血脂达标率为92.8%,对照组患者的血脂达标率为65.6%,二者相比差异显著(P<0.05),有统计学意义。在为两组患者进行治疗后3个月复查其血脂水平的结果显示,观察组患者的血脂达标率为89%,对照组患者的血脂达标率为45...", "ispublishahead": "", "year": "2014", "issue": "17", "corejournal": "", "sourcecode": "QYWA", "filetype": "3564:2827"}'},
        {'title': '森海塞尔上海音乐厅平移十周年纪念', 'type': 2, 'tag': None,
         'content': '{"type": "CJFD", "typech": "期刊", "id": "YYAH201411001", "source": "音乐爱好者", "contributor": "", "creator": "", "titlecopy": "森海塞尔上海音乐厅平移十周年纪念", "title": "森海塞尔上海音乐厅平移十周年纪念", "updatedate": "2014-12-17", "subjectcode": "F086", "subjectsubcolumncode": "F086_17", "citedtimes": "0", "downloadedtimes": "18", "date": "2014-11-10", "summary": "2002年8月31日,上海音乐厅在原址举行了最后一场音乐会,然后往东南方向平移了66.46米。2004年10月1日,上海音乐厅重新开张,这个平移工程成为建筑保护历史上的奇迹。这十年,上海音乐厅推出了一系列乐迷熟知喜爱的品牌项目,在上海的文化版图上占据着重要位置。2014年10月12日,上海音乐厅把十年精华浓缩成一日欢庆,举办了包括星期广播音乐会\\"德意志回声\\"、音乐午茶\\"当我遇见你\\"、银杏音乐会\\"潮\\"、", "ispublishahead": "", "year": "2014", "issue": "11", "corejournal": "", "sourcecode": "YYAH", "filetype": ""}'},
        {'title': '“杏林”考辨', 'type': 2, 'tag': None,
         'content': '{"type": "CJFD", "typech": "期刊", "id": "HZWZ201404016", "source": "汉字文化", "contributor": "佛山科学技术学院文学院", "creator": "蒋书红", "titlecopy": "“杏林”考辨", "title": "“杏林”考辨", "updatedate": "2014-10-24", "subjectcode": "F084", "subjectsubcolumncode": "F084_24", "citedtimes": "0", "downloadedtimes": "85", "date": "2014-08-25", "summary": "\\"杏林\\"指代医学,由来已久,然其中之\\"杏\\"当为何物,却有疑议,甚至是误解。?\\"杏林\\"指代医学,来源于东晋葛洪《神仙传》卷十《董奉》所载:董奉者,字君异,侯官县人也。昔吴先主时,……又君异居山间,为人治病,不取钱物,使人重病愈者,使栽杏五株,轻者一株,如此数年,计得十万余株,郁然成林,而山中百虫群兽,游戏杏下,竟不生草,有如耘治也。于是杏子大熟,君异于杏林下作箪仓,语时人曰:欲买杏者,不须来报,径自取之。得将谷一器", "ispublishahead": "", "year": "2014", "issue": "04", "corejournal": "", "sourcecode": "HZWZ", "filetype": ""}'},
        {'title': '班子成员间的共事准则', 'type': 2, 'tag': None,
         'content': '{"type": "CJFD", "typech": "期刊", "id": "SPMF201417036", "source": "检察风云", "contributor": "中共上海市委党校", "creator": "陈尤文;张新国", "titlecopy": "班子成员间的共事准则", "title": "班子成员间的共事准则", "updatedate": "2014-11-20", "subjectcode": "J167", "subjectsubcolumncode": "J167_1", "citedtimes": "0", "downloadedtimes": "10", "date": "2014-09-01", "summary": "班子成员相处要按准则行事,无论是党政一把手,还是正副职都必须依据准则的要求规范言行,任何随意的行为都会消解班子的合力,影响班子成员之间团结与同心协力地共事。\\"跑风漏气\\"要不得故事:一班子会议刚开完,班子讨论的一些敏感问题就已经传得沸沸扬扬。单位里的一些群众听说,在奖励分配问题上班子成员有不同意见,就开始找有关领导陈述自己的意见,班子成员感到很为难,同时为自己的话被到处传而窝火!", "ispublishahead": "", "year": "2014", "issue": "17", "corejournal": "", "sourcecode": "SPMF", "filetype": "XML;EPUB"}'},
        {'title': '《计算机应用基础》分层教学的探索与实践——成都信息工程学院<em class="textred">银杏<\\/em>酒店管理学院个案研究', 'type': 2, 'tag': 'x',
         'content': '{"type": "CJFD", "typech": "期刊", "id": "ZQGZ201411146", "source": "中小企业管理与科技(中旬刊)", "contributor": "成都信息工程学院<em class=\\"textred\\">银杏<\\\\/em>酒店管理学院", "creator": "周旭东;丁莉", "titlecopy": "《计算机应用基础》分层教学的探索与实践——成都信息工程学院银杏酒店管理学院个案研究", "title": "《计算机应用基础》分层教学的探索与实践——成都信息工程学院<em class=\\"textred\\">银杏<\\\\/em>酒店管理学院个案研究", "updatedate": "2014-12-08", "subjectcode": "H131;I137", "subjectsubcolumncode": "H131_3;I137_11", "citedtimes": "0", "downloadedtimes": "22", "date": "2014-11-15", "summary": "随着高考招生规模的不断扩大,生源质量参差不齐的现象日益突出。为了切实贯彻\\"因材施教\\"教学原则,优化计算机基础课程教学效果,让每位学生得到充分发展,真正实现教育公平,从而更好地满足信息时代对多层次人才的需求,在现行班级组织框架下推行班级分层教学十分重要。", "ispublishahead": "", "year": "2014", "issue": "11", "corejournal": "", "sourcecode": "ZQGZ", "filetype": "6;1697998"}'}]

    data.extend(type_2)

    from saver.basesaver import Saver

    for d in data:
        Saver(data).save(d)



if __name__ == '__main__':

    from config.urls.zgzwconfig import ZgzwConfig

    zg = ZgzwConfig()

    json_obj = zg.parser()
    # db.connect()
    Test3.create_table()
    # # create_table()
    # Test3.create(name='hj', content=json_obj)
    # Test3.create(name='ynm', content=json_obj)
    # db.close()
    save(json_obj)