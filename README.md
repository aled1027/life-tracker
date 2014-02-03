To work on:

1. Get static files working on heroku server
	- Use AWS
	- https://devcenter.heroku.com/articles/s3
	- http://www.realpython.com/blog/python/migrating-your-django-project-to-heroku/#.Uu8_Kd_Tk8o
2. Add tests
3. Create error pages and error related code
4. Consider redoing model structure to use inheritance aka abstract base classes in documenation
5. User download data - mostly working for admin
	- http://djangotricks.blogspot.com/2013/12/how-to-export-data-as-excel.html
6. Add coooooookies. mmmmm
7. add help_text to django model fields

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


