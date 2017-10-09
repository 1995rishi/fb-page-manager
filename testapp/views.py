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
			
	print(d)
	header='OAuth ' + pageToken
	url="https://graph.facebook.com/"+pageId
	details=call('POST', url,data=d, headers={"Authorization": header})
	return HttpResponse(json.dumps(details.json()))

