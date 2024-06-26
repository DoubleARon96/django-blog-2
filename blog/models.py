from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.event_name


class Ticket(models.Model):
    ticket_holder = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users_tickets"
    )
    date_issued = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="event_tickets"
    )


    def __str__(self):
        return f"Ticket for {self.ticket_holder}"   

    """
    Stores a single blog post entry related to :model:`auth.User`.
    """

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"
    
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`.
    """

class Comment(models.Model):
    # Relationship with the Post model (many-to-one)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')

    # Relationship with the built-in User model (many-to-one)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')

    # Comment body
    body = models.TextField()

    # Approval status (defaults to False)
    approved = models.BooleanField(default=False)

    # Created timestamp (auto-populated when a comment is added)
    created_on = models.DateTimeField(auto_now_add=True)

    challenge = models.CharField(max_length=100, default='')

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"



#class Country(models.Model):
    # …
    #capital_city = models.OneToOneField(
    #    CapitalCity,
    #    on_delete=models.CASCADE,
    #    related_name="capital_of"
    #)
    # …

class Ticket(models.Model):
    ticket_holder = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users_tickets"
    )
    date_issued = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="event_tickets"
    )

    def __str__(self):
        return f"Ticket for {self.ticket_holder}"
    
