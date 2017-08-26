import re

text = "He was carefully disguised but captured quickly by police."
# print(str(re.search(r"\w+ly", text)))


html = """
<div id="Zoom">
<!--Content Start-->
<p><img src="http://img.diannao1.com/d/file/html/gndy/dyzz/2017-08-10/643fea779cd071781949ea1e1550d513.jpg" alt="de683f54170fcdd3aa33d5f99f5b6de6.jpg" width="518" height="725">&nbsp;</p>
<p>◎译　　名　李雷和韩梅梅之昨日重现/How Are You</p>
<p>◎片　　名　李雷和韩梅梅</p>
<p>◎年　　代　2017</p>
<p>◎产　　地　中国大陆</p>
<p>◎类　　别　剧情/喜剧/爱情</p>
<p>◎语　　言　汉语普通话</p>
<p>◎字　　幕　中文字幕</p>
<p>◎上映日期　2017-06-09(中国大陆)</p>
<p>◎豆瓣评分　3.1/10 from 11329 users</p>
<p>◎文件格式　x264 + ACC</p>
<p>◎视频尺寸　1280 x 720</p>
<p>◎文件大小　950 MB</p>
<p>◎片　　长　90 Mins</p>
<p>◎导　　演　杨永春 Yongchun Yang</p>
<p>◎主　　演　张子枫 Zifeng Zhang</p>
<p>　　　　　　张逸杰 Yijie Zhang</p>
<p>　　　　　　成梓宁 Zining Cheng</p>
<p>　　　　　　李家成 Jiacheng Li</p>
<p>　　　　　　常铖 Cheng Chang</p>
<p>　　　　　　王旭东 Xudong Wang</p>
<p>　　　　　　张诚航 Chenghang Zhang</p>
<p>　　　　　　苗皓钧 Haizhong Miao</p>
<p>　　　　　　花希 Xi Hua</p>
<p>　　　　　　马泽涵 Zehan Ma</p>
<p>　　　　　　应亦涵 Yihan Ying</p>
<p>　　　　　　朱子岩 Ziyan Zhu</p>
<p>　　　　　　李扬 Yang Li</p>
<p>　　　　　　郝平 Ping Hao</p>
<p>　　　　　　王菁华 Jinghua Wang</p>
<p>　　　　　　塞拉斯·列维·纽豪斯 Silas·Levi·Neuhaus</p>
<p>◎简　　介</p>
<p>　　运动全能的中学女汉子韩梅梅（张子枫 饰），各项成绩尚可，但一提起英语就头疼得要命。&nbsp;</p>
<p>　　在结束了快乐的初中生活后，韩梅梅和魏华（成梓宁 饰）、林涛（李家成 饰）等一起升上了高中，同时还有李雷（张逸杰 饰）。如今的李雷已是脱胎换骨，从一个不起眼的小男生变成了又高又帅的男神，还有一口英伦范的纯正英语。&nbsp;</p>
<p>　　韩梅梅也是不知不觉地喜欢上了李雷，却迟迟不敢开口，于是古灵精怪的她制定出各种作战计划，意图攻陷李雷。&nbsp;</p>
<p>　　然而，天有不测风云，一场又一场的麻烦和变故，接二连三地降落在他们身上……&nbsp;</p>
<p>　　多年后，韩梅梅和李雷，还能牵手吗？</p>
<p>◎幕后制作</p>
<p>　　该片依托英语教科书中的经典CP“李雷和韩梅梅“人物原型，保留“鹦鹉Polly”“Miss Gao”、“Jim”、“Uncle Wang “等“回忆杀”代表元素，复盘近2亿人的青春记忆。</p>
<p>◎影片截图</p>
<div><img src="http://img.diannao1.com/d/file/html/gndy/dyzz/2017-08-10/a4841742b89cb0fc43c32ca75a04a282.jpg" alt="李雷和韩梅梅HD高清国语中字.mkv_thumbs_2017.08.10.12_12_25.jpg" width="926" height="857"></div><!--duguPlayList Start-->
<!--xunleiDownList Start-->
    <p>&nbsp;</p>
    <p style="margin: 0px; padding: 0px; color: rgb(24, 55, 120); font-family: Verdana, Arial, Helvetica, sans-serif;"><font color="#ff0000"><strong><font size="4">【迅雷下载地址】 </font></strong></font></p>
          <p style="margin: 0px; padding: 0px; color: rgb(24, 55, 120); font-family: Verdana, Arial, Helvetica, sans-serif;">&nbsp;</p>
          <table style="BORDER-BOTTOM: #cccccc 1px dotted; BORDER-LEFT: #cccccc 1px dotted; TABLE-LAYOUT: fixed; BORDER-TOP: #cccccc 1px dotted; BORDER-RIGHT: #cccccc 1px dotted" border="0" cellspacing="0" cellpadding="6" width="95%" align="center">
          <tbody>
              <tr>
                  <td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><anchor><a target="_self" href="#" title="迅雷专用高速下载" thunderpid="00000" thundertype="" thunderrestitle="" onclick="return OnDownloadClick_Simple(this,2)" oncontextmenu="ThunderNetwork_SetHref(this)" fbhwdbxo="thunder://QUFmdHA6Ly9kOmRAZHlnb2RqOC5jb206MTIzMTEvWyVFNyU5NCVCNSVFNSVCRCVCMSVFNSVBNCVBOSVFNSVBMCU4Mnd3dy5keTIwMTguY29tXSVFNiU5RCU4RSVFOSU5QiVCNyVFNSU5MiU4QyVFOSU5RiVBOSVFNiVBMiU4NSVFNiVBMiU4NUhEJUU5JUFCJTk4JUU2JUI4JTg1JUU1JTlCJUJEJUU4JUFGJUFEJUU0JUI4JUFEJUU1JUFEJTk3Lm1rdlpa">ftp://d:d@dygodj8.com:12311/[电影天堂www.dy2018.com]李雷和韩梅梅HD高清国语中字.mkv</a>&nbsp;&nbsp;</anchor></td>
              </tr>
          </tbody>
      </table>
      <p style="margin: 0px; padding: 0px; color: rgb(24, 55, 120); font-family: Verdana, Arial, Helvetica, sans-serif;">&nbsp;</p>
      
      
<script type="text/javascript">if(goPAGE()=="win"){document.writeln("<SCRIPT src='/jsdd/750.js'></SCR"+"IPT>")}</script><script src="/jsdd/750.js"></script>

<br>
      
        <hr color="#CC6600" size="1px">
      

        <center><font color="#ff000">请把www.dy2018.com分享给你的朋友,更多人使用，速度更快 电影天堂www.dy2018.com欢迎你每天来!</font></center>
</div>
"""

a = re.search(r'<p>◎主　　演　(.*)</p>\n(<p>　　　　　　(.*)</p>\n)*', html).group(0)
line_list = a.split("\n")
actors = [re.match(r'<p>(◎主\u3000\u3000演)?[\u3000]+(.*)</p>',tag_p).group(2) for tag_p in line_list]
