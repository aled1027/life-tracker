
- add help_text to django model fields
- removing tag functionality. Ask sam if he wants it .. add in later.
- names of things are unique to everyone, make only unique to a single user
- work on templates for activity
- Add account view to see user information
- add tutorial to home
- make default on datetime fields now. 
- Accounts:
	accounts/register has no view...
	add a main index page for accounts
	make sure user is logged in before proceeding anywhere.  I don't want to mess with that shit. 

     <p> use the following format for dates/times: '10/25/2006 14:30'<p>

To use South:
	python manage.py..
		schemamigration activity --initial or --auto
		migrate activity
		if the above doesn't work, 
			migrate activity --fake
			migrate activity


code: TENBUX

