"""Posts app models."""


from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Group model description."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        """Returns string view of title field."""
        return self.title


class Post(models.Model):
    """Post model description."""
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE,
        related_name="posts", blank=True, null=True
    )

    def __str__(self):
        """Returns string view of title field."""
        return self.text


class Comment(models.Model):
    """Comment model description."""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    """Follow model description."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_follow_pair'
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F('following')),
                name='user_and_author_can_not_be_equal'
            ),
        ]
