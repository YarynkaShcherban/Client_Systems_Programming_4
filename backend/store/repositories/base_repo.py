from abc import ABC, abstractmethod
from django.db.models import Model


class BaseRepo(ABC):
    def __init__(self, model: Model):
        self.model = model

    def get_all(self): 
        return self.model.objects.all()

    def get_by_id(self, _id):
        try:
            return self.model.objects.get(pk=_id)
        except self.model.DoesNotExist:
            return None

    def create(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def update(self, _id, **kwargs):
        instance = self.get_by_id(_id)
        if not instance:
            return None
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def delete(self, _id):
        instance = self.get_by_id(_id)
        if not instance:
            return False
        instance.delete()
        return True

    def filter_by(self, **kwargs): 
        return self.model.objects.filter(**kwargs)

    def get_first(self, **kwargs): 
        return self.model.objects.filter(**kwargs).first()

    def count(self): 
        return self.model.objects.count()