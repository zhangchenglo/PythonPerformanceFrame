"""
@Project ：PythonPerformanceTestFrame 
@File    ：HttpBinModule.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/10/29 11:04 
@explain ：
"""
import os

from locust import TaskSet, task, between, constant, SequentialTaskSet

from api import Cookie
from config import BASE_DIR


class HttpBinModule(SequentialTaskSet):  # 设定用户行为 继承 SequentialTaskSet 表示 从上而下执行任务顺序

    get_url = "/get"
    post_url = "/post"
    put_url = "/put"
    delete_url = "/delete"

    headers = {
        "Cookie": Cookie
    }

    # 获取 httpbin get 接口
    @task(1)
    def httpbin_get(self):

        # 固定等待 1 秒
        constant(1)

        response = self.client.get(url=self.get_url,
                                   headers=self.headers,
                                   name="httpbin get 接口")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    @task(2)
    def httpbin_post(self):
        between(1, 5)  # 等待时间为 1 到 5 秒之间，包含 1 和 5
        payload = {
            'name': 'username',
            'password': '123456'
        }

        image_path = BASE_DIR + os.sep + "data" + os.sep + "images" + os.sep + "my.png"

        files = [
            ('image', open(image_path, 'rb'))
        ]

        response = self.client.post(url=self.post_url, headers=self.headers, data=payload, files=files,
                                    name="httpbin post 接口")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    @task(2)
    def httpbin_put(self):
        response = self.client.put(url=self.put_url,
                                   headers=self.headers,
                                   name="httpbin put 接口")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    @task(1)
    def httpbin_delete(self):
        response = self.client.delete(url=self.delete_url, headers=self.headers, name="httpbin delete 接口")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"







