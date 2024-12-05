class PersonParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "CreateNewPersonParameter",
            "parameter_field_name": "person"
        }
        return param_names

    @staticmethod
    def get_serializer_class():
        serializer_options = {
            "param_serializer": "UserSerializer",
            "param_serializer_import_str": "from test_app.build.serializers.definitions.User.UserSerializer import UserSerializer",
            "param_serializer_required": False,
            "param_serializer_array": False
        }
        return serializer_options
        

    @staticmethod
    def get_serializer_field():
        pass

    @staticmethod
    def get_url_regex():
        pass