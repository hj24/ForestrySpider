# coding=gbk
from bs4 import BeautifulSoup
from parser import baseparser

class GinkgoParser(baseparser.BaseParser):

    def __init__(self, content):
        super().__init__(content)

    @property
    def info(self):
        fonts = self.soup.find_all('font')
        infos = []
        for i, f in enumerate(fonts):
            if f['color'] == '#990000' and i < 4:
                infos.append(f)
        return infos

    def parse_title(self):
        return self.soup.find(self.TITLE).string

    def parse_author(self, *args, **kwargs):
        return self.info[0].string

    def parse_source(self, *args, **kwargs):
        return self.info[1].string

    def parse_date(self, *args, **kwargs):
        return self.info[2].string

    def parse_body(self, *args, **kwargs):
        pass

    def parse_link(self, *args, **kwargs):
        pass

if __name__ == '__main__':
    con = """ 
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
        <TITLE>���ӹ��Ĺ�Ч������_��������̬_������-�й�������</TITLE>
        <META NAME="copyright" CONTENT="�й�������>
        <META NAME="Author" CONTENT="�й�������">
        <META NAME="Keywords" CONTENT="���ӹ��Ĺ�Ч������,��������̬,��">
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
          <LI class="sitenav-mobile">���ã���ӭ����<a href=http://www.cnyxs.com/>�й�������</a> </LI>
          <LI><A style="color: rgb(255, 102, 0);" 
          href="http://www.cnyxs.com/user_dl.asp">���¼ </A></LI>
          <LI><A href="http://www.cnyxs.com/user_zc.asp" target="_blank">���ע��</A></LI>
          <LI class="remove"><A href="http://www.cnyxs.com/fabu.asp">������Ϣ</A></LI>
           <LI class="remove"><A href="http://www.cnyxs.com/zhuomian.asp">���ص�����</A></LI>
          </UL>
        
        
        <UL class="weibo">
        <a href="http://e.weibo.com/zgyxcom" target="_blank"><img src="images/ico_t_sina.gif" alt="����΢��" vspace="0" border="0"></a>
        <a href="http://e.weibo.com/zgyxcom" target="_blank" ref="nofollow">�й�������</a><a href="http://e.weibo.com/zgyxcom" target="_blank"><img src="images/ico_t_sinav.gif" border="0"></a>   
         <a href="http://t.qq.com/zgyxcom/" target="_blank" ref="nofollow"><img src="images/ico_t_qq.gif" alt="��Ѹ΢��" border="0"></a>
        </UL>
        
        </DIV>
        </DIV>  
        <DIV class="header">
        <DIV class="masthead">
        <DIV class="logo"><A title="�й�������ҵ�Ż���վ" href="http://www.cnyxs.com/" target="_blank"><IMG src="http://www.cnyxs.com/images/logo.gif" 
        alt="�й�������" border="0"></A></DIV>
        
        <DIV class="sj">
        <a href="http://www.cnyxs.com/yinxingshu/" target="_blank">������</a>  <a href="http://www.cnyxs.com/yinxingguo/" target="_blank">���ӹ�</a> 
        
                      <a href="http://www.cnyxs.com/yinxingye/" target="_blank">����Ҷ</a> <a href="http://www.cnyxs.com/yinxingcha/" target="_blank">���Ӳ�</a> <a href="http://www.cnyxs.com/yinxingjiu/" target="_blank">���Ӿ�</a>  <a href="http://www.cnyxs.com/baiguo/">�׹�</a><br />
                      
                 <a href="http://www.cnyxs.com/yinxingpenjing/" target="_blank">�����辰</a>   <a href="http://www.cnyxs.com/yinxinghuangtong/" target="_blank">���ӻ�ͪ</a> <a href="http://www.cnyxs.com/yinxingyepian/" target="_blank">����ҶƬ</a> <a href="http://www.cnyxs.com/" target="_blank">����Ҷ��ȡ��</a>
        </DIV>
        
        
        
        <DIV class="zx">
        <a href="http://www.cnyxs.com/xw.asp?lb=��������" target="_blank">��������</a> <a href="http://www.cnyxs.com/xw.asp?lb=�����Ļ�" target="_blank">�����Ļ�</a> <a href="http://www.cnyxs.com/xw.asp?lb=���ӿƼ�" target="_blank">���ӿƼ�</a>  <a href="http://www.cnyxs.com/xw.asp?lb=����ѧԺ" target="_blank">����ѧԺ</a> <a href="http://www.cnyxs.com/xw.asp?lb=��������" target="_blank">��������</a><br /> 
        <a href="http://www.cnyxs.com/zp.asp" target="_blank">��ƸƵ��</a> <a href="http://www.cnyxs.com/rc.asp" target="_blank">�˲�Ƶ��</a>  <a href="http://www.cnyxs.com/tougao.asp" target="_blank">����Ͷ��</a>  <a href="http://www.cnyxs.com/xw.asp?lb=���Ӽ۸�" target="_blank">���Ӽ۸�</a> <a href="http://www.cnyxs.com/xw.asp?lb=������" target="_blank">��վ��̬</a> 
        </DIV>
        
        <DIV class="fz">
        <a href="http://www.cnyxs.com/pizhou/" target="_blank">��������</a> <a href="http://www.cnyxs.com/tancheng/" target="_blank">ɽ��۰��</a><br />
         <a href="http://www.cnyxs.com/taixing/" target="_blank">����̩��</a> <a href="http://www.cnyxs.com/anlu/" target="_blank">������½</a> 
         <br />
        </DIV>
        
        </DIV>
        </DIV>
        
        </DIV>
        <!--������ʼ-->
        <DIV class="gb_nav">
        <LI><A class="ahover1" href="http://www.cnyxs.com/">��ҳ</A>
        <LI><A href="http://www.cnyxs.com/gqxx.asp?lb=��Ӧ">��Ӧ</A>
        <LI><A href="http://www.cnyxs.com/gqxx.asp?lb=��">��</A>
        <LI><A href="http://www.cnyxs.com/qy.asp">��ҵ</A>
        <LI><A href="http://www.cnyxs.com/cp.asp">��Ʒ</A>
        <LI><A href="http://www.cnyxs.com/jg.asp">����</A>
        <LI><A href="http://www.cnyxs.com/zh.asp">չ��</A>
        <LI><A href="http://www.cnyxs.com/ztbd.asp">ר��</A>
        <LI><A href="http://www.cnyxs.com/photo.asp">ͼƬ</A>
        <LI><A href="http://www.cnyxs.com/blog/">����</A>
        <LI><A href="http://hao.cnyxs.com/">��ַ</A>
        <LI><A href="http://www.cnyxs.com/qq/">QQȺ</A>
        <LI><A href="http://www.cnyxs.com/cnyxs/">�ɰ�</A></LI></DIV>
          <!--��������-->
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
                        �㵱ǰ��λ�ã�<a href="http://www.cnyxs.com" target="_blank">�й�������</a>&gt;&gt;
                        
                        <a href="http://www.cnyxs.com/xw.asp?lb=������" target="_blank"><b>������</b></a>
                        
                        &gt;&gt; <a href="http://www.cnyxs.com/news.asp?lb=��������̬" target="_blank">��������̬</a> </td>
                    </tr>
                  </table>
                  </td>
              </tr>
              <tr>
                <td align="center" style="PADDING-LEFT: 10px; PADDING-TOP: 10px; PADDING-bottom: 10px;line-height:400%;"><h1>���ӹ��Ĺ�Ч������</h1>
                  <table width="98%" border="0" align="center" cellpadding="0" cellspacing="0">
          <tr>
            <td><hr size="1" /></td>
          </tr>
        </table></td>
              </tr>
              
              <tr>
                <td align="center"><a href="http://www.cnyxs.com/tougao.asp"><font color="red"><b>��ҪͶ��</b></font></a> ���ߣ�<font color="#990000">�й�������</font> ������<font color="#990000">�й������� </font> ʱ�䣺<font color="#990000">2019/5/31</font>�� ���<a href="http://www.cnyxs.com/news.asp?lb=��������̬" target="_blank"><font color="#990000">��������̬</font></a> ������<font color="#990000">150 </font></td>
              </tr>
              <tr>
                <td height="480" valign="top" style="PADDING-LEFT: 10px; PADDING-TOP: 10px;line-height:200%;font-size:15px;text-align:left;"><p>����<a href=http://www.cnyxs.com/ target=_blank title=���� alt=����><font color=#ff0000><b>����</b></font></a>���׳���<a href=http://www.cnyxs.com/baiguo/ target=_blank title=�׹� alt=�׹�><font color=#ff0000><b>�׹�</b></font></a>��Ҳ��<a href=http://www.cnyxs.com/yinxingshu/ target=_blank title=������ alt=������>������</a>�����ӡ�<a href=http://www.cnyxs.com/yinxingshu/ target=_blank title=�׹��� alt=�׹���>�׹���</a>�������꣬���Ի����׹���������Ǥ�己ֳ��Ҳ�������ӷ�ֳ�������ӷ�ֳ�İ׹���Ҫ20-30����ܽ�������԰׹����ֽй��������׹������ҹ�����Ʒ�֣�����Ϊ�����ϵĻʯ���ҹ�����̩���ǰ׹�֮�硣</p><p>����<a href=http://www.cnyxs.com/yinxingguo/ target=_blank title=���ӹ� alt=���ӹ�>���ӹ�</a>��Ӫ����ֵ</p><p>�������ӹ����ж���Ӫ��Ԫ�أ�����ۡ������ʡ�֬��������֮�⣬������ά����c���˻��ء����ܲ��ء��ơ��ס������ء�þ��΢��Ԫ�أ��Լ������ᡢ�׹��ӡ���̼���ǡ�֬�̴��ȳɷ֡�������������οȴ���ֹ���桢��С�㡢ƽ���塢��Ѫ�ܡ�����Ѫ������ʳ�����ú�ҽ��Ч����</p><p>����Ӫ���ɷ�</p><p>����ÿ100�˰׹��к�������6.4�ˣ�֬��2.4�ˣ�̼ˮ������36�ˣ�����ά1.2�ˣ����ܲ���320΢�ˣ��˻���50΢�ˣ�����5.2�ˣ���ԭ��1.1�ˣ���19���ˣ���10���ˣ���218���ˣ���l���ˡ�</p><p>�����׹���Ӫ����ֵ�ḻ��ʳ�����Σ�������ɬ����ֹ�������Ƚ��ˡ�</p><p>�������ӹ��Ĺ�Ч������</p><p>����1���ٽ�ѪҺѭ���������Ԥ������Ѫ�ܼ�������Ѫ˨���з�;</p><p>����2��Ԥ�����Ĳ����Ľ�ʹ����Ѫѹ����Ѫ֬����Ѫ��;</p><p>����3����ǿ������Ԥ������մ�֢;</p><p>����4���ӻ�˥����ǿϸ����ֳ�����ӳ�ϸ������;</p><p>����5���ֿ����䣬���ӻ���������������Ч�������Թ���ϸ����ֳ����������;</p><p>����6�����ḻ��ά���غ����ʵ�ˮ�ܵ��ף������õĻ��νⶾ���޸�����֯���˵Ĺ�Ч;</p><p>����7�����ƺ�ɱ������ϸ�����������������ڻ��ơ����ƺ�ĸ����ã������߰�ϸ����ȷ��Ч��;</p><p>����8����θ���ġ��ȡ��ǣ����ʵ���Ȼ��Ʒ;</p><p>����9�����ջ��������ݼ�Ʒ�����ۼ�������ֹƤ���ֲڣ��ӻ�ϸ��˥�ϣ������ഺ����;����10������ͷʹ����������ѣ�����������Ρ��ֽű���֢״�� 
        ����������̵�ԣ��״������ǣ��ž����ܲ���С��Ƶ����</p><p>�������ӹ����óԷ�</p><p>����һ�����ǳ�ը�ࣺ</p><p>����1�����ΰ׹���</p><p>���������� ȡ���ǰ׹�һ�����ý��κͰ׹�һ����ڹ��ڳ�ը���죬����ȥ��ʳ�á�</p><p>����Ҫ�������ԡ�����ʳ�á���ʳʳ֮�ɿ����㣬��ʳʳ֮�ɿ���ζ���д�����ʱ��ÿ��һ����150-200��Ϊ�ˡ�</p><p>����2���򵥵�����ʪë����ŷ⽫�׹���ס������΢��¯С��������ӣ�����žž�죬���䱬���Ϳ�ʳ�ã���Ө������ζ���㣬�ڸ���Ŵ��</p><p>��������ȥ����ʳ�ࣺ</p><p>����1���׹��ࣺ��Ԫ���������ࡢ��˥�ϣ����ꡢ�����ಡ���ȼѡ�������ʳ֮���塣�˼�ͥʳ�á�</p><p>���������� �׹���(ȥ�Ǻ��÷�ˮ��ȥ����Ƥ)6-10������������������2����ˮ������ͬʱ������У��Ļ����켴�ɡ��Ծ��׳ɺ���״���ɡ�</p><p>�����׹���������������ǵ����������䣬��׹��˱��ࡢ�׹��̶��ࡢ�׹�ɳ��������ȣ����Ա��ǡ�����Ϊ�ˡ�</p><p>����2��С������������ˣ��𻨰׹������ǰ׹���</p><p>���������׹���Բ��</p><p>���������� ���׹���25�˺�࣬�зۣ����Ͱ��죬��۳��ƣ���֥�鳴�㵷�á�</p><p>����������ѹ����״��������ǡ��׹��ۡ���֥�飬���ϼ��ͼӳ��棬����ڶ���</p><p>������Ŵ�׷ۺ��ȣ��ֳ�С�ţ������ڶ���������Բ��</p><p>����������ˮ�����У�����Բ�¹����Ļ�������Բ����ˮ����3-5���Ӽ��ɡ�</p><p>�����ص㣺 ���ڼ���׹�����ף��&quot;ǧ�ﳤ��&quot;֮�⡣</p><p><br/></p>
                </span></td>
              </tr>
              
              <tr>
                <td align="left"><table width="100%" border="0" cellspacing="0" cellpadding="0">
                  <tr>
                    <td width="18%"></td>
                    <td width="82%"></td>
                  </tr>
                </table> ���ĵ�ַ:<a href="http://www.cnyxs.com/news_type.asp?id=34946">http://www.cnyxs.com/news_type.asp?id=34946</a>
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
                  <b>��һƪ<a href="http://www.cnyxs.com/news.asp?lb=��������̬" target="_blank">��������̬</a>���£�</b>
                  <a href=http://www.cnyxs.com/news_type.asp?id=34924  target=_blank>���������ԭ�������</a>
                  <br />
                  <b>��һƪ<a href="http://www.cnyxs.com/news.asp?lb=��������̬" target="_blank">��������̬</a>���£�</b>
                  û����һ��<a href=http://www.cnyxs.com/news.asp?lb=��������̬>��������̬</a>�����ˣ�</td>
              </tr>
              <tr>
                <td align="right"><font color="#990000">��<a href="http://www.cnyxs.com/tougao.asp">��ҪͶ��</a>��������<a href="http://bbs.cnyxs.com/" target="_blank">������̳</a>�����Ƽ������ѡ���<a href="http://bbs.cnyxs.com/"><font color="#990000">��������</font></a>����<a href="javascript:window.close()"><font color="#990000">�رմ���</font></a>��</font></td>
              </tr>
            </table></td>
            <td width="206" valign="top"><table width="238" border="0" cellpadding="0" cellspacing="1" bgcolor="#D9D9D9">
              <tr>
                <td height="150" valign="top" bgcolor="#FFFFFF"><table width="100%" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                      <td height="25" align="left" background="images/left_bg1.jpg">��<a href="http://www.cnyxs.com/photo.asp" target="_blank"><font color="#ffffff"><b>����ͼƬ</b></font></a></td>
                    </tr>
                  </table>
                    
                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr>
                        <td align="center"><a href="http://www.cnyxs.com/news_type.asp?id=30839" target="_blank"><img src="ginkgo/edit/UploadFile/2015410144315664.jpg" width="85" height="75" hspace="2" vspace="4" border="0" 
                          align="absmiddle" /></a><br />
                            <a href="http://www.cnyxs.com/news_type.asp?id=30839" target="_blank">�أ�����������</a>
                            </td>
                        <td align="center">
                            <a href="http://www.cnyxs.com/news_type.asp?id=30578" target="_blank"><img src="ginkgo/edit/UploadFile/2015116134642270.jpg" width="85" height="75" hspace="2" vspace="4" border="0" 
                          align="absmiddle" /></a><br />
                            <a href="http://www.cnyxs.com/news_type.asp?id=30578" target="_blank">�أ������д��</a>
                        </td>
                      </tr>
                    </table>
                  
                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr>
                        <td align="center"><a href="http://www.cnyxs.com/news_type.asp?id=30549" target="_blank"><img src="ginkgo/edit/UploadFile/20151993755443.jpg" width="85" height="75" hspace="2" vspace="4" border="0" 
                          align="absmiddle" /></a><br />
                            <a href="http://www.cnyxs.com/news_type.asp?id=30549" target="_blank">�أ������н���</a>
                            </td>
                        <td align="center">
                            <a href="http://www.cnyxs.com/news_type.asp?id=30529" target="_blank"><img src="ginkgo/edit/UploadFile/201515141840900.jpg" width="85" height="75" hspace="2" vspace="4" border="0" 
                          align="absmiddle" /></a><br />
                            <a href="http://www.cnyxs.com/news_type.asp?id=30529" target="_blank">�أ�˶�����̻�</a>
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
                        <td height="25" align="left" background="images/left_bg1.jpg">��
                            
                            <a href="http://www.cnyxs.com/xw.asp?lb=������" target="_blank"><font color="#ffffff"><b>������</b></font></a>
                            
                            <font color="#ffffff">�������</font></td>
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
                          <td align="left" valign="top"> �� <a href="http://www.cnyxs.com/ztt.asp?id=193" target="_blank">�й����������ӹ�����Ϣƽ̨</a>
                              </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
                        </tr>
                        </td>
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
                          <td align="left" valign="top"> �� <a href="http://www.cnyxs.com/ztt.asp?id=12" target="_blank">�й��������ר��</a>
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
                        <td height="25" align="left" background="images/left_bg1.jpg">��
                            <a href="http://www.cnyxs.com/news.asp?lb=��������̬" target="_blank"><font color="#ffffff"><b>��������̬</b></font></a>
                   
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
                          <td align="left" valign="top"> �� <a href="http://www.cnyxs.com/news_type.asp?id=34946" target="_blank">���ӹ��Ĺ�Ч������</a>
                              </td>
                        </tr>
                        
                        <tr>
                          <td align="left" valign="top"> �� <a href="http://www.cnyxs.com/news_type.asp?id=34924" target="_blank">���������ԭ�������</a>
                              </td>
                        </tr>
                        
                        <tr>
                          <td align="left" valign="top"> �� <a href="http://www.cnyxs.com/news_type.asp?id=34923" target="_blank">����������ֲ����Ҫע��ʲô</a>
                              </td>
                        </tr>
                        
                        <tr>
                          <td align="left" valign="top"> �� <a href="http://www.cnyxs.com/news_type.asp?id=30268" target="_blank">ǿ����ʩ��ȷ�����ӱ���ʳƷ��������</a>
                              </td>
                        </tr>
                        
                        <tr>
                          <td align="left" valign="top"> �� <a href="http://www.cnyxs.com/news_type.asp?id=30224" target="_blank">���������� ���г������е�ʵ������</a>
                              </td>
                        </tr>
                        
                        <tr>
                          <td align="left" valign="top"> �� <a href="http://www.cnyxs.com/news_type.asp?id=30187" target="_blank">��������ľ�ı��õ��˴ӷֵ�����</a>
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
                        <td height="25" align="left" background="images/left_bg1.jpg">��<b><font color="#fffffff">�������ӱ���</font></b></td>
                      </tr>
                    </table>
                      
                    ��<a href="http://www.cnyxs.com/news_type.asp?id=34949" title="�������۸�ʲô����?��ô�����������۸�?" target="_blank">�������۸�ʲô����?��ô</a><br />
                    
                    ��<a href="http://www.cnyxs.com/news_type.asp?id=34948" title="����ҶҲ������ͷ�ˣ��ô�������" target="_blank">����ҶҲ������ͷ�ˣ��ô���</a><br />
                    
                    ��<a href="http://www.cnyxs.com/news_type.asp?id=34947" title="�������ļ��ַ�ֳ��������֪�����٣�" target="_blank">�������ļ��ַ�ֳ��������֪</a><br />
                    
                    ��<a href="http://www.cnyxs.com/news_type.asp?id=34946" title="���ӹ��Ĺ�Ч������" target="_blank">���ӹ��Ĺ�Ч������</a><br />
                    
                    ��<a href="http://www.cnyxs.com/news_type.asp?id=34945" title="��ι������������������۸���ô��?" target="_blank">��ι������������������۸�</a><br />
                    
                    ��<a href="http://www.cnyxs.com/news_type.asp?id=34944" title="�������������ˮ�ã��ݺ��Ժ������������" target="_blank">�������������ˮ�ã��ݺ��</a><br />
                    
                    ��<a href="http://www.cnyxs.com/news_type.asp?id=34943" title="�������г��۸������ô����" target="_blank">�������г��۸������ô����</a><br />
                    
                    ��<a href="http://www.cnyxs.com/news_type.asp?id=34942" title="����������ר������̸�й����������" target="_blank">����������ר������̸�й���</a><br />
                    
                    ��<a href="http://www.cnyxs.com/news_type.asp?id=34941" title="����������ʮ��֮Լ �ൺ����־Ը��������ľ�ѳɲ�" target="_blank">����������ʮ��֮Լ �ൺ��</a><br />
                    
                    ��<a href="http://www.cnyxs.com/news_type.asp?id=34940" title="21��ʦ���������������� ѧ����181��С�����ɳ�" target="_blank">21��ʦ���������������� </a><br />
                    
                    ��<a href="http://www.cnyxs.com/news_type.asp?id=34939" title="��Ҫ����������������Щ֪ʶ�ü��Σ�" target="_blank">��Ҫ����������������Щ֪</a><br />
                    
                    ��<a href="http://www.cnyxs.com/news_type.asp?id=34938" title="������������ͷ�� ���ݵ�ʤ����ľ���Ϊɶ�׷׵���" target="_blank">������������ͷ�� ���ݵ�ʤ</a><br />
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
              <td width="34" height="30" align="right"><img src="images/icon_warning_24x24.gif" alt="����" width="24" height="24" hspace="5" /></td>
              <td width="946" class="font7"><a href="http://www.cnyxs.com/" target="_blank"><b><font color="red">�й�������</font></b></a><b>����������</b> ������չʾ����Ϣ����ҵ����������ṩ�����ݵ���ʵ�ԡ�׼ȷ�ԺͺϷ����ɷ�����ҵ����˸���<a href="http://www.cnyxs.com/" target="_blank">�й�������</a>�Դ˲��е��κα�֤���Ρ���վ��Ϣ���Ի�����,�ɹ��ο�������Ϊ��ʵ����,��վ����ת�ػ����������漰��Ȩ����,������������ϵ QQ:18708455</td>
            </tr>
          </table>
        </div>
        <!--�ײ���ʼ-->
        <DIV class="foot">
        <SCRIPT type="text/javascript" src="images/foot.js"></SCRIPT><p>
        <a href="http://www.cnyxs.com">�й�������</a>�ؼ���:<a href="http://www.cnyxs.com" target="_blank">����</a>-<a href="http://www.cnyxs.com/yinxingshu/" target="_blank">������</a>-<a href="http://www.cnyxs.com" target="_blank">�������۸�</a>-<a href="http://www.cnyxs.com/yinxingguo/" target="_blank">���ӹ�</a> - <a href="http://www.cnyxs.com/yinxingye/" target="_blank">����Ҷ</a> - <a href="http://www.cnyxs.com/yinxingcha/" target="_blank">���Ӳ�</a> - <a href="http://www.cnyxs.com/baiguo/" target="_blank">�׹�</a></p>
        <P>
        ��ѯ���ߣ�0516-<SPAN class="footkuang">81581111 </SPAN></p>
        <P>����Ӣ������:<STRONG style="color: rgb(255, 0, 0);"> <A 
        href="http://www.cnyxs.com/">www.cnyxs.com</A></STRONG> ��������:<STRONG style="color: rgb(255, 0, 0);"> <A 
        href="http://www.cnyxs.com/">�й�������</A></STRONG>.com���й���רҵ��<A style="padding: 0px;" 
        href="http://www.cnyxs.com/">����</A><a href="http://www.cnyxs.com/baiguo/" target="_blank">�׹�</a>��ҵ�Ż���վ</P>
        <P><A href="http://www.cnyxs.com/" rel="nofollow">�й�������</A>  ��Ȩ���� &copy; 2005-2020 ��ICP��07021153�� <script src="http://s22.cnzz.com/stat.php?id=3259912&web_id=3259912" language="JavaScript"></script></p>
        </DIV>
        <!--�ײ�����-->
        
        </body>
        </html>
    """
    # print(con.encode('utf-8').decode('utf-8'))
    p = GinkgoParser(con)
    print(p.parse_title())
    # print(p.info)
    print(p.parse_author())
    print(p.parse_source())
    print(p.parse_date())
