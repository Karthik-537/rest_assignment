from test_app.build.serializers.definitions.User.UserSerializer import UserSerializer
from test_app.build.serializers.definitions.User.UserSerializer import UserType
from test_app.build.serializers.definitions.UserWithExtraFields.UserWithExtraFields.Schema1.Schema1Serializer import Schema1Serializer
from test_app.build.serializers.definitions.UserWithExtraFields.UserWithExtraFields.Schema1.Schema1Serializer import Schema1Type

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize

class UserWithExtraFieldsType(UserType, Schema1Type):
    def __init__(self, **validated_data):
        UserType.__init__(self, **validated_data)
        Schema1Type.__init__(self, **validated_data)
        

class UserWithExtraFieldsSerializer(UserSerializer, Schema1Serializer):
    def create(self, validated_data):
        
        userSerializer, _ = deserialize(UserSerializer, validated_data, many=False, partial=True)
        validated_data.update(userSerializer.__dict__)
        
        schema1Serializer, _ = deserialize(Schema1Serializer, validated_data, many=False, partial=True)
        validated_data.update(schema1Serializer.__dict__)
        
        return UserWithExtraFieldsType(**validated_data)
