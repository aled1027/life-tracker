
- work on templates for activity
- Add account view to see user information
- add tutorial to home
- Accounts:
	accounts/register has no view...

     <p> use the following format for dates/times: '10/25/2006 14:30'<p>

To use South:
	python manage.py..
		schemamigration activity --initial or --auto
		migrate activity
		if the above doesn't work, 
			migrate activity --fake
			migrate activity


