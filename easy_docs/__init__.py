#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :  __init__.py
@Date    :  2022/03/23
@Author  :  Yaronzz
@Version :  1.0
@Contact :  yaronhuang@foxmail.com
@Desc    :  
"""

import getopt
import sys
import os
import easy_docs.docsify
import easy_docs.util
from http.server import HTTPServer, SimpleHTTPRequestHandler

def help():
    print("-h or --help    : show help-message")
    print("-i or --init    : init doc index")
    print("-u or --update  : update sidebar")
    print("-r or --remove  : does not contain some directories")
    print("-s or --server  : test server")
    
def main():
    print("============EASY DOC=================")
    try:
        opts, args = getopt.getopt(sys.argv[1:], 
                                   "hiur:s", 
                                   ["help", "init", "update", "remove=", "server"])
    except getopt.GetoptError as errmsg:
        print('Err:' + vars(errmsg)['msg'] + ". Use 'easydoc -h' for useage.")
        return

    writeIndex = False
    writeSidebar = False
    skipPath = []
    
    for opt, val in opts:
        if opt in ('-h', '--help'):
            help()
            return
        if opt in ('-i', '--init'):
            writeIndex = True
            writeSidebar = True
        if opt in ('-u', '--update'):
            writeSidebar = True
        if opt in ('-r', '--remove'):
            skipPath.append(val)
        if opt in ('-s', '--server'):
            print(f"Serving {os.getcwd()} now.")
            print(f"Listening at http://localhost:3000")
            server = HTTPServer(('0.0.0.0', 3000), SimpleHTTPRequestHandler)
            server.serve_forever()
            return

    if writeIndex:
        easy_docs.docsify.init('./')
    if writeSidebar:
        easy_docs.util.createSidebarFile('./', skipPath)

