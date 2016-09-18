#coding=utf8
import codecs
import os
import pymongo

if __name__ == "__main__":
    conn = pymongo.MongoClient("202.120.24.213", 27017, connect=False)
    secCom = conn.secCom.rssInfo
    #已下载
    # downLoaded = set()
    # with codecs.open('/Users/liangxiansong/Desktop/XBRLDown/folder.txt') as file:
    #     for line in file.readlines():
    #         dirNameList = line.split('#')
    #         if len(dirNameList) < 2:
    #             continue
    #         cik = dirNameList[-1].strip()
    #         acceptTime = os.path.basename(dirNameList[0])
    #         # print 'add to downLoaded Set %s' % cik+'_'+acceptTime
    #         downLoaded.add(cik+'_'+acceptTime)
    # print '已下载',len(downLoaded)
    #
    # #全集
    # allSet = set()
    # filePath = '/Users/liangxiansong/Desktop/XBRLDown/all.txt'
    # with codecs.open(filePath) as file:
    #     for line in file.readlines():
    #         dirNameList = line.split('_')
    #         if len(dirNameList) < 2:
    #             continue
    #         acceptTime = dirNameList[-1].strip()
    #         cik = os.path.basename(dirNameList[0])
    #         # print 'add to all Set %s' % cik+'_'+acceptTime
    #         allSet.add(cik+'_'+acceptTime)
    # print '全集',len(allSet)
    #
    # #比较
    # resultSet = allSet - downLoaded
    # print '结果',len(resultSet)
    #
    # filePath = '/Users/liangxiansong/Desktop/unDownload.txt'
    # file = codecs.open(filePath,'w+', encoding='utf8')
    # for record in resultSet:
    #     print '写入文件。。。。',  record
    #     file.write(record + '\n')


    allSet = set()
    filePath = '/Users/liangxiansong/Desktop/all.txt'
    file = codecs.open(filePath,'w+', encoding='utf8')
    for item in secCom.find():
        print item['cikNumber'],item['acceptanceDatetime']
        print 'add to allSet %s' % item['cikNumber']+'_'+item['acceptanceDatetime']
        allSet.add(item['cikNumber']+'_'+item['acceptanceDatetime'])

    print len(allSet)


    for record in allSet:
        print '写入文件。。。。',  record
        file.write(record + '\n')

