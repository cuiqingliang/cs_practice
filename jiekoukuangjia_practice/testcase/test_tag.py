'''
测试接口的增删查
'''
import pytest

from jiekoukuangjia_practice.page.api import Api

class TestTag():
    def setup_class(self):
        self.api=Api()
        self.api.get_token()
        #数据清洗,清空数据，使环境保持干净
        r=self.api.search_list()
        id_list=r.json()['tag_group']
        for id in id_list:
            group_id=id['group_id']
            self.api.delete_tag(group_id)
    #查询标签测试
    def test_search_list(self):
        r=self.api.search_list()
        print(self.api.exchange(r.json()))
        assert r.json()['errcode']==0

    #增加标签，单个新增重复标签名
    @pytest.mark.parametrize('group_name,tag_name',[
        ["lagou1",[{"name":"11"}]],
        ["lagou2",[{"name":"21"},{"name":"22"}]],
        ["lagou3",[{"name":"33"},{"name":"33"}]]
    ])
    def test_add_tag(self,group_name,tag_name):
        r=self.api.add_tag(group_name,tag_name)
        s = self.api.search_list()
        print(self.api.exchange(s.json()))
        assert r==0

    #新增标签重复验证
    @pytest.mark.parametrize('group_name,tag_name', [
        ["lagou1", [{"name": "11"}]],
        ["lagou1", [{"name": "11"}]]
    ])
    def test_add_fail(self,group_name,tag_name):
        try:
            r = self.api.add_tag(group_name, tag_name)
            s = self.api.search_list()
            print(self.api.exchange(s.json()))
            print(r)
        except:
            assert r == 40071

    ## 新增为空验证
    @pytest.mark.parametrize('group_name,tag_name', [
        ["lagou1", [{"name": ""}]],
    ])
    def test_add_null(self,group_name,tag_name):
        try:
            r = self.api.add_tag(group_name, tag_name)
            print(r)
        except:
            assert r == 41018

    ## 新增长度验证
    @pytest.mark.parametrize('group_name,tag_name', [
        ["lagou1", [{"name": "1111111111111111111111111111111"}]],
    ])
    def test_add_lenth(self, group_name, tag_name):
        try:
            r = self.api.add_tag(group_name, tag_name)
            print(r)
        except:
            assert r == 40058




