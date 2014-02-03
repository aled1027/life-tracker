To work on:

- Images are not updating immediately. Sometimes they are not updating at all. 
	What I mean is that /activity/1/startTime/vigor/chart.png will not necessarily display a chart with those axes/data
	It will display a previously accessed chart in its stead. Even after multiple refreshes, the image is not updating to 
	reflect the url's parameters



1. Add html/css/javascript
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
