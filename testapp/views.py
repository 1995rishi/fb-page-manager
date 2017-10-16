from django.shortcuts import render
from requests import request as call
from django.http import HttpResponse
import json

# Create your views here.
def homepage(request):
	return render(request, "home.html",{})

def pages(request):
	token=request.POST.get("token",'')
	header="OAuth "+ token
	details=call('GET', 'https://graph.facebook.com/me/accounts', headers={"Authorization": header})
	d2=call('GET','https://graph.facebook.com/me', headers={"Authorization":header})
	details=json.dumps(details.json())
	d2=json.dumps(d2.json())
	# print(details)
	return render(request, "pages.html",{'pages': details, 'personal':d2})


def getPageDetails(request):
	if request.method=='POST':
		fields='category,name,phone,general_info,about,bio,location,emails,website,description,company_overview'
		pageToken=request.POST.get("pageToken",'')
		pageId=request.POST.get("pageId",'')
		header='OAuth ' + pageToken
		url="https://graph.facebook.com/"+pageId + "?fields="+fields
		details=call('GET', url, headers={"Authorization": header})
		details=json.dumps(details.json())
		return HttpResponse(details)
	return HttpResponse(400)

def updatePageDetails(request):
	d={}
	pageToken=request.POST.get("access_token",'')
	pageId=request.POST.get("pageId",'')
	d1={}
	d['access_token']=pageToken
	if request.POST.get("phone") is not None:
		d['phone']=request.POST.get("phone",'')
	if request.POST.get("emails") is not None:
		d['emails']=request.POST.get("emails",'')
	if request.POST.get("general_info") is not None:
		d['general_info']=request.POST.get("general_info",'')
	if request.POST.get("about") is not None:
		d['about']=request.POST.get("about",'')
	if request.POST.get("bio") is not None:
		d['bio']=request.POST.get("bio",'')
	if request.POST.get("website") is not None:
		d['website']=request.POST.get("website",'')
	if request.POST.get("description") is not None:
		d['description']=request.POST.get("description",'')
	if request.POST.get("company_overview") is not None:
		d['company_overview']=request.POST.get("company_overview",'')
	if request.POST.get("lname") is not None:
		d1['name']=request.POST.get("lname")
	if request.POST.get("city") is not None:
		d1['city']=request.POST.get("city")
	if request.POST.get("state") is not None:
		d1['state']=request.POST.get("state")
	if request.POST.get("country") is not None:
		d1['country']=request.POST.get("country")
	if request.POST.get("street") is not None:
		d1['street']=request.POST.get("street")
	if request.POST.get("zip") is not None:
		d1['zip']=request.POST.get("zip")
			
	# d['location']=d1
	print(d)
	header='OAuth ' + pageToken
	url="https://graph.facebook.com/"+pageId
	urll=url+"/location"
	details1=call('POST', url, data=d1, headers={"Authorization":header})
	details=call('POST', url,data=d, headers={"Authorization": header})
	return HttpResponse(json.dumps(details.json()))

