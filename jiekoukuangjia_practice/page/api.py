'''
web端企业微信的标签接口练习
'''
import json
import requests

#方法接口封装
class Api():
    access_token=''
    corpid='ww5ad19db6a32eae0e'
    corpsecret='8-grfsNu2r7ern6p8iOFHCRUaNori99RDT-3pi_SKaM'
    url_get_token='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    url_search_list='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list'
    url_add_tag='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag'
    url_delete_tag='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag'
    #token获取封装
    def get_token(self):
        r=requests.get(
            url=self.url_get_token,
            params={
                'corpid':self.corpid,
                'corpsecret':self.corpsecret
            }
        )
        self.access_token=r.json()['access_token']
    #标签查询封装
    def search_list(self):
        r=requests.post(
            url=self.url_search_list,
            params={
                'access_token':self.access_token,
                'tag_id':[]
            }
        )
        return r
    #添加标签封装
    def add_tag(self,group_name,tag_name,group_id=None):
        result=''
        if group_id==None:
            r=requests.post(
                url=self.url_add_tag,
                params={'access_token': self.access_token},
                json={
                    'group_name':group_name,
                    'tag':tag_name
                }
            )
            result=r.json()['errcode']
        elif group_id is not  None:
            r=requests.post(
                url=self.url_add_tag,
                params={'access_token': self.access_token},
                json={
                    'group_id': group_id,
                    'tag': tag_name
                }
            )
            result=r.json()['errcode']
        return result
    #删除标签封装
    def delete_tag(self,group_id):
        r=requests.post(
            url=self.url_delete_tag,
            params={'access_token': self.access_token},
            json={'group_id':group_id}
        )
        result=r.json()['errcode']
        return result
    def exchange(self,r):
        result=json.dumps(r,indent=2)
        return result
