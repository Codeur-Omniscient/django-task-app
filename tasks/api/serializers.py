from rest_framework import serializers
from tasks.models import Task



class TaskSerializers(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"