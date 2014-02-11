from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from activity.models import *
from activity.forms import *


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
		#rIs = []
		#for r in rS:
			#rIs.append(RateActivityInstance.objects.get(rateActivity=r, activityInstance=aI))
		rIs = [RateActivityInstance.objects.get(rateActivity=r, activityInstance=aI) for r in rS]
		rForms = [RateActivityInstanceForm(request.POST, prefix=str(x), instance=rI) for x,rI in zip(range(0,n),rIs)]

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
				new_rI.rating = rF.cleaned_data['rating']
				new_rI.save() # going wrong here... not saving to database
				print new_rI
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
			i = 0
			for r in rS:
				# get rate activityInstances of activity
				try:
					rI = RateActivityInstance.objects.get(activityInstance=aI, rateActivity=r)
					rForm = RateActivityInstanceForm(instance=rI, prefix=str(i))
					rForm.name = r.name
					rForms.append(rForm)
				except:
					rI = RateActivityInstance(rateActivity=r, activityInstance=aI)
					rI.activityInstance = aI
					rI.save()
					rForm = RateActivityInstanceForm(instance=rI, prefix=str(i))
					rForm.name = r.name
					rForms.append(rForm)
				i=i+1
		else:
			i = 0
			for r in rS:
				name = r.name
				rForm = RateActivityInstanceForm(prefix=str(i))
				rForm.name = name
				rForms.append(rForm)
				i=i+1
		return render(request, "activityInstance_form.html", {"form": form, "rForms": rForms, "activity": activity})

def chartView(request, a_id, xaxis, yaxis):
	#from django.utils import simplejson
	import simplejson as simplejson

	# get data
	a = get_object_or_404(Activity, pk=a_id)
	aIs = ActivityInstance.objects.filter(activity=a).order_by('startTime')
	try:
		# check if axis is a core value of an activity instance
		xs = [[getattr(aI, xaxis), aI.startTime] for aI in aIs]
	except:
		# if above failed, the value is part of a Rate Activity
		try:
			rA = get_object_or_404(RateActivity, name=xaxis)
			xs = [[rAI.rating, rAI.activityInstance.startTime] for rAI in RateActivityInstance.objects.filter(rateActivity=rA)]
		except:
			raise Http404
	try:
		ys = [[getattr(aI, yaxis), aI.startTime] for aI in aIs]
	except:
		# if above failed, the value is part of a Rate Activity
		try:
			rA = get_object_or_404(RateActivity, name=yaxis)
			ys = [[rAI.rating, rAI.activityInstance.startTime] for rAI in RateActivityInstance.objects.filter(rateActivity=rA)]
		except:
			raise Http404
	#make data points
	if len(xs) == len(ys):
		print xs
		print ys
		data = [(x[0],y[0]) for x,y in zip(xs,ys)]
	else:
		data = []
		i = 0
		y = ys[i]
		for x in xs:
			while x[1]!=y[1] and i<len(ys)-1:
				i=i+1
				y = ys[i]
			data.append((x[0], y[0]))
		print data

	return render(request, "chart.html", {"js_data": data})

def chartFormView(request, a_id):
	if request.method == 'POST':
		form = ChartForm(None, request.POST)
		if form.is_valid():
			form.data['xaxis']
			return HttpResponseRedirect(reverse('chart', args=(1,form.data['xaxis'], form.data['yaxis'])))
		else:
			pass
			return HttpResponseRedirect(reverse('home'))
	else:
		activity = get_object_or_404(Activity, pk=a_id)
		choices = [(rA.name, rA.name) for rA in RateActivity.objects.filter(activity=activity)]
		choices.append(('startTime', 'Start Time'))
		choices.append(('endTime', 'End Time'))
		choices.append(('duration', 'Duration'))
		form = ChartForm(choices=[tuple(choices), tuple(choices)])
		return render(request, "form.html", {'form': form})

def searchActivitiesView(request):
	if request.method=="POST":
		search_text = request.POST['search_text']
	else:
		search_text = ''
	activities = Activity.objects.filter(name__contains=search_text)
	return render(request, 'ajax_search.html', {'activities': activities})

