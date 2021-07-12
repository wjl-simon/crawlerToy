# crawlerToy
a toy crawler for the binance k line data


## TIPS：powershell/cmd下开启ss （for Windows）
众所周知binanace数据（包括websocket）需要高科技获取，ss是个好工具然而默认command line的proxy设置不影响。因此我们需要运行以下命令设置proxy：

#### cmd下
```
set http_proxy=http://127.0.0.1:1080
set https_proxy=http://127.0.0.1:1080
```

#### powershell下
```
$env:http_proxy="http://127.0.0.1:1080"
$env:https_proxy="http://127.0.0.1:1080"
```

参考链接：<https://gist.github.com/dreamlu/cf7cbc0b8329ac145fa44342d6a1c01d>

---

### update 0.1
简陋的爬取bnb-btc的toy版本