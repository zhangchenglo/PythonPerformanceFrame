"""
@Project ：PythonPerformanceTestFrame 
@File    ：__init__.py.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/10/29 11:02 
@explain ：
"""
from utils.LoadEnvUtil import LoadEnvUtil

BASE_URL = LoadEnvUtil.get_env_params("BASE_URL")

Cookie = "SESSION=" + LoadEnvUtil.get_env_params("SESSION")
