# encoding=utf-8
import re
from parser import ginkgoparser
from bs4 import BeautifulSoup

content = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<TITLE>银杏叶保健食品市场未来可期_银杏新闻_中国银杏网</TITLE>
<META http-equiv="Content-Type" content="text/html; charset=gb2312">
<meta content="width=device-width,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" name="viewport" />
<meta name="format-detection" content="telephone=no">
<META NAME="Robots" CONTENT="all">
<META NAME="Keywords" CONTENT="银杏叶保健食品市场未来可期">
<META NAME="Keywords" CONTENT="银杏叶保健食品市场未来可期,银杏新闻,无">
<link rel="stylesheet" type="text/css" href="css/skin.css">
<style>
body{background:#ffffff;}


.news_detailinfo img {width:100%;}
.pro_detail_info img {width:100%;}
.wap_job_detailcont img {width:100%;}
.wap_downfile img {width:100%;}

</style>
</head>
<body>
<div class="wapMain">
	<div class="wap_top">		
		<table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td><a href="http://m.cnyxs.com"><img src="images/1155.jpg" border="0" width="100%" height="60px"/></a></td>
  </tr>
</table>

<div class="dh"><ul>
        <li><a href="http://m.cnyxs.com">首页</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏树">银杏树</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏果">银杏果</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏叶">银杏叶</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏酒">银杏酒</a></li>
</ul>
<ul>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=白果">白果</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏茶">银杏茶</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏网">银杏网</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏盆景">银杏盆景</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏树价格">银杏价格</a></li>
</ul>
<ul>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏新闻">银杏新闻</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏文化">银杏文化</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏科技">银杏科技</a></li>
      <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏黄酮">银杏黄酮</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏学院">银杏学院</a></li>

</ul>
</div>


	</div>
<div class="wap_container edit_putHere" id="edit_putHere_area1" saveTitle="area1">
<div align="center">

  <div class="web2t">
<div class="webt1"><a href="http://m.cnyxs.com/news.asp?lb=银杏新闻" class="more"><strong>银杏新闻</strong></a></div></div>


  </div>
  </div>
  银杏新闻
	<div class="wap_label labelDis" id="1" rel="1" titles="文章内容">
	<div class="wap_news_detail">
		<div class="wap_label_content">
			<div style=" height:10px;"></div>
			<div class="news_detailtitle">银杏叶保健食品市场未来可期 </div>
			<div style=" height:10px;"></div>
			<div class="line">
				<span class="news_author">新闻类型：银杏新闻</span>
				<span class="news_time01">2019年6月26日</span>
				<div class="clear"></div>
			</div>
			<div class="news_detailinfo">
				<p>　　众所周知，银杏叶是一种中药材，同时还可以食用，被列为《可用于保健食品的物品名单》之一。自2015年“银杏叶事件”风波之后，银杏制剂药品、银杏叶保健食品行业受到很大冲击，经过监管部门的全面整治，银杏叶保健食品产业现已规范管理，市场迎来了新的生机。</p><p>　　我国是银杏的主产地，银杏叶资源丰富。现代医学研究发现，从银杏叶中可提取的有效药用成分高达160多种。其中，黄酮类化合物35种，氨基酸和多种微量元素17种。银杏叶中最具代表性的功能成分是银杏萜内酯和黄酮苷，具有消除人体内自由基和抑制血小板凝集的作用，被广泛应用于保健食品、化妆品、药品等多个领域。</p><p>　　银杏叶保健食品是国际市场上最受欢迎的植物保健食品之一，在保健食品市场占据很大份额，可见其需求量之大。它的主要作用可通过强化人体毛细血管，增强血管的抗压能力，起到较好的辅助降压作用;还能辅助调节血糖水平、减少胰岛素注射量;并可以帮助促进脑动脉或末梢血管强壮，使硬化的血管恢复一定弹性，改善变窄的血管，可使萎缩的脑细胞恢复生机，从而可辅助改善记忆力等。</p><p>　　银杏叶益处虽多，但需注意的是，直接从银杏树上摘取下来的、未经加工的银杏叶是有毒的，其中含有大量银杏酸，若食用量较大，可能导致中毒。另外，银杏叶中的主要成分黄酮类化合物是一种强力血小板激活因子抑制剂，长期服用可能会抑制血小板的凝聚功能，并不能同时与阿司匹林或华法林等抗凝剂一起服用，两方面均会增加脑出血的风险，所以，服用银杏叶保健食品要适可而止，须定期检测凝血情况，不要盲目长期服用，尤其对于已有老年性血管硬化或血管变脆的患者而言更要注意，以免造成脑出血。</p><p>　　此外，为保障产品质量，在购买含银杏叶成分的保健食品时，须在正规药店或渠道购买，服用时严格按照说明书中标示的剂量，切不可过量，以免对身体产生不必要的影响。</p><p>　　经过近几年的升级发展，银杏叶保健产品在营养干预、预防高血压、高血糖等慢性疾病领域迎来新的发展机遇，前途无限，未来可期!</p><p><br/></p>
			</div>
			<div style=" height:8px;"></div>
			<div>				
				 	<a href=http://m.cnyxs.com/news_type.asp?id=34952 target=_blank urlName=3 cName=96>上一个：世界上最美的几种树，银杏树被称为植物界的活化石，寿命极长</a>
			</div>
			<div style=" height:8px;"></div>
			<div>
				 
			</div>
			<div class="clear" style=" height:8px;"></div>
		</div>
	</div>
</div>
<script type="text/javascript">removeImgSize(".news_detailinfo");</script>

</div>

<!--/*底部导航*/-->
<table width="95%" height="47" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td>&nbsp;</td>
  </tr>
</table>
<div class="navibar">
    <ul class="main">
        <li><a href="tel:15365831111"><i class="tel"><img src="images/f1.png" width="115" height="28" border="0" ></i></a></li>
   
    </ul>
</div>
	
<script type="text/javascript">
wapPhoneNavStyle(1);   //引用导航效果
$(".wap_btm_nav").wapBottomNavFixed({pc:1});	
$(window).resize(function(){$(".wap_btm_nav").wapBottomNavFixed();});	
</script> 

</div>

</body>
</html>
"""

main_page = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<TITLE>银杏网动态-中国银杏网</TITLE>
<META NAME="copyright" CONTENT="">
<META NAME="Author" CONTENT="">
<META NAME="Robots" CONTENT="all">
<META NAME="Robots" CONTENT="all">
<META NAME="Keywords" CONTENT="银杏网动态,中国银杏网">
<META NAME="Description" CONTENT="银杏网动态,银杏,银杏树,中国银杏网-中国银杏行业门户网站">

<meta content="width=device-width,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" name="viewport" />
<meta name="format-detection" content="telephone=no">
<link rel="stylesheet" type="text/css" href="css/skin.css">

</head>
<body>
<div class="wapMain">
	<div class="wap_top">		
		<table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td><a href="http://m.cnyxs.com"><img src="images/1155.jpg" border="0" width="100%" height="60px"/></a></td>
  </tr>
</table>

<div class="dh"><ul>
        <li><a href="http://m.cnyxs.com">首页</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏树">银杏树</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏果">银杏果</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏叶">银杏叶</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏酒">银杏酒</a></li>
</ul>
<ul>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=白果">白果</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏茶">银杏茶</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏网">银杏网</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏盆景">银杏盆景</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏树价格">银杏价格</a></li>
</ul>
<ul>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏新闻">银杏新闻</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏文化">银杏文化</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏科技">银杏科技</a></li>
      <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏黄酮">银杏黄酮</a></li>
        <li><a href="http://m.cnyxs.com/xw.asp?lb=银杏学院">银杏学院</a></li>

</ul>
</div>


	</div>
<div class="wap_container edit_putHere" id="edit_putHere_area1" saveTitle="area1">
<div align="center">

<div class="web2t">
<div class="webt1"><a href="http://m.cnyxs.com/news.asp?lb=" class="more"><strong></strong></a></div>
<div class="webt2"><a href="http://m.cnyxs.com/news.asp?lb=" class="more">更多>></a></div></div>


  </div>
	<div class="wap_label" id="16" rel="16" titles="幻灯片">
	<div class="wap_slide">
		<div class="wap_label_content">
			<div class="bd" id="bd16">
				
			</div>
		</div>
	</div>
</div>
<script type="text/javascript">
$(".wap_slide16").bnWapPPt({
startSlide: 0,//Swipe开始的索引
speed: 400, //滑动的速度，单位毫秒
auto: 6000,//自动滑动之间的间隔时间
continuous: true, //是否可以循环播放
disableScroll: false, //停止触摸滑动
nav: 1 //按钮显示
});
</script>
<div class="wap_label" id="34" rel="34" titles="文章列表">
	<div class="wap_news">
		<div class="wap_label_content">
		
		
			<ul class="wap_news_list"  id="articlelist34" >
				
				<li><a href="news_type.asp?id=34946" class="news_name" urlName="3" cName="95">银杏果的功效与作用</a><span class="news_date"></span></li><br />
				 
				<li><a href="news_type.asp?id=34924" class="news_name" urlName="3" cName="95">银杏树落果原因与防治</a><span class="news_date"></span></li><br />
				 
				<li><a href="news_type.asp?id=34923" class="news_name" urlName="3" cName="95">银杏树在种植上需要注意什么</a><span class="news_date"></span></li><br />
				 
				<li><a href="news_type.asp?id=30268" class="news_name" urlName="3" cName="95">强化措施，确保银杏保健食品开发质量</a><span class="news_date"></span></li><br />
				 
				<li><a href="news_type.asp?id=30224" class="news_name" urlName="3" cName="95">银杏苗树形 在市场交易中的实际意义</a><span class="news_date"></span></li><br />
				 
				<li><a href="news_type.asp?id=30187" class="news_name" urlName="3" cName="95">银杏树的木材被得到了从分的利用</a><span class="news_date"></span></li><br />
				 
				<li><a href="news_type.asp?id=30180" class="news_name" urlName="3" cName="95">贺江苏省邳州市明宇银杏树发展中心www.yxs77.com</a><span class="news_date"></span></li><br />
				 
				<li><a href="news_type.asp?id=30175" class="news_name" urlName="3" cName="95">银杏产品发货忙，乡镇物流来帮忙</a><span class="news_date"></span></li><br />
				 
				<li><a href="news_type.asp?id=30153" class="news_name" urlName="3" cName="95">新鲜白果如何保存?能冷冻起来吗?</a><span class="news_date"></span></li><br />
				 
				<li><a href="news_type.asp?id=30124" class="news_name" urlName="3" cName="95">中国银杏网慧网公司2014年国庆节放假通知</a><span class="news_date"></span></li><br />
				 
				<li><a href="news_type.asp?id=30114" class="news_name" urlName="3" cName="95">银杏树幼苗批发价格</a><span class="news_date"></span></li><br />
				 
				<li><a href="news_type.asp?id=30107" class="news_name" urlName="3" cName="95">银杏树的绿化意义重大</a><span class="news_date"></span></li><br />
				 
				<li><a href="news_type.asp?id=30096" class="news_name" urlName="3" cName="95">这些惨遭“杀头”的银杏树，有解救的办法吗</a><span class="news_date"></span></li><br />
				 
				<li><a href="news_type.asp?id=30049" class="news_name" urlName="3" cName="95">园林苗行业的显性成本主要是劳动力、地租和资本三部分</a><span class="news_date"></span></li><br />
				 
				<li><a href="news_type.asp?id=30042" class="news_name" urlName="3" cName="95">银杏养殖技术及管理才能提高成活率  </a><span class="news_date"></span></li><br />
				 
				<li><a href="news_type.asp?id=30014" class="news_name" urlName="3" cName="95">改善生活坏境的作用,银杏树以风靡全国</a><span class="news_date"></span></li><br />
				 
				<li><a href="news_type.asp?id=30009" class="news_name" urlName="3" cName="95">中国银杏文化源远流长的历史轨迹和博大精深的文化内涵</a><span class="news_date"></span></li><br />
				 
				<li><a href="news_type.asp?id=29996" class="news_name" urlName="3" cName="95">世界各国的银杏树都是直接或间接从我国传入的，都源于中国 </a><span class="news_date"></span></li><br />
				 
				<li><a href="news_type.asp?id=29991" class="news_name" urlName="3" cName="95">山东郯城是银杏苗木首选的供应基地</a><span class="news_date"></span></li><br />
				 
				<li><a href="news_type.asp?id=29969" class="news_name" urlName="3" cName="95">国外银杏栽培现状</a><span class="news_date"></span></li><br />
				 <p align=right style= line-height:30px;>首页&nbsp;&nbsp;上一页&nbsp;&nbsp;<a class=Black href=http://m.cnyxs.com/news.asp?lb=银杏网动态&pageno=2&gjz=>下一页</a>&nbsp;&nbsp;<a class=Black href=http://m.cnyxs.com/news.asp?lb=银杏网动态&pageno=19&gjz=>尾页</a>&nbsp;&nbsp;第1页/共19页&nbsp;&nbsp;共373条文章</p>
				<div class="clear"></div>
			</ul>
			
			
		</div>
	</div>
</div>

</div>
<!--/*底部导航*/-->
<table width="95%" height="47" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td>&nbsp;</td>
  </tr>
</table>
<div class="navibar">
    <ul class="main">
        <li><a href="tel:15365831111"><i class="tel"><img src="images/f1.png" width="115" height="28" border="0" ></i></a></li>
   
    </ul>
</div>
	
<script type="text/javascript">
wapPhoneNavStyle(1);   //引用导航效果
$(".wap_btm_nav").wapBottomNavFixed({pc:1});	
$(window).resize(function(){$(".wap_btm_nav").wapBottomNavFixed();});	
</script> 


</div>

</body>
</html>

"""



LINK_PATTERN = '.*?本文地址:<a.*?href="(.*?)">.*?</a>'

PAGE_NUMS_PATTERN = '</a>&nbsp;&nbsp;下一页&nbsp;&nbsp;尾页&nbsp;&nbsp;第.*?页/共(.*?)页&nbsp;&nbsp;共.*?条银杏网动态</td>'

url = '<td.*?width="99%".*?height="26">\[.*?\]&nbsp;<a.*?href="(.*?)".*?target="_blank">.*?</a>.*?</td>'
_ = 'http://www.cnyxs.com/news_type.asp?id=34946'


