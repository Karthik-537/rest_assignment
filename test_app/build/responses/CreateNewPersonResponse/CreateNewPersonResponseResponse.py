class CreateNewPersonResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"firstName": "string", "lastName": "string", "username": "string", "age": 1, "createdOn": "string", "userId": "string"}',
            "response_serializer": "UserWithExtraFieldsSerializer",
            "response_serializer_import_str": "from test_app.build.serializers.definitions.UserWithExtraFields.UserWithExtraFieldsSerializer import UserWithExtraFieldsSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass