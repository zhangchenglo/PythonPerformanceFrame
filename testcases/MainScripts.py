"""
@Project ：PythonPerformanceTestFrame 
@File    ：MainScripts.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/10/29 11:03 
@explain ：
"""

from locust import LoadTestShape, HttpUser, between

from api.HttpBinModule import HttpBinModule


class CustomLoadShape(LoadTestShape):  # LoadTestShape 启动负载均衡模式
    """
    自定义负载均衡形状，定义用户数量和速率在不同时间阶段的变化
    """

    def tick(self):
        run_time = self.get_run_time()

        if run_time < 60:
            # 第一个阶段：0-60秒，有 10 个并发用户，每秒增加 2 个用户
            return (10, 2)
        elif run_time < 120:
            # 第二个阶段：60-120秒，有 20 个并发用户，每秒增加 3 个用户
            return (20, 3)
        elif run_time < 180:
            # 第三个阶段：120-180秒，逐渐减少用户
            return (15, 2)
        else:
            # 结束测试
            return None


"""
压测地址 ： http://www.httpbin.org
"""


class WebsiteUser(HttpUser):   # 继承 HttpUser
    wait_time = between(2, 3)  # 发送请求前后等待时间
    # # 设置 tasks 中的权重，ArticleModule 权重为 2，UserModule 权重为 1  类之间的权重
    # tasks = {
    #     ArticleModule: 2,  # UserBehavior 权重为 2
    #     UserModule: 1  # UserBehavior2 权重为 1
    # }
    tasks = {
        HttpBinModule
    }


