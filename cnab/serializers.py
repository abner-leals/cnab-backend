from rest_framework import serializers
from .models import Transaction, TransactionType

# create a serializer


class FileSerializer(serializers.Serializer):

    file = serializers.FileField()

    class Meta:
        fields = ["file"]


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = "__all__"


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = ["description"]


class TransactionSerializer(serializers.ModelSerializer):
    # type = DescriptionSerializer(read_only=True)
    type = DescriptionSerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = "__all__"

    def create(self, validated_data):
        transaction, _ = Transaction.objects.get_or_create(**validated_data)
        return transaction


class StoreNameSerializer(serializers.Serializer):
    value = serializers.FloatField(read_only=True)
    store = serializers.CharField()
    owner = serializers.CharField(read_only=True)
