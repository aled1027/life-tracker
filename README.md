To work on:
1. restrict user access to only things they should have access to 
	- add foreigkey = user to every model? There must be easier way... to google!!!
1. User download data - mostly working for admin
	- for analysis of collected data:
	- http://djangotricks.blogspot.com/2013/12/how-to-export-data-as-excel.html
3. User ability to look at data in tables more easily
4. User able to look at tables and graphs of data
5. Add tests

- add help_text to django model fields

- removing tag functionality. Ask sam if he wants it .. add in later.

To use South:
	python manage.py..
		schemamigration activity --initial or --auto
		migrate activity
		if the above doesn't work, 
			migrate activity --fake
			migrate activity


