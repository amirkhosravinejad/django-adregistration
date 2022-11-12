from rest_framework import serializers
from regist.models import advertise

class adSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    seller = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    #photo = serializers.ImageField()

    def create(self, data):
        return advertise.objects.create(**data)

    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.seller = data.get('seller', instance.seller)
        instance.email = data.get('email', instance.email)

        instance.save()
        return instance