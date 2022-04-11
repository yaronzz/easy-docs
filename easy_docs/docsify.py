#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :  docsify.py
@Date    :  2022/03/23
@Author  :  Yaronzz
@Version :  1.0
@Contact :  yaronhuang@foxmail.com
@Desc    :  
"""

_HTML_CONTENT = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>EASYDOC</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta name="description" content="Description">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
    <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css">
    <!-- sidebar-collapse -->
    <!-- <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify-sidebar-collapse/dist/sidebar.min.css" /> -->
</head>

<body>
    <div id="app">LOADING</div>
    <script>
        window.$docsify = {
            name: 'EASYDOC',
            repo: 'yaronzz/EasyDoc',
            loadSidebar: true,
            auto2top: true,
            subMaxLevel: 1,
            
            // pagination
            pagination: {
                previousText: "上一页",
                nextText: "下一页",
                crossChapter: true,
                crossChapterText: true,
            },
            // countable
            count: {
                countable: true,
                position: "top",
                margin: "10px",
                float: "right",
                fontsize: "0.9em",
                color: "green",
                localization: {
                    words: "",
                    minute: "",
                },
                isExpected: true,
            },
            // search
            search: {
                depth: 6,
                noData: "NO RESULT!",
                placeholder: "Search...",
                namespace: "website-1",
            },
        }
    </script>
    <!-- Docsify v4 -->
    <script src="//cdn.jsdelivr.net/npm/docsify@4"></script>
    
    <!-- pagination -->
    <script src="https://cdn.jsdelivr.net/npm/docsify-pagination@2/dist/docsify-pagination.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/docsify@4/lib/plugins/external-script.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/docsify@4/lib/plugins/ga.min.js"></script>
    
    <!-- copy-code -->
    <script src="https://cdn.jsdelivr.net/npm/docsify-copy-code@2/dist/docsify-copy-code.min.js"></script>
    
    <!-- zoom-image -->
    <script src="https://cdn.jsdelivr.net/npm/docsify@4/lib/plugins/zoom-image.min.js"></script>
   
    <!-- countable -->
    <script src="https://cdn.jsdelivr.net/npm/docsify-count@latest/dist/countable.min.js"></script>
    
    <!-- search -->
    <script src="https://cdn.jsdelivr.net/npm/docsify@4/lib/plugins/search.js"></script>
    
    <!-- emoji -->
    <script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/emoji.min.js"></script>
    
    <!-- sidebar-collapse -->
    <!-- <script src="https://cdn.jsdelivr.net/npm/docsify-sidebar-collapse/dist/docsify-sidebar-collapse.min.js"></script> -->
    
    <!-- highlight -->
    <script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-bash.min.js"></script>
    <script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-python.min.js"></script>
    <script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-cmake.min.js"></script>
    <script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-java.min.js"></script>
    <script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-csharp.min.js"></script>
    <script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-docker.min.js"></script>

</body>

</html>
'''


def init(path: str):
    with open(f"{path}/index.html", "w+", encoding='utf-8') as fd:
        fd.writelines(_HTML_CONTENT)
    print(f"Write {path}/index.html success.")

    with open(f"{path}/.nojekyll", "w+", encoding='utf-8') as fd:
        pass
    print(f"Write {path}/.nojekyll success.")
