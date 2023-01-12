from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse

from mainApp.models import *
from .forms import *
import datetime
import json
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from collections import Counter
import hashlib

from django.contrib.auth.decorators import user_passes_test
from django.core import serializers

from django.db import connection






def index(request):

    # flyerList = Flyer.objects.filter(Event_date__gte = datetime.date.today()
    #                                 ).filter(Event_date__lte = datetime.date.today()+ datetime.timedelta(days=6))
    
    # Flyer_Image.objects.get(id=444).delete()

    # flyerList = Event.objects.all().order_by('-Posistion')
    flyerList = Event.objects.all()

    # moreInfo_data = json.dumps(list(Flyer.objects.all().values()),default=str)
    


    # flyerList = Flyer.objects.filter(Boro='brooklyn').order_by('-Posistion')
    # print(serializers.serialize('json', flyerList))
    return render(request, 'mainApp/index.html', {'flyerList':flyerList}) # ,'moreInfo_data':moreInfo_data

def index2(request):
    
    flyerList = Flyer.objects.filter(Event_date__gte = datetime.date.today()
                                    ).filter(Event_date__lte = datetime.date.today()+ datetime.timedelta(days=6))
    
    return render(request, 'mainApp/index2.html', {'flyerList':flyerList})

# class FlyerCreateView(CreateView):
#     model = Flyer
#     form_class = FlyerForm



def watchList(request):

    if request.method == "GET":

        flyer_ids = []
        reminders = Reminder.objects.filter(User_email = request.GET.get('useremail', ''))

        for flyer in reminders:
            flyer_ids.append(flyer.Flyer.pk)

        return JsonResponse({"flyers": flyer_ids}, status=200)

    if request.method == "POST":

        postData = json.loads(request.body)
        email, id, func  = postData["email"], postData["id"], postData["func"]
        flyer = get_object_or_404(Flyer, pk = id)

        if postData["func"] == 'add':

            new_watched_flyer = Reminder(User_email = postData["email"], Flyer = flyer)
            new_watched_flyer.save()
            return HttpResponse('200')
        
        elif postData["func"] == 'del':

            watched_flyer = Reminder.objects.filter(User_email=email).filter(Flyer=flyer)
            watched_flyer.delete()
            return HttpResponse('200')
        
        else:
            return HttpResponse('ERROR')



def uploadImage(request):
    return render(request, 'mainApp/uploadImage.html')


def saveImage(request):
    
    # print (request.POST['imageInput'])
    form = Flyer_ImageForm(request.POST, request.FILES)
    # clearMessages(request)
    # print(form.errors)
    if form.is_valid():
        
        print("okkkkkkkkk")
        newImg = form.save()

        #create md5
        with open(f'media/{newImg.Flyer_image}', 'rb') as saved_image_file:
            f = saved_image_file.read()
            new_md5 = hashlib.md5(f).hexdigest()
            newImg.Hash = new_md5
            newImg.save()
        # print(newImg.pk)

        return redirect('newFlyerFormMobile', imgPk = newImg.pk)
    return HttpResponse(str(form.errors()))



def newFlyerFormMobile(request, imgPk):
    return render(request, 'mainApp/newFlyerFormMobile.html',{'imgPk':imgPk})

def saveFlyerMobile(request):

    # try:
    
    p = request.POST.dict()
    new_img = Flyer_Image.objects.get(pk=p['Flyer_image'])

    print('s'+p['Date'])

    newFlyer = Flyer(Flyer_image=new_img, Boro=p["Boro"], Event_type=p['Event_type'], Description=p['Description'],
                            Contact_information=p['Contact_information'], Address=p['Address'])

    newFlyer.full_clean()
    newFlyer.save()


    dates = json.loads(p['Date'])
    days_of_week = json.loads(p['Day_of_week'])

    for i, date in enumerate(dates):

        newEvent = Event(Date = date, Day_of_week =days_of_week[i], Flyer = newFlyer)

        newEvent.full_clean()
        newEvent.save()

    messages.add_message(request, messages.ERROR, 'Successfully Posted')
    return redirect('index')

    # except:
    messages.add_message(request, messages.ERROR, 'There was an error, please try again.')
    return redirect('uploadImage')

#SAVE DESKTOP
def saveFlyerDesktop(request):
    # clearMessages()
    # print(00)
    # print(request.POST)
    # print(request.FILES)

    imageForm = Flyer_ImageForm(request.POST, request.FILES)
    for field in imageForm:
        # print(field)
        for error in field.errors:
             print(error)
    if imageForm.is_valid():
        newImg = imageForm.save()
        # print(1)

#create md5
        with open(f'media/{newImg.Flyer_image}', 'rb') as saved_image_file:
            f = saved_image_file.read()
            new_md5 = hashlib.md5(f).hexdigest()
            newImg.Hash = new_md5
            newImg.save()

        p = request.POST.dict()

        #formatting time
        # formatted_date = datetime.datetime.strptime(p['Event_date'], "%m/%d/%Y").strftime("%Y-%m-%d")

        #removing 'https' and replacing with 'http'
        # formatted_contact_info = 

        newFlyer = Flyer(Flyer_image=newImg, Boro=p["Boro"], Event_type=p['Event_type'], Description=p['Description'],
                            Contact_information=p['Contact_information'], Address=p['Address'])
        # print(f'img:{newImg}')
        # print(p)
        #REMEMBER TO CLEAN DATA!!!!!
        # try:
        newFlyer.full_clean()
        newFlyer.save()

        # Create and save Event object

        dates = json.loads(p['Date'])
        days_of_week = json.loads(p['Day_of_week'])

        for i, date in enumerate(dates):

            newEvent = Event(Date = date, Day_of_week =days_of_week[i], Flyer = newFlyer)

            newEvent.full_clean()
            newEvent.save()
        

        messages.add_message(request, messages.ERROR, 'Successfully Posted')
        return redirect('index')
        # except Exception as e:
        #     print (e)
        # except:
        # except ValidationError as e:
        #     print(e.message_dict)
            # messages.add_message(request, messages.ERROR, 'There was an error, please try again.')
            # return redirect('uploadImage')
    messages.add_message(request, messages.ERROR, 'There was an error, please try again.')
    return redirect('uploadImage')

def test(request):
    # form = FlyerForm()
    # return render(request, 'mainApp/test.html',{'form':form})

    # flyerList = list(Reminder.objects.all().values())
    # flyerList=list(Flyer.objects.filter(event__isnull=True).values())

    # flyerList=list(Flyer_Image.objects.filter(Flyer__event__isnull=False).values())

    #get all flyer_imgs that dont have any events
    # flyerList=list(Flyer_Image.objects.filter(flyer__event__isnull=True).values())

    # flyerList = list(Event.objects.all().values('Flyer'))


    # print(flyerList.query)
    # return JsonResponse(flyerList,safe=False);

    # Flyer_Image.objects.all().delete()

    flyerList = Event.objects.all()
    # flyerList = Flyer.objects.filter(Boro='brooklyn').order_by('-Posistion')
    # print(serializers.serialize('json', flyerList))
    return render(request, 'mainApp/x.html', {'flyerList':flyerList})

    return render(request, 'mainApp/e.html')

    # with connection.cursor() as cursor:

    #     cursor.execute("SELECT mainApp_event.Day_of_week, mainApp_event.Flyer_id, mainApp_flyer.Address  "
    #                     "FROM mainApp_event INNER JOIN mainApp_flyer ON mainApp_event.Flyer_id=mainApp_flyer.Flyer_image_id;")
    #     row = cursor.fetchall()

    # return JsonResponse(row,safe=False);

# def clearMessages(request):
#     storage = messages.get_messages(request)
#     for _ in storage:
#         # This is important
#         # Without this loop `_loaded_messages` is empty
#         pass
#     for _ in list(storage._loaded_messages):
#         del storage._loaded_messages[0]

def data(request):
    # users = list(Reminder.objects.values("User_email").distinct().values("Flyer__Boro"))
    # q = list(Reminder.objects.values("User_email", brkln=Count("Flyer__Boro")))
    # r = list(Reminder.objects.raw('select * from mainApp_reminder').values())
    d = list(Reminder.objects.values("User_email", "Flyer__Boro", "Flyer__Event_type"))
    
    # c = count(d)
    u = Reminder.objects.all()
    # c = Counter([d])
    # print(u)
    # out = {"email": "null", "brooklyn":0, "manhttn":0, "comedy":0, "food":0}
    output ={}
    for e in u:
        if e.User_email not in output:
            output[e.User_email]={'Boro':[], 'Event_type':[]}
        output[e.User_email]['Boro'].append(e.Flyer.Boro)
        output[e.User_email]['Event_type'].append(e.Flyer.Event_type)
        # print(e.Flyer.Boro)

    for key, value in output.items():

        value['Boro']= Counter(value['Boro'])
        value['Event_type']= Counter(value['Event_type'])
        # print(value['Boro'])
    # print(output)
    j = json.dumps(output)
        # print(e.User_email)
    # print(output)
    # return JsonResponse(u, safe=False)
    # return HttpResponse(data, content_type='application/json')
    return HttpResponse(j)

def promote(request):
    return render(request, 'mainApp/promotionPage.html')

def about(request):
    return render(request, 'mainApp/about.html')

@user_passes_test(lambda u: u.is_superuser)
def uploadMultiple(request):
    
    return render(request, 'mainApp/uploadMultiple.html')

def saveMultiple(request):

    p = json.loads(request.body)
    
    for obj in p['new_flyers_data']:
         
        #create new img object
        new_img = Flyer_Image(Img_src_url = obj['Img_src_url'], Orientation= obj['Orientation'])

        new_img.full_clean()
        new_img.save()

        

        #create ne flyer object
        new_flyer = Flyer( Boro = obj['Boro'], Address= obj['Address'], 
                            Event_type= obj['Event_type'], Contact_information= obj['Contact_information'],
                            Description= obj['Description'], Posted_by_me= obj['Posted_by_me'],
                            Lattitude= obj['lattitude'], Longitude= obj['longitude'],
                            Flyer_image= new_img )

        new_flyer.full_clean()
        new_flyer.save()


        #create new event object
        new_event = Event(Date= obj['Date'], Day_of_week= obj['Day_of_week'],
                            Flyer= new_flyer)

        new_event.full_clean()
        new_event.save()
    
    return HttpResponse('okll')
    