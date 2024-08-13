from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

# Create your models here.
class Accounts(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(max_length=200, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}'
    
class Tree(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class PlantedTree(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE, related_name='planted_tree_account')
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE, related_name='planted_tree_tree')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    planted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Árvore plantada por {self.user.username}, com latitude {self.latitude} e longitude {self.longitude}'
    
class UserExtension(User):
    class Meta:
        proxy = True

    def plant_tree(self, latitude: Decimal, longitude: Decimal):
        PlantedTree.objects.create(user=self, latitude=latitude, longitude=longitude)

    def plant_trees(self, locations:list):
        for location in locations:
            self.plant_tree(location[0], location[1])

