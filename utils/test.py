# encoding=utf-8
import re
from parser import ginkgoparser
from bs4 import BeautifulSoup

content = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<TITLE>银杏果的功效与作用_银杏网动态_银杏网-中国银杏网</TITLE>
<META NAME="copyright" CONTENT="中国银杏网>
<META NAME="Author" CONTENT="中国银杏网">
<META NAME="Keywords" CONTENT="银杏果的功效与作用,银杏网动态,无">
<META NAME="Robots" CONTENT="all">
<META http-equiv="Content-Type" content="text/html; charset=gb2312">
<link rel="icon" href="http://www.cnyxs.com/favicon.ico"/>
<link rel="shortcut icon" href="http://www.cnyxs.com/favicon.ico" /> 

<LINK href="images/css.css" type=text/css rel=stylesheet>
</head>
<script>
if(/Android|webOS|iPhone|iPod|BlackBerry/i.test(navigator.userAgent)) {
    window.location.href = "http://m.cnyxs.com/news_type.asp?id=34946";
}
</script>
<body bgcolor="#ffffff" leftmargin="0" topmargin="0" marginheight="0" marginwidth="0"><DIV class="topnav">
<DIV class="site-nav">


<UL class="quick-menu">
  <LI class="sitenav-mobile">您好，欢迎来到<a href=http://www.cnyxs.com/>中国银杏网</a> </LI>
  <LI><A style="color: rgb(255, 102, 0);" 
  href="http://www.cnyxs.com/user_dl.asp">请登录 </A></LI>
  <LI><A href="http://www.cnyxs.com/user_zc.asp" target="_blank">免费注册</A></LI>
  <LI class="remove"><A href="http://www.cnyxs.com/fabu.asp">发布信息</A></LI>
   <LI class="remove"><A href="http://www.cnyxs.com/zhuomian.asp">下载到桌面</A></LI>
  </UL>


<UL class="weibo">
<a href="http://e.weibo.com/zgyxcom" target="_blank"><img src="images/ico_t_sina.gif" alt="新浪微博" vspace="0" border="0"></a>
<a href="http://e.weibo.com/zgyxcom" target="_blank" ref="nofollow">中国银杏网</a><a href="http://e.weibo.com/zgyxcom" target="_blank"><img src="images/ico_t_sinav.gif" border="0"></a>   
 <a href="http://t.qq.com/zgyxcom/" target="_blank" ref="nofollow"><img src="images/ico_t_qq.gif" alt="腾迅微博" border="0"></a>
</UL>

</DIV>
</DIV>  
<DIV class="header">
<DIV class="masthead">
<DIV class="logo"><A title="中国银杏行业门户网站" href="http://www.cnyxs.com/" target="_blank"><IMG src="http://www.cnyxs.com/images/logo.gif" 
alt="中国银杏网" border="0"></A></DIV>

<DIV class="sj">
<a href="http://www.cnyxs.com/yinxingshu/" target="_blank">银杏树</a>  <a href="http://www.cnyxs.com/yinxingguo/" target="_blank">银杏果</a> 

              <a href="http://www.cnyxs.com/yinxingye/" target="_blank">银杏叶</a> <a href="http://www.cnyxs.com/yinxingcha/" target="_blank">银杏茶</a> <a href="http://www.cnyxs.com/yinxingjiu/" target="_blank">银杏酒</a>  <a href="http://www.cnyxs.com/baiguo/">白果</a><br />
			  
         <a href="http://www.cnyxs.com/yinxingpenjing/" target="_blank">银杏盆景</a>   <a href="http://www.cnyxs.com/yinxinghuangtong/" target="_blank">银杏黄酮</a> <a href="http://www.cnyxs.com/yinxingyepian/" target="_blank">银杏叶片</a> <a href="http://www.cnyxs.com/" target="_blank">银杏叶提取物</a>
</DIV>



<DIV class="zx">
<a href="http://www.cnyxs.com/xw.asp?lb=银杏新闻" target="_blank">银杏新闻</a> <a href="http://www.cnyxs.com/xw.asp?lb=银杏文化" target="_blank">银杏文化</a> <a href="http://www.cnyxs.com/xw.asp?lb=银杏科技" target="_blank">银杏科技</a>  <a href="http://www.cnyxs.com/xw.asp?lb=银杏学院" target="_blank">银杏学院</a> <a href="http://www.cnyxs.com/xw.asp?lb=帮助中心" target="_blank">帮助中心</a><br /> 
<a href="http://www.cnyxs.com/zp.asp" target="_blank">招聘频道</a> <a href="http://www.cnyxs.com/rc.asp" target="_blank">人才频道</a>  <a href="http://www.cnyxs.com/tougao.asp" target="_blank">在线投稿</a>  <a href="http://www.cnyxs.com/xw.asp?lb=银杏价格" target="_blank">银杏价格</a> <a href="http://www.cnyxs.com/xw.asp?lb=银杏网" target="_blank">本站动态</a> 
</DIV>

<DIV class="fz">
<a href="http://www.cnyxs.com/pizhou/" target="_blank">江苏邳州</a> <a href="http://www.cnyxs.com/tancheng/" target="_blank">山东郯城</a><br />
 <a href="http://www.cnyxs.com/taixing/" target="_blank">江苏泰兴</a> <a href="http://www.cnyxs.com/anlu/" target="_blank">湖北安陆</a> 
 <br />
</DIV>

</DIV>
</DIV>

</DIV>
<!--导航开始-->
<DIV class="gb_nav">
<LI><A class="ahover1" href="http://www.cnyxs.com/">首页</A>
<LI><A href="http://www.cnyxs.com/gqxx.asp?lb=供应">供应</A>
<LI><A href="http://www.cnyxs.com/gqxx.asp?lb=求购">求购</A>
<LI><A href="http://www.cnyxs.com/qy.asp">企业</A>
<LI><A href="http://www.cnyxs.com/cp.asp">产品</A>
<LI><A href="http://www.cnyxs.com/jg.asp">行情</A>
<LI><A href="http://www.cnyxs.com/zh.asp">展会</A>
<LI><A href="http://www.cnyxs.com/ztbd.asp">专题</A>
<LI><A href="http://www.cnyxs.com/photo.asp">图片</A>
<LI><A href="http://www.cnyxs.com/blog/">博客</A>
<LI><A href="http://hao.cnyxs.com/">网址</A>
<LI><A href="http://www.cnyxs.com/qq/">QQ群</A>
<LI><A href="http://www.cnyxs.com/cnyxs/">旧版</A></LI></DIV>
  <!--导航结束-->
 <SCRIPT src="http://www.cnyxs.com/top.js?v=1"></SCRIPT>

<div align=center>
<table width="980" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td width="732" valign="top"><table width="730" border="0" cellspacing="0" cellpadding="0">
      <tr>
        <td align="center" style="PADDING-LEFT: 10px; PADDING-TOP: 10px; PADDING-bottom: 10px;line-height:400%;">
          <table width="100%" border="0" align="center" cellpadding="00" cellspacing="0" background="images/top_bg3.jpg">
            <tr>
              <td width="2%" height="29"><img src="images/detail_c1_02.jpg" width="12" height="12" hspace="6" /></td>
              <td width="98%" height="29" align="left">
                你当前的位置：<a href="http://www.cnyxs.com" target="_blank">中国银杏网</a>&gt;&gt;
                
                <a href="http://www.cnyxs.com/xw.asp?lb=银杏网" target="_blank"><b>银杏网</b></a>
                
                &gt;&gt; <a href="http://www.cnyxs.com/news.asp?lb=银杏网动态" target="_blank">银杏网动态</a> </td>
            </tr>
          </table>
          </td>
      </tr>
      <tr>
        <td align="center" style="PADDING-LEFT: 10px; PADDING-TOP: 10px; PADDING-bottom: 10px;line-height:400%;"><h1>银杏果的功效与作用</h1>
          <table width="98%" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td><hr size="1" /></td>
  </tr>
</table></td>
      </tr>
      
      <tr>
        <td align="center"><a href="http://www.cnyxs.com/tougao.asp"><font color="red"><b>我要投稿</b></font></a> 作者：<font color="#990000">中国银杏网</font> 出处：<font color="#990000">中国银杏网 </font> 时间：<font color="#990000">2019/5/31</font>　 类别：<a href="http://www.cnyxs.com/news.asp?lb=银杏网动态" target="_blank"><font color="#990000">银杏网动态</font></a> 人气：<font color="#990000">150 </font></td>
      </tr>
      <tr>
        <td height="480" valign="top" style="PADDING-LEFT: 10px; PADDING-TOP: 10px;line-height:200%;font-size:15px;text-align:left;"><p>　　<a href=http://www.cnyxs.com/ target=_blank title=银杏 alt=银杏><font color=#ff0000><b>银杏</b></font></a>果俗称生<a href=http://www.cnyxs.com/baiguo/ target=_blank title=白果 alt=白果><font color=#ff0000><b>白果</b></font></a>，也是<a href=http://www.cnyxs.com/yinxingshu/ target=_blank title=银杏树 alt=银杏树>银杏树</a>的种子。<a href=http://www.cnyxs.com/yinxingshu/ target=_blank title=白果树 alt=白果树>白果树</a>雌雄异株，单性花，白果树可以用扦插繁殖，也可以种子繁殖，用种子繁殖的白果树要20-30年才能结果，所以白果树又叫公孙树。白果树是我国特有品种，被称为地球上的活化石，我国江苏泰兴是白果之乡。</p><p>　　<a href=http://www.cnyxs.com/yinxingguo/ target=_blank title=银杏果 alt=银杏果>银杏果</a>的营养价值</p><p>　　银杏果含有多种营养元素，除淀粉、蛋白质、脂肪、糖类之外，还含有维生素c，核黄素、胡萝卜素、钙、磷、铁、钾、镁等微量元素，以及银杏酸、白果酚、五碳多糖、脂固醇等成分。具有益肺气、治咳喘、止带虫、缩小便、平皴皱、护血管、增加血流量等食疗作用和医用效果。</p><p>　　营养成分</p><p>　　每100克白果中含蛋白质6.4克，脂肪2.4克，碳水化合物36克，粗纤维1.2克，胡萝卜素320微克，核黄素50微克，蔗糖5.2克，还原糖1.1克，钾19毫克，钙10毫克，磷218毫克，铁l毫克。</p><p>　　白果是营养价值丰富的食物，可润肺，定喘，涩精，止带，寒热皆宜。</p><p>　　银杏果的功效与作用</p><p>　　1、促进血液循环，因此能预防心脑血管疾病、脑血栓与中风;</p><p>　　2、预防冠心病、心绞痛、高血压、高血脂、高血糖;</p><p>　　3、增强记忆力预防老年痴呆症;</p><p>　　4、延缓衰老增强细胞繁殖力，延长细胞寿命;</p><p>　　5、抵抗辐射，增加机体免疫力，能有效缓解辐射对骨骼细胞增殖的抑制作用;</p><p>　　6、含丰富的维生素和优质的水溶蛋白，有良好的护肝解毒、修复肝组织损伤的功效;</p><p>　　7、抑制和杀伤肿瘤细胞，减轻肿瘤患者在化疗、放疗后的副作用，对升高白细胞有确切效果;</p><p>　　8、肠胃病的“救”星，减肥的天然珍品;</p><p>　　9、养颜护肤，美容佳品，柔嫩肌肤，防止皮肤粗糙，延缓细胞衰老，保持青春魅力;　　10、减轻头痛、耳鸣、晕眩、健忘、多梦、手脚冰等症状。 
主治哮喘，痰嗽，白带，白浊，遗精，淋病，小便频数。</p><p>　　银杏果常用吃法</p><p>　　一、带壳炒炸类：</p><p>　　1、椒盐白果：</p><p>　　做法： 取带壳白果一碟，用椒盐和白果一起放在锅内炒炸至熟，即可去壳食用。</p><p>　　要即炒即吃、趁热食用。热食食之可口清香，冷食食之干苦无味。招待客人时，每桌一碟，150-200克为宜。</p><p>　　2、简单的是用湿毛巾或信封将白果包住，放入微波炉小火二三分钟，听到啪啪响，将其爆开就可食用，清莹如玉，气味很香，口感软糯。</p><p>　　二、去壳甜食类：</p><p>　　1、白果粥：益元气、补五脏、抗衰老，老年、体弱多病者尤佳。正常人食之健体。宜家庭食用。</p><p>　　做法： 白果仁(去壳后用沸水烫去内种皮)6-10粒，冰糖少量，粳米2两，水适量，同时放入锅中，文火煮熟即成。以粳米成糊糜状即可。</p><p>　　白果宜与其他淡甜低糖的米粥类相配，如白果八宝粥、白果绿豆粥、白果沙参莲子粥等，糖以冰糖、白糖为宜。</p><p>　　2、小吃中用来做甜菜，桂花白果，冰糖白果。</p><p>　　三、白果汤圆：</p><p>　　做法： 将白果仁25克烘脆，研粉，鸡油熬熟，面粉炒黄，黑芝麻炒香捣烂。</p><p>　　将蜂蜜压成泥状，加入白糖、白果粉、黑芝麻，和上鸡油加炒面，揉成馅儿。</p><p>　　将糯米粉合匀，分成小团，包上馅儿，作成汤圆。</p><p>　　待锅内水开至沸，将汤圆下锅，文火煮至汤圆浮在水面上3-5分钟即成。</p><p>　　特点： 馅内加入白果，有祝福&quot;千秋长存&quot;之意。</p><p><br/></p>
        </span></td>
      </tr>
      
      <tr>
        <td align="left"><table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td width="18%"></td>
            <td width="82%"></td>
          </tr>
        </table> 本文地址:<a href="http://www.cnyxs.com/news_type.asp?id=34946">http://www.cnyxs.com/news_type.asp?id=34946</a>
        <br />
        
 </td>
      </tr>

      <tr>
        <td><!-- Baidu Button BEGIN -->
<div id="bdshare" class="bdshare_t bds_tools_32 get-codes-bdshare">
<a class="bds_tsina"></a>
<a class="bds_tqq"></a>
<a class="bds_qzone"></a>
<a class="bds_t163"></a>
<a class="bds_tsohu"></a>
<a class="bds_thx"></a>
<a class="bds_tfh"></a>
<a class="bds_people"></a>
<a class="bds_kaixin001"></a>
<a class="bds_tieba"></a>
<a class="bds_renren"></a>
<a class="bds_hi"></a>
<a class="bds_tqf"></a>
<a class="bds_douban"></a>
<span class="bds_more"></span>
<a class="shareCount"></a>
</div>
<script type="text/javascript" id="bdshare_js" data="type=tools&amp;uid=424789" ></script>
<script type="text/javascript" id="bdshell_js"></script>
<script type="text/javascript">
document.getElementById("bdshell_js").src = "http://bdimg.share.baidu.com/static/js/shell_v2.js?cdnversion=" + Math.ceil(new Date()/3600000)
</script>
<!-- Baidu Button END --></td>
      </tr>
      <tr>
        <td align=left>
          <b>上一篇<a href="http://www.cnyxs.com/news.asp?lb=银杏网动态" target="_blank">银杏网动态</a>文章：</b>
          <a href=http://www.cnyxs.com/news_type.asp?id=34924  target=_blank>银杏树落果原因与防治</a>
          <br />
          <b>下一篇<a href="http://www.cnyxs.com/news.asp?lb=银杏网动态" target="_blank">银杏网动态</a>文章：</b>
          没有下一条<a href=http://www.cnyxs.com/news.asp?lb=银杏网动态>银杏网动态</a>文章了！</td>
      </tr>
      <tr>
        <td align="right"><font color="#990000">【<a href="http://www.cnyxs.com/tougao.asp">我要投稿</a>】【进入<a href="http://bbs.cnyxs.com/" target="_blank">银杏论坛</a>】【推荐给朋友】【<a href="http://bbs.cnyxs.com/"><font color="#990000">发表评论</font></a>】【<a href="javascript:window.close()"><font color="#990000">关闭窗口</font></a>】</font></td>
      </tr>
    </table></td>
    <td width="206" valign="top"><table width="238" border="0" cellpadding="0" cellspacing="1" bgcolor="#D9D9D9">
      <tr>
        <td height="150" valign="top" bgcolor="#FFFFFF"><table width="100%" border="0" cellspacing="0" cellpadding="0">
            <tr>
              <td height="25" align="left" background="images/left_bg1.jpg">　<a href="http://www.cnyxs.com/photo.asp" target="_blank"><font color="#ffffff"><b>银杏图片</b></font></a></td>
            </tr>
          </table>
            
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
              <tr>
                <td align="center"><a href="http://www.cnyxs.com/news_type.asp?id=30839" target="_blank"><img src="ginkgo/edit/UploadFile/2015410144315664.jpg" width="85" height="75" hspace="2" vspace="4" border="0" 
                  align="absmiddle" /></a><br />
                    <a href="http://www.cnyxs.com/news_type.asp?id=30839" target="_blank">贺：邳州市王季</a>
                    </td>
                <td align="center">
                    <a href="http://www.cnyxs.com/news_type.asp?id=30578" target="_blank"><img src="ginkgo/edit/UploadFile/2015116134642270.jpg" width="85" height="75" hspace="2" vspace="4" border="0" 
                  align="absmiddle" /></a><br />
                    <a href="http://www.cnyxs.com/news_type.asp?id=30578" target="_blank">贺：邳州市大观</a>
                </td>
              </tr>
            </table>
          
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
              <tr>
                <td align="center"><a href="http://www.cnyxs.com/news_type.asp?id=30549" target="_blank"><img src="ginkgo/edit/UploadFile/20151993755443.jpg" width="85" height="75" hspace="2" vspace="4" border="0" 
                  align="absmiddle" /></a><br />
                    <a href="http://www.cnyxs.com/news_type.asp?id=30549" target="_blank">贺：邳州市锦鸿</a>
                    </td>
                <td align="center">
                    <a href="http://www.cnyxs.com/news_type.asp?id=30529" target="_blank"><img src="ginkgo/edit/UploadFile/201515141840900.jpg" width="85" height="75" hspace="2" vspace="4" border="0" 
                  align="absmiddle" /></a><br />
                    <a href="http://www.cnyxs.com/news_type.asp?id=30529" target="_blank">贺：硕阳洋绿化</a>
                </td>
              </tr>
            </table>
          </td>
      </tr>
    </table>
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr>
          <td height="3"></td>
        </tr>
      </table>
      <table width="238" border="0" cellpadding="0" cellspacing="1" bgcolor="#D9D9D9">
        <tr>
          <td height="150" align="center" valign="top" bgcolor="#FFFFFF"><table width="100%" border="0" cellspacing="0" cellpadding="0">
              <tr>
                <td height="25" align="left" background="images/left_bg1.jpg">　
                    
                    <a href="http://www.cnyxs.com/xw.asp?lb=银杏网" target="_blank"><font color="#ffffff"><b>银杏网</b></font></a>
                    
                    <font color="#ffffff">相关主题</font></td>
              </tr>
            </table>
              <table width="100%" border="0" cellspacing="1" cellpadding="0">
                <tr>
                  <td height="7"></td>
                </tr>
              </table>
              
              <table cellspacing="0" cellpadding="0" width="100%" align="center" 
border="0">
                </td>
                </tr>
                </td>
                </tr>
                
                <tr>
                  <td align="left" valign="top"> · <a href="http://www.cnyxs.com/ztt.asp?id=193" target="_blank">中国银杏网银杏供求信息平台</a>
                      </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                
                <tr>
                  <td align="left" valign="top"> · <a href="http://www.cnyxs.com/ztt.asp?id=12" target="_blank">中国银杏网活动专题</a>
                      </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                </td>
                </tr>
                
              </table>
              </td>
        </tr>
      </table>
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr>
          <td height="3"></td>
        </tr>
      </table>
      <table width="238" border="0" cellpadding="0" cellspacing="1" bgcolor="#D9D9D9">
        <tr>
          <td height="150" align="center" valign="top" bgcolor="#FFFFFF"><table width="100%" border="0" cellspacing="0" cellpadding="0">
              <tr>
                <td height="25" align="left" background="images/left_bg1.jpg">　
                    <a href="http://www.cnyxs.com/news.asp?lb=银杏网动态" target="_blank"><font color="#ffffff"><b>银杏网动态</b></font></a>
           
</td>
              </tr>
            </table>
              <table width="100%" border="0" cellspacing="1" cellpadding="0">
                <tr>
                  <td height="7"></td>
                </tr>
              </table>
              
              <table cellspacing="0" cellpadding="0" width="100%" align="center" 
border="0">
                
                <tr>
                  <td align="left" valign="top"> · <a href="http://www.cnyxs.com/news_type.asp?id=34946" target="_blank">银杏果的功效与作用</a>
                      </td>
                </tr>
                
                <tr>
                  <td align="left" valign="top"> · <a href="http://www.cnyxs.com/news_type.asp?id=34924" target="_blank">银杏树落果原因与防治</a>
                      </td>
                </tr>
                
                <tr>
                  <td align="left" valign="top"> · <a href="http://www.cnyxs.com/news_type.asp?id=34923" target="_blank">银杏树在种植上需要注意什么</a>
                      </td>
                </tr>
                
                <tr>
                  <td align="left" valign="top"> · <a href="http://www.cnyxs.com/news_type.asp?id=30268" target="_blank">强化措施，确保银杏保健食品开发质量</a>
                      </td>
                </tr>
                
                <tr>
                  <td align="left" valign="top"> · <a href="http://www.cnyxs.com/news_type.asp?id=30224" target="_blank">银杏苗树形 在市场交易中的实际意义</a>
                      </td>
                </tr>
                
                <tr>
                  <td align="left" valign="top"> · <a href="http://www.cnyxs.com/news_type.asp?id=30187" target="_blank">银杏树的木材被得到了从分的利用</a>
                      </td>
                </tr>
                
              </table>
            </td>
        </tr>
      </table>
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr>
          <td height="3"></td>
        </tr>
      </table>
      <table width="238" border="0" cellpadding="0" cellspacing="1" bgcolor="#D9D9D9">
        <tr>
          <td height="150" align="left" valign="top" bgcolor="#FFFFFF"><table width="100%" border="0" cellspacing="0" cellpadding="0">
              <tr>
                <td height="25" align="left" background="images/left_bg1.jpg">　<b><font color="#fffffff">最新银杏报道</font></b></td>
              </tr>
            </table>
              
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34949" title="银杏树价格按什么计算?怎么计算银杏树价格?" target="_blank">银杏树价格按什么计算?怎么</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34948" title="银杏叶也能做枕头了？好处还不少" target="_blank">银杏叶也能做枕头了？好处还</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34947" title="银杏树的几种繁殖方法，你知道多少？" target="_blank">银杏树的几种繁殖方法，你知</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34946" title="银杏果的功效与作用" target="_blank">银杏果的功效与作用</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34945" title="如何购买银杏树，银杏树价格怎么样?" target="_blank">如何购买银杏树，银杏树价格</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34944" title="银杏树在哪里风水好，屋后和院子内能栽种吗" target="_blank">银杏树在哪里风水好，屋后和</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34943" title="银杏树市场价格今年怎么样？" target="_blank">银杏树市场价格今年怎么样？</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34942" title="听养老领域专家王锦谈中国人如何养老" target="_blank">听养老领域专家王锦谈中国人</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34941" title="与银杏树的十年之约 青岛公交志愿者认养树木已成材" target="_blank">与银杏树的十年之约 青岛公</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34940" title="21中师生挥锹种下银杏树 学生与181棵小树共成长" target="_blank">21中师生挥锹种下银杏树 </a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34939" title="想要银杏树尽快结果，这些知识得记牢！" target="_blank">想要银杏树尽快结果，这些知</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34938" title="银杏树被“剃头” 杭州德胜东村的居民为啥纷纷点赞" target="_blank">银杏树被“剃头” 杭州德胜</a><br />
            </td>
        </tr>
      </table></td>
  </tr>
</table></div>
<table cellspacing="0" cellpadding="0" width="980" align="center" border="0">
  <tbody>
    <tr>
      <td height="8"><img height="1" 
      src="mages\spacer.gif" 
    width="1" /></td>
    </tr>
  </tbody>
</table>
<div align=center>
  <table width="980" border="0" align="center" cellpadding="0" cellspacing="0">
    <tr>
      <td width="34" height="30" align="right"><img src="images/icon_warning_24x24.gif" alt="银杏" width="24" height="24" hspace="5" /></td>
      <td width="946" class="font7"><a href="http://www.cnyxs.com/" target="_blank"><b><font color="red">中国银杏网</font></b></a><b>免责声明：</b> 以上所展示的信息由企业或个人自行提供，内容的真实性、准确性和合法性由发布企业或个人负责。<a href="http://www.cnyxs.com/" target="_blank">中国银杏网</a>对此不承担任何保证责任。本站信息来自互联网,可供参考不能作为真实依据,另本站如有转载或引用文章涉及版权问题,请速与我们联系 QQ:18708455</td>
    </tr>
  </table>
</div>
<!--底部开始-->
<DIV class="foot">
<SCRIPT type="text/javascript" src="images/foot.js"></SCRIPT><p>
<a href="http://www.cnyxs.com">中国银杏网</a>关键字:<a href="http://www.cnyxs.com" target="_blank">银杏</a>-<a href="http://www.cnyxs.com/yinxingshu/" target="_blank">银杏树</a>-<a href="http://www.cnyxs.com" target="_blank">银杏树价格</a>-<a href="http://www.cnyxs.com/yinxingguo/" target="_blank">银杏果</a> - <a href="http://www.cnyxs.com/yinxingye/" target="_blank">银杏叶</a> - <a href="http://www.cnyxs.com/yinxingcha/" target="_blank">银杏茶</a> - <a href="http://www.cnyxs.com/baiguo/" target="_blank">白果</a></p>
<P>
咨询热线：0516-<SPAN class="footkuang">81581111 </SPAN></p>
<P>本网英文域名:<STRONG style="color: rgb(255, 0, 0);"> <A 
href="http://www.cnyxs.com/">www.cnyxs.com</A></STRONG> 中文域名:<STRONG style="color: rgb(255, 0, 0);"> <A 
href="http://www.cnyxs.com/">中国银杏网</A></STRONG>.com－中国最专业的<A style="padding: 0px;" 
href="http://www.cnyxs.com/">银杏</A><a href="http://www.cnyxs.com/baiguo/" target="_blank">白果</a>行业门户网站</P>
<P><A href="http://www.cnyxs.com/" rel="nofollow">中国银杏网</A>  版权所有 &copy; 2005-2020 苏ICP备07021153号 <script src="http://s22.cnzz.com/stat.php?id=3259912&web_id=3259912" language="JavaScript"></script></p>
</DIV>
<!--底部结束-->

</body>
</html>
"""

main_page = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<TITLE>银杏新闻-中国银杏网</TITLE>
<META http-equiv="Content-Type" content="text/html; charset=gb2312">
<LINK href="http://www.cnyxs.com/images/css.css" type=text/css rel=stylesheet>
<link rel="icon" href="http://www.cnyxs.com/favicon.ico"/><link rel="shortcut icon" href="http://www.cnyxs.com/favicon.ico" /> 
<META NAME="copyright" CONTENT="中国银杏网-www.cnyxs.com">
<META NAME="Author" CONTENT="中国银杏网-www.cnyxs.com">
<META NAME="Robots" CONTENT="all">
<META NAME="Keywords" CONTENT="银杏新闻,中国银杏网">
<META NAME="Description" CONTENT="银杏新闻,,银杏新闻,企业动态,市场分析,名企推荐,银杏人物,地方传真,聚焦三农,中国银杏网-中国银杏行业门户网站">
</head>
<body bgcolor="#ffffff" leftmargin="0" topmargin="0" marginheight="0" marginwidth="0"><DIV class="topnav">
<DIV class="site-nav">


<UL class="quick-menu">
  <LI class="sitenav-mobile">您好，欢迎来到<a href=http://www.cnyxs.com/>中国银杏网</a> </LI>
  <LI><A style="color: rgb(255, 102, 0);" 
  href="http://www.cnyxs.com/user_dl.asp">请登录 </A></LI>
  <LI><A href="http://www.cnyxs.com/user_zc.asp" target="_blank">免费注册</A></LI>
  <LI class="remove"><A href="http://www.cnyxs.com/fabu.asp">发布信息</A></LI>
   <LI class="remove"><A href="http://www.cnyxs.com/zhuomian.asp">下载到桌面</A></LI>
  </UL>


<UL class="weibo">
<a href="http://e.weibo.com/zgyxcom" target="_blank"><img src="images/ico_t_sina.gif" alt="新浪微博" vspace="0" border="0"></a>
<a href="http://e.weibo.com/zgyxcom" target="_blank" ref="nofollow">中国银杏网</a><a href="http://e.weibo.com/zgyxcom" target="_blank"><img src="images/ico_t_sinav.gif" border="0"></a>   
 <a href="http://t.qq.com/zgyxcom/" target="_blank" ref="nofollow"><img src="images/ico_t_qq.gif" alt="腾迅微博" border="0"></a>
</UL>

</DIV>
</DIV>  
<DIV class="header">
<DIV class="masthead">
<DIV class="logo"><A title="中国银杏行业门户网站" href="http://www.cnyxs.com/" target="_blank"><IMG src="http://www.cnyxs.com/images/logo.gif" 
alt="中国银杏网" border="0"></A></DIV>

<DIV class="sj">
<a href="http://www.cnyxs.com/yinxingshu/" target="_blank">银杏树</a>  <a href="http://www.cnyxs.com/yinxingguo/" target="_blank">银杏果</a> 

              <a href="http://www.cnyxs.com/yinxingye/" target="_blank">银杏叶</a> <a href="http://www.cnyxs.com/yinxingcha/" target="_blank">银杏茶</a> <a href="http://www.cnyxs.com/yinxingjiu/" target="_blank">银杏酒</a>  <a href="http://www.cnyxs.com/baiguo/">白果</a><br />
			  
         <a href="http://www.cnyxs.com/yinxingpenjing/" target="_blank">银杏盆景</a>   <a href="http://www.cnyxs.com/yinxinghuangtong/" target="_blank">银杏黄酮</a> <a href="http://www.cnyxs.com/yinxingyepian/" target="_blank">银杏叶片</a> <a href="http://www.cnyxs.com/" target="_blank">银杏叶提取物</a>
</DIV>



<DIV class="zx">
<a href="http://www.cnyxs.com/xw.asp?lb=银杏新闻" target="_blank">银杏新闻</a> <a href="http://www.cnyxs.com/xw.asp?lb=银杏文化" target="_blank">银杏文化</a> <a href="http://www.cnyxs.com/xw.asp?lb=银杏科技" target="_blank">银杏科技</a>  <a href="http://www.cnyxs.com/xw.asp?lb=银杏学院" target="_blank">银杏学院</a> <a href="http://www.cnyxs.com/xw.asp?lb=帮助中心" target="_blank">帮助中心</a><br /> 
<a href="http://www.cnyxs.com/zp.asp" target="_blank">招聘频道</a> <a href="http://www.cnyxs.com/rc.asp" target="_blank">人才频道</a>  <a href="http://www.cnyxs.com/tougao.asp" target="_blank">在线投稿</a>  <a href="http://www.cnyxs.com/xw.asp?lb=银杏价格" target="_blank">银杏价格</a> <a href="http://www.cnyxs.com/xw.asp?lb=银杏网" target="_blank">本站动态</a> 
</DIV>

<DIV class="fz">
<a href="http://www.cnyxs.com/pizhou/" target="_blank">江苏邳州</a> <a href="http://www.cnyxs.com/tancheng/" target="_blank">山东郯城</a><br />
 <a href="http://www.cnyxs.com/taixing/" target="_blank">江苏泰兴</a> <a href="http://www.cnyxs.com/anlu/" target="_blank">湖北安陆</a> 
 <br />
</DIV>

</DIV>
</DIV>

</DIV>
<!--导航开始-->
<DIV class="gb_nav">
<LI><A class="ahover1" href="http://www.cnyxs.com/">首页</A>
<LI><A href="http://www.cnyxs.com/gqxx.asp?lb=供应">供应</A>
<LI><A href="http://www.cnyxs.com/gqxx.asp?lb=求购">求购</A>
<LI><A href="http://www.cnyxs.com/qy.asp">企业</A>
<LI><A href="http://www.cnyxs.com/cp.asp">产品</A>
<LI><A href="http://www.cnyxs.com/jg.asp">行情</A>
<LI><A href="http://www.cnyxs.com/zh.asp">展会</A>
<LI><A href="http://www.cnyxs.com/ztbd.asp">专题</A>
<LI><A href="http://www.cnyxs.com/photo.asp">图片</A>
<LI><A href="http://www.cnyxs.com/blog/">博客</A>
<LI><A href="http://hao.cnyxs.com/">网址</A>
<LI><A href="http://www.cnyxs.com/qq/">QQ群</A>
<LI><A href="http://www.cnyxs.com/cnyxs/">旧版</A></LI></DIV>
  <!--导航结束-->
 <SCRIPT src="http://www.cnyxs.com/top.js?v=1"></SCRIPT>
<div align="center">
<table width="980" height="126" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td width="242" valign="top"><table width="238" border="0" cellpadding="0" cellspacing="1" bgcolor="#D9D9D9">
      <tr>
        <td height="150" align="center" valign="top" bgcolor="#FFFFFF"><table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td height="25" align="left" background="images/left_bg1.jpg">　
	  <a href="http://www.cnyxs.com/xw.asp?lb=" target="_blank"><font color="#ffffff"><b></b></font></a>
	   </td>
          </tr>
        </table>
              
              <table width="157" border="0" cellspacing="0" cellpadding="0">
                <tr>
                  <td width="157" height="25" align="left" background="images/bg_title.jpg">&nbsp;&nbsp;
                      <a href=http://www.cnyxs.com/news.asp?lb=银杏新闻><font color=#000000><b>银杏新闻</b></font></a></td>
                </tr>
                <tr>
                  <td height="5"></td>
                </tr>
              </table>
          
              <table width="157" border="0" cellspacing="0" cellpadding="0">
                <tr>
                  <td width="157" height="25" align="left" background="images/bg_title.jpg">&nbsp;&nbsp;
                      <a href=http://www.cnyxs.com/news.asp?lb=银杏新闻><font color=#000000><b>银杏新闻</b></font></a></td>
                </tr>
                <tr>
                  <td height="5"></td>
                </tr>
              </table>
          
              <table width="157" border="0" cellspacing="0" cellpadding="0">
                <tr>
                  <td width="157" height="25" align="left" background="images/bg_title.jpg">&nbsp;&nbsp;
                      <a href=http://www.cnyxs.com/news.asp?lb=企业动态><font color=#000000><b>企业动态</b></font></a></td>
                </tr>
                <tr>
                  <td height="5"></td>
                </tr>
              </table>
          
              <table width="157" border="0" cellspacing="0" cellpadding="0">
                <tr>
                  <td width="157" height="25" align="left" background="images/bg_title.jpg">&nbsp;&nbsp;
                      <a href=http://www.cnyxs.com/news.asp?lb=市场分析><font color=#000000><b>市场分析</b></font></a></td>
                </tr>
                <tr>
                  <td height="5"></td>
                </tr>
              </table>
          
              <table width="157" border="0" cellspacing="0" cellpadding="0">
                <tr>
                  <td width="157" height="25" align="left" background="images/bg_title.jpg">&nbsp;&nbsp;
                      <a href=http://www.cnyxs.com/news.asp?lb=名企推荐><font color=#000000><b>名企推荐</b></font></a></td>
                </tr>
                <tr>
                  <td height="5"></td>
                </tr>
              </table>
          
              <table width="157" border="0" cellspacing="0" cellpadding="0">
                <tr>
                  <td width="157" height="25" align="left" background="images/bg_title.jpg">&nbsp;&nbsp;
                      <a href=http://www.cnyxs.com/news.asp?lb=银杏人物><font color=#000000><b>银杏人物</b></font></a></td>
                </tr>
                <tr>
                  <td height="5"></td>
                </tr>
              </table>
          
              <table width="157" border="0" cellspacing="0" cellpadding="0">
                <tr>
                  <td width="157" height="25" align="left" background="images/bg_title.jpg">&nbsp;&nbsp;
                      <a href=http://www.cnyxs.com/news.asp?lb=地方传真><font color=#000000><b>地方传真</b></font></a></td>
                </tr>
                <tr>
                  <td height="5"></td>
                </tr>
              </table>
          
              <table width="157" border="0" cellspacing="0" cellpadding="0">
                <tr>
                  <td width="157" height="25" align="left" background="images/bg_title.jpg">&nbsp;&nbsp;
                      <a href=http://www.cnyxs.com/news.asp?lb=聚焦三农><font color=#000000><b>聚焦三农</b></font></a></td>
                </tr>
                <tr>
                  <td height="5"></td>
                </tr>
              </table>
          
          <table width="157" border="0" cellspacing="0" cellpadding="0">
            <tr>
              <td width="157" height="25" align="left" background="images/bg_title.jpg">&nbsp;&nbsp; 
          <a href="http://bbs.cnyxs.com/" target="_blank"><font color="#000000"><b>银杏论坛</b></font></a>
          </td>
            </tr>
            <tr>
              <td height="5"></td>
            </tr>
          </table>
          </td>
      </tr>
    </table>
        <table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td height="3"></td>
          </tr>
        </table>
        <table width="238" border="0" cellpadding="0" cellspacing="1" bgcolor="#D9D9D9">
          <tr>
            <td height="150" align="center" valign="top" bgcolor="#FFFFFF"><table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                  <td height="25" align="left" background="images/left_bg1.jpg">　
	  <a href="http://www.cnyxs.com/xw.asp?lb=" target="_blank"><font color="#ffffff"><b></b></font></a>
	   <font color="#ffffff">相关主题</font></td>
                </tr>
              </table>
                <table width="100%" border="0" cellspacing="1" cellpadding="0">
                  <tr>
                    <td height="7"></td>
                  </tr>
                </table>
              
                <table cellspacing="0" cellpadding="0" width="100%" align="center" 
border="0">
                  
                  <tr>
                    <td align="left" valign="top"> · <a href="http://www.cnyxs.com/ztt.asp?id=195" target="_blank">2014年中国银杏产业发展论坛暨第二届中国（郯城）银杏产品交易会</a>
                        </td>
                  </tr>
                  
                  <tr>
                    <td align="left" valign="top"> · <a href="http://www.cnyxs.com/ztt.asp?id=194" target="_blank">银杏树风水</a>
                        </td>
                  </tr>
                  
                  <tr>
                    <td align="left" valign="top"> · <a href="http://www.cnyxs.com/ztt.asp?id=193" target="_blank">中国银杏网银杏供求信息平台</a>
                        </td>
                  </tr>
                  
                  <tr>
                    <td align="left" valign="top"> · <a href="http://www.cnyxs.com/ztt.asp?id=192" target="_blank">首届中国（郯城）银杏产品交易会</a>
                        </td>
                  </tr>
                  
                  <tr>
                    <td align="left" valign="top"> · <a href="http://www.cnyxs.com/ztt.asp?id=191" target="_blank">北京银杏树</a>
                        </td>
                  </tr>
                  
                  <tr>
                    <td align="left" valign="top"> · <a href="http://www.cnyxs.com/ztt.asp?id=190" target="_blank">辽宁大学银杏树</a>
                        </td>
                  </tr>
                  
                  <tr>
                    <td align="left" valign="top"> · <a href="http://www.cnyxs.com/ztt.asp?id=189" target="_blank">家庭禁忌银杏盆景</a>
                        </td>
                  </tr>
                  
                  <tr>
                    <td align="left" valign="top"> · <a href="http://www.cnyxs.com/ztt.asp?id=188" target="_blank">银杏果能吃吗 </a>
                        </td>
                  </tr>
                  
                  <tr>
                    <td align="left" valign="top"> · <a href="http://www.cnyxs.com/ztt.asp?id=187" target="_blank">银杏果的食用方法</a>
                        </td>
                  </tr>
                  
                  <tr>
                    <td align="left" valign="top"> · <a href="http://www.cnyxs.com/ztt.asp?id=186" target="_blank">银杏茶多少钱一盒</a>
                        </td>
                  </tr>
                  
                  <tr>
                    <td align="left" valign="top"> · <a href="http://www.cnyxs.com/ztt.asp?id=185" target="_blank">银杏茶哪个牌子好</a>
                        </td>
                  </tr>
                  
                  <tr>
                    <td align="left" valign="top"> · <a href="http://www.cnyxs.com/ztt.asp?id=184" target="_blank">银杏叶提取物胶囊</a>
                        </td>
                  </tr>
                  
                  <tr>
                    <td align="left" valign="top"> · <a href="http://www.cnyxs.com/ztt.asp?id=183" target="_blank">银杏盆景的鉴赏</a>
                        </td>
                  </tr>
                  
                  <tr>
                    <td align="left" valign="top"> · <a href="http://www.cnyxs.com/ztt.asp?id=182" target="_blank">银杏茶的功效与作用</a>
                        </td>
                  </tr>
                  
                  <tr>
                    <td align="left" valign="top"> · <a href="http://www.cnyxs.com/ztt.asp?id=181" target="_blank">银杏果怎么去皮</a>
                        </td>
                  </tr>
                  
                  <tr>
                    <td align="left" valign="top"> · <a href="http://www.cnyxs.com/ztt.asp?id=180" target="_blank">银杏果什么时候成熟</a>
                        </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  </td>
                  </tr>
                  
                </table>
              </td>
          </tr>
        </table>
        <table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td height="3"></td>
          </tr>
        </table>
        <table width="238" border="0" cellpadding="0" cellspacing="1" bgcolor="#D9D9D9">
          <tr>
            <td height="150" valign="top" bgcolor="#FFFFFF"><table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                  <td height="25" align="left" background="images/left_bg1.jpg">　<a href="http://www.cnyxs.com/photo.asp" target="_blank"><font color="#ffffff"><b>银杏图片</b></font></a></td>
                </tr>
              </table>
                
                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                  <tr>
                    <td><a href="http://www.cnyxs.com/news_type.asp?id=30839" target="_blank"><img src="ginkgo/edit/UploadFile/2015410144315664.jpg" width="100" height="85" hspace="2" vspace="4" border="0" 
                  align="absmiddle" /></a><br />
                        <a href="news_type.asp?id=30839" target="_blank">贺：邳州市王季</a>
                        </td>
                    <td>
                        <a href="http://www.cnyxs.com/news_type.asp?id=30578" target="_blank"><img src="ginkgo/edit/UploadFile/2015116134642270.jpg" width="100" height="85" hspace="2" vspace="4" border="0" 
                  align="absmiddle" /></a><br />
                        <a href="http://www.cnyxs.com/news_type.asp?id=30578" target="_blank">贺：邳州市大观</a>
                        </td>
                  </tr>
                </table>
              
                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                  <tr>
                    <td><a href="http://www.cnyxs.com/news_type.asp?id=30549" target="_blank"><img src="ginkgo/edit/UploadFile/20151993755443.jpg" width="100" height="85" hspace="2" vspace="4" border="0" 
                  align="absmiddle" /></a><br />
                        <a href="news_type.asp?id=30549" target="_blank">贺：邳州市锦鸿</a>
                        </td>
                    <td>
                        <a href="http://www.cnyxs.com/news_type.asp?id=30529" target="_blank"><img src="ginkgo/edit/UploadFile/201515141840900.jpg" width="100" height="85" hspace="2" vspace="4" border="0" 
                  align="absmiddle" /></a><br />
                        <a href="http://www.cnyxs.com/news_type.asp?id=30529" target="_blank">贺：硕阳洋绿化</a>
                        </td>
                  </tr>
                </table>
              
                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                  <tr>
                    <td><a href="http://www.cnyxs.com/news_type.asp?id=30377" target="_blank"><img src="ginkgo/edit/UploadFile/20141124172231147.jpg" width="100" height="85" hspace="2" vspace="4" border="0" 
                  align="absmiddle" /></a><br />
                        <a href="news_type.asp?id=30377" target="_blank">贺：邳州市尚林</a>
                        </td>
                    <td>
                        <a href="http://www.cnyxs.com/news_type.asp?id=30235" target="_blank"><img src="ginkgo/edit/UploadFile/2014102410531670.jpg" width="100" height="85" hspace="2" vspace="4" border="0" 
                  align="absmiddle" /></a><br />
                        <a href="http://www.cnyxs.com/news_type.asp?id=30235" target="_blank">贺：江苏3E苗</a>
                        </td>
                  </tr>
                </table>
              </td>
          </tr>
        </table>
        <table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td height="3"></td>
          </tr>
        </table>
        <table width="238" border="0" cellpadding="0" cellspacing="1" bgcolor="#D9D9D9">
          <tr>
            <td height="150" valign="top" bgcolor="#FFFFFF"><table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                  <td height="25" align="left" background="images/left_bg1.jpg">　<b><font color=#fffffff>最新银杏报道</font></b></td>
                </tr>
              </table>
              
·<a href="http://www.cnyxs.com/news_type.asp?id=34953" title="银杏叶保健食品市场未来可期" target="_blank">银杏叶保健食品市场未来可期</a><br />

·<a href="http://www.cnyxs.com/news_type.asp?id=34952" title="世界上最美的几种树，银杏树被称为植物界的活化石，寿命极长" target="_blank">世界上最美的几种树，银杏树</a><br />

·<a href="http://www.cnyxs.com/news_type.asp?id=34951" title="揭开银杏家世之谜" target="_blank">揭开银杏家世之谜</a><br />

·<a href="http://www.cnyxs.com/news_type.asp?id=34950" title="想要银杏树尽快结果，这些知识得记牢！" target="_blank">想要银杏树尽快结果，这些知</a><br />

·<a href="http://www.cnyxs.com/news_type.asp?id=34949" title="银杏树价格按什么计算?怎么计算银杏树价格?" target="_blank">银杏树价格按什么计算?怎么</a><br />

·<a href="http://www.cnyxs.com/news_type.asp?id=34948" title="银杏叶也能做枕头了？好处还不少" target="_blank">银杏叶也能做枕头了？好处还</a><br />

·<a href="http://www.cnyxs.com/news_type.asp?id=34947" title="银杏树的几种繁殖方法，你知道多少？" target="_blank">银杏树的几种繁殖方法，你知</a><br />
</td>
          </tr>
        </table>
        <table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td height="3"></td>
          </tr>
        </table>
    </td>
    <td width="738" valign="top"><table width="100%" border="0" align="center" cellpadding="0" cellspacing="0" background="images/top_bg3.jpg">
      <tr>
        <td width="738" height="29"><img src="images/detail_c1_02.jpg" width="12" height="12" hspace="6" />
            
          你当前的位置：<a href="http://www.cnyxs.com"><b>中国银杏网</b></a><a href="http://www.cnyxs.com">银杏</a>&gt;&gt;
	  <a href="http://www.cnyxs.com/xw.asp?lb=" target="_blank"><b></b></a>
	    &gt;&gt; <a href="http://www.cnyxs.com/news.asp?lb=银杏新闻"><b>银杏新闻</b></a> </td>
      </tr>
    </table>
      <table width="650" border="0" align="center" cellpadding="0" cellspacing="0">
        <tr>
          <td height="30" align="center"><a class=Black href=http://www.cnyxs.com/news.asp?lb=银杏新闻&gjz=>首页</a>&nbsp;&nbsp;<a class=Black href=http://www.cnyxs.com/news.asp?lb=银杏新闻&pageno=87&gjz=>上一页</a>&nbsp;&nbsp;<a class=Black href=http://www.cnyxs.com/news.asp?lb=银杏新闻&pageno=89&gjz=>下一页</a>&nbsp;&nbsp;<a href=http://www.cnyxs.com/news.asp?lb=银杏新闻&pageno=182&gjz=>尾页</a>&nbsp;&nbsp;第88页/共182页&nbsp;&nbsp;共8164条银杏新闻</td>
        </tr>
      </table>
      
      <table width="650" border="0" align="center" cellpadding="2" cellspacing="0" background="images/detail_c1_03.jpg">
	  
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=11003" target="_blank">寻找今冬最美银杏路 成都郊外更冷先变色(图)</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=11002" target="_blank">北京西山卧佛寺银杏节正式拉开帷幕</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=11001" target="_blank">银杏道旁立养眼又洗肺</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=11000" target="_blank">秋色浓郁的古银杏村</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10999" target="_blank">百年古树突然一夜消失 换来五年牢狱</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10998" target="_blank">都江堰市大观镇宿仙村现在生态好转，导致松鼠增多，危害银杏树，损失惨重</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10997" target="_blank">上塘路将多一片金灿灿的美景　要种一千多棵银杏</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10996" target="_blank">上塘路（大关路—登云路段）银杏林荫道打造工程已开始</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10994" target="_blank">诱人无数 网友拍电子科大银杏美景</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10993" target="_blank">北京的银杏叶黄了</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10992" target="_blank">深秋，小浦八都岕观银杏</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10991" target="_blank">看银杏金黄 赏枫叶火红</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10990" target="_blank">走马古银杏长廊体验原生态美景</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10989" target="_blank">霜染银杏秋色浓</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10988" target="_blank">石家庄：长安公园银杏林尽显斑斓秋色（图）</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10987" target="_blank">太原：迎泽公园内银杏树进入最佳观赏期(图)</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10986" target="_blank">古银杏旅游节亮点纷呈成效突出</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10985" target="_blank">神仙树大院拉锯战 规划局建议宣传广告要谨慎</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10984" target="_blank">护肤品推陈出新 银杏叶极度滋养膏喜得桂冠</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10983" target="_blank">北京西山卧佛寺银杏节正式拉开序幕</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10982" target="_blank">都江堰一座826户村庄种植银杏年销售额亿元</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10981" target="_blank">成都推行银杏等落叶只拣不扫为市民留美景(图)</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10979" target="_blank">四问长兴银杏林 村民为您讲解美丽背后的奥秘</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10978" target="_blank">"金秋美景"——大觉寺银杏迎四方宾客</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10977" target="_blank">节庆搭台 经贸唱戏</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10976" target="_blank">走进临安指南村 探访华东最美古村</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10975" target="_blank">聚焦神仙树大院会所变餐馆 业主维权进行时</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10974" target="_blank">银杏树下的别样风景</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10973" target="_blank">量价齐飞 花木市场“欣欣向荣” </a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10972" target="_blank">长寿之乡的千年银杏树:五六个成年人才能合抱(图)</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10971" target="_blank">肥胖者的福音：奥露娜左旋肉碱倡导健康减肥</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10970" target="_blank">城市绿了苗木俏了银杏香樟半年价翻番</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10969" target="_blank">山东郯城为3000岁"银杏王"庆功</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10968" target="_blank">千米银杏大道，非资本不足以如此奢华</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10967" target="_blank">苏城三条道路试点保留落叶景观</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10965" target="_blank">山东郯城:古郯金秋美如画</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10964" target="_blank">天目银杏知秋早 大树王国迎森博</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10963" target="_blank">叩访山村 探华东最美五大赏秋线--银杏</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10962" target="_blank">河西河旁银杏树被绑？ 原来是养护期必要手段</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10961" target="_blank">嵩县第二届千年银杏节隆重开幕</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10960" target="_blank">滁城两株千年古银杏树挂上“身份证”</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10959" target="_blank">城市绿了苗木俏了银杏香樟半年价</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10958" target="_blank">四川：城市绿了苗木俏了银杏香樟半年价</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10956" target="_blank">选用珍贵银杏树苗 "龙的传人故乡林"落户北京</a></td>
        </tr>
		
        <tr>
          <td width="1%" align="right" valign="top">&nbsp;</td>
          <td width="99%" height="26">[<a href="http://www.cnyxs.com/news.asp?lb=银杏新闻" target="_blank">银杏新闻</a>]&nbsp;<a href="http://www.cnyxs.com/news_type.asp?id=10955" target="_blank">农家遇拆迁难舍古银杏</a></td>
        </tr>
		
      </table>
      
      <table width="650" border="0" align="center" cellpadding="0" cellspacing="0">
        <tr>
          <td height="30" align="center"><a class=Black href=http://www.cnyxs.com/news.asp?lb=银杏新闻&gjz=>首页</a>&nbsp;&nbsp;<a class=Black href=http://www.cnyxs.com/news.asp?lb=银杏新闻&pageno=87&gjz=>上一页</a>&nbsp;&nbsp;<a class=Black href=http://www.cnyxs.com/news.asp?lb=银杏新闻&pageno=89&gjz=>下一页</a>&nbsp;&nbsp;<a href=http://www.cnyxs.com/news.asp?lb=银杏新闻&pageno=182&gjz=>尾页</a>&nbsp;&nbsp;第88页/共182页&nbsp;&nbsp;共8164条银杏新闻</td>
        </tr>
      </table></td>
  </tr>
</table></div>
<div align=center>
  <table width="980" border="0" align="center" cellpadding="0" cellspacing="0">
    <tr>
      <td width="34" height="30" align="right"><img src="images/icon_warning_24x24.gif" alt="银杏" width="24" height="24" hspace="5" /></td>
      <td width="946" class="font7"><a href="http://www.cnyxs.com/" target="_blank"><b><font color="red">中国银杏网</font></b></a><b>免责声明：</b> 以上所展示的信息由企业或个人自行提供，内容的真实性、准确性和合法性由发布企业或个人负责。<a href="http://www.cnyxs.com/" target="_blank">中国银杏网</a>对此不承担任何保证责任。本站信息来自互联网,可供参考不能作为真实依据,另本站如有转载或引用文章涉及版权问题,请速与我们联系 QQ:18708455</td>
    </tr>
  </table>
</div>
<!--底部开始-->
<DIV class="foot">
<SCRIPT type="text/javascript" src="images/foot.js"></SCRIPT><p>
<a href="http://www.cnyxs.com">中国银杏网</a>关键字:<a href="http://www.cnyxs.com" target="_blank">银杏</a>-<a href="http://www.cnyxs.com/yinxingshu/" target="_blank">银杏树</a>-<a href="http://www.cnyxs.com" target="_blank">银杏树价格</a>-<a href="http://www.cnyxs.com/yinxingguo/" target="_blank">银杏果</a> - <a href="http://www.cnyxs.com/yinxingye/" target="_blank">银杏叶</a> - <a href="http://www.cnyxs.com/yinxingcha/" target="_blank">银杏茶</a> - <a href="http://www.cnyxs.com/baiguo/" target="_blank">白果</a></p>
<P>
咨询热线：0516-<SPAN class="footkuang">81581111 </SPAN></p>
<P>本网英文域名:<STRONG style="color: rgb(255, 0, 0);"> <A 
href="http://www.cnyxs.com/">www.cnyxs.com</A></STRONG> 中文域名:<STRONG style="color: rgb(255, 0, 0);"> <A 
href="http://www.cnyxs.com/">中国银杏网</A></STRONG>.com－中国最专业的<A style="padding: 0px;" 
href="http://www.cnyxs.com/">银杏</A><a href="http://www.cnyxs.com/baiguo/" target="_blank">白果</a>行业门户网站</P>
<P><A href="http://www.cnyxs.com/" rel="nofollow">中国银杏网</A>  版权所有 &copy; 2005-2020 苏ICP备07021153号 <script src="http://s22.cnzz.com/stat.php?id=3259912&web_id=3259912" language="JavaScript"></script></p>
</DIV>
<!--底部结束-->

</body>
</html>
"""



LINK_PATTERN = '.*?本文地址:<a.*?href="(.*?)">.*?</a>'

PAGE_NUMS_PATTERN = '</a>&nbsp;&nbsp;下一页&nbsp;&nbsp;尾页&nbsp;&nbsp;第.*?页/共(.*?)页&nbsp;&nbsp;共.*?条银杏网动态</td>'

url = '<td.*?width="99%".*?height="26">\[.*?\]&nbsp;<a.*?href="(.*?)".*?target="_blank">.*?</a>.*?</td>'
_ = 'http://www.cnyxs.com/news_type.asp?id=34946'


