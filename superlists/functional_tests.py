from selenium import  webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 伊迪斯听说有一个很酷的在线待办事项应用
        # 她去看了应用首页
        self.browser.get('http://localhost')

        # 她注意到网页的标题和头部都包含“To-DO”
        self.assertIn('To-Do',self.browser.title)
        self.fail('Finish the test!')

        # 应用邀请她输入一个待办事项

        # 她在一个文本框中输入了“Buy peacock feathers”(购买孔雀羽毛)
        # 伊迪斯的爱好是制作鱼

        # 她按回车后页面更新了
        # 待办事项表格内显示了“1：Buy peacock feathers”

        # 页面中又显示了一个文本框，可以输入其他待办事项
        # 她输入了“Use peacock feathers to make a fly”(使用羽毛做鱼)
        # 伊迪斯做事很有条理

        # 页面再次更新，她的清单中显示有两条待办事项

        # 伊迪斯想知道这个网站是否会记住她的清单

        # 她看到网站为她生成了一个唯一的URL
        # 而且页面中有些文字解说这个功能

        # 她访问那个URL，发现她的待办事项列表还在

        # 她很满意的离开了

if __name__ == '__main__':
    unittest.main(warnings='ignore')