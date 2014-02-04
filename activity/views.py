from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from activity.models import *
from activity.forms import *
from chartit import DataPool, Chart


def activityHomeView(request):
	return render(request, "activity_home.html", {})

@login_required
def activityFormView(request, a_id=None):
	if a_id:
		a = get_object_or_404(Activity, pk=a_id)
	else:
		a  = None
	if request.method == "POST":
		form = ActivityForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			return HttpResponseRedirect(reverse('activity_list'))
		else:
			return HttpResponseRedirect(reverse('home'))
	else:
		form = ActivityForm(instance=a)
		return render(request, "form.html", {'form': form})

@login_required
def activityDetailView(request, a_id):
	a = get_object_or_404(Activity, pk=a_id)
	if a.user == request.user:
		return render(request, "activity_detail.html", {"activity": a})
	else:
		raise Http404
def activityViewDataView(request, a_id):
	a = get_object_or_404(Activity, pk=a_id)
	if a.user == request.user:
		return render(request, "activity_viewdata.html", {"activity": a})
	else:
		raise Http404

@login_required
def activityListView(request):
	try:
		activities = Activity.objects.all(user=request.user)
	except:
		raise Http404
	return render(request, "activity_list.html", {"activities": activities})

@login_required
def rateActivityDetailView(request, a_id, r_id):
	r = RateActivity.objects.get(pk=r_id)
	a = Activity.objects.get(pk=a_id)
	if a.user == request.user:
		return render(request, "rateActivity_detail.html", {"rateActivity": r, "activity": a})
	else:
		raise Http404

@login_required
def rateActivityFormView(request, a_id, r_id=None):
	if r_id:
		r = get_object_or_404(RateActivity, pk=r_id)
	else:
		r = None
	if request.method == "POST":
		form = RateActivityForm(request.POST, request.FILES)
		if form.is_valid():
			activity = get_object_or_404(Activity, pk=a_id)
			instance = form.save(commit=False) # could do instance = form.save() if I want to access the object
			instance.activity = activity
			instance.save()
			instance = form.save() # could do instance = form.save() if I want to access the object
			return HttpResponseRedirect(reverse('rateActivity_detail', args=(a_id, instance.id)))
		else:
			# DO SOMETHING HERE .. WE HAVE AN ERROR SAVING THE FORM
			# Probably because there is a duplicate.. unique=True on name field
			return HttpResponseRedirect(reverse("home"))
	else:
		form = RateActivityForm(instance=r)
		return render(request, "rateActivity_form.html", {"form": form})

@login_required
def activityInstanceFormView(request, a_id, aI_id=None):
	if aI_id:
		aI = get_object_or_404(ActivityInstance, pk=aI_id)
	else:
		aI = None
	if request.method == "POST":
		form = ActivityInstanceForm(request.POST, request.FILES, prefix="aIForm")
		a = get_object_or_404(Activity, pk=a_id)
		n = len(RateActivity.objects.filter(activity=a)) # amount of RateActivities for this activity
		rForms = [RateActivityInstanceForm(request.POST, prefix=str(x)) for x in range(0,n)]
		if form.is_valid() and all([rF.is_valid() for rF in rForms]):
			activity = get_object_or_404(Activity, pk=a_id)
			new_activityInstance = form.save(commit=False)
			if new_activityInstance.hasError == True:
				# FIGURE THIS OUT
				 pass # skips to past if statement
			new_activityInstance.activity = activity
			new_activityInstance.save()
			rateActivities = RateActivity.objects.filter(activity=a)
			for rF, rateActivity in zip(rForms,rateActivities):
				new_rI = rF.save(commit=False)
				new_rI.activityInstance = new_activityInstance
				new_rI.rateActivity = rateActivity
				new_rI.save()
			return HttpResponseRedirect(reverse('activityInstance_detail', args=(a_id, new_activityInstance.id)))
		# DO SOMETHING HERE .. WE HAVE AN ERROR SAVING THE FORM
		# probably a duplication/uniqueness error
		return HttpResponse(form.errors)
	else:
		# can optimize this. Or make it cleaner
		# form has no activityInstance associated with it
		activity  = get_object_or_404(Activity, pk=a_id)
		form = ActivityInstanceForm(instance=aI, prefix="aIForm") # was aI_id
		rS = RateActivity.objects.filter(activity=activity)
		rForms = []
		if aI_id:
			for r in rS:
				# get rate activityInstances of activity
				rI = RateActivityInstance.objects.get(activityInstance=aI, rateActivity=r)
				rForm = RateActivityInstanceForm(instance=rI)
				rForm.name = r.name
				rForms.append(rForm)
		else:
			i = 0
			for r in rS:
				name = r.name
				rForm = RateActivityInstanceForm(prefix=str(i))
				rForm.name = name
				rForms.append(rForm)
				i=i+1
		return render(request, "activityInstance_form.html", {"form": form, "rForms": rForms, "activity": activity})

@login_required
def activityInstanceDetailView(request, a_id, aI_id):
	aI = get_object_or_404(ActivityInstance, pk=aI_id)
	a = get_object_or_404(Activity, pk=a_id)
	if a.user == request.user:
		return render(request, "activityInstance_detail.html", {"activityInstance": aI, "activity": a})
	else:
		raise Http404
	# get all ratings associated with this activity and instance


@login_required
def rateActivityInstanceFormView(request, a_id, r_id, aI_id, rI_id=None):
	if rI_id:
		rI = get_object_or_404(RateActivityInstance, pk=rI_id)
	else:
		rI = None
	if request.method == "POST":
		form = RateActivityForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.activity = get_object_or_404(Activity, pk=a_id)
			instance = form.save()
			return HttpResponseRedirect(reverse('rateActivityInstance_detail', args=(a_id, r_id, instance.id)))
		else:
			# DO SOMETHING HERE .. WE HAVE AN ERROR SAVING THE FORM
			# probably a duplication/uniqueness error
			return HttpResponseRedirect(reverse("home"))
	else:
		form = RateActivityInstanceForm(instance=rI)
		return render(request, "form.html", {"form": form})

def activityEditView(request, a_id):
	a = get_object_or_404(Activity, pk=a_id)
	if request.method=="POST":
		form = ActivityForm(request.POST, instance=a)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('activity_detail', args=(a_id)))
	else:
		form = ActivityForm(instance=a)
		return render(request, "form.html", {"form":form})

def activityInstanceEditView(request, a_id, aI_id):
	aI = get_object_or_404(ActivityInstance, pk=aI_id)
	activity = get_object_or_404(Activity, pk=a_id)
	rS = RateActivity.objects.filter(activity=activity)

	if request.method == "POST":
		form = ActivityInstanceForm(request.POST, prefix="aIForm", instance=aI)

		n = len(RateActivity.objects.filter(activity=activity)) # amount of RateActivities for this activity
		rForms = [RateActivityInstanceForm(request.POST, prefix=str(x), instance=r) for x,r in zip(range(0,n),rS)]

		if form.is_valid() and all([rF.is_valid() for rF in rForms]):
			new_activityInstance = form.save(commit=False)
			if new_activityInstance.hasError == True:
				# FIGURE THIS OUT
				 pass # skips to past if statement
			new_activityInstance.activity = activity
			new_activityInstance.save()
			rateActivities = RateActivity.objects.filter(activity=activity)
			for rF, rateActivity in zip(rForms,rateActivities):
				new_rI = rF.save(commit=False)
				new_rI.activityInstance = new_activityInstance
				new_rI.rateActivity = rateActivity
				new_rI.save()
			return HttpResponseRedirect(reverse('activityInstance_detail', args=(a_id, new_activityInstance.id)))
		# DO SOMETHING HERE .. WE HAVE AN ERROR SAVING THE FORM
		# probably a duplication/uniqueness error
		return HttpResponse(form.errors)
	else:
		# can optimize this. Or make it cleaner
		# form has no activityInstance associated with it
		form = ActivityInstanceForm(instance=aI, prefix="aIForm") # was aI_id
		rForms = []
		if aI_id:
			for r in rS:
				# get rate activityInstances of activity
				rI = RateActivityInstance.objects.get(activityInstance=aI, rateActivity=r)
				rForm = RateActivityInstanceForm(instance=rI)
				rForm.name = r.name
				rForms.append(rForm)
		else:
			i = 0
			for r in rS:
				name = r.name
				rForm = RateActivityInstanceForm(prefix=str(i))
				rForm.name = name
				rForms.append(rForm)
				i=i+1
		return render(request, "activityInstance_form.html", {"form": form, "rForms": rForms, "activity": activity})

def chartsView(request):
 #Step 1: Create a DataPool with the data we want to retrieve.
     data = \
         DataPool(
             series=
                 [{'options': {
                     'source': ActivityInstance.objects.all()},
                     'terms': [
						 'length_hours',
						 'duration']}
				])

     #step 2: Create the Chart object
     cht = Chart(
         datasource = data,
         series_options =
             [{'options':{
                 'type': 'line',
                 'stacking': False},
             'terms':{
				 'length_hours' : [
					'duration']
			 }}],
         chart_options =
             {'title': {
                 'text': 'Weather Data of Boston and Houston'},
                 'xAxis': {
                     'title': {
                         'text': 'duration'}}})
     #Step 3: Send the chart object to the template.
     return render(request, "chart.html", {'chart': cht})

def showStaticImage(request):
	""" Simply return a static image as a png """
	imagePath = "/home/alex/Pictures/pic2.png"
	from PIL import Image
	Image.init()
	i = Image.open(imagePath)
	response = HttpResponse(mimetype='image/png')
	i.save(response,'PNG')
	return response

def showDynamicImage(request, a_id):
	import matplotlib.pyplot as plt
	import numpy as np
	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	from matplotlib.figure import Figure
	from matplotlib.dates import DateFormatter, date2num, AutoDateFormatter

	a = get_object_or_404(Activity, pk=a_id)
	aIs = ActivityInstance.objects.filter(activity=a).order_by('startTime')
	durations = [aI.duration for aI in aIs]
	startTimes = [aI.startTime for aI in aIs]

	x = startTimes
	y = durations

	fig, ax = plt.subplots()
	s = datetime.now()
	ax.plot_date(x, y, '-') #'-' signifies line graph
	#ax.fmt_xdata = DateFormatter('%Y-%m-%d')
	ax.xaxis.set_major_formatter( DateFormatter('%m-%d %H:%M') ) #https://github.com/matplotlib/matplotlib/issues/2205 # uses strftime
	# change to 24 hour time - replace %I
	fig.autofmt_xdate()


	plt.title('X verse Y for %s' % a.name)
	ax.set_xlabel('xlabel')
	ax.set_ylabel('ylabel')
	plt.rc('font', size=8)

	canvas = FigureCanvas(plt.figure(1))
	response = HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response

# http://stackoverflow.com/questions/17987468/custom-date-range-x-axis-in-time-series-with-matplotlib

def chartView(request, a_id, xaxis, yaxis):
	# capital letters matter for query of rateActivity

	# TODO:
	# 1. fix names for axis and title labels
	# 2. Add units?
	import matplotlib.pyplot as plt
	import numpy as np
	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	from matplotlib.figure import Figure
	from matplotlib.dates import DateFormatter, date2num, AutoDateFormatter

	a = get_object_or_404(Activity, pk=a_id)
	aIs = ActivityInstance.objects.filter(activity=a).order_by('startTime')

	try:
		# check if axis is a core value of an activity instance
		x = [getattr(aI, xaxis) for aI in aIs]
	except:
		# if above failed, the value is part of Rate Activity
		try:
			rA = get_object_or_404(RateActivity, name=xaxis)
			x = [rAI.rating for rAI in RateActivityInstance.objects.filter(rateActivity=rA)]
		except:
			raise Http404
	try:
		y = [getattr(aI, yaxis) for aI in aIs]
	except:
		try:
			rA = get_object_or_404(RateActivity, name=yaxis)
			y = [rAI.rating for rAI in RateActivityInstance.objects.filter(rateActivity=rA)]
		except:
			raise Http404

	fig, ax = plt.subplots()
	s = datetime.now()
	if ('endTime' in xaxis) or ('startTime' in xaxis):
		ax.plot_date(x, y, '-') #'-' signifies line graph
		ax.xaxis.set_major_formatter( DateFormatter('%m-%d %H:%M') ) #uses strftime
		fig.autofmt_xdate()
	else:
		ax.plot(x,y,'-')

	if ('endTime' in yaxis or 'startTime' in yaxis):
		ax.yaxis.set_major_formatter( DateFormatter('%m-%d %H:%M') )

	# fix these names
	xaxisName = xaxis
	yaxisName = yaxis
	plt.title('%s verse %s for %s' % (xaxisName, yaxisName, a.name))
	ax.set_xlabel(xaxisName)
	ax.set_ylabel(yaxisName)
	plt.rc('font', size=8)

	canvas = FigureCanvas(plt.figure(1))
	response = HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response

def chartFormView(request, a_id):
	if request.method == 'POST':
		form = MyForm(None, request.POST)
		if form.is_valid():
			form.data['xaxis']
			return HttpResponseRedirect(reverse('chart', args=(1,form.data['xaxis'], form.data['yaxis'])))
		else:
			return HttpResponseRedirect(reverse('home'))
	else:
		activity = get_object_or_404(Activity, pk=a_id)
		choices = []
		for rA in RateActivity.objects.filter(activity=activity):
			choices.append((rA.name, rA.name))
		choices.append(('startTime', 'Start Time'))
		choices.append(('endTime', 'End Time'))
		choices.append(('duration', 'Duration'))
		xaxis = tuple(choices)
		form = MyForm(choices=[xaxis, xaxis])
		return render(request, "form.html", {'form': form})

def searchActivitiesView(request):
	if request.method=="POST":
		search_text = request.POST['search_text']
	else:
		search_text = ''
	activities = Activity.objects.filter(name__contains=search_text)
	return render(request, 'ajax_search.html', {'activities': activities})
