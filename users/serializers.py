from rest_framework import serializers

# We can use several serializer
class UserSerializer(serializers.Serializer):  # help to convert model to json
    id = serializers.IntegerField(read_only=True)  # read_only=True specify, because if we use post method, it will require id
    name = serializers.CharField(max_length=20)
    age = serializers.IntegerField()
    status = serializers.BooleanField()
    weight = serializers.FloatField()

    def