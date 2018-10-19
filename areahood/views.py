from django.shortcuts import render,redirect
from .models import Profile,Post,Neighbourhood
from django.contrib.auth import authenticate,login
from .forms import ProfileForm
from django.http import HttpResponse
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template.loader import render_to_string
# from .tokens import account_activation_token
# from django.contrib.auth.models import User
# from django.core.mail import EmailMessage
# import datetime as dt
# from django.contrib.auth.decorators import login_required

#profile views
def create_profile_view(request):
    current_user = request.user
    profile = Profile.objects.filter(user=request.user)
    post = Post.objects.filter(user=current_user)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=current_user.profile) 
        if form.is_valid():
           form.save()
    else:        
        form =ProfileForm() 
    return render(request,'profile/profile.html',{"form":form,"profile":profile,"post":post})

