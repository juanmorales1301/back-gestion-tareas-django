class ResponseModel:
    def __init__(
        self,
        mensaje,
        code,
        status=200,
        correcto=True,
        data=None,
        access_token=None,
        token_type=None,
    ):
        self.status = status
        self.mensaje = mensaje
        self.code = code
        self.correcto = correcto
        self.data = data or {}
        self.access_token = access_token
        self.token_type = token_type

    def to_dict(self):
        response = {
            "mensaje": self.mensaje,
            "code": self.code,
            "correcto": self.correcto,
            "data": self.data,
            "status_code": self.status,
        }
        if self.access_token:
            response["access_token"] = self.access_token
        if self.token_type:
            response["token_type"] = self.token_type
        return response
