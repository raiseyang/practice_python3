"""
https://blog.csdn.net/yannanxiu/article/details/53557657
https://blog.csdn.net/iszhenyu/article/details/56846551
"""
from flask import current_app


def d(msg):
    current_app.logger.debug(msg)
