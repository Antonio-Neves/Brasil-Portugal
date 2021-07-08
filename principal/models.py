from django.db import models


class BaseModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)


class Category(BaseModel):
	category_id = models.AutoField(primary_key=True)
	category_name = models.CharField('Category', max_length=100, unique=True)
	category_slug = models.SlugField(max_length=150, unique=True)

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'
		ordering = ['category_name']

	def __str__(self):
		return self.category_name


class SubCategory(BaseModel):
	sub_category_id = models.AutoField(primary_key=True)
	sub_category_category = models.ForeignKey(
		Category, related_name='subcategorycategory', on_delete=models.CASCADE
	)
	sub_category_name = models.CharField(
		'Sub Category', max_length=100, unique=True
	)
	sub_category_slug = models.SlugField(max_length=150, unique=True)

	class Meta:
		verbose_name = 'Subcategory'
		verbose_name_plural = 'Subcategories'
		ordering = ['sub_category_name']

	def __str__(self):
		return self.sub_category_name


class Article(BaseModel):

	ARTICLE_STATUS = (
		('0', 'Draft'),
		('1', 'Publish')
	)

	article_id = models.AutoField(primary_key=True)
	article_cat = models.ForeignKey(
		SubCategory, related_name='articlesubcategory', on_delete=models.CASCADE)
	article_name = models.CharField('Name', max_length=100, unique=True)
	article_slug = models.SlugField(max_length=150, unique=True)
	article_content = models.TextField()
	article_status = models.CharField(
		max_length=1, choices=ARTICLE_STATUS, default=0
	)

	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = 'Articles'
		ordering = ['article_name']

	def __str__(self):
		return self.article_name
