from rest_framework import serializers

from apps.orders.models import OrderModel
from apps.users.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    users = UserSerializer(
        many=True,
        read_only=True)  # use instead of depth, because with 'depth = 1'  we have response with not unnecessary fields, for exam. order_id, so we need to use

    # set read_only=True, and now when we create orders without specifying users

    class Meta:
        model = OrderModel
        fields = ('id', 'status', 'total_price', 'day', 'comment', 'quantity_of_products','users')
        # depth = 1  # depth of inner values

    def validate_price(self, total_price):
        if total_price <= 0:
            raise serializers.ValidationError('total_price must be greater than 0')
        return total_price

    def validate(self, attrs):
        total_price = attrs.get('total_price')
        status = attrs.get('status')
        # attrs is use for all fields

        # Check that total_price is positive and status is provided
        if total_price is not None and total_price <= 0:
            raise serializers.ValidationError('total_price must be greater than 0')

        if status is None:
            raise serializers.ValidationError('status must be provided')
        return attrs  # after validation, we need to return all fields
