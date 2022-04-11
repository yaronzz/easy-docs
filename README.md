# EasyDoc
一键生成文档网站

## 📺 安装 
需要 Python 版本大于或等于 3.7
```shell
pip3 install easydoc --upgrade
```

## 🤖 功能

- 生成与更新文档目录
- 配置`docsify`样例首页

## 💽 界面
[样例 Python-100-Days](http://yaronzz.com/Python-100-Days/#/)

![image-20220411100211300](https://s2.loli.net/2022/04/11/Z2ODRxbTCB1MtPv.png)

## 🎄使用

先`cd`进入文档的目录

1. 初始化文档
```shell
easydoc -i 
```

2. 测试文档网页
```shell
easydoc -s
```

3. 更新目录
```shell
easydoc -u

#更新目录，不包含tmp目录
easydoc -u -r ./tmp/
```


4. 修改文档网页

打开目录下生成的`index.html`，根据[docsify官方文档](https://docsify.js.org/#/zh-cn/configuration)配置自己的网页

## 🎨库与引用

- [docsify](https://github.com/docsifyjs/docsify/)
