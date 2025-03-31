from rest_framework import serializers

from apps.orders.models import OrderModel
from apps.users.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    users = UserSerializer(
        many=True, read_only=True)  # use instead of depth, because with 'depth = 1'  we have response with not unnecessary fields, for exam. order_id, so we need to use
    # set read_only=True, and now when we create orders without specifying users

    class Meta:
        model = OrderModel
        fields = ('id', 'status', 'total_price', 'users')
        # depth = 1  # depth of inner values
