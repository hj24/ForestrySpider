# encoding=utf-8
import re
from parser import ginkgoparser
from bs4 import BeautifulSoup

content = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<TITLE>中国银杏网慧网公司2014年国庆节放假通知_银杏网动态_银杏网-中国银杏网</TITLE>
<META NAME="copyright" CONTENT="中国银杏网>
<META NAME="Author" CONTENT="中国银杏网">
<META NAME="Keywords" CONTENT="中国银杏网慧网公司2014年国庆节放假通知,银杏网动态,无">
<META NAME="Robots" CONTENT="all">
<META http-equiv="Content-Type" content="text/html; charset=gb2312">
<link rel="icon" href="http://www.cnyxs.com/favicon.ico"/>
<link rel="shortcut icon" href="http://www.cnyxs.com/favicon.ico" /> 

<LINK href="images/css.css" type=text/css rel=stylesheet>
</head>
<script>
if(/Android|webOS|iPhone|iPod|BlackBerry/i.test(navigator.userAgent)) {
    window.location.href = "http://m.cnyxs.com/news_type.asp?id=30124";
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
        <td align="center" style="PADDING-LEFT: 10px; PADDING-TOP: 10px; PADDING-bottom: 10px;line-height:400%;"><h1>中国银杏网慧网公司2014年国庆节放假通知</h1>
          <table width="98%" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td><hr size="1" /></td>
  </tr>
</table></td>
      </tr>
      
      <tr>
        <td align="center"><a href="http://www.cnyxs.com/tougao.asp"><font color="red"><b>我要投稿</b></font></a> 作者：<font color="#990000">中国银杏网</font> 出处：<font color="#990000">中国银杏网 </font> 时间：<font color="#990000">2014/9/30</font>　 类别：<a href="http://www.cnyxs.com/news.asp?lb=银杏网动态" target="_blank"><font color="#990000">银杏网动态</font></a> 人气：<font color="#990000">5354 </font></td>
      </tr>
      <tr>
        <td height="480" valign="top" style="PADDING-LEFT: 10px; PADDING-TOP: 10px;line-height:200%;font-size:15px;text-align:left;"><P><FONT face=Verdana>尊敬的中国<a href=http://www.cnyxs.com/ target=_blank title=银杏 alt=银杏><font color=#ff0000><b>银杏</b></font></a>网用户：<a href=http://www.cnyxs.com/ target=_blank><font color=#ffffff>www.cnyxs.com</font></a><br>&nbsp;&nbsp;&nbsp; <br>&nbsp;&nbsp;&nbsp;&nbsp; 恰逢国庆节来临之际，<a href=http://www.cnyxs.com/ target=_blank title=中国银杏网 alt=中国银杏网>中国银杏网</a>全体员工祝您假期愉快、生活幸福！感谢您一如既往地对中国银杏网的支持与帮助，在未来的日子里，我们将以更优质的产品和更真诚的服务回馈广大客户！<br>&nbsp;&nbsp; <br>&nbsp;&nbsp;&nbsp;&nbsp; 根据国务院对2014年国庆节放假通知精神，结合本网实际，为方便为您提供服务，本网国庆放假具体安排通知如下：<br>&nbsp;&nbsp; <br>&nbsp;&nbsp;&nbsp;&nbsp; 10月1日（周三）至10月7日（周二），共7天。<br>&nbsp;&nbsp; <br>&nbsp;&nbsp;&nbsp;&nbsp; 从10月1号开始，您新发布的信息将处于审核中状态，于10月8日上班后统一审核。如给您造成不便，敬请谅解！<br>&nbsp;&nbsp; <br>&nbsp;&nbsp;&nbsp;&nbsp; 期间如有疑问，请拨打400 663 0516值班电话咨询。<br>&nbsp;&nbsp; <br>&nbsp;&nbsp;&nbsp;&nbsp; 再次感谢您对中国银杏网的支持！祝您及您的家人身体健康，事业更上一层楼！ </FONT></P>
<P><FONT face=Verdana></FONT>&nbsp;</P>
        </span></td>
      </tr>
      
      <tr>
        <td align="left"><table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td width="18%"></td>
            <td width="82%"></td>
          </tr>
        </table> 本文地址:<a href="http://www.cnyxs.com/news_type.asp?id=30124">http://www.cnyxs.com/news_type.asp?id=30124</a>
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
          <a href=http://www.cnyxs.com/news_type.asp?id=30114  target=_blank>银杏树幼苗批发价格</a>
          <br />
          <b>下一篇<a href="http://www.cnyxs.com/news.asp?lb=银杏网动态" target="_blank">银杏网动态</a>文章：</b>
          <a href=http://www.cnyxs.com/news_type.asp?id=30153  target=_blank>新鲜白果如何保存?能冷冻起来吗?</a></td>
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
              
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34953" title="银杏叶保健食品市场未来可期" target="_blank">银杏叶保健食品市场未来可期</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34952" title="世界上最美的几种树，银杏树被称为植物界的活化石，寿命极长" target="_blank">世界上最美的几种树，银杏树</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34951" title="揭开银杏家世之谜" target="_blank">揭开银杏家世之谜</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34950" title="想要银杏树尽快结果，这些知识得记牢！" target="_blank">想要银杏树尽快结果，这些知</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34949" title="银杏树价格按什么计算?怎么计算银杏树价格?" target="_blank">银杏树价格按什么计算?怎么</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34948" title="银杏叶也能做枕头了？好处还不少" target="_blank">银杏叶也能做枕头了？好处还</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34947" title="银杏树的几种繁殖方法，你知道多少？" target="_blank">银杏树的几种繁殖方法，你知</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34946" title="银杏果的功效与作用" target="_blank">银杏果的功效与作用</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34945" title="如何购买银杏树，银杏树价格怎么样?" target="_blank">如何购买银杏树，银杏树价格</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34944" title="银杏树在哪里风水好，屋后和院子内能栽种吗" target="_blank">银杏树在哪里风水好，屋后和</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34943" title="银杏树市场价格今年怎么样？" target="_blank">银杏树市场价格今年怎么样？</a><br />
            
            ·<a href="http://www.cnyxs.com/news_type.asp?id=34942" title="听养老领域专家王锦谈中国人如何养老" target="_blank">听养老领域专家王锦谈中国人</a><br />
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


