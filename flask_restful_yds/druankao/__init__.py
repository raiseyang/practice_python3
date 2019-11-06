import json

from flask import Response


class CommonResponse(object):
    """
    通用返回类
    """

    def __init__(self, status=1000, msg="ok", data=None):
        if data is None:
            data = {}
        self.status = status
        self.msg = msg
        self.data = data

    def to_json_response(self):
        return Response(json.dumps(self, default=lambda o: o.__dict__),
                        content_type='application/json')
