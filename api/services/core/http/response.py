from ....models.core.response_model import ResponseModel

def new_response(mensaje, code, status=200, correcto=True, data=None, access_token=None, token_type=None):
    # Crear una instancia del modelo de respuesta
    response = ResponseModel(
        mensaje=mensaje,
        code=code,
        status=status,
        correcto=correcto,
        data=data,
        access_token=access_token,
        token_type=token_type,
    )
    
    # Retornar la respuesta como un diccionario
    return response.to_dict()
