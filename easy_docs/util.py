#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :  util.py
@Date    :  2022/03/23
@Author  :  Yaronzz
@Version :  1.0
@Contact :  yaronhuang@foxmail.com
@Desc    :  
"""

import os


def formatDirPath(path: str):
    """格式化目录"""
    path = path.replace('\\', '/')
    path = path.replace('//', '/')
    if path.endswith('/'):
        return path
    return path + '/'


def inFilterPaths(path: str, filterPaths: list):
    for filter in filterPaths:
        if path.startswith(filter):
            return True
    return False


def getFiles(path: str, filterPaths: list):
    try:
        ret = []
        if os.path.isdir(path) is False:
            return ret

        for root, dirs, files in os.walk(path):
            for item in files:
                itemPath = root + '/' + item
                itemPath = itemPath.replace('\\', '/')
                itemPath = itemPath.replace('//', '/')

                if not item.endswith('.md') and not item.endswith('.MD'):
                    continue

                if '_sidebar' in item:
                    continue

                if inFilterPaths(itemPath, filterPaths):
                    continue

                ret.append(itemPath)
        return ret
    except:
        return []


def splitPath(path: str):
    if path.count('/') <= 0:
        return "", path

    index = path.rindex('/') + 1
    fileDir = path[:index]
    fileName = path[index:]
    fileName = fileName[:len(fileName)-3].replace('/', '')
    return fileDir, fileName


def formatPath2(path: str):
    path = path.replace(' ', '%20')
    if path.startswith('/'):
        return path
    else:
        return '/' + path


def createSidebarFile(path: str, filterPaths: list):
    path = formatDirPath(path)
    filterPaths = list(formatDirPath(item) for item in filterPaths)

    array = getFiles(path, filterPaths)

    txtLines = []
    curPath = ''

    for item in array:
        item = item[len(path):]
        itemPath, itemName = splitPath(item)

        if itemPath != curPath:
            curPath = itemPath
            txtLines.append(f"* **{itemPath[:len(itemPath)-1].replace('/', '')}**\n")

        if itemPath != '':
            txtLines.append(f"  ")
        txtLines.append(f"- [{itemName}]({formatPath2(item)})\n")

    with open(f"{path}/_sidebar.md", "w+", encoding='utf-8') as fd:
        fd.writelines(txtLines)
    print(f"Write {path}/_sidebar.md success.")

if __name__ == '__main__':
    createSidebarFile('./test/Python-100-Days', ['./test/Python-100-Days/公开课'])
