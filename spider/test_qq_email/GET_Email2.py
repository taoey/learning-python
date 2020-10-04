from selenium import webdriver
from lxml import etree
import time,random


def get_freshList(dataList):
    '处理获得的list数据,清除多余的字符'
    freshList=[]
    for i in dataList:
        freshList.append("".join(i.replace('\n','').replace(' ','').replace('\t','')))

    return freshList

if __name__ == '__main__':

    web_data = """
        D:\CCApplication\an3\python.exe E:/Code/python/spy/QQ_Email/GET_Email2.py
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" class="ver54"><head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="keywords" content="QQ群,群,群教育,一键加群,加群,群开放能力,群开放,群认证,2000人群,2K人群,QQ,Tencent">
    <meta name="description" content="腾讯QQ群官方网站。提供QQ群最新功能介绍、群应用接入、开放接口、群认证等丰富内容，群聚你我精彩。">
    <link rel="stylesheet" href="//s2.url.cn/qqun/qun/css/member-33c75.css">
    <link rel="shortcut icon" href="//im.qq.com/favicon.ico">
    <script src="http://jsqmt.qq.com/cdn_djl.js" type="text/javascript" async=""></script><script>
    	var dt0 = new Date();
    </script>
    <title>QQ群官网-成员管理</title>
    <script src="//jqmt.qq.com/cdn_dianjiliu.js?a=0.5019544216338545"></script></head>
    <body>
    	    <div class="header">
            <div class="header-top">
                <a href="//qun.qq.com" class="logo"></a>

                <div class="header-nav">
                    <ul id="headerNav">
                        <li><a href="/index.html#click">首页</a></li>
                        <li><a href="http://buluo.qq.com/buluoadmin/home.html?platform=qun" target="_blank">群订阅号</a></li>
                        <li><a href="/open.html#click">开放能力</a></li>
                        <li class="selected"><a href="/manage.html#click" data-tag="manage">群管理</a></li>
                        <li><a href="http://buluo.qq.com/p">兴趣部落</a></li>
                        <li><a href="/join.html" data-tag="join">加群组件</a></li>
                        <li><a href="http://kf.qq.com/product/group.html" target="_blank" data-tag="help">帮助</a></li>
                    </ul>
                    <div class="header-info" id="headerInfo"><p class="user-info"><a class="user-nick" title="(๑• . •๑)">(๑• . •๑)</a>&nbsp;<a cmd="loginoff" data-tag="logout" class="logout">[退出]</a></p><p>|</p><p><a href="http://support.qq.com/write.shtml?fid=35&amp;ADPUBNO=" target="_blank" data-tag="fk">反馈</a></p></div>
                </div>
            </div>
        </div>

    	<div class="body">
    		<dl>
    			<dt>
    				<div class="group-tit">
    					<span id="groupTit">燕大失物招领①群(165636732)</span> <a id="changeGroup" data-tag="changegroup">[切换QQ群]</a>
    				</div>
    			</dt>
    			<dd>
    				<div class="group-tools">
    					<div class="group-members" id="groupMemberTit">
    		群成员人数: <span id="groupMemberNum">995</span>/1000



    	</div>
    					<div class="group-search">
    						<div class="group-input">
    							<input type="text" id="searchValue" data-def="搜索关键词" value="搜索关键词">
    							<button id="searchBtn" data-tag="search" class="icon-search-btn"></button>
    						</div>
    						<div class="group-select-btn" data-tag="more">
    							<a data-tag="more">
    								<span data-tag="more">更多筛选</span>
    								<i data-tag="more" class="icon-arrow-blue"></i>
    							</a>
    						</div>
    					</div>
    					<div id="moreAction">
    						<div class="child group-select-more hide">
    							<div class="group-top">
    								<div></div>
    							</div>
    							<ul data-key="credit" data-tag="信用" data-type="0">
    								<li>
    									<label>信　　用：</label>
    								</li>
    								<li class="query-filter selected">不限</li>
    								<li class="query-filter">不良记录成员</li>
    							</ul>
    							<ul data-key="g" data-tag="性别" data-type="1">
    								<li>
    									<label>性　　别：</label>
    								</li>
    								<li class="query-filter selected">不限</li>
    								<li class="query-filter">男</li>
    								<li class="query-filter">女</li>
    							</ul>
    							<ul data-key="qage" data-tag="Q龄" data-type="2">
    								<li>
    									<label>Q　　龄：</label>
    								</li>
    								<li class="query-filter selected">不限</li>
    								<li class="query-filter">1年内</li>
    								<li class="query-filter">1年-3年</li>
    								<li class="query-filter">3年-5年</li>
    								<li class="query-filter">5-7年</li>
    								<li class="query-filter">7年以上</li>
    								<li class="query-filter sl" data-val="年"><input type="text" maxlength="2"> - <input type="text" maxlength="2"> 年</li>
    							</ul>
    							<ul data-key="join_time" data-tag="入群时长" data-type="3">
    								<li>
    									<label>入群时长：</label>
    								</li>
    								<li class="query-filter selected">不限</li>
    								<li class="query-filter">1个月内</li>
    								<li class="query-filter">1-3个月</li>
    								<li class="query-filter">3-6个月</li>
    								<li class="query-filter">6-12个月</li>
    								<li class="query-filter">12个月以上</li>
    								<li class="query-filter sl" data-val="月"><input type="text" maxlength="3"> - <input type="text" maxlength="3"> 月</li>
    							</ul>
    							<ul data-key="lv" id="groupLevel" class="hide" data-tag="群等级" data-type="5" style="display: block;">
    		<li>
    			<label>等　　级：</label>
    		</li>
    		<li class="query-filter selected" data-idx="0">不限</li>

    			<li class="query-filter " data-idx="1">潜水</li>

    			<li class="query-filter " data-idx="2">冒泡</li>

    			<li class="query-filter " data-idx="3">吐槽</li>

    			<li class="query-filter " data-idx="4">活跃</li>

    			<li class="query-filter " data-idx="5">话唠</li>

    			<li class="query-filter " data-idx="6">传说</li>

    			<li class="query-filter " data-idx="10">一见倾心</li>

    			<li class="query-filter " data-idx="11">超凡脱俗</li>

    			<li class="query-filter " data-idx="12">风华绝代</li>

    			<li class="query-filter " data-idx="13">崭露头角</li>

    			<li class="query-filter " data-idx="14">金玉满堂</li>

    			<li class="query-filter " data-idx="15">富甲一方</li>

    			<li class="query-filter " data-idx="101">LV.1</li>

    			<li class="query-filter " data-idx="102">LV.2</li>

    			<li class="query-filter " data-idx="103">LV.3</li>

    			<li class="query-filter " data-idx="104">LV.4</li>

    			<li class="query-filter " data-idx="105">LV.5</li>

    			<li class="query-filter " data-idx="106">LV.6</li>

    			<li class="query-filter " data-idx="107">LV.7</li>

    			<li class="query-filter " data-idx="108">LV.8</li>

    			<li class="query-filter " data-idx="109">LV.9</li>

    			<li class="query-filter " data-idx="110">LV.10</li>

    			<li class="query-filter " data-idx="111">LV.11</li>

    			<li class="query-filter " data-idx="112">LV.12</li>

    			<li class="query-filter " data-idx="113">LV.13</li>

    			<li class="query-filter " data-idx="114">LV.14</li>

    			<li class="query-filter " data-idx="115">LV.15</li>

    			<li class="query-filter " data-idx="116">LV.16</li>

    			<li class="query-filter " data-idx="117">LV.17</li>

    			<li class="query-filter " data-idx="118">LV.18</li>

    			<li class="query-filter " data-idx="197">小酋长</li>

    			<li class="query-filter " data-idx="198">大酋长</li>

    			<li class="query-filter " data-idx="199">首席酋长</li>

    	</ul>
    							<ul data-key="last_speak_time" data-tag="最后发言" data-type="4">
    								<li>
    									<label>最后发言：</label>
    								</li>
    								<li class="query-filter selected">不限</li>
    								<li class="query-filter">1个月内</li>
    								<li class="query-filter">1-3个月</li>
    								<li class="query-filter">3-6个月</li>
    								<li class="query-filter">6-12个月</li>
    								<li class="query-filter">12个月以上</li>
    								<li class="query-filter sl" data-val="月"><input type="text" maxlength="3"> - <input type="text" maxlength="3"> 月</li>
    							</ul>
    							<div class="group-select-more-btm" id="groupSelectMoreBtm">
    								<div>筛选条件:</div>
    								<div id="selectResultTips">
    								</div>
    								<div class="select-result">
    									<button class="clear disabled" disabled="disabled">清除</button>
    									<button class="submit" data-tag="moresub">确定</button>
    								</div>
    								<div class="clear"></div>
    							</div>
    						</div>
    						<div class="child group-select-result hide" id="groupSelectResult">

    						</div>
    					</div>

    				</div>

    				<div class="group-memeber">
    					<table cellspacing="0" cellpadding="0" border="0" width="100%" id="groupMember" align="center">
    						<tbody><tr id="groupTh">
    		<th width="32" class="td-right">

    		</th>
    		<th width="30"></th>
    		<th class="th-left1" width="200">成员</th>
    		<th class="th-left th-card" width="160">群名片</th>

    		<th class="th-left" width="100">QQ号</th>
    		<th class="th-left" width="90">性别</th>
    		<th class="th-left th-desc" width="90">
    			<div class="group-ff">
    				<div class="group-desc">
    					<a class="link">Q龄</a> <i class="arrow"></i> <i class="icon-more-select"></i>
    					<ul class="group-desc-arrow">
    						<li cmd="desc" data-tag="age" data-idx="0" idx="0">默认</li>
    						<li cmd="desc" data-tag="age" data-idx="0" idx="9" order="0"><a data-tag="age" data-idx="0">Q龄</a> <i class="icon-arrow-desc"></i></li>
    						<li cmd="desc" data-tag="age" data-idx="1" idx="8" order="1"><a data-tag="age" data-idx="1">Q龄</a> <i class="icon-arrow-desc1"></i></li>
    					</ul>
    				</div>
    			</div>
    		</th>
    		<th class="th-left th-desc" width="120">
    			<div class="group-ff">
    				<div class="group-desc">
    					<a class="link">入群时间</a> <i class="arrow"></i> <i class="icon-more-select"></i>
    					<ul class="group-desc-arrow">
    						<li cmd="desc" data-tag="jointime" data-idx="0" idx="0">默认</li>
    						<li cmd="desc" data-tag="jointime" data-idx="0" idx="11" order="0"><a data-tag="jointime" data-idx="0">入群时间</a> <i class="icon-arrow-desc"></i></li>
    						<li cmd="desc" data-tag="jointime" data-idx="1" idx="10" order="1"><a data-tag="jointime" data-idx="1">入群时间</a> <i class="icon-arrow-desc1"></i></li>
    					</ul>
    				</div>
    			</div>
    		</th>

    		<th class="th-left th-desc th-lv" width="120">
    			<div class="group-ff">
    				<div class="group-desc">
    					<a class="link">等级(积分)</a> <i class="arrow"></i> <i class="icon-more-select"></i>
    					<ul class="group-desc-arrow">
    						<li cmd="desc" data-tag="rank" data-idx="0" idx="0">默认</li>
    						<li cmd="desc" data-tag="rank" data-idx="0" idx="15" order="0"><a data-tag="orderlv" data-idx="0">等级(积分)</a> <i class="icon-arrow-desc"></i></li>
    						<li cmd="desc" data-tag="rank" data-idx="1" idx="14" order="1"><a data-tag="orderlv" data-idx="1">等级(积分)</a> <i class="icon-arrow-desc1"></i></li>
    					</ul>
    				</div>
    			</div>
    		</th>

    		<th class="th-left th-desc" width="110">
    			<div class="group-ff">
    				<div class="group-desc">
    					<a class="link">最后发言</a> <i class="arrow"></i> <i class="icon-more-select"></i>
    					<ul class="group-desc-arrow">
    						<li cmd="desc" data-tag="lastmsg" data-idx="0" idx="0">默认</li>
    						<li cmd="desc" data-tag="lastmsg" data-idx="0" idx="17" order="0"><a data-tag="orderspeak" data-idx="0">最后发言</a> <i class="icon-arrow-desc"></i></li>
    						<li cmd="desc" data-tag="lastmsg" data-idx="1" idx="16" order="1"><a data-tag="orderspeak" data-idx="1">最后发言</a> <i class="icon-arrow-desc1"></i></li>
    					</ul>
    				</div>
    			</div>
    		</th>
    		<th width="20"></th>
    	</tr>
    					</tbody>
    		<tbody class="list">

    		<tr class="mb mb895290134">
    			<td class="td-right">

    			</td>
    			<td class="td-no">1</td>
    			<td class="td-user-nick">

    					<a class="group-master-a"><i class="icon-group-master"></i></a>

    				<img class="" src="//q3.qlogo.cn/g?b=qq&amp;k=Fe163fFic3vlQvkkQDH4iaNg&amp;s=41&amp;t=1488769125" id="useIcon895290134">

    				<span>

    						矛与盾的争执

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							此号不做任何回
    						</span>


    			</td>

    			<td>

    						895290134

    			</td>
    			<td>

    				男

    			</td>
    			<td>8年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>冒泡(13)</td>

    			<td>

    					2017/04/12

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb869879123">
    			<td class="td-right">

    			</td>
    			<td class="td-no">2</td>
    			<td class="td-user-nick">

    					<a class="group-manage-a"><i class="icon-group-manage manage869879123"></i></a>

    				<img class="" src="//q4.qlogo.cn/g?b=qq&amp;k=y1gjjiblbT1iaUxpDDyBpfmA&amp;s=41&amp;t=1488621055" id="useIcon869879123">

    				<span>

    						拎着自己飞🌵

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							材料—无机—冯
    						</span>


    			</td>

    			<td>

    						869879123

    			</td>
    			<td>

    				未知

    			</td>
    			<td>9年</td>
    			<td>

    				2016/09/21

    			</td>

    			<td>活跃(72)</td>

    			<td>

    					2017/04/14

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb1447643340">
    			<td class="td-right">

    			</td>
    			<td class="td-no">3</td>
    			<td class="td-user-nick">

    					<a class="group-manage-a"><i class="icon-group-manage manage1447643340"></i></a>

    				<img class="" src="//q1.qlogo.cn/g?b=qq&amp;k=29qCWYFEiaNZaic764xlI4zQ&amp;s=41&amp;t=1488605566" id="useIcon1447643340">

    				<span>

    						二进制╮

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							生活服务部&nbsp;&nbsp;&nbsp;化
    						</span>


    			</td>

    			<td>

    						1447643340

    			</td>
    			<td>

    				女

    			</td>
    			<td>6年</td>
    			<td>

    				2016/09/06

    			</td>

    			<td>吐槽(24)</td>

    			<td>

    					2017/04/18

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb1360950914">
    			<td class="td-right">

    			</td>
    			<td class="td-no">4</td>
    			<td class="td-user-nick">

    					<a class="group-manage-a"><i class="icon-group-manage manage1360950914"></i></a>

    				<img class="" src="//q3.qlogo.cn/g?b=qq&amp;k=parU1fnKibYEy6G6ueyWD5A&amp;s=41&amp;t=1483627846" id="useIcon1360950914">

    				<span>

    						囧杨毅

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							16土木杨毅
    						</span>


    			</td>

    			<td>

    						1360950914

    			</td>
    			<td>

    				男

    			</td>
    			<td>7年</td>
    			<td>

    				2016/09/21

    			</td>

    			<td>吐槽(21)</td>

    			<td>

    					2017/04/18

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb1010735179">
    			<td class="td-right">

    			</td>
    			<td class="td-no">5</td>
    			<td class="td-user-nick">

    					<a class="group-manage-a"><i class="icon-group-manage manage1010735179"></i></a>

    				<img class="" src="//q4.qlogo.cn/g?b=qq&amp;k=ASUBpNfRe09tMQee0W96vg&amp;s=41&amp;t=1489847194" id="useIcon1010735179">

    				<span>

    						▎℡没鈊没肺ㄨ

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							生活服务部～机
    						</span>


    			</td>

    			<td>

    						1010735179

    			</td>
    			<td>

    				未知

    			</td>
    			<td>6年</td>
    			<td>

    				2016/09/12

    			</td>

    			<td>冒泡(17)</td>

    			<td>

    					2017/04/05

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb1437112548">
    			<td class="td-right">

    			</td>
    			<td class="td-no">6</td>
    			<td class="td-user-nick">

    					<a class="group-manage-a"><i class="icon-group-manage manage1437112548"></i></a>

    				<img class="" src="//q1.qlogo.cn/g?b=qq&amp;k=ZGX8FmI9K2UnP12cSiaIXrQ&amp;s=41&amp;t=1491567153" id="useIcon1437112548">

    				<span>

    						炸毛猫

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">

    						</span>


    			</td>

    			<td>

    						1437112548

    			</td>
    			<td>

    				女

    			</td>
    			<td>7年</td>
    			<td>

    				2016/09/21

    			</td>

    			<td>冒泡(17)</td>

    			<td>

    					2017/04/16

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb1757911483">
    			<td class="td-right">

    			</td>
    			<td class="td-no">7</td>
    			<td class="td-user-nick">

    					<a class="group-manage-a"><i class="icon-group-manage manage1757911483"></i></a>

    				<img class="" src="//q4.qlogo.cn/g?b=qq&amp;k=Vj36BWdeCRBibIrD8t1CxUQ&amp;s=41&amp;t=1490683498" id="useIcon1757911483">

    				<span>

    						这里会长出一朵花.🌿

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							16文法&nbsp;王莹
    						</span>


    			</td>

    			<td>

    						1757911483

    			</td>
    			<td>

    				女

    			</td>
    			<td>6年</td>
    			<td>

    				2016/09/03

    			</td>

    			<td>冒泡(14)</td>

    			<td>

    					2017/04/19

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb929461898">
    			<td class="td-right">

    			</td>
    			<td class="td-no">8</td>
    			<td class="td-user-nick">

    					<a class="group-manage-a"><i class="icon-group-manage manage929461898"></i></a>

    				<img class="" src="//q3.qlogo.cn/g?b=qq&amp;k=roCq0IcTt8fXNFK2MB6QicA&amp;s=41&amp;t=1489482448" id="useIcon929461898">

    				<span>

    						ζั͡&nbsp;&nbsp;&nbsp;&nbsp;๓

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">

    						</span>


    			</td>

    			<td>

    						929461898

    			</td>
    			<td>

    				女

    			</td>
    			<td>7年</td>
    			<td>

    				2016/09/14

    			</td>

    			<td>冒泡(13)</td>

    			<td>

    					2017/04/14

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb592366245">
    			<td class="td-right">

    			</td>
    			<td class="td-no">9</td>
    			<td class="td-user-nick">

    					<a class="group-manage-a"><i class="icon-group-manage manage592366245"></i></a>

    				<img class="" src="//q2.qlogo.cn/g?b=qq&amp;k=SnjOjeaBpxnnmBySTJ6Uww&amp;s=41&amp;t=1490688610" id="useIcon592366245">

    				<span>

    						你指尖闪烁的电光

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							生活服务部&nbsp;测
    						</span>


    			</td>

    			<td>

    						592366245

    			</td>
    			<td>

    				男

    			</td>
    			<td>10年</td>
    			<td>

    				2016/11/06

    			</td>

    			<td>冒泡(8)</td>

    			<td>

    					2017/04/18

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb497275782">
    			<td class="td-right">

    			</td>
    			<td class="td-no">10</td>
    			<td class="td-user-nick">

    					<a class="group-manage-a"><i class="icon-group-manage manage497275782"></i></a>

    				<img class="" src="//q3.qlogo.cn/g?b=qq&amp;k=4toMoyM1dDY5aniadXkwvvg&amp;s=41&amp;t=1483324283" id="useIcon497275782">

    				<span>

    						爆栗方圆

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							生活服务部-电
    						</span>


    			</td>

    			<td>

    						497275782

    			</td>
    			<td>

    				男

    			</td>
    			<td>10年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					2016/09/28

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb2902459153">
    			<td class="td-right">

    			</td>
    			<td class="td-no">11</td>
    			<td class="td-user-nick">

    					<a><i class="manage2902459153" data-id="2902459153"></i></a>

    				<img class="" src="//q2.qlogo.cn/g?b=qq&amp;k=mkmM7wniabwlKDeIdZq2UrQ&amp;s=41&amp;t=1489853929" id="useIcon2902459153">

    				<span>

    						大西瓜

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">

    						</span>


    			</td>

    			<td>

    						2902459153

    			</td>
    			<td>

    				男

    			</td>
    			<td>2年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					2016/07/05

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb591902795">
    			<td class="td-right">

    			</td>
    			<td class="td-no">12</td>
    			<td class="td-user-nick">

    					<a><i class="manage591902795" data-id="591902795"></i></a>

    				<img class="" src="//q4.qlogo.cn/g?b=qq&amp;k=H7dRCqZkOIhiaicdCbXDKbDA&amp;s=41&amp;t=1488618994" id="useIcon591902795">

    				<span>

    						🍄

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							14国贸王翊璇
    						</span>


    			</td>

    			<td>

    						591902795

    			</td>
    			<td>

    				未知

    			</td>
    			<td>10年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					-

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb913511565">
    			<td class="td-right">

    			</td>
    			<td class="td-no">13</td>
    			<td class="td-user-nick">

    					<a><i class="manage913511565" data-id="913511565"></i></a>

    				<img class="" src="//q2.qlogo.cn/g?b=qq&amp;k=SRH2kvvoMacXydnvVXfDAQ&amp;s=41&amp;t=1492592468" id="useIcon913511565">

    				<span>

    						懒惰啊！就是菜鸡的原罪

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							15化工王轶伦
    						</span>


    			</td>

    			<td>

    						913511565

    			</td>
    			<td>

    				男

    			</td>
    			<td>8年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					2016/09/19

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb1668380019">
    			<td class="td-right">

    			</td>
    			<td class="td-no">14</td>
    			<td class="td-user-nick">

    					<a><i class="manage1668380019" data-id="1668380019"></i></a>

    				<img class="" src="//q4.qlogo.cn/g?b=qq&amp;k=L0gHPibZgwe178rpjPibQNSA&amp;s=41&amp;t=1483296149" id="useIcon1668380019">

    				<span>

    						淡忘的记忆

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							孙学凯
    						</span>


    			</td>

    			<td>

    						1668380019

    			</td>
    			<td>

    				男

    			</td>
    			<td>3年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					-

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb724750170">
    			<td class="td-right">

    			</td>
    			<td class="td-no">15</td>
    			<td class="td-user-nick">

    					<a><i class="manage724750170" data-id="724750170"></i></a>

    				<img class="" src="//q3.qlogo.cn/g?b=qq&amp;k=y5FUZUwWyXT7dBaFicBW5UA&amp;s=41&amp;t=1492008556" id="useIcon724750170">

    				<span>

    						妄

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							环化张浩
    						</span>


    			</td>

    			<td>

    						724750170

    			</td>
    			<td>

    				男

    			</td>
    			<td>10年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					-

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb307810112">
    			<td class="td-right">

    			</td>
    			<td class="td-no">16</td>
    			<td class="td-user-nick">

    					<a><i class="manage307810112" data-id="307810112"></i></a>

    				<img class="" src="//q1.qlogo.cn/g?b=qq&amp;k=WRicDl3aSdiaJ5gXINFI1QIQ&amp;s=41&amp;t=1483307938" id="useIcon307810112">

    				<span>

    						恩。

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">

    						</span>


    			</td>

    			<td>

    						307810112

    			</td>
    			<td>

    				男

    			</td>
    			<td>13年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					-

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb1509920574">
    			<td class="td-right">

    			</td>
    			<td class="td-no">17</td>
    			<td class="td-user-nick">

    					<a><i class="manage1509920574" data-id="1509920574"></i></a>

    				<img class="" src="//q3.qlogo.cn/g?b=qq&amp;k=XS1XLtSibtFITru0wv6SNFA&amp;s=41&amp;t=1483282561" id="useIcon1509920574">

    				<span>

    						我非圣贤

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							机械-何贤盛
    						</span>


    			</td>

    			<td>

    						1509920574

    			</td>
    			<td>

    				男

    			</td>
    			<td>6年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					-

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb732269460">
    			<td class="td-right">

    			</td>
    			<td class="td-no">18</td>
    			<td class="td-user-nick">

    					<a><i class="manage732269460" data-id="732269460"></i></a>

    				<img class="" src="//q1.qlogo.cn/g?b=qq&amp;k=woH5u53TMNzTiaqTXibqPJWw&amp;s=41&amp;t=1492317900" id="useIcon732269460">

    				<span>

    						JoY～💋

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							文法—姚翡
    						</span>


    			</td>

    			<td>

    						732269460

    			</td>
    			<td>

    				女

    			</td>
    			<td>6年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					2015/10/13

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb909549255">
    			<td class="td-right">

    			</td>
    			<td class="td-no">19</td>
    			<td class="td-user-nick">

    					<a><i class="manage909549255" data-id="909549255"></i></a>

    				<img class="" src="//q4.qlogo.cn/g?b=qq&amp;k=A6k8MxQDI9golibianXnnsxA&amp;s=41&amp;t=1483360348" id="useIcon909549255">

    				<span>

    						吴振豪

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							14石油-吴振豪
    						</span>


    			</td>

    			<td>

    						909549255

    			</td>
    			<td>

    				男

    			</td>
    			<td>7年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					2015/10/14

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb1045949889">
    			<td class="td-right">

    			</td>
    			<td class="td-no">20</td>
    			<td class="td-user-nick">

    					<a><i class="manage1045949889" data-id="1045949889"></i></a>

    				<img class="" src="//q2.qlogo.cn/g?b=qq&amp;k=ZWB1gGgGmvaPyQbXtsXtTw&amp;s=41&amp;t=1483372307" id="useIcon1045949889">

    				<span>

    						滇山之子

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">

    						</span>


    			</td>

    			<td>

    						1045949889

    			</td>
    			<td>

    				男

    			</td>
    			<td>6年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					-

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb1076566519">
    			<td class="td-right">

    			</td>
    			<td class="td-no">21</td>
    			<td class="td-user-nick">

    					<a><i class="manage1076566519" data-id="1076566519"></i></a>

    				<img class="icon-deficon" src="//qun.qq.com/css/imgs/space.gif" id="useIcon1076566519">

    				<span>

    						保护我方安琪拉

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							公寓机自朱佳琳
    						</span>


    			</td>

    			<td>

    						1076566519

    			</td>
    			<td>

    				未知

    			</td>
    			<td>7年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					-

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		</tbody>
    	</table>
    					<div id="searchEmpty" style="display: none;"></div>
    				</div>

    			</dd>
    		</dl>
    	</div>

    		<div class="footer">
    		<p>友情链接：<a href="http://im.qq.com/" target="_blank">QQ官方网站</a> | <a href="http://open.qq.com/" target="_blank">腾讯开放平台</a> | <a href="http://qun.qq.com/qunlearn/qunlearn.html" target="_blank">在线教育介绍</a> | <a href="http://shang.qq.com" target="_blank">QQ商家</a> | <a href="http://vip.qq.com/" target="_blank">QQ会员</a></p>
    	    <p>Copyright © 1998-2015 Tencent. All Rights Reserved.</p>
    	    <p>腾讯公司 版权所有</p>
    	</div>
    	<script type="text/javascript">
    	    function loadJs(){
    	        var href = location.href;
    	        var dom = document.createElement('script');
    	        if(href.indexOf('https://') >= 0){
    	            dom.src = 'https://pingjs.qq.com/tcss.ping.https.js';
    	        }else{
    	            dom.src = 'http://pingjs.qq.com/tcss.ping.js';
    	        }
    	        document.body.appendChild(dom);
    	    }
    	    loadJs();
    	</script><script src="http://pingjs.qq.com/tcss.ping.js"></script>


    	<script type="text/template" id="newGroupMemberTmp">
    		<%
    			for(var i in list){
    				var item = list[i];
    		%>
    			<li>
    				<a>
    					<span><img src="<%=avater(item.uin)%>" /><%=item.name%>(<%=html(item.uin)%>)</span>
    					<div class="i-link" data-id="<%=attr(item.uin)%>"><p><i class="icon-close"></i></p></div>
    				</a>
    			</li>
    		<%}%>
    	</script>

    	<script type="text/template" id="friendsmartTmp">
    		<ul>
    		<%
    		for(var i=0,l=list.length;i<l;i++){
    			var item = list[i];
    		%>
    			<li title=<%=attr(item.name)%> data-id="<%=attr(item.uin)%>">
    				<a><img src="<%=avater(item.uin)%>" /><%=item.oname%>(<%=item.ouin%>)</a>
    			</li>
    		<%}%>
    		</ul>
    	</script>

    	<script type="text/template" id="myFriendTmp">
    		<div class="member-body">
    			<div class="input-tit">
    				<div class="input-search">
    					<input type="text" class="dialog-search-input" value="搜索关键词" data-def="搜索关键词" />
    					<button class="group-search-btn icon-search-btn"></button>
    				</div>
    				<div class="search-smart">
    				</div>
    			</div>
    			<div class="my-friend">
    				<ul class="my-friend-list" id="myFriendList">
    					<%
    						for(var i in list){
    							var item = list[i];
    					%>
    						<li class="friend-group">
    							<a class="friend-group-name" data-child="<%if(item.mems){%>1<%}else{%>0<%}%>"><i <%if(item.mems){%>class="icon-arrow-left"<%}%>></i> <span><%if(item.gname){%><%=item.gname%><%}else{%>我的好友<%}%></span> <i data-idx="<%=i%>" class="icon-friend-join"></i></a>
    							<%if(item.mems){%>
    								<ul class="friend-group-list">
    									<%
    										for(var m=0,n=item.mems.length;m<n;m++){
    											var obj = item.mems[m];
    									%>
    									<li>
    										<a class="friend" data-id="<%=attr(obj.uin)%>"><img src="<%=avater(obj.uin)%>" /><%=obj.name%>(<%=obj.uin%>)</a>
    									</li>
    									<%}%>
    								</ul>
    							<%}%>
    						</li>
    					<%}%>
    				</ul>
    				<div class="icon-arrow-join"></div>
    				<ul class="selected-friend" id="newGroupMemberList">

    				</ul>
    			</div>
    		</div>
    	</script>

    	<script type="text/template" id="searchResultTmp">
    		<div class="clear"></div>
    		<%if(!$.isEmptyObject(tips)){%>
    		<div>筛选条件:</div>
    		<div class="result-zone" id="groupSelectResultTips">
    			<%
    				for(var i in tips){
    					var item = tips[i];
    			%>
    			<a class="select-result select-result<%=attr(item.type)%>"><span><%=html(item.tag)%>： <%=html(item.value)%></span> <i class="icon-close" data-key="<%=attr(item.key)%>"></i></a>
    			<%}%>
    		</div>
    		<div class="select-result" id="searchResult">
    			<%if(key!=''){%>搜索条件：<span><%=html(key)%></span><%}%>   共<span>  <%=html(num)%> </span> 人符合条件，<a class="reset-search">清空条件</a>
    		</div>
    		<%}else{%>
    			共搜索出含“<span><%=html(key)%></span>”的群成员：<span> <%=html(num)%> 人</span>　
    			<a class="reset-search">返回全员列表</a>
    		<%}%>
    		<div class="clear"></div>
    	</script>

    	<script type="text/template" id="tagMenuTmp">
    		<div class="mark-div">
    			<div class="mark-select">
    				<div class="mark-select-tit">
    					<span><%if(tag>=0 && list[tag]){%><%=list[tag]%><%}%></span>
    					<i class="icon-arrow-gray"></i>
    				</div>

    				<ul>
    					<%
    						for(var i in list){
    					%>
    						<li><a data-tag="changetag" data-idx="<%=attr(i)%>"><%=list[i]%></a></li>
    					<%}%>
    					<li><a data-tag="changetag" data-idx="-1">&nbsp;</a></li>
    				</ul>
    				<div class="mark-select-add">
    					<a><i class="icon-add-mark"></i>添加</a>
    				</div>
    			</div>
    		</div>
    	</script>

    	<script type="text/template" id="searchResultTipTmp">
    		<a class="select-result <%if(type){%>select-result<%=attr(type)%><%}%> <%if(key){%>select-result<%=attr(key)%><%}%>"><span><%=html(tag)%>： <%=html(value)%></span> <i class="icon-close" data-type="<%=attr(type)%>" data-key="<%=attr(key)%>"></i></a>
    	</script>

    	<script type="text/template" id="groupMemberThTmp">
    		<th width="32" class="td-right">
    			<%if(show){%>
    				<input id="selectAll" type="checkbox" class="check-input" />
    			<%}%>
    		</th>
    		<th width="30"></th>
    		<th class="th-left1" width="<%=w.member%>">成员</th>
    		<th class="th-left th-card" width="<%=w.card%>">群名片</th>
    		<%if(tag){%>
    		<th class="th-left th-mark" width="110">标签</th>
    		<%}%>
    		<th class="th-left" width="<%=w.qq%>">QQ号</th>
    		<th class="th-left" width="<%=w.sex%>">性别</th>
    		<th class="th-left th-desc" width="<%=w.qage%>">
    			<div class="group-ff">
    				<div class="group-desc">
    					<a class="link">Q龄</a> <i class="arrow"></i> <i class="icon-more-select"></i>
    					<ul class="group-desc-arrow">
    						<li cmd="desc" data-tag="age" data-idx="0" idx="0">默认</li>
    						<li cmd="desc" data-tag="age" data-idx="0" idx="9" order="0"><a data-tag="age" data-idx="0">Q龄</a> <i class="icon-arrow-desc"></i></li>
    						<li cmd="desc" data-tag="age" data-idx="1" idx="8" order="1"><a data-tag="age" data-idx="1">Q龄</a> <i class="icon-arrow-desc1"></i></li>
    					</ul>
    				</div>
    			</div>
    		</th>
    		<th class="th-left th-desc" width="<%=w.join%>">
    			<div class="group-ff">
    				<div class="group-desc">
    					<a class="link">入群时间</a> <i class="arrow"></i> <i class="icon-more-select"></i>
    					<ul class="group-desc-arrow">
    						<li cmd="desc" data-tag="jointime" data-idx="0" idx="0">默认</li>
    						<li cmd="desc" data-tag="jointime" data-idx="0" idx="11" order="0"><a data-tag="jointime" data-idx="0">入群时间</a> <i class="icon-arrow-desc"></i></li>
    						<li cmd="desc" data-tag="jointime" data-idx="1" idx="10" order="1"><a data-tag="jointime" data-idx="1">入群时间</a> <i class="icon-arrow-desc1"></i></li>
    					</ul>
    				</div>
    			</div>
    		</th>
    		<%if(lv){%>
    		<th class="th-left th-desc th-lv" width="<%=w.lv%>">
    			<div class="group-ff">
    				<div class="group-desc">
    					<a class="link">等级(积分)</a> <i class="arrow"></i> <i class="icon-more-select"></i>
    					<ul class="group-desc-arrow">
    						<li cmd="desc" data-tag="rank" data-idx="0" idx="0">默认</li>
    						<li cmd="desc" data-tag="rank" data-idx="0" idx="15" order="0"><a data-tag="orderlv" data-idx="0">等级(积分)</a> <i class="icon-arrow-desc"></i></li>
    						<li cmd="desc" data-tag="rank" data-idx="1" idx="14" order="1"><a data-tag="orderlv" data-idx="1">等级(积分)</a> <i class="icon-arrow-desc1"></i></li>
    					</ul>
    				</div>
    			</div>
    		</th>
    		<%}%>
    		<th class="th-left th-desc" width="110">
    			<div class="group-ff">
    				<div class="group-desc">
    					<a class="link">最后发言</a> <i class="arrow"></i> <i class="icon-more-select"></i>
    					<ul class="group-desc-arrow">
    						<li cmd="desc" data-tag="lastmsg" data-idx="0"  idx="0">默认</li>
    						<li cmd="desc" data-tag="lastmsg" data-idx="0"  idx="17" order="0"><a data-tag="orderspeak" data-idx="0" >最后发言</a> <i class="icon-arrow-desc"></i></li>
    						<li cmd="desc" data-tag="lastmsg" data-idx="1"  idx="16" order="1"><a  data-tag="orderspeak" data-idx="1" >最后发言</a> <i class="icon-arrow-desc1"></i></li>
    					</ul>
    				</div>
    			</div>
    		</th>
    		<th width="20"></th>
    	</script>

    	<script type="text/template" id="groupMemberEmptyTmp">
    		<div class="empty">没有符合筛选条件的群成员</div>
    	</script>

    	<script type="text/template" id="groupMemberTmp">
    		<tbody class="list">
    		<%
    			for(var i =0,l=list.length;i<l;i++){
    				var item = list[i];
    				st++
    		%>
    		<tr class="mb mb<%=item.uin%>">
    			<td class="td-right">
    				<%if(type == 'create'){%>
    					<%if(item.role != 0){%>
    					<input id="input<%=attr(item.uin)%>" type="checkbox" class="check-input" value="<%=attr(item.uin)%>" data-type="<%=item.role%>" />
    					<%}%>
    				<%}else if(type=='manage'){%>
    					<%if(item.role == 2){%>
    						<input  id="input<%=attr(item.uin)%>" type="checkbox" class="check-input" value="<%=attr(item.uin)%>" data-type="<%=item.role%>" />
    					<%}%>
    				<%}%>
    			</td>
    			<td class="td-no"><%=html(st)%></td>
    			<td class="td-user-nick">
    				<%if(item.role==0){%>
    					<a class="group-master-a"><i class="icon-group-master"></i></a>
    				<%}else if(item.role==1){%>
    					<a class="group-manage-a"><i class="icon-group-manage manage<%=item.uin%>" <%if(type == 'create'){%>title="取消管理员" data-tag="delmanage" data-id="<%=item.uin%>"<%}%>></i></a>
    				<%}else{%>
    					<a><i class="manage<%=item.uin%>" data-id="<%=item.uin%>"></i></a>
    				<%}%>
    				<img class="icon-deficon" src="//qun.qq.com/css/imgs/space.gif" id="useIcon<%=item.uin%>" />
    				<%if(item.flag & 0x1){%>
    					<a class="flag" <%if(ie6){%>href="javascript:void(0);"<%}%> hidefocus="true" title="不良记录成员"><i class="icon-member-flag"></i></a>
    				<%}%>
    				<span>
    					<%
    						if(item.match && item.match.type & 0x2){
    					%>
    						<%=show(item.match.word,html(item.nick))%>
    					<%}else{%>
    						<%=html(item.nick)%>
    					<%}%>
    				</span>
    			</td>
    			<td class="td-card">
    					<%
    						if((type!='join' && !(item.flag&0x2)) || item.uin == my){
    					%>
    					<span>
    						<span class="group-card group-card<%=item.uin%>">
    							<%if(item.match && item.match.type & 0x1){%>
    								<%=show(item.match.word,html(item.card))%>
    							<%}else{%>
    								<%=html(item.card)%>
    							<%}%>
    						</span>
    						<input class="member-card" id="member-card<%=item.uin%>" value="<%if(item.card){%><%=item.card%><%}%>" type="text" data-old="<%if(item.card){%><%=item.card%><%}%>" data-id="<%=item.uin%>" <%if(item.match && item.match.type==1){%>data-key="<%=item.match.word%>"<%}%> />
    					</span>
    					<%}else{%>
    						<span class="white">
    							<%if(item.card){%><%=html(item.card)%><%}%>
    						</span>
    					<%}%>

    			</td>
    			<%if(tag){%>
    			<td class="td-mark"  data-tags="<%=attr(item.tags)%>" data-id="<%=item.uin%>">
    				<%if(type != 'join' || item.uin == my){%>
    				<div class="td-mark-old" data-type="<%=item.tags%>">
    					<span>
    						<%if(tag && item.tags>=0){%><%=tag[item.tags]%><%}else{%>　<%}%>
    					</span>
    					<i class="icon-arrow-gray"></i>
    				</div>
    				<%}else{%>
    					<%if(tag && item.tags>=0){%><%=tag[item.tags]%><%}%>
    				<%}%>
    			</td>
    			<%}%>
    			<td>
    					<%if(item.match && item.match.type&0x4){%>
    						<%=show(item.match.word,item.uin)%>
    					<%}else{%>
    						<%=item.uin%>
    					<%}%>
    			</td>
    			<td>
    				<%if(item.g === 1){%>
    				女
    				<%}else if(item.g === 0){%>
    				男
    				<%}else{%>
    				未知
    				<%}%>
    			</td>
    			<td><%if(typeof item.qage != 'undefined'){%><%=item.qage%>年<%}%></td>
    			<td>
    				<%if(item.join_time){%>
    				<%=time(item.join_time)%>
    				<%}else{%>
    					2012年5月以前
    				<%}%>
    			</td>
    			<%if(lv){%>
    			<td><%if(lv){%><%=lv[item.lv.level]%>(<%=item.lv.point%>)<%}%></td>
    			<%}%>
    			<td>
    				<%if(item.last_speak_time){%>
    					<%=time(item.last_speak_time)%>
    				<%}else{%>
    					-
    				<%}%>
    			</td>
    			<td class="td-delete">
    				<%if(type == 'create'){%>
    					<%if(item.role != 0){%>
    					<i class="icon-close" title="删除该成员" data-tag="delmemberico" data-id="<%=attr(item.uin)%>"></i>
    					<%}%>
    				<%}else if(type=='manage'){%>
    					<%if(item.role == 2){%>
    						<i class="icon-close" title="删除该成员" data-tag="delmemberico" data-id="<%=attr(item.uin)%>"></i>
    					<%}%>
    				<%}%>
    			</td>
    		</tr>
    		<%}%>
    		</tbody>
    	</script>

    	<script type="text/template" id="groupMemberTitTmp">
    		群成员人数: <span id="groupMemberNum"><%=html(num)%></span>/<%=html(all)%>
    		<%if(type == 'create' || type == 'manage'){%>
    		<button cmd="add" class="add-member" data-tag="addmember">添加成员</button>
    		<%}%>
    		<%if(type == 'create'){%>
    		<button cmd="set" disabled class="set-manage disabled" data-tag="setmanage">设置管理员</button>
    		<%}%>
    		<%if(type == 'create' || type == 'manage'){%>
    		<button cmd="del" disabled class="disabled del-member" data-tag="delmemberbtn">删除成员</button>
    		<%}%>
    	</script>

    	<script type="text/template" id="groupLevelTmp">
    		<li>
    			<label>等　　级：</label>
    		</li>
    		<li class="query-filter <%if(!filter.lv){%>selected<%}%>" data-idx="0">不限</li>
    		<%
    			for(var i in list){
    		%>
    			<li class="query-filter <%if(filter.lv && filter.lv == i){%>selected<%}%>" data-idx="<%=attr(i)%>"><%=list[i]%></li>
    		<%}%>
    	</script>

    	<script type="text/template" id="smartTmp">
    		<ul>
    		<%
    		for(var i=0,l=list.length;i<l;i++){
    			var item = list[i];
    		%>
    			<li title="<%=item.gn%>" data-tag="clicksearch" data-id="<%=attr(item.gc)%>">
    				<a data-tag="clicksearch"><img data-tag="clicksearch" class="icon-def-gicon gicon<%=attr(item.gc)%>" <%if(item.face){%>src="<%=item.face%>"<%}%> />
    				<%=item.ogn%>(<%=item.ogc%>)</a>
    			</li>
    		<%}%>
    		</ul>
    	</script>

    	<script type="text/template" id="myGroupTmp">
    	<div class="member-body">
    		<%if(data.nums){%>
    		<div class="input-tit">
    			<div class="input-search">
    				<input type="text" class="dialog-search-input" value="搜索群名称或群号" data-def="搜索群名称或群号" />
    				<button class="group-search-btn icon-search-btn"></button>
    			</div>
    			<div class="search-smart">
    			</div>
    		</div>
    		<div class="my-all-group">

    			<%if(data.create && data.create.length){%>
    			<h4>我创建的群(<%=data.create.length%>)</h4>
    			<ul class="my-group-list">
    				<%
    					for(var i = 0,l=data.create.length;i<l;i++){
    						var item = data.create[i];
    				%>
    				<li title=<%=attr(item.gn)%> data-id="<%=attr(item.gc)%>">
    					<img class="icon-def-gicon gicon<%=attr(item.gc)%>" <%if(item.face){%>src="<%=item.face%>"<%}%> />
    					<%=item.gn%>
    				</li>
    				<%}%>
    			</ul>
    			<%}%>

    			<%if(data.manage && data.manage.length){%>
    			<h4 class="top">我管理的群(<%=data.manage.length%>)</h4>
    			<ul class="my-group-list">
    				<%
    					for(var i = 0,l=data.manage.length;i<l;i++){
    						var item = data.manage[i];
    				%>
    				<li title=<%=attr(item.gn)%> data-id="<%=attr(item.gc)%>">
    					<img  class="icon-def-gicon gicon<%=attr(item.gc)%>"  <%if(item.face){%>src="<%=item.face%>"<%}%> />
    					<%=item.gn%>
    				</li>
    				<%}%>
    			</ul>
    			<%}%>

    			<%if(data.join && data.join.length){%>
    			<h4 class="top">我加入的群(<%=data.join.length%>)</h4>
    			<ul class="my-group-list">
    				<%
    					for(var i = 0,l=data.join.length;i<l;i++){
    						var item = data.join[i];
    				%>
    				<li title=<%=attr(item.gn)%> data-id="<%=attr(item.gc)%>">
    					<img class="icon-def-gicon gicon<%=attr(item.gc)%>"  <%if(item.face){%>src="<%=item.face%>"<%}%> />
    					<%=item.gn%>
    				</li>
    				<%}%>
    			</ul>
    			<%}%>
    			</div>
    		<%}else{%>
    			<div class="my-all-group">
    			<div class="tips"><i class="icon-dialog-alert"></i>您当前没有加入任何群，现在就去<a href="//id.qq.com/index.html#qun-create" target="_blank">创建群</a>吧！</div>
    			</div>
    		<%}%>

    	</div>
    	</script>

    	<script type="text/template" id="oneTipsTmp">
    		<li class="tags-li"><a><input type="text" value="<%=name%>" /> <i class="icon-close" data-name="<%=name%>"></i></a></li>
    	</script>

    	<script type="text/template" id="addTipsTmp">
    		<div class="member-body">
    			<div class="input-tit">
    				<div class="input-search">
    					<input type="text" class="group-tips-txt" />
    				</div>
    				<div class="input-btn">
    					<input type="button" value="添加" />
    				</div>
    			</div>
    			<div style="clear:both;height:200px;">
    				<div class="dialog-tips">
    					<i class="icon-dialog-tips"></i><span>标签名称长度不超过8个汉字</span>
    				</div>
    				<ul class="member-label-list" id="memberLabelList">
    					<%
    						for(var i in list){
    							var item = list[i];
    					%>
    						<li class="tags-li"><a <%if(ie6){%>href="javascript:void(0);"<%}%>><input class="tags-input"  data-id="<%=i%>" type="text" value="<%=item%>" /> <i class="icon-close" data-id="<%=i%>"></i></a></li>
    					<%}%>
    				</ul>
    				<div class="dialog-tips">
    					<i class="icon-dialog-tips"></i><span>标签个数不超过20个</span></div>
    				<div class="clear"></div>
    			</div>
    		</div>
    	</script>

    	<script>
    		var BJ_REPORT = (function(global) {
    		    if (global.BJ_REPORT) return global.BJ_REPORT;

    		    var _error = [];
    		    var orgError = global.onerror;
    		    global.onerror = function(msg, url, line, col, error) {
    		    };

    		    var _config = {
    		        id: 0,
    		        uin: 0,
    		        url: "",
    		        combo: 1,
    		        ext: {},
    		        level: 4, // 1-debug 2-info 4-error 8-fail
    		        ignore: [],
    		        random: 1,
    		        delay: 1000,
    		        submit: null
    		    };

    		    var _isOBJByType = function(o, type) {
    		        return Object.prototype.toString.call(o) === "[object " + (type || "Object") + "]";
    		    };

    		    var _isOBJ = function(obj) {
    		        var type = typeof obj;
    		        return type === 'object' && !!obj;
    		    };


    		    var _processError = function(errObj) {
    		        try {
    		            if (errObj.stack) {
    		                var url = errObj.stack.match('//[^\n]+');
    		                url = url ? url[0] : "";
    		                var rowCols = url.match(':([0-9]+):([0-9]+)');
    		                if (!rowCols) {
    		                    rowCols = [0, 0, 0];
    		                }

    		                var stack = _processStackMsg(errObj);
    		                return {
    		                    msg: stack,
    		                    rowNum: rowCols[1],
    		                    colNum: rowCols[2],
    		                    target: url.replace(rowCols[0], '')
    		                        /* stack : stack*/
    		                };
    		            } else {
    		                return errObj;
    		            }
    		        } catch (err) {
    		            return errObj;
    		        }
    		    };

    		    var _processStackMsg = function(error) {
    		        var stack = error.stack.replace(/\n/gi, '').split(/\bat\b/).slice(0, 5).join("@").replace(/\?[^:]+/gi, "");
    		        var msg = error.toString();
    		        if (stack.indexOf(msg) < 0) {
    		            stack = msg + "@" + stack;
    		        }
    		        return stack;
    		    };

    		    var _error_tostring = function(error, index) {
    		        var param = [];
    		        var params = [];
    		        var stringify = [];
    		        if (_isOBJ(error)) {
    		            error.level = error.level || _config.level;
    		            for (var key in error) {
    		                var value = error[key] || "";
    		                if (value) {
    		                    if (_isOBJ(value)) {
    		                        try {
    		                            value = JSON.stringify(value);
    		                        } catch (err) {
    		                            value = "[BJ_REPORT detect value stringify error] " + err.toString();
    		                        }
    		                    }
    		                    stringify.push(key + ":" + value);
    		                    param.push(key + "=" + encodeURIComponent(value));
    		                    params.push(key + "[" + index + "]=" + encodeURIComponent(value));
    		                }
    		            }
    		        }

    		        // msg[0]=msg&target[0]=target -- combo report
    		        // msg:msg,target:target -- ignore
    		        // msg=msg&target=target -- report with out combo
    		        return [params.join("&"), stringify.join(","), param.join("&")];
    		    };

    		    var _imgs = [];
    		    var _submit = function(url) {
    		        if (_config.submit) {
    		            _config.submit(url);
    		        } else {
    		            var _img = new Image();
    		            _imgs.push(_img);
    		            _img.src = url;
    		        }
    		    };

    		    var error_list = [];
    		    var comboTimeout = 0;
    		    var _send = function(isReoprtNow) {
    		        if (!_config.report) return;

    		        while (_error.length) {
    		            var isIgnore = false;
    		            var error = _error.shift();
    		            var error_str = _error_tostring(error, error_list.length);
    		            for (var i = 0, l = _config.ignore.length; i < l; i++) {
    		                var rule = _config.ignore[i];
    		                if ((_isOBJByType(rule, "RegExp") && rule.test(error_str[1])) ||
    		                    (_isOBJByType(rule, "Function") && rule(error, error_str[1]))) {
    		                    isIgnore = true;
    		                    break;
    		                }
    		            }
    		            if (!isIgnore) {
    		                if (_config.combo) {
    		                    error_list.push(error_str[0]);
    		                } else {
    		                    _submit(_config.report + error_str[2] + "&_t=" + (+new Date));
    		                }
    		                _config.onReport && (_config.onReport(_config.id, error));
    		            }
    		        }

    		        // 合并上报
    		        var count = error_list.length;
    		        if (count) {
    		            var comboReport = function() {
    		                clearTimeout(comboTimeout);
    		                _submit(_config.report + error_list.join("&") + "&count=" + count + "&_t=" + (+new Date));
    		                comboTimeout = 0;
    		                error_list = [];
    		            };

    		            if (isReoprtNow) {
    		                comboReport(); // 立即上报
    		            } else if (!comboTimeout) {
    		                comboTimeout = setTimeout(comboReport, _config.delay); // 延迟上报
    		            }
    		        }
    		    };

    		    var report = {
    		        push: function(msg) { // 将错误推到缓存池
    		            if (Math.random() >= _config.random) {
    		                return report;
    		            }
    		            _error.push(_isOBJ(msg) ? _processError(msg) : {
    		                msg: msg
    		            });
    		            _send();
    		            return report;
    		        },
    		        info : function(msg){
    			    	if(Math.random()*100>2){
    			    		return;
    			    	}

    		            if (!msg) {
    		                return report;
    		            }
    		            if (_isOBJ(msg)) {
    		                msg.level = 2;
    		            } else {
    		                msg = {
    		                    msg: msg,
    		                    level: 2
    		                };
    		            }
    		            report.push(msg);
    		            return report;
    		        },
    		        init: function(config) { // 初始化
    		            if (_isOBJ(config)) {
    		                for (var key in config) {
    		                    _config[key] = config[key];
    		                }
    		            }
    		            // 没有设置id将不上报
    		            var id = parseInt(_config.id, 10);
    		            if (id) {
    		                _config.report = (_config.url || "//badjs2.qq.com/badjs") + "?id=" + id + "&uin=" + parseInt(_config.uin || (document.cookie.match(/\buin=\D+(\d+)/) || [])[1], 10) + "&from=" + encodeURIComponent(location.href) + "&ext=" + JSON.stringify(_config.ext) + "&";
    		            }
    		            return report;
    		        },

    		        __onerror__: global.onerror


    		    };

    		    return report;
    		}(window));

    		BJ_REPORT.init({
    		    id: 85
    		});
    	</script>

    	<script charset="utf-8" src="//s.url.cn/pub/js/qreport.js?_bid=2231"></script>

    	<script src="//s1.url.cn/qqun/qun/js/lib/jquery-9519b.js"></script>

    	<script src="//s1.url.cn/qqun/qun/js/lib/jquery.base-fe8ad.js"></script>

    	<script src="//s1.url.cn/qqun/qun/js/public/base_member-0ca65.js"></script><div class="ui-overlay"></div>
    	<script src="//s1.url.cn/qqun/qun/js/member-12177.js"></script>



    </body></html>
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" class="ver54"><head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="keywords" content="QQ群,群,群教育,一键加群,加群,群开放能力,群开放,群认证,2000人群,2K人群,QQ,Tencent">
    <meta name="description" content="腾讯QQ群官方网站。提供QQ群最新功能介绍、群应用接入、开放接口、群认证等丰富内容，群聚你我精彩。">
    <link rel="stylesheet" href="//s2.url.cn/qqun/qun/css/member-33c75.css">
    <link rel="shortcut icon" href="//im.qq.com/favicon.ico">
    <script src="http://jsqmt.qq.com/cdn_djl.js" type="text/javascript" async=""></script><script>
    	var dt0 = new Date();
    </script>
    <title>QQ群官网-成员管理</title>
    <script src="//jqmt.qq.com/cdn_dianjiliu.js?a=0.5019544216338545"></script></head>
    <body>
    	    <div class="header">
            <div class="header-top">
                <a href="//qun.qq.com" class="logo"></a>

                <div class="header-nav">
                    <ul id="headerNav">
                        <li><a href="/index.html#click">首页</a></li>
                        <li><a href="http://buluo.qq.com/buluoadmin/home.html?platform=qun" target="_blank">群订阅号</a></li>
                        <li><a href="/open.html#click">开放能力</a></li>
                        <li class="selected"><a href="/manage.html#click" data-tag="manage">群管理</a></li>
                        <li><a href="http://buluo.qq.com/p">兴趣部落</a></li>
                        <li><a href="/join.html" data-tag="join">加群组件</a></li>
                        <li><a href="http://kf.qq.com/product/group.html" target="_blank" data-tag="help">帮助</a></li>
                    </ul>
                    <div class="header-info" id="headerInfo"><p class="user-info"><a class="user-nick" title="(๑• . •๑)">(๑• . •๑)</a>&nbsp;<a cmd="loginoff" data-tag="logout" class="logout">[退出]</a></p><p>|</p><p><a href="http://support.qq.com/write.shtml?fid=35&amp;ADPUBNO=" target="_blank" data-tag="fk">反馈</a></p></div>
                </div>
            </div>
        </div>

    	<div class="body">
    		<dl>
    			<dt>
    				<div class="group-tit">
    					<span id="groupTit">燕大失物招领①群(165636732)</span> <a id="changeGroup" data-tag="changegroup">[切换QQ群]</a>
    				</div>
    			</dt>
    			<dd>
    				<div class="group-tools">
    					<div class="group-members" id="groupMemberTit">
    		群成员人数: <span id="groupMemberNum">995</span>/1000



    	</div>
    					<div class="group-search">
    						<div class="group-input">
    							<input type="text" id="searchValue" data-def="搜索关键词" value="搜索关键词">
    							<button id="searchBtn" data-tag="search" class="icon-search-btn"></button>
    						</div>
    						<div class="group-select-btn" data-tag="more">
    							<a data-tag="more">
    								<span data-tag="more">更多筛选</span>
    								<i data-tag="more" class="icon-arrow-blue"></i>
    							</a>
    						</div>
    					</div>
    					<div id="moreAction">
    						<div class="child group-select-more hide">
    							<div class="group-top">
    								<div></div>
    							</div>
    							<ul data-key="credit" data-tag="信用" data-type="0">
    								<li>
    									<label>信　　用：</label>
    								</li>
    								<li class="query-filter selected">不限</li>
    								<li class="query-filter">不良记录成员</li>
    							</ul>
    							<ul data-key="g" data-tag="性别" data-type="1">
    								<li>
    									<label>性　　别：</label>
    								</li>
    								<li class="query-filter selected">不限</li>
    								<li class="query-filter">男</li>
    								<li class="query-filter">女</li>
    							</ul>
    							<ul data-key="qage" data-tag="Q龄" data-type="2">
    								<li>
    									<label>Q　　龄：</label>
    								</li>
    								<li class="query-filter selected">不限</li>
    								<li class="query-filter">1年内</li>
    								<li class="query-filter">1年-3年</li>
    								<li class="query-filter">3年-5年</li>
    								<li class="query-filter">5-7年</li>
    								<li class="query-filter">7年以上</li>
    								<li class="query-filter sl" data-val="年"><input type="text" maxlength="2"> - <input type="text" maxlength="2"> 年</li>
    							</ul>
    							<ul data-key="join_time" data-tag="入群时长" data-type="3">
    								<li>
    									<label>入群时长：</label>
    								</li>
    								<li class="query-filter selected">不限</li>
    								<li class="query-filter">1个月内</li>
    								<li class="query-filter">1-3个月</li>
    								<li class="query-filter">3-6个月</li>
    								<li class="query-filter">6-12个月</li>
    								<li class="query-filter">12个月以上</li>
    								<li class="query-filter sl" data-val="月"><input type="text" maxlength="3"> - <input type="text" maxlength="3"> 月</li>
    							</ul>
    							<ul data-key="lv" id="groupLevel" class="hide" data-tag="群等级" data-type="5" style="display: block;">
    		<li>
    			<label>等　　级：</label>
    		</li>
    		<li class="query-filter selected" data-idx="0">不限</li>

    			<li class="query-filter " data-idx="1">潜水</li>

    			<li class="query-filter " data-idx="2">冒泡</li>

    			<li class="query-filter " data-idx="3">吐槽</li>

    			<li class="query-filter " data-idx="4">活跃</li>

    			<li class="query-filter " data-idx="5">话唠</li>

    			<li class="query-filter " data-idx="6">传说</li>

    			<li class="query-filter " data-idx="10">一见倾心</li>

    			<li class="query-filter " data-idx="11">超凡脱俗</li>

    			<li class="query-filter " data-idx="12">风华绝代</li>

    			<li class="query-filter " data-idx="13">崭露头角</li>

    			<li class="query-filter " data-idx="14">金玉满堂</li>

    			<li class="query-filter " data-idx="15">富甲一方</li>

    			<li class="query-filter " data-idx="101">LV.1</li>

    			<li class="query-filter " data-idx="102">LV.2</li>

    			<li class="query-filter " data-idx="103">LV.3</li>

    			<li class="query-filter " data-idx="104">LV.4</li>

    			<li class="query-filter " data-idx="105">LV.5</li>

    			<li class="query-filter " data-idx="106">LV.6</li>

    			<li class="query-filter " data-idx="107">LV.7</li>

    			<li class="query-filter " data-idx="108">LV.8</li>

    			<li class="query-filter " data-idx="109">LV.9</li>

    			<li class="query-filter " data-idx="110">LV.10</li>

    			<li class="query-filter " data-idx="111">LV.11</li>

    			<li class="query-filter " data-idx="112">LV.12</li>

    			<li class="query-filter " data-idx="113">LV.13</li>

    			<li class="query-filter " data-idx="114">LV.14</li>

    			<li class="query-filter " data-idx="115">LV.15</li>

    			<li class="query-filter " data-idx="116">LV.16</li>

    			<li class="query-filter " data-idx="117">LV.17</li>

    			<li class="query-filter " data-idx="118">LV.18</li>

    			<li class="query-filter " data-idx="197">小酋长</li>

    			<li class="query-filter " data-idx="198">大酋长</li>

    			<li class="query-filter " data-idx="199">首席酋长</li>

    	</ul>
    							<ul data-key="last_speak_time" data-tag="最后发言" data-type="4">
    								<li>
    									<label>最后发言：</label>
    								</li>
    								<li class="query-filter selected">不限</li>
    								<li class="query-filter">1个月内</li>
    								<li class="query-filter">1-3个月</li>
    								<li class="query-filter">3-6个月</li>
    								<li class="query-filter">6-12个月</li>
    								<li class="query-filter">12个月以上</li>
    								<li class="query-filter sl" data-val="月"><input type="text" maxlength="3"> - <input type="text" maxlength="3"> 月</li>
    							</ul>
    							<div class="group-select-more-btm" id="groupSelectMoreBtm">
    								<div>筛选条件:</div>
    								<div id="selectResultTips">
    								</div>
    								<div class="select-result">
    									<button class="clear disabled" disabled="disabled">清除</button>
    									<button class="submit" data-tag="moresub">确定</button>
    								</div>
    								<div class="clear"></div>
    							</div>
    						</div>
    						<div class="child group-select-result hide" id="groupSelectResult">

    						</div>
    					</div>

    				</div>

    				<div class="group-memeber">
    					<table cellspacing="0" cellpadding="0" border="0" width="100%" id="groupMember" align="center">
    						<tbody><tr id="groupTh">
    		<th width="32" class="td-right">

    		</th>
    		<th width="30"></th>
    		<th class="th-left1" width="200">成员</th>
    		<th class="th-left th-card" width="160">群名片</th>

    		<th class="th-left" width="100">QQ号</th>
    		<th class="th-left" width="90">性别</th>
    		<th class="th-left th-desc" width="90">
    			<div class="group-ff">
    				<div class="group-desc">
    					<a class="link">Q龄</a> <i class="arrow"></i> <i class="icon-more-select"></i>
    					<ul class="group-desc-arrow">
    						<li cmd="desc" data-tag="age" data-idx="0" idx="0">默认</li>
    						<li cmd="desc" data-tag="age" data-idx="0" idx="9" order="0"><a data-tag="age" data-idx="0">Q龄</a> <i class="icon-arrow-desc"></i></li>
    						<li cmd="desc" data-tag="age" data-idx="1" idx="8" order="1"><a data-tag="age" data-idx="1">Q龄</a> <i class="icon-arrow-desc1"></i></li>
    					</ul>
    				</div>
    			</div>
    		</th>
    		<th class="th-left th-desc" width="120">
    			<div class="group-ff">
    				<div class="group-desc">
    					<a class="link">入群时间</a> <i class="arrow"></i> <i class="icon-more-select"></i>
    					<ul class="group-desc-arrow">
    						<li cmd="desc" data-tag="jointime" data-idx="0" idx="0">默认</li>
    						<li cmd="desc" data-tag="jointime" data-idx="0" idx="11" order="0"><a data-tag="jointime" data-idx="0">入群时间</a> <i class="icon-arrow-desc"></i></li>
    						<li cmd="desc" data-tag="jointime" data-idx="1" idx="10" order="1"><a data-tag="jointime" data-idx="1">入群时间</a> <i class="icon-arrow-desc1"></i></li>
    					</ul>
    				</div>
    			</div>
    		</th>

    		<th class="th-left th-desc th-lv" width="120">
    			<div class="group-ff">
    				<div class="group-desc">
    					<a class="link">等级(积分)</a> <i class="arrow"></i> <i class="icon-more-select"></i>
    					<ul class="group-desc-arrow">
    						<li cmd="desc" data-tag="rank" data-idx="0" idx="0">默认</li>
    						<li cmd="desc" data-tag="rank" data-idx="0" idx="15" order="0"><a data-tag="orderlv" data-idx="0">等级(积分)</a> <i class="icon-arrow-desc"></i></li>
    						<li cmd="desc" data-tag="rank" data-idx="1" idx="14" order="1"><a data-tag="orderlv" data-idx="1">等级(积分)</a> <i class="icon-arrow-desc1"></i></li>
    					</ul>
    				</div>
    			</div>
    		</th>

    		<th class="th-left th-desc" width="110">
    			<div class="group-ff">
    				<div class="group-desc">
    					<a class="link">最后发言</a> <i class="arrow"></i> <i class="icon-more-select"></i>
    					<ul class="group-desc-arrow">
    						<li cmd="desc" data-tag="lastmsg" data-idx="0" idx="0">默认</li>
    						<li cmd="desc" data-tag="lastmsg" data-idx="0" idx="17" order="0"><a data-tag="orderspeak" data-idx="0">最后发言</a> <i class="icon-arrow-desc"></i></li>
    						<li cmd="desc" data-tag="lastmsg" data-idx="1" idx="16" order="1"><a data-tag="orderspeak" data-idx="1">最后发言</a> <i class="icon-arrow-desc1"></i></li>
    					</ul>
    				</div>
    			</div>
    		</th>
    		<th width="20"></th>
    	</tr>
    					</tbody>
    		<tbody class="list">

    		<tr class="mb mb895290134">
    			<td class="td-right">

    			</td>
    			<td class="td-no">1</td>
    			<td class="td-user-nick">

    					<a class="group-master-a"><i class="icon-group-master"></i></a>

    				<img class="" src="//q3.qlogo.cn/g?b=qq&amp;k=Fe163fFic3vlQvkkQDH4iaNg&amp;s=41&amp;t=1488769125" id="useIcon895290134">

    				<span>

    						矛与盾的争执

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							此号不做任何回
    						</span>


    			</td>

    			<td>

    						895290134

    			</td>
    			<td>

    				男

    			</td>
    			<td>8年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>冒泡(13)</td>

    			<td>

    					2017/04/12

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb869879123">
    			<td class="td-right">

    			</td>
    			<td class="td-no">2</td>
    			<td class="td-user-nick">

    					<a class="group-manage-a"><i class="icon-group-manage manage869879123"></i></a>

    				<img class="" src="//q4.qlogo.cn/g?b=qq&amp;k=y1gjjiblbT1iaUxpDDyBpfmA&amp;s=41&amp;t=1488621055" id="useIcon869879123">

    				<span>

    						拎着自己飞🌵

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							材料—无机—冯
    						</span>


    			</td>

    			<td>

    						869879123

    			</td>
    			<td>

    				未知

    			</td>
    			<td>9年</td>
    			<td>

    				2016/09/21

    			</td>

    			<td>活跃(72)</td>

    			<td>

    					2017/04/14

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb1447643340">
    			<td class="td-right">

    			</td>
    			<td class="td-no">3</td>
    			<td class="td-user-nick">

    					<a class="group-manage-a"><i class="icon-group-manage manage1447643340"></i></a>

    				<img class="" src="//q1.qlogo.cn/g?b=qq&amp;k=29qCWYFEiaNZaic764xlI4zQ&amp;s=41&amp;t=1488605566" id="useIcon1447643340">

    				<span>

    						二进制╮

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							生活服务部&nbsp;&nbsp;&nbsp;化
    						</span>


    			</td>

    			<td>

    						1447643340

    			</td>
    			<td>

    				女

    			</td>
    			<td>6年</td>
    			<td>

    				2016/09/06

    			</td>

    			<td>吐槽(24)</td>

    			<td>

    					2017/04/18

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb1360950914">
    			<td class="td-right">

    			</td>
    			<td class="td-no">4</td>
    			<td class="td-user-nick">

    					<a class="group-manage-a"><i class="icon-group-manage manage1360950914"></i></a>

    				<img class="" src="//q3.qlogo.cn/g?b=qq&amp;k=parU1fnKibYEy6G6ueyWD5A&amp;s=41&amp;t=1483627846" id="useIcon1360950914">

    				<span>

    						囧杨毅

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							16土木杨毅
    						</span>


    			</td>

    			<td>

    						1360950914

    			</td>
    			<td>

    				男

    			</td>
    			<td>7年</td>
    			<td>

    				2016/09/21

    			</td>

    			<td>吐槽(21)</td>

    			<td>

    					2017/04/18

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb1010735179">
    			<td class="td-right">

    			</td>
    			<td class="td-no">5</td>
    			<td class="td-user-nick">

    					<a class="group-manage-a"><i class="icon-group-manage manage1010735179"></i></a>

    				<img class="" src="//q4.qlogo.cn/g?b=qq&amp;k=ASUBpNfRe09tMQee0W96vg&amp;s=41&amp;t=1489847194" id="useIcon1010735179">

    				<span>

    						▎℡没鈊没肺ㄨ

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							生活服务部～机
    						</span>


    			</td>

    			<td>

    						1010735179

    			</td>
    			<td>

    				未知

    			</td>
    			<td>6年</td>
    			<td>

    				2016/09/12

    			</td>

    			<td>冒泡(17)</td>

    			<td>

    					2017/04/05

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb1437112548">
    			<td class="td-right">

    			</td>
    			<td class="td-no">6</td>
    			<td class="td-user-nick">

    					<a class="group-manage-a"><i class="icon-group-manage manage1437112548"></i></a>

    				<img class="" src="//q1.qlogo.cn/g?b=qq&amp;k=ZGX8FmI9K2UnP12cSiaIXrQ&amp;s=41&amp;t=1491567153" id="useIcon1437112548">

    				<span>

    						炸毛猫

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">

    						</span>


    			</td>

    			<td>

    						1437112548

    			</td>
    			<td>

    				女

    			</td>
    			<td>7年</td>
    			<td>

    				2016/09/21

    			</td>

    			<td>冒泡(17)</td>

    			<td>

    					2017/04/16

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb1757911483">
    			<td class="td-right">

    			</td>
    			<td class="td-no">7</td>
    			<td class="td-user-nick">

    					<a class="group-manage-a"><i class="icon-group-manage manage1757911483"></i></a>

    				<img class="" src="//q4.qlogo.cn/g?b=qq&amp;k=Vj36BWdeCRBibIrD8t1CxUQ&amp;s=41&amp;t=1490683498" id="useIcon1757911483">

    				<span>

    						这里会长出一朵花.🌿

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							16文法&nbsp;王莹
    						</span>


    			</td>

    			<td>

    						1757911483

    			</td>
    			<td>

    				女

    			</td>
    			<td>6年</td>
    			<td>

    				2016/09/03

    			</td>

    			<td>冒泡(14)</td>

    			<td>

    					2017/04/19

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb929461898">
    			<td class="td-right">

    			</td>
    			<td class="td-no">8</td>
    			<td class="td-user-nick">

    					<a class="group-manage-a"><i class="icon-group-manage manage929461898"></i></a>

    				<img class="" src="//q3.qlogo.cn/g?b=qq&amp;k=roCq0IcTt8fXNFK2MB6QicA&amp;s=41&amp;t=1489482448" id="useIcon929461898">

    				<span>

    						ζั͡&nbsp;&nbsp;&nbsp;&nbsp;๓

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">

    						</span>


    			</td>

    			<td>

    						929461898

    			</td>
    			<td>

    				女

    			</td>
    			<td>7年</td>
    			<td>

    				2016/09/14

    			</td>

    			<td>冒泡(13)</td>

    			<td>

    					2017/04/14

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb592366245">
    			<td class="td-right">

    			</td>
    			<td class="td-no">9</td>
    			<td class="td-user-nick">

    					<a class="group-manage-a"><i class="icon-group-manage manage592366245"></i></a>

    				<img class="" src="//q2.qlogo.cn/g?b=qq&amp;k=SnjOjeaBpxnnmBySTJ6Uww&amp;s=41&amp;t=1490688610" id="useIcon592366245">

    				<span>

    						你指尖闪烁的电光

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							生活服务部&nbsp;测
    						</span>


    			</td>

    			<td>

    						592366245

    			</td>
    			<td>

    				男

    			</td>
    			<td>10年</td>
    			<td>

    				2016/11/06

    			</td>

    			<td>冒泡(8)</td>

    			<td>

    					2017/04/18

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb497275782">
    			<td class="td-right">

    			</td>
    			<td class="td-no">10</td>
    			<td class="td-user-nick">

    					<a class="group-manage-a"><i class="icon-group-manage manage497275782"></i></a>

    				<img class="" src="//q3.qlogo.cn/g?b=qq&amp;k=4toMoyM1dDY5aniadXkwvvg&amp;s=41&amp;t=1483324283" id="useIcon497275782">

    				<span>

    						爆栗方圆

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							生活服务部-电
    						</span>


    			</td>

    			<td>

    						497275782

    			</td>
    			<td>

    				男

    			</td>
    			<td>10年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					2016/09/28

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb2902459153">
    			<td class="td-right">

    			</td>
    			<td class="td-no">11</td>
    			<td class="td-user-nick">

    					<a><i class="manage2902459153" data-id="2902459153"></i></a>

    				<img class="" src="//q2.qlogo.cn/g?b=qq&amp;k=mkmM7wniabwlKDeIdZq2UrQ&amp;s=41&amp;t=1489853929" id="useIcon2902459153">

    				<span>

    						大西瓜

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">

    						</span>


    			</td>

    			<td>

    						2902459153

    			</td>
    			<td>

    				男

    			</td>
    			<td>2年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					2016/07/05

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb591902795">
    			<td class="td-right">

    			</td>
    			<td class="td-no">12</td>
    			<td class="td-user-nick">

    					<a><i class="manage591902795" data-id="591902795"></i></a>

    				<img class="" src="//q4.qlogo.cn/g?b=qq&amp;k=H7dRCqZkOIhiaicdCbXDKbDA&amp;s=41&amp;t=1488618994" id="useIcon591902795">

    				<span>

    						🍄

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							14国贸王翊璇
    						</span>


    			</td>

    			<td>

    						591902795

    			</td>
    			<td>

    				未知

    			</td>
    			<td>10年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					-

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb913511565">
    			<td class="td-right">

    			</td>
    			<td class="td-no">13</td>
    			<td class="td-user-nick">

    					<a><i class="manage913511565" data-id="913511565"></i></a>

    				<img class="" src="//q2.qlogo.cn/g?b=qq&amp;k=SRH2kvvoMacXydnvVXfDAQ&amp;s=41&amp;t=1492592468" id="useIcon913511565">

    				<span>

    						懒惰啊！就是菜鸡的原罪

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							15化工王轶伦
    						</span>


    			</td>

    			<td>

    						913511565

    			</td>
    			<td>

    				男

    			</td>
    			<td>8年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					2016/09/19

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb1668380019">
    			<td class="td-right">

    			</td>
    			<td class="td-no">14</td>
    			<td class="td-user-nick">

    					<a><i class="manage1668380019" data-id="1668380019"></i></a>

    				<img class="" src="//q4.qlogo.cn/g?b=qq&amp;k=L0gHPibZgwe178rpjPibQNSA&amp;s=41&amp;t=1483296149" id="useIcon1668380019">

    				<span>

    						淡忘的记忆

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							孙学凯
    						</span>


    			</td>

    			<td>

    						1668380019

    			</td>
    			<td>

    				男

    			</td>
    			<td>3年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					-

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb724750170">
    			<td class="td-right">

    			</td>
    			<td class="td-no">15</td>
    			<td class="td-user-nick">

    					<a><i class="manage724750170" data-id="724750170"></i></a>

    				<img class="" src="//q3.qlogo.cn/g?b=qq&amp;k=y5FUZUwWyXT7dBaFicBW5UA&amp;s=41&amp;t=1492008556" id="useIcon724750170">

    				<span>

    						妄

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							环化张浩
    						</span>


    			</td>

    			<td>

    						724750170

    			</td>
    			<td>

    				男

    			</td>
    			<td>10年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					-

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb307810112">
    			<td class="td-right">

    			</td>
    			<td class="td-no">16</td>
    			<td class="td-user-nick">

    					<a><i class="manage307810112" data-id="307810112"></i></a>

    				<img class="" src="//q1.qlogo.cn/g?b=qq&amp;k=WRicDl3aSdiaJ5gXINFI1QIQ&amp;s=41&amp;t=1483307938" id="useIcon307810112">

    				<span>

    						恩。

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">

    						</span>


    			</td>

    			<td>

    						307810112

    			</td>
    			<td>

    				男

    			</td>
    			<td>13年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					-

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb1509920574">
    			<td class="td-right">

    			</td>
    			<td class="td-no">17</td>
    			<td class="td-user-nick">

    					<a><i class="manage1509920574" data-id="1509920574"></i></a>

    				<img class="" src="//q3.qlogo.cn/g?b=qq&amp;k=XS1XLtSibtFITru0wv6SNFA&amp;s=41&amp;t=1483282561" id="useIcon1509920574">

    				<span>

    						我非圣贤

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							机械-何贤盛
    						</span>


    			</td>

    			<td>

    						1509920574

    			</td>
    			<td>

    				男

    			</td>
    			<td>6年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					-

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb732269460">
    			<td class="td-right">

    			</td>
    			<td class="td-no">18</td>
    			<td class="td-user-nick">

    					<a><i class="manage732269460" data-id="732269460"></i></a>

    				<img class="" src="//q1.qlogo.cn/g?b=qq&amp;k=woH5u53TMNzTiaqTXibqPJWw&amp;s=41&amp;t=1492317900" id="useIcon732269460">

    				<span>

    						JoY～💋

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							文法—姚翡
    						</span>


    			</td>

    			<td>

    						732269460

    			</td>
    			<td>

    				女

    			</td>
    			<td>6年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					2015/10/13

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb909549255">
    			<td class="td-right">

    			</td>
    			<td class="td-no">19</td>
    			<td class="td-user-nick">

    					<a><i class="manage909549255" data-id="909549255"></i></a>

    				<img class="" src="//q4.qlogo.cn/g?b=qq&amp;k=A6k8MxQDI9golibianXnnsxA&amp;s=41&amp;t=1483360348" id="useIcon909549255">

    				<span>

    						吴振豪

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							14石油-吴振豪
    						</span>


    			</td>

    			<td>

    						909549255

    			</td>
    			<td>

    				男

    			</td>
    			<td>7年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					2015/10/14

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb1045949889">
    			<td class="td-right">

    			</td>
    			<td class="td-no">20</td>
    			<td class="td-user-nick">

    					<a><i class="manage1045949889" data-id="1045949889"></i></a>

    				<img class="" src="//q2.qlogo.cn/g?b=qq&amp;k=ZWB1gGgGmvaPyQbXtsXtTw&amp;s=41&amp;t=1483372307" id="useIcon1045949889">

    				<span>

    						滇山之子

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">

    						</span>


    			</td>

    			<td>

    						1045949889

    			</td>
    			<td>

    				男

    			</td>
    			<td>6年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					-

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		<tr class="mb mb1076566519">
    			<td class="td-right">

    			</td>
    			<td class="td-no">21</td>
    			<td class="td-user-nick">

    					<a><i class="manage1076566519" data-id="1076566519"></i></a>

    				<img class="icon-deficon" src="//qun.qq.com/css/imgs/space.gif" id="useIcon1076566519">

    				<span>

    						保护我方安琪拉

    				</span>
    			</td>
    			<td class="td-card">

    						<span class="white">
    							公寓机自朱佳琳
    						</span>


    			</td>

    			<td>

    						1076566519

    			</td>
    			<td>

    				未知

    			</td>
    			<td>7年</td>
    			<td>

    				2015/10/13

    			</td>

    			<td>潜水(0)</td>

    			<td>

    					-

    			</td>
    			<td class="td-delete">

    			</td>
    		</tr>

    		</tbody>
    	</table>
    					<div id="searchEmpty" style="display: none;"></div>
    				</div>

    			</dd>
    		</dl>
    	</div>

    		<div class="footer">
    		<p>友情链接：<a href="http://im.qq.com/" target="_blank">QQ官方网站</a> | <a href="http://open.qq.com/" target="_blank">腾讯开放平台</a> | <a href="http://qun.qq.com/qunlearn/qunlearn.html" target="_blank">在线教育介绍</a> | <a href="http://shang.qq.com" target="_blank">QQ商家</a> | <a href="http://vip.qq.com/" target="_blank">QQ会员</a></p>
    	    <p>Copyright © 1998-2015 Tencent. All Rights Reserved.</p>
    	    <p>腾讯公司 版权所有</p>
    	</div>
    	<script type="text/javascript">
    	    function loadJs(){
    	        var href = location.href;
    	        var dom = document.createElement('script');
    	        if(href.indexOf('https://') >= 0){
    	            dom.src = 'https://pingjs.qq.com/tcss.ping.https.js';
    	        }else{
    	            dom.src = 'http://pingjs.qq.com/tcss.ping.js';
    	        }
    	        document.body.appendChild(dom);
    	    }
    	    loadJs();
    	</script><script src="http://pingjs.qq.com/tcss.ping.js"></script>


    	<script type="text/template" id="newGroupMemberTmp">
    		<%
    			for(var i in list){
    				var item = list[i];
    		%>
    			<li>
    				<a>
    					<span><img src="<%=avater(item.uin)%>" /><%=item.name%>(<%=html(item.uin)%>)</span>
    					<div class="i-link" data-id="<%=attr(item.uin)%>"><p><i class="icon-close"></i></p></div>
    				</a>
    			</li>
    		<%}%>
    	</script>

    	<script type="text/template" id="friendsmartTmp">
    		<ul>
    		<%
    		for(var i=0,l=list.length;i<l;i++){
    			var item = list[i];
    		%>
    			<li title=<%=attr(item.name)%> data-id="<%=attr(item.uin)%>">
    				<a><img src="<%=avater(item.uin)%>" /><%=item.oname%>(<%=item.ouin%>)</a>
    			</li>
    		<%}%>
    		</ul>
    	</script>

    	<script type="text/template" id="myFriendTmp">
    		<div class="member-body">
    			<div class="input-tit">
    				<div class="input-search">
    					<input type="text" class="dialog-search-input" value="搜索关键词" data-def="搜索关键词" />
    					<button class="group-search-btn icon-search-btn"></button>
    				</div>
    				<div class="search-smart">
    				</div>
    			</div>
    			<div class="my-friend">
    				<ul class="my-friend-list" id="myFriendList">
    					<%
    						for(var i in list){
    							var item = list[i];
    					%>
    						<li class="friend-group">
    							<a class="friend-group-name" data-child="<%if(item.mems){%>1<%}else{%>0<%}%>"><i <%if(item.mems){%>class="icon-arrow-left"<%}%>></i> <span><%if(item.gname){%><%=item.gname%><%}else{%>我的好友<%}%></span> <i data-idx="<%=i%>" class="icon-friend-join"></i></a>
    							<%if(item.mems){%>
    								<ul class="friend-group-list">
    									<%
    										for(var m=0,n=item.mems.length;m<n;m++){
    											var obj = item.mems[m];
    									%>
    									<li>
    										<a class="friend" data-id="<%=attr(obj.uin)%>"><img src="<%=avater(obj.uin)%>" /><%=obj.name%>(<%=obj.uin%>)</a>
    									</li>
    									<%}%>
    								</ul>
    							<%}%>
    						</li>
    					<%}%>
    				</ul>
    				<div class="icon-arrow-join"></div>
    				<ul class="selected-friend" id="newGroupMemberList">

    				</ul>
    			</div>
    		</div>
    	</script>

    	<script type="text/template" id="searchResultTmp">
    		<div class="clear"></div>
    		<%if(!$.isEmptyObject(tips)){%>
    		<div>筛选条件:</div>
    		<div class="result-zone" id="groupSelectResultTips">
    			<%
    				for(var i in tips){
    					var item = tips[i];
    			%>
    			<a class="select-result select-result<%=attr(item.type)%>"><span><%=html(item.tag)%>： <%=html(item.value)%></span> <i class="icon-close" data-key="<%=attr(item.key)%>"></i></a>
    			<%}%>
    		</div>
    		<div class="select-result" id="searchResult">
    			<%if(key!=''){%>搜索条件：<span><%=html(key)%></span><%}%>   共<span>  <%=html(num)%> </span> 人符合条件，<a class="reset-search">清空条件</a>
    		</div>
    		<%}else{%>
    			共搜索出含“<span><%=html(key)%></span>”的群成员：<span> <%=html(num)%> 人</span>　
    			<a class="reset-search">返回全员列表</a>
    		<%}%>
    		<div class="clear"></div>
    	</script>

    	<script type="text/template" id="tagMenuTmp">
    		<div class="mark-div">
    			<div class="mark-select">
    				<div class="mark-select-tit">
    					<span><%if(tag>=0 && list[tag]){%><%=list[tag]%><%}%></span>
    					<i class="icon-arrow-gray"></i>
    				</div>

    				<ul>
    					<%
    						for(var i in list){
    					%>
    						<li><a data-tag="changetag" data-idx="<%=attr(i)%>"><%=list[i]%></a></li>
    					<%}%>
    					<li><a data-tag="changetag" data-idx="-1">&nbsp;</a></li>
    				</ul>
    				<div class="mark-select-add">
    					<a><i class="icon-add-mark"></i>添加</a>
    				</div>
    			</div>
    		</div>
    	</script>

    	<script type="text/template" id="searchResultTipTmp">
    		<a class="select-result <%if(type){%>select-result<%=attr(type)%><%}%> <%if(key){%>select-result<%=attr(key)%><%}%>"><span><%=html(tag)%>： <%=html(value)%></span> <i class="icon-close" data-type="<%=attr(type)%>" data-key="<%=attr(key)%>"></i></a>
    	</script>

    	<script type="text/template" id="groupMemberThTmp">
    		<th width="32" class="td-right">
    			<%if(show){%>
    				<input id="selectAll" type="checkbox" class="check-input" />
    			<%}%>
    		</th>
    		<th width="30"></th>
    		<th class="th-left1" width="<%=w.member%>">成员</th>
    		<th class="th-left th-card" width="<%=w.card%>">群名片</th>
    		<%if(tag){%>
    		<th class="th-left th-mark" width="110">标签</th>
    		<%}%>
    		<th class="th-left" width="<%=w.qq%>">QQ号</th>
    		<th class="th-left" width="<%=w.sex%>">性别</th>
    		<th class="th-left th-desc" width="<%=w.qage%>">
    			<div class="group-ff">
    				<div class="group-desc">
    					<a class="link">Q龄</a> <i class="arrow"></i> <i class="icon-more-select"></i>
    					<ul class="group-desc-arrow">
    						<li cmd="desc" data-tag="age" data-idx="0" idx="0">默认</li>
    						<li cmd="desc" data-tag="age" data-idx="0" idx="9" order="0"><a data-tag="age" data-idx="0">Q龄</a> <i class="icon-arrow-desc"></i></li>
    						<li cmd="desc" data-tag="age" data-idx="1" idx="8" order="1"><a data-tag="age" data-idx="1">Q龄</a> <i class="icon-arrow-desc1"></i></li>
    					</ul>
    				</div>
    			</div>
    		</th>
    		<th class="th-left th-desc" width="<%=w.join%>">
    			<div class="group-ff">
    				<div class="group-desc">
    					<a class="link">入群时间</a> <i class="arrow"></i> <i class="icon-more-select"></i>
    					<ul class="group-desc-arrow">
    						<li cmd="desc" data-tag="jointime" data-idx="0" idx="0">默认</li>
    						<li cmd="desc" data-tag="jointime" data-idx="0" idx="11" order="0"><a data-tag="jointime" data-idx="0">入群时间</a> <i class="icon-arrow-desc"></i></li>
    						<li cmd="desc" data-tag="jointime" data-idx="1" idx="10" order="1"><a data-tag="jointime" data-idx="1">入群时间</a> <i class="icon-arrow-desc1"></i></li>
    					</ul>
    				</div>
    			</div>
    		</th>
    		<%if(lv){%>
    		<th class="th-left th-desc th-lv" width="<%=w.lv%>">
    			<div class="group-ff">
    				<div class="group-desc">
    					<a class="link">等级(积分)</a> <i class="arrow"></i> <i class="icon-more-select"></i>
    					<ul class="group-desc-arrow">
    						<li cmd="desc" data-tag="rank" data-idx="0" idx="0">默认</li>
    						<li cmd="desc" data-tag="rank" data-idx="0" idx="15" order="0"><a data-tag="orderlv" data-idx="0">等级(积分)</a> <i class="icon-arrow-desc"></i></li>
    						<li cmd="desc" data-tag="rank" data-idx="1" idx="14" order="1"><a data-tag="orderlv" data-idx="1">等级(积分)</a> <i class="icon-arrow-desc1"></i></li>
    					</ul>
    				</div>
    			</div>
    		</th>
    		<%}%>
    		<th class="th-left th-desc" width="110">
    			<div class="group-ff">
    				<div class="group-desc">
    					<a class="link">最后发言</a> <i class="arrow"></i> <i class="icon-more-select"></i>
    					<ul class="group-desc-arrow">
    						<li cmd="desc" data-tag="lastmsg" data-idx="0"  idx="0">默认</li>
    						<li cmd="desc" data-tag="lastmsg" data-idx="0"  idx="17" order="0"><a data-tag="orderspeak" data-idx="0" >最后发言</a> <i class="icon-arrow-desc"></i></li>
    						<li cmd="desc" data-tag="lastmsg" data-idx="1"  idx="16" order="1"><a  data-tag="orderspeak" data-idx="1" >最后发言</a> <i class="icon-arrow-desc1"></i></li>
    					</ul>
    				</div>
    			</div>
    		</th>
    		<th width="20"></th>
    	</script>

    	<script type="text/template" id="groupMemberEmptyTmp">
    		<div class="empty">没有符合筛选条件的群成员</div>
    	</script>

    	<script type="text/template" id="groupMemberTmp">
    		<tbody class="list">
    		<%
    			for(var i =0,l=list.length;i<l;i++){
    				var item = list[i];
    				st++
    		%>
    		<tr class="mb mb<%=item.uin%>">
    			<td class="td-right">
    				<%if(type == 'create'){%>
    					<%if(item.role != 0){%>
    					<input id="input<%=attr(item.uin)%>" type="checkbox" class="check-input" value="<%=attr(item.uin)%>" data-type="<%=item.role%>" />
    					<%}%>
    				<%}else if(type=='manage'){%>
    					<%if(item.role == 2){%>
    						<input  id="input<%=attr(item.uin)%>" type="checkbox" class="check-input" value="<%=attr(item.uin)%>" data-type="<%=item.role%>" />
    					<%}%>
    				<%}%>
    			</td>
    			<td class="td-no"><%=html(st)%></td>
    			<td class="td-user-nick">
    				<%if(item.role==0){%>
    					<a class="group-master-a"><i class="icon-group-master"></i></a>
    				<%}else if(item.role==1){%>
    					<a class="group-manage-a"><i class="icon-group-manage manage<%=item.uin%>" <%if(type == 'create'){%>title="取消管理员" data-tag="delmanage" data-id="<%=item.uin%>"<%}%>></i></a>
    				<%}else{%>
    					<a><i class="manage<%=item.uin%>" data-id="<%=item.uin%>"></i></a>
    				<%}%>
    				<img class="icon-deficon" src="//qun.qq.com/css/imgs/space.gif" id="useIcon<%=item.uin%>" />
    				<%if(item.flag & 0x1){%>
    					<a class="flag" <%if(ie6){%>href="javascript:void(0);"<%}%> hidefocus="true" title="不良记录成员"><i class="icon-member-flag"></i></a>
    				<%}%>
    				<span>
    					<%
    						if(item.match && item.match.type & 0x2){
    					%>
    						<%=show(item.match.word,html(item.nick))%>
    					<%}else{%>
    						<%=html(item.nick)%>
    					<%}%>
    				</span>
    			</td>
    			<td class="td-card">
    					<%
    						if((type!='join' && !(item.flag&0x2)) || item.uin == my){
    					%>
    					<span>
    						<span class="group-card group-card<%=item.uin%>">
    							<%if(item.match && item.match.type & 0x1){%>
    								<%=show(item.match.word,html(item.card))%>
    							<%}else{%>
    								<%=html(item.card)%>
    							<%}%>
    						</span>
    						<input class="member-card" id="member-card<%=item.uin%>" value="<%if(item.card){%><%=item.card%><%}%>" type="text" data-old="<%if(item.card){%><%=item.card%><%}%>" data-id="<%=item.uin%>" <%if(item.match && item.match.type==1){%>data-key="<%=item.match.word%>"<%}%> />
    					</span>
    					<%}else{%>
    						<span class="white">
    							<%if(item.card){%><%=html(item.card)%><%}%>
    						</span>
    					<%}%>

    			</td>
    			<%if(tag){%>
    			<td class="td-mark"  data-tags="<%=attr(item.tags)%>" data-id="<%=item.uin%>">
    				<%if(type != 'join' || item.uin == my){%>
    				<div class="td-mark-old" data-type="<%=item.tags%>">
    					<span>
    						<%if(tag && item.tags>=0){%><%=tag[item.tags]%><%}else{%>　<%}%>
    					</span>
    					<i class="icon-arrow-gray"></i>
    				</div>
    				<%}else{%>
    					<%if(tag && item.tags>=0){%><%=tag[item.tags]%><%}%>
    				<%}%>
    			</td>
    			<%}%>
    			<td>
    					<%if(item.match && item.match.type&0x4){%>
    						<%=show(item.match.word,item.uin)%>
    					<%}else{%>
    						<%=item.uin%>
    					<%}%>
    			</td>
    			<td>
    				<%if(item.g === 1){%>
    				女
    				<%}else if(item.g === 0){%>
    				男
    				<%}else{%>
    				未知
    				<%}%>
    			</td>
    			<td><%if(typeof item.qage != 'undefined'){%><%=item.qage%>年<%}%></td>
    			<td>
    				<%if(item.join_time){%>
    				<%=time(item.join_time)%>
    				<%}else{%>
    					2012年5月以前
    				<%}%>
    			</td>
    			<%if(lv){%>
    			<td><%if(lv){%><%=lv[item.lv.level]%>(<%=item.lv.point%>)<%}%></td>
    			<%}%>
    			<td>
    				<%if(item.last_speak_time){%>
    					<%=time(item.last_speak_time)%>
    				<%}else{%>
    					-
    				<%}%>
    			</td>
    			<td class="td-delete">
    				<%if(type == 'create'){%>
    					<%if(item.role != 0){%>
    					<i class="icon-close" title="删除该成员" data-tag="delmemberico" data-id="<%=attr(item.uin)%>"></i>
    					<%}%>
    				<%}else if(type=='manage'){%>
    					<%if(item.role == 2){%>
    						<i class="icon-close" title="删除该成员" data-tag="delmemberico" data-id="<%=attr(item.uin)%>"></i>
    					<%}%>
    				<%}%>
    			</td>
    		</tr>
    		<%}%>
    		</tbody>
    	</script>

    	<script type="text/template" id="groupMemberTitTmp">
    		群成员人数: <span id="groupMemberNum"><%=html(num)%></span>/<%=html(all)%>
    		<%if(type == 'create' || type == 'manage'){%>
    		<button cmd="add" class="add-member" data-tag="addmember">添加成员</button>
    		<%}%>
    		<%if(type == 'create'){%>
    		<button cmd="set" disabled class="set-manage disabled" data-tag="setmanage">设置管理员</button>
    		<%}%>
    		<%if(type == 'create' || type == 'manage'){%>
    		<button cmd="del" disabled class="disabled del-member" data-tag="delmemberbtn">删除成员</button>
    		<%}%>
    	</script>

    	<script type="text/template" id="groupLevelTmp">
    		<li>
    			<label>等　　级：</label>
    		</li>
    		<li class="query-filter <%if(!filter.lv){%>selected<%}%>" data-idx="0">不限</li>
    		<%
    			for(var i in list){
    		%>
    			<li class="query-filter <%if(filter.lv && filter.lv == i){%>selected<%}%>" data-idx="<%=attr(i)%>"><%=list[i]%></li>
    		<%}%>
    	</script>

    	<script type="text/template" id="smartTmp">
    		<ul>
    		<%
    		for(var i=0,l=list.length;i<l;i++){
    			var item = list[i];
    		%>
    			<li title="<%=item.gn%>" data-tag="clicksearch" data-id="<%=attr(item.gc)%>">
    				<a data-tag="clicksearch"><img data-tag="clicksearch" class="icon-def-gicon gicon<%=attr(item.gc)%>" <%if(item.face){%>src="<%=item.face%>"<%}%> />
    				<%=item.ogn%>(<%=item.ogc%>)</a>
    			</li>
    		<%}%>
    		</ul>
    	</script>

    	<script type="text/template" id="myGroupTmp">
    	<div class="member-body">
    		<%if(data.nums){%>
    		<div class="input-tit">
    			<div class="input-search">
    				<input type="text" class="dialog-search-input" value="搜索群名称或群号" data-def="搜索群名称或群号" />
    				<button class="group-search-btn icon-search-btn"></button>
    			</div>
    			<div class="search-smart">
    			</div>
    		</div>
    		<div class="my-all-group">

    			<%if(data.create && data.create.length){%>
    			<h4>我创建的群(<%=data.create.length%>)</h4>
    			<ul class="my-group-list">
    				<%
    					for(var i = 0,l=data.create.length;i<l;i++){
    						var item = data.create[i];
    				%>
    				<li title=<%=attr(item.gn)%> data-id="<%=attr(item.gc)%>">
    					<img class="icon-def-gicon gicon<%=attr(item.gc)%>" <%if(item.face){%>src="<%=item.face%>"<%}%> />
    					<%=item.gn%>
    				</li>
    				<%}%>
    			</ul>
    			<%}%>

    			<%if(data.manage && data.manage.length){%>
    			<h4 class="top">我管理的群(<%=data.manage.length%>)</h4>
    			<ul class="my-group-list">
    				<%
    					for(var i = 0,l=data.manage.length;i<l;i++){
    						var item = data.manage[i];
    				%>
    				<li title=<%=attr(item.gn)%> data-id="<%=attr(item.gc)%>">
    					<img  class="icon-def-gicon gicon<%=attr(item.gc)%>"  <%if(item.face){%>src="<%=item.face%>"<%}%> />
    					<%=item.gn%>
    				</li>
    				<%}%>
    			</ul>
    			<%}%>

    			<%if(data.join && data.join.length){%>
    			<h4 class="top">我加入的群(<%=data.join.length%>)</h4>
    			<ul class="my-group-list">
    				<%
    					for(var i = 0,l=data.join.length;i<l;i++){
    						var item = data.join[i];
    				%>
    				<li title=<%=attr(item.gn)%> data-id="<%=attr(item.gc)%>">
    					<img class="icon-def-gicon gicon<%=attr(item.gc)%>"  <%if(item.face){%>src="<%=item.face%>"<%}%> />
    					<%=item.gn%>
    				</li>
    				<%}%>
    			</ul>
    			<%}%>
    			</div>
    		<%}else{%>
    			<div class="my-all-group">
    			<div class="tips"><i class="icon-dialog-alert"></i>您当前没有加入任何群，现在就去<a href="//id.qq.com/index.html#qun-create" target="_blank">创建群</a>吧！</div>
    			</div>
    		<%}%>

    	</div>
    	</script>

    	<script type="text/template" id="oneTipsTmp">
    		<li class="tags-li"><a><input type="text" value="<%=name%>" /> <i class="icon-close" data-name="<%=name%>"></i></a></li>
    	</script>

    	<script type="text/template" id="addTipsTmp">
    		<div class="member-body">
    			<div class="input-tit">
    				<div class="input-search">
    					<input type="text" class="group-tips-txt" />
    				</div>
    				<div class="input-btn">
    					<input type="button" value="添加" />
    				</div>
    			</div>
    			<div style="clear:both;height:200px;">
    				<div class="dialog-tips">
    					<i class="icon-dialog-tips"></i><span>标签名称长度不超过8个汉字</span>
    				</div>
    				<ul class="member-label-list" id="memberLabelList">
    					<%
    						for(var i in list){
    							var item = list[i];
    					%>
    						<li class="tags-li"><a <%if(ie6){%>href="javascript:void(0);"<%}%>><input class="tags-input"  data-id="<%=i%>" type="text" value="<%=item%>" /> <i class="icon-close" data-id="<%=i%>"></i></a></li>
    					<%}%>
    				</ul>
    				<div class="dialog-tips">
    					<i class="icon-dialog-tips"></i><span>标签个数不超过20个</span></div>
    				<div class="clear"></div>
    			</div>
    		</div>
    	</script>

    	<script>
    		var BJ_REPORT = (function(global) {
    		    if (global.BJ_REPORT) return global.BJ_REPORT;

    		    var _error = [];
    		    var orgError = global.onerror;
    		    global.onerror = function(msg, url, line, col, error) {
    		    };

    		    var _config = {
    		        id: 0,
    		        uin: 0,
    		        url: "",
    		        combo: 1,
    		        ext: {},
    		        level: 4, // 1-debug 2-info 4-error 8-fail
    		        ignore: [],
    		        random: 1,
    		        delay: 1000,
    		        submit: null
    		    };

    		    var _isOBJByType = function(o, type) {
    		        return Object.prototype.toString.call(o) === "[object " + (type || "Object") + "]";
    		    };

    		    var _isOBJ = function(obj) {
    		        var type = typeof obj;
    		        return type === 'object' && !!obj;
    		    };


    		    var _processError = function(errObj) {
    		        try {
    		            if (errObj.stack) {
    		                var url = errObj.stack.match('//[^\n]+');
    		                url = url ? url[0] : "";
    		                var rowCols = url.match(':([0-9]+):([0-9]+)');
    		                if (!rowCols) {
    		                    rowCols = [0, 0, 0];
    		                }

    		                var stack = _processStackMsg(errObj);
    		                return {
    		                    msg: stack,
    		                    rowNum: rowCols[1],
    		                    colNum: rowCols[2],
    		                    target: url.replace(rowCols[0], '')
    		                        /* stack : stack*/
    		                };
    		            } else {
    		                return errObj;
    		            }
    		        } catch (err) {
    		            return errObj;
    		        }
    		    };

    		    var _processStackMsg = function(error) {
    		        var stack = error.stack.replace(/\n/gi, '').split(/\bat\b/).slice(0, 5).join("@").replace(/\?[^:]+/gi, "");
    		        var msg = error.toString();
    		        if (stack.indexOf(msg) < 0) {
    		            stack = msg + "@" + stack;
    		        }
    		        return stack;
    		    };

    		    var _error_tostring = function(error, index) {
    		        var param = [];
    		        var params = [];
    		        var stringify = [];
    		        if (_isOBJ(error)) {
    		            error.level = error.level || _config.level;
    		            for (var key in error) {
    		                var value = error[key] || "";
    		                if (value) {
    		                    if (_isOBJ(value)) {
    		                        try {
    		                            value = JSON.stringify(value);
    		                        } catch (err) {
    		                            value = "[BJ_REPORT detect value stringify error] " + err.toString();
    		                        }
    		                    }
    		                    stringify.push(key + ":" + value);
    		                    param.push(key + "=" + encodeURIComponent(value));
    		                    params.push(key + "[" + index + "]=" + encodeURIComponent(value));
    		                }
    		            }
    		        }

    		        // msg[0]=msg&target[0]=target -- combo report
    		        // msg:msg,target:target -- ignore
    		        // msg=msg&target=target -- report with out combo
    		        return [params.join("&"), stringify.join(","), param.join("&")];
    		    };

    		    var _imgs = [];
    		    var _submit = function(url) {
    		        if (_config.submit) {
    		            _config.submit(url);
    		        } else {
    		            var _img = new Image();
    		            _imgs.push(_img);
    		            _img.src = url;
    		        }
    		    };

    		    var error_list = [];
    		    var comboTimeout = 0;
    		    var _send = function(isReoprtNow) {
    		        if (!_config.report) return;

    		        while (_error.length) {
    		            var isIgnore = false;
    		            var error = _error.shift();
    		            var error_str = _error_tostring(error, error_list.length);
    		            for (var i = 0, l = _config.ignore.length; i < l; i++) {
    		                var rule = _config.ignore[i];
    		                if ((_isOBJByType(rule, "RegExp") && rule.test(error_str[1])) ||
    		                    (_isOBJByType(rule, "Function") && rule(error, error_str[1]))) {
    		                    isIgnore = true;
    		                    break;
    		                }
    		            }
    		            if (!isIgnore) {
    		                if (_config.combo) {
    		                    error_list.push(error_str[0]);
    		                } else {
    		                    _submit(_config.report + error_str[2] + "&_t=" + (+new Date));
    		                }
    		                _config.onReport && (_config.onReport(_config.id, error));
    		            }
    		        }

    		        // 合并上报
    		        var count = error_list.length;
    		        if (count) {
    		            var comboReport = function() {
    		                clearTimeout(comboTimeout);
    		                _submit(_config.report + error_list.join("&") + "&count=" + count + "&_t=" + (+new Date));
    		                comboTimeout = 0;
    		                error_list = [];
    		            };

    		            if (isReoprtNow) {
    		                comboReport(); // 立即上报
    		            } else if (!comboTimeout) {
    		                comboTimeout = setTimeout(comboReport, _config.delay); // 延迟上报
    		            }
    		        }
    		    };

    		    var report = {
    		        push: function(msg) { // 将错误推到缓存池
    		            if (Math.random() >= _config.random) {
    		                return report;
    		            }
    		            _error.push(_isOBJ(msg) ? _processError(msg) : {
    		                msg: msg
    		            });
    		            _send();
    		            return report;
    		        },
    		        info : function(msg){
    			    	if(Math.random()*100>2){
    			    		return;
    			    	}

    		            if (!msg) {
    		                return report;
    		            }
    		            if (_isOBJ(msg)) {
    		                msg.level = 2;
    		            } else {
    		                msg = {
    		                    msg: msg,
    		                    level: 2
    		                };
    		            }
    		            report.push(msg);
    		            return report;
    		        },
    		        init: function(config) { // 初始化
    		            if (_isOBJ(config)) {
    		                for (var key in config) {
    		                    _config[key] = config[key];
    		                }
    		            }
    		            // 没有设置id将不上报
    		            var id = parseInt(_config.id, 10);
    		            if (id) {
    		                _config.report = (_config.url || "//badjs2.qq.com/badjs") + "?id=" + id + "&uin=" + parseInt(_config.uin || (document.cookie.match(/\buin=\D+(\d+)/) || [])[1], 10) + "&from=" + encodeURIComponent(location.href) + "&ext=" + JSON.stringify(_config.ext) + "&";
    		            }
    		            return report;
    		        },

    		        __onerror__: global.onerror


    		    };

    		    return report;
    		}(window));

    		BJ_REPORT.init({
    		    id: 85
    		});
    	</script>

    	<script charset="utf-8" src="//s.url.cn/pub/js/qreport.js?_bid=2231"></script>

    	<script src="//s1.url.cn/qqun/qun/js/lib/jquery-9519b.js"></script>

    	<script src="//s1.url.cn/qqun/qun/js/lib/jquery.base-fe8ad.js"></script>

    	<script src="//s1.url.cn/qqun/qun/js/public/base_member-0ca65.js"></script><div class="ui-overlay"></div>
    	<script src="//s1.url.cn/qqun/qun/js/member-12177.js"></script>



    </body></html>

    Process finished with exit code 0


        """
    chromedriver = "D:\CCApplication\Mozilla Firefox\firefox.exe"
    driver = webdriver.Firefox()
    # chromedriver = "D:\CCApplication\phantomjs-2.1.1-windows\bin\phantomjs.exe"
    # driver = webdriver.PhantomJS()
    driver.get("http://qun.qq.com/member.html#gid=165636732")

    IframeElement=driver.find_element_by_name("login_frame")
    driver.switch_to_frame(IframeElement)

    driver.find_element_by_xpath("//*[@id='bottom_qlogin']/a[1]").click()  # 登录界面
    driver.find_element_by_xpath("//*[@id='u']").send_keys("741494582")
    driver.find_element_by_xpath("//*[@id='p']").send_keys("")  #输入你的密码

    driver.find_element_by_xpath("//*[@id='login_button']").click()  #点击登录
    time.sleep(2)


    driver.switch_to_default_content()  #防止出现TypeError: can't access dead object 错误特别重要
    time.sleep(2)
    web_data = driver.page_source
    selector = etree.HTML(web_data)
    people_num=selector.xpath("//*[@id='groupMemberNum']/text()")               #获取群组人数量
    people_num=int(people_num[0])

    count = 1
    for _ in range(int(people_num/20)):
        js = "var q=document.documentElement.scrollTop=500000"
        driver.execute_script(js)
        time.sleep(random.randint(2, 6))
        print(count)
        count+=1




    web_data = driver.page_source                                              #重新获取网页源代码
    selector = etree.HTML(web_data)


    people_nicks=selector.xpath("//tbody[@class='list']/tr/td[3]/span/text()")   #获取昵称
    people_nicks=get_freshList(people_nicks)

    people_QQs=selector.xpath("//tbody[@class='list']/tr/td[5]/text()")         #获取qq号
    people_QQs=get_freshList(people_QQs)

    people_sexs=selector.xpath("//tbody[@class='list']/tr/td[6]/text()")       #获取性别
    people_sexs=get_freshList(people_sexs)

    people_ages=selector.xpath("//tbody[@class='list']/tr/td[7]/text()")      #获取Q龄
    people_ages=get_freshList(people_ages)

    people_grades=selector.xpath("//tbody[@class='list']/tr/td[9]/text()")   #获取活跃度
    people_grades=get_freshList(people_grades)

    print(people_sexs,people_ages,people_grades,len(people_ages))

    driver.quit()










