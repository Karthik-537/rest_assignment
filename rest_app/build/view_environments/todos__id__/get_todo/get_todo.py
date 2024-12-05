from dsu.runtime.security.request_response import request_response
from dsu.dsu_gen.openapi.constants.config import PARSER_MAPPING
from dsu.dsu_gen.openapi.constants.config import RENDERER_MAPPING
from rest_app.build.view_environments.todos__id__.get_todo.GetTodoRequestPathParamSerializer import GetTodoRequestPathParamSerializer
from rest_app.build.serializers.definitions.Todo.TodoSerializer import TodoSerializer
from rest_app.build.serializers.definitions.DefaultHttpExceptionFields.DefaultHttpExceptionFieldsSerializer import DefaultHttpExceptionFieldsSerializer
from rest_app.build.serializers.definitions.DefaultHttpExceptionFields.DefaultHttpExceptionFieldsSerializer import DefaultHttpExceptionFieldsSerializer
from rest_app.build.serializers.definitions.DefaultHttpExceptionFields.DefaultHttpExceptionFieldsSerializer import DefaultHttpExceptionFieldsSerializer


options = {
    'METHOD': 'GET',
    'REQUEST_WRAPPING_REQUIRED': False,
    'REQUEST_ENCRYPTION_REQUIRED': False,
    'REQUEST_IS_PARTIAL': False,
    'PARSER_CLASSES': [
        PARSER_MAPPING["application/json"]
    ],
    'RENDERER_CLASSES': [
        RENDERER_MAPPING["application/json"]
    ],
    'REQUEST_QUERY_PARAMS_SERIALIZER': None,
    'REQUEST_HEADERS_SERIALIZER': None,
    'REQUEST_PATH_PARAMS_SERIALIZER': GetTodoRequestPathParamSerializer,
    'DEFAULT_REQUEST_PATH_PARAMS': {"id": 301},
    'REQUEST_SERIALIZER': None,
    'REQUEST_SERIALIZER_MANY_ITEMS': False,
    'RESPONSE': {
        
        '200': {
           'RESPONSE_SERIALIZER': TodoSerializer,
           'RESPONSE_SERIALIZER_MANY_ITEMS':  False,
           'HEADERS_SERIALIZER': None,
        }
        ,
        
        '401': {
           'RESPONSE_SERIALIZER': DefaultHttpExceptionFieldsSerializer,
           'RESPONSE_SERIALIZER_MANY_ITEMS':  False,
           'HEADERS_SERIALIZER': None,
        }
        ,
        
        '403': {
           'RESPONSE_SERIALIZER': DefaultHttpExceptionFieldsSerializer,
           'RESPONSE_SERIALIZER_MANY_ITEMS':  False,
           'HEADERS_SERIALIZER': None,
        }
        ,
        
        '404': {
           'RESPONSE_SERIALIZER': DefaultHttpExceptionFieldsSerializer,
           'RESPONSE_SERIALIZER_MANY_ITEMS':  False,
           'HEADERS_SERIALIZER': None,
        }
        
    },
    "SECURITY": {

        "oauth" : [
            "read"
            
        ]
    },
    'LOG_CONFIG': {'request_log_selector': 'ENABLE_COMPLETE_LOG', 'response_log_selector': 'ENABLE_COMPLETE_LOG'}
}

app_name = "rest_app"
operation_id  = "get_todo"
group_name = ""


@request_response(options=options, app_name=app_name, operation_id=operation_id, group_name=group_name)
def get_todo(request, *args, **kwargs):
    args = (request,) + args
    from dsu.dsu_gen.openapi.wrappers.view_env_wrapper import view_env_wrapper
    return view_env_wrapper(app_name, "get_todo", group_name, *args, **kwargs)
