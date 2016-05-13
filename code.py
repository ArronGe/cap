#coding:utf-8
import web
import sys, re, json
#import httplib, urllib
import datetime

ERR_URL_WITHTOUT_NECESSARY_ATTR = 1

reload(sys)
sys.setdefaultencoding('utf-8')


urls = (
        #主机页面部分
        '/index'            , 'index',
        '/hostinfo'         , 'hostinfo',
        '/hostlist'         , 'hostlist',
        '/baselinelist'     , 'baselinelist',
        '/baselineinfo'     , 'baselineinfo',
        '/addhost'          , 'addhost',
        '/addhostBulk'      , 'addhostBulk',
        '/addbaseline'      , 'addbaseline',
        '/changepw'         , 'changepw',

        #CMDB API调用部分
        '/ajax_ci'              , 'cmdbAPI.ajax_ci',
        '/ajax_cirela'          , 'cmdbAPI.ajax_cirela',
        '/ajax_ciattr'          , 'cmdbAPI.ajax_ciattr',
        '/ajax_citype'          , 'cmdbAPI.ajax_citype',
        '/ajax_cirelatype'      , 'cmdbAPI.ajax_cirelatype',
        '/ajax_ciattrtype'      , 'cmdbAPI.ajax_ciattrtype',
        '/ajax_copy_ci'         , 'cmdbAPI.ajax_copy_ci',
        '/ajax_get_hostlist'    , 'cmdbAPI.ajax_get_hostlist',
        '/ajax_baselinelist'    , 'cmdbAPI.ajax_baselinelist',
                
        #公共操作接口
        '/ajax_uploadFile'      , 'common.ajax_uploadFile',
        '/ajax_bulkhostlist'    , 'common.ajax_bulkhostlist',
        
       )

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
