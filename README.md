To work on:
1. User download data - mostly working for admin
	- http://djangotricks.blogspot.com/2013/12/how-to-export-data-as-excel.html
3. User ability to look at data in tables more easily
4. User able to look at tables and graphs of data
5. Add tests
6. Create error pages and error related code

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
