To work on:
7. User ability to delete and edit everything
8. User ability to look at graphs and things

- add help_text to django model fields
- Accounts:
	accounts/register has no view...
	add a main index page for accounts
	make sure user is logged in before proceeding anywhere.  I don't want to mess with that shit. 
- for analysis of collected data:
	http://djangotricks.blogspot.com/2013/12/how-to-export-data-as-excel.html
- removing tag functionality. Ask sam if he wants it .. add in later.

     <p> use the following format for dates/times: '10/25/2006 14:30'<p>

To use South:
	python manage.py..
		schemamigration activity --initial or --auto
		migrate activity
		if the above doesn't work, 
			migrate activity --fake
			migrate activity


