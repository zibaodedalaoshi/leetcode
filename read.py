import os
with open("D:\\FineReport_11.0\\webapps\\webroot\\WEB-INF\\reportlets\\10.0-下拉框参数联动.cpt",encoding="utf-8")as f:
    alltext=f.read()
    s=alltext.find('<![CDATA[参数]]></PWTitle>')
    print(s)
    e=alltext.rfind('<![CDATA[]]></O>')
    print(e)
    print(alltext[s:e])
    f.close()