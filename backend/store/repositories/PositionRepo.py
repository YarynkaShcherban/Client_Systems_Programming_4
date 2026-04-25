from store.repositories.base_repo import BaseRepo
from store.models import Position


class PositionRepo(BaseRepo):
    def __init__(self):
        super().__init__(Position)

    def get_salary_range(self, min_salary, max_salary):
        return self.model.objects.filter(salary__gte=min_salary, salary__lte=max_salary)

    def find_by_role(self, role):
        return self.model.objects.filter(role__icontains=role)