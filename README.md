To work on:


Let's just make a model based on https://docs.djangoproject.com/en/dev/ref/models/fields/ and then make a form with meta: class=thatModel and work from there. I think that should work. 

Although, I'm unsure why this doesn't work. I guess because there is no field for the data to go???


2 views. One for template; one with url to image

1. Add graphs
	http://www.youtube.com/watch?v=zxbCkftGyds
	http://www.thebigblob.com/making-charts-and-outputing-them-as-images-to-the-browser-in-django/
	https://blog.dbrgn.ch/2013/9/26/plot-django-registered-users/
	http://bitsofpy.blogspot.com/2009/07/matplotlib-in-django.html
	http://matplotlib.org/users/recipes.html
2. User download data - mostly working for admin
	- http://djangotricks.blogspot.com/2013/12/how-to-export-data-as-excel.html
3. Add tests
4. Create error pages and error related code
5. Consider redoing model structure to use inheritance aka abstract base classes in documenation
6. Add a page about the site. The features, how they are implemented, my process and so on
7. Add coooooookies. mmmmm

- add help_text to django model fields

- removing tag functionality. Ask sam if he wants it .. add in later.

To use South:
	python manage.py..
		schemamigration activity --initial or --auto
		migrate activity
		if the above doesn't work, 
			migrate activity --fake
			migrate activity


	- http://zmsmith.com/2010/04/using-custom-django-querysets/
	- http://stackoverflow.com/questions/4762524/is-it-possible-to-override-objects-on-a-django-model
	- https://docs.djangoproject.com/en/dev/topics/db/managers/

Marketing Ideas:
	- Using Malcolm Gladwell's Idea of 3k hours
	- building on what you've done. Understanding what works -- for you
		- Improvement happens different for each individual
		- We all have different needs
