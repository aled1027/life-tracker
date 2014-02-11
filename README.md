Finish site by this friday. Start new project. 

1. Make a getting started page
2. Fix register user
3. Make css for forms nicer
4. Finish up all forms
5. Finish charts

4. Add tests?

Other things:
- Add coooooookies. mmmmm
- User download data - mostly working for admin
	- http://djangotricks.blogspot.com/2013/12/how-to-export-data-as-excel.html
- Consider redoing model structure to use inheritance aka abstract base classes in documenation

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

FAQ HELP:

500 Error:
	Did you migrate south? Is it a database issue?
