from django.db import models
from django.contrib.auth import get_user_model
import readtime


User = get_user_model()

class Author(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_picture = models.ImageField()
	profile = models.TextField()

	def __str__(self):
		return self.user.username

class Category(models.Model):
	title = models.CharField(max_length=20)

	def __str__(self):
		return self.title

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	first_content = models.TextField(blank=True, default='')
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	categories = models.ManyToManyField(Category, related_name='posts') 
	time_stamp = models.DateTimeField(auto_now_add=True)
	image = models.ImageField()
	preview =  models.CharField(max_length=170)
	subhead1 = models.CharField(max_length=100, blank=True, default='')
	subhead2 = models.CharField(max_length=100)		

	def get_readtime(self):
		result = readtime.of_text(self.content)
		return result.text

	def __str__(self):
		return self.title

class Client(models.Model):
	name = models.CharField(max_length=50)
	position = models.CharField(max_length=50)
	pic = models.ImageField()
	testimonial = models.TextField()

	def __str__(self):
		return self.name		

class Comment(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	website = models.CharField(max_length=100, blank=True)
	message = models.TextField()
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
	time_stamp = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(default='static_env/generic.jpg')

	def __str__(self):
		return '%s - %s' % (self.post.title, self.name)
