"""
@Project ：PythonPerformanceTestFrame 
@File    ：LoadEnvUtil.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/10/29 10:54 
@explain ：
"""
import os

from dotenv import load_dotenv, set_key


# 安装方式 pip install python-dotenv


class LoadEnvUtil:

    @classmethod
    def get_env_params(cls, params):
        load_dotenv()  # 加载env变量
        return os.environ.get(params)

    @classmethod
    def set_env_params(cls, params, value):
        # 检查 .env 文件是否存在，如果不存在则创建
        env_file = '.env'
        if not os.path.exists(env_file):
            with open(env_file, 'w') as f:
                pass  # 创建空的 .env 文件

        load_dotenv()
        set_key(env_file, params, value, quote_mode='never')
        print(f"{params} 已写入 env 文件")