from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL


# class User(AbstractUser):
#     follows = models.ManyToManyField(
#         "User",
#         blank=True,
#         related_name="followers"
#     )

# # A post has a foreign key to user - many to one relationship
# # Also needs a text value, create is a model so we can add more later


# class Project(models.Model):
#     """
#     Foreign key with user (related name = projects), has a post Charfield for text of post
#     """
#     user = models.ForeignKey(
#         User,
#         on_delete=CASCADE, related_name="projects")
#     description = models.CharField(
#         max_length=1000,
#         verbose_name="Description:"
#     )
#     github = models.URLField(
#         verbose_name="Link to Github Repo:"
#     )
#     title = models.CharField(max_length=100)
#     programming_language = models.TextChoices
#     # User can like many projects and projects can have many likes, both can be null and blank.
#     likes = models.ManyToManyField(
#         User,
#         blank=True,
#         related_name="likedProjects"
#     )
#     date = models.DateTimeField(
#         verbose_name="Published:",
#         auto_now_add=True,
#         blank=True
#     )


# class Comment(models.Model):
#     pass
