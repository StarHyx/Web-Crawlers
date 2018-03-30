## 用Python写的几个简单的爬虫

### WikipediaCrawler

运行后从`start_url`指定的维基百科词条爬取，不断点击第一个链接，直到到达`target_url`指定的维基百科词条为止
可以用来分析某两个词条之间的关系

***

### DoubanCrawler

选取想了解的电影电影类型 —— `category_list`
运行后获得一个包含这些类型、所有地区，评分超过9分的完整电影对象的列表—— `movies.csv`
程序还可以统计所选取的每个电影类别中，数量排名前三的地区，输出到输出文件 `output.txt`