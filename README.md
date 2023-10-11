配置要求：python3 chrome浏览器 对应的chrome脚本

首先，下载chrome，然后 设置，关于 chrome 查看 chrome 版本 ，然后在 http://npm.taobao.org/mirrors/chromedriver/ 网站里面找到对应chrome版本的chrome driver，然后在项目配置中 main.py service = Service("chrome driver path")  在 chrome driver path 里面输入你自己的chrome driver路径，同时main.py里面的path是输出csv路径的path，默认是相对路径下的ranking.csv

应用到的python库：selenium request lxml

运行时可能会在option2.click() 这个地方报错，是小概率事件，是由于未加载完导致的，重新运行一下就可以了。

原理:调用 selenium 自动化框架自动测试，首先点击使用cookie，以获取最大的显示窗口，然后点击排名指标，然后下拉到显示一排显示多少的框，调到all，然后获取当前界面的html源代码，然后解析所有学校的QS描述网址，然后依次访问学校的网址进行爬取数据。

爬取的网址再QS_ranking.py下的第15行，如果出了新版本的QS排名的话只要不更改网页框架还是可以用的

爬取出来的数据最终汇总到目录下的ranking.csv文件中，一共有以下几个列

'Ranking','University Name','Country','Source','Private/Public university','Focus','No of students'
                 ,'Academic Reputation','Employer Reputation','Faculty Student Ratio','Citations Per Faculty'
                 ,'International Faculty Radio','International Students Radio'

其中获取学校创建时间和网站是基于维基百科的，有很多学校都获取不到（用QS上面的学校名称查询维基百科找不到），所以如果不想要的话可以关闭,只需要注释掉QS_ranking中第124行和第125行就可以了

作者：laris

QQ：1292199899
