[ENGLISH](https://github.com/yaronzz/easy-docs) | [中文文档](https://github.com/yaronzz/easy-docs/blob/master/README_CN.md)

# Easy-Docs
One-click generation of documentation website

## 📺 Install 
Python version >= 3.7
```shell
pip3 install easy-docs --upgrade
```

## 🤖 Features

- Generate and update documentation catalogs
- Generate `docsify` index page

## 💽 UI
[Python-100-Days](http://yaronzz.com/Python-100-Days/#/)

![image-20220411100211300](https://s2.loli.net/2022/04/11/Z2ODRxbTCB1MtPv.png)

## 🎄Use

`cd` to the directory of documents.

1. Initialize the document
```shell
easy-docs -i 
```

2. Test
```shell
easy-docs -s
```

3. Update documentation catalogs
```shell
easy-docs -u

#does not contain the tmp directory
easy-docs -u -r ./tmp/
```


4. Modify documentation pages

    Open `index.html`，and modify the configuration according to the 【documentation](https://docsify.js.org/#/configuration).
