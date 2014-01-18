bug: saving activityInstance over and over again, instead of replacing the old one. 
	- not getting rateActivityInstances rating from the form?

Make sure that when one adds an rateActivity that all previously
made activityInstances aren't all fucked up. I think make the 
rate activity instnace optional for activityInstances

To work on:
1. Editing and deleting
1. User download data - mostly working for admin
	- for analysis of collected data:
	- http://djangotricks.blogspot.com/2013/12/how-to-export-data-as-excel.html
2. User ability to delete and edit everything
3. User ability to look at data in tables more easily
4. User able to look at graphs of data
5. Add tests

- add help_text to django model fields
- Accounts:


- removing tag functionality. Ask sam if he wants it .. add in later.

To use South:
	python manage.py..
		schemamigration activity --initial or --auto
		migrate activity
		if the above doesn't work, 
			migrate activity --fake
			migrate activity


