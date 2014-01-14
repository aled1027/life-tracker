from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from activity.models import *
from activity.forms import *


# Create your views here.
def homeView(request):
	args = {}
	return render(request, "home.html", args)

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
			return HttpResponseRedirect(reverse('activity_detail', args=[instance.id]))
		else:
			return HttpResponseRedirect(reverse('home'))
	else:
		form = ActivityForm(instance=a)
		return render(request, "form.html", {'form': form})

def activityDetailView(request, a_id):
	try:
		a = Activity.objects.get(pk=a_id)
	except Activity.DoesNotExist:
		raise Http404
	return render(request, "activity_detail.html", {"activity": a})

def rateActivityDetailView(request, a_id, r_id):
	try:
		r = RateActivity.objects.get(pk=r_id)
		a = Activity.objects.get(pk=a_id)
	except Activity.DoesNotExist:
		raise Http404
	return render(request, "rateActivity_detail.html", {"rateActivity": r, "activity": a})

def rateActivityFormView(request, a_id, r_id=None):
	if r_id:
		r = get_Object_or_404(RateActivity, pk=r_id)
	else:
		r = None
	if request.method == "POST":
		form = RateActivityForm(request.POST, request.FILES)
		if form.is_valid():
			activity = get_object_or_404(Activity, pk=a_id)
			form.activty = activity
			instance = form.save() # could do instance = form.save() if I want to access the object
			return HttpResponseRedirect(reverse('rateActivity_detail', args=(a_id, instance.id)))
		else:
			print "couldn't save form in rateActivityFormView"
			# DO SOMETHING HERE .. WE HAVE AN ERROR SAVING THE FORM
			# Probably because there is a duplicate.. unique=True on name field
			return HttpResponseRedirect(reverse("home"))
	else:
		form = RateActivityForm(instance=r)
		return render(request, "rateActivity_form.html", {"form": form})

def activityInstanceFormView(request, a_id, aI_id=None):
	if aI_id:
		aI = get_Object_or_404(RateActivity, pk=aI_id)
	else:
		r = None
	if request.method == "POST":
		form = RateActivityForm(request.POST, request.FILES)
		if form.is_valid():
			activity = get_object_or_404(Activity, pk=a_id)
			form.activty = activity
			instance = form.save() # could do instance = form.save() if I want to access the object
			return HttpResponseRedirect(reverse('activityInstance_detail', args=(a_id, instance.id)))
		else:
			print "couldn't save form in rateActivityFormView"
			# DO SOMETHING HERE .. WE HAVE AN ERROR SAVING THE FORM
			# probably a duplication/uniqueness error
			return HttpResponseRedirect(reverse("home"))
	else:
		form = ActivityInstanceForm(instance=aI_id)
		return render(request, "form.html", {"form": form})

def activityInstanceDetailView(request, a_id, aI_id):
	try:
		aI = get_object_or_404(ActivityInstance, pk=aI_id)
		a = get_object_or_404(Activity, pk=a_id)
	except ActivityInstance.DoesNotExist or Activity.DoesNotExist:
		raise Http404
	return render(request, "activityInstance_detail.html", {"activityInstance": aI, "activity": a})

def rateActivityInstanceFormView(request, a_id, r_id, aI_id, rI_id=None):
	if rI_id:
		rI = get_object_or_404(RateActivityInstance, pk=rI_id)
	else:
		rI = None
	if request.method == "POST":
		form = RateActivityForm(request.POST, request.FILES)
		if form.is_valid():
			 #= get_object_or_404(RateActivity, pk=r_id)
			#form.rateActivty = get_object_or_404(RateActivity, pk=r_id)
			instance = form.save()
			return HttpResponseRedirect(reverse('rateActivityInstance_detail', args=(a_id, r_id, instance.id)))
		else:
			print "couldn't save form in rateActivityFormView"
			# DO SOMETHING HERE .. WE HAVE AN ERROR SAVING THE FORM
			# probably a duplication/uniqueness error
			return HttpResponseRedirect(reverse("home"))
	else:
		form = RateActivityInstanceForm(instance=rI)
		return render(request, "form.html", {"form": form})

def rateActivityInstanceDetailView(request, a_id, r_id, aI_id, rI_id):
	return HttpResponseRedirect(reverse('activityInstance_detail', args=[a_id, aI_id]))


