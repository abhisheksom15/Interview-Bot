from django.shortcuts import render,get_object_or_404,get_list_or_404
from Front.forms import UserForm,UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from Front.models import UserProfileInfo,User,questions,result_user,company_post,company_marks
from gtts import gTTS
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

import random
# Create your views here.
def welcome(request):
    cp=company_post.objects.all()
    return render(request,'welcome.html',{'cp':cp})
def score(request,pk_cp):
    cp=get_object_or_404(company_post,pk=pk_cp)
    try:
        cm=list(company_marks.objects.filter(Company_name=cp,cm_position=cp.Position))
        return render(request,'score.html',{'cm':cm,'company':cp})
    except company_marks.DoesNotExist:
        HttpResponse("No User give the interview till now!")
@login_required
def description(request,pk):
    comp=get_object_or_404(company_post,pk=pk)
    return render(request,'description.html',{'company':comp})
@login_required
def complete(request,pk):
    ru=get_object_or_404(result_user,pk=pk)
    mark=ru.marks
    if(int(mark)>=75):
        s="Congratulation, You passed the Technical round and soon your HR round will be conducted"
    else:
        s="Sorry, Your score is below the passing marks, better luck next time"
    return render(request,'done.html',{'marks':mark,'s':s})
def register(request):

    registered=False

    if(request.method=="POST"):
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if(user_form.is_valid() and profile_form.is_valid()):
            user=user_form.save(commit=False)
            try:
                validate_password(user.password, user)
            except ValidationError as e:
                user_form.add_error('password', e)
                return render(request,'Registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered,"Warning":"Password not strong"})
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user

            if('profile_pic' in request.FILES):
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()

            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,'Registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('welcome'))

@login_required
def special(request):
    HttpResponse('you are logged in !! nice')


@login_required
def Interview(request,pk,comp_pk,count=0):
    company=get_object_or_404(company_post,pk=comp_pk)
    exam_diff=company.Difficulty_level
    max_diff=exam_diff+10
    min_diff=exam_diff-5
    user=get_object_or_404(User,pk=pk)

    extras=["in","is","am","i","not","did","of","where","what","are","here","there","the","it","it's","its","you","yours","me","my","to","this","they","there","then","than"]


    user_profile_info=get_object_or_404(UserProfileInfo,user=user)
    tech=user_profile_info.technical_skills_and_language
    hr=["HR","GK",user_profile_info.Main_Hobbies,user_profile_info.Other_Hobbies]
    TECH=[user_profile_info.technical_skills_and_language,user_profile_info.Other_skills,"Concept"]
    fscore=[]
    questions1=[]
    answer1=[]
    score1=[]
    c=0
    for cat in TECH:
        if(get_list_or_404(questions,Question_Type="TECHNICAL",Category=cat)):
            questions_tech=get_list_or_404(questions,Question_Type="TECHNICAL",Category=cat)
            for quest in questions_tech:
                if(quest.Difficulty_level>=min_diff and quest.Difficulty_level<=max_diff):
                    questions1.append(quest.Question)
                    answer1.append(quest.Answer)
                    score1.append(quest.Difficulty_level)
    if(count==0):
        random_questions_total=random.randint(15,50)
        r_list=[]
        for i in range(random_questions_total):
            r_list.append(random.randrange(len(questions1)))
        r_list=list(set(r_list))
        r_string=""
        for val in r_list:
            r_string+=(str(val)+' ')
        try:
            p= result_user.objects.get(user_result=user)
            p.marks=''
            p.quest_list=r_string
            p.save()
        except result_user.DoesNotExist:
            p=result_user(user_result=user,marks=0,exam_name="TEST",quest_list=r_string)
            p.save()
        try:
            checking_test_company= company_marks.objects.get(Company_name=company,cm_position=company.Position,user_name=p)
            return HttpResponse("You have already given the Interview for this post ! ")
        except company_marks.DoesNotExist:
            true=True
    m_r=get_object_or_404(result_user,user_result=user)
    list_quest_num=m_r.quest_list.split()
    questions2=[]
    answer2=[]
    score2=[]
    for var in list_quest_num:
        i=int(var)
        questions2.append(questions1[i])
        answer2.append(answer1[i])
        score2.append(score1[i])
    questions1=questions2
    answer1=answer2
    score1=score2
    print(questions1)
    if(request.method=='POST'):
        answer_input=request.POST.get('answer')
        ans=answer1[count-1]
        ans=ans.lower()
        ans_match_list=ans.split()
        answer_input=answer_input.lower()
        answer_list=answer_input.split()
        for word in extras:
            if word in answer_list:
                answer_list.remove(word)
            if word in ans_match_list:
                ans_match_list.remove(word)
        l=len(ans_match_list)
        c_ans=0
        l_input=len(answer_list)

        for word in ans_match_list:
            for i in range(l_input):
                if(word==answer_list[i]):
                    c_ans+=1
        if(l==1 or l==2):
            req_ans=1
        elif(l<=5):
            req_ans=l-1
        elif(l<=10):
            req_ans=l//2
        elif(l<=20):
            req_ans=l//3
        else:
            req_ans=l//3
        if(req_ans<=c_ans):
            score_question=score1[count-2]
        elif(req_ans>=2 and (req_ans//4)<=c_ans):
            score_question=int((c_ans/req_ans)*score1[count-2])
        else:
            score_question=0

        m_r.marks+=(' '+str(count-1)+','+str(score_question))
        m_r.save(update_fields=['marks'])
    maxc=len(questions1)
    if(count==maxc):
        marks_list=m_r.marks.split(' ')
        marks_list_score=[0 for x in range(len(score1))]
        for i in range(1,len(marks_list)):
            marks_item=marks_list[i].split(',')
            print(marks_list)
            print(marks_item)
            marks_list_score[int(marks_item[0])]=int(marks_item[1])
        m_r.marks=str(int((sum(marks_list_score)/sum(score1))*100))
        m_r.save()
        company_marks_stored=company_marks(user_name=m_r,Company_name=company,cm_marks=int(m_r.marks),cm_position=company.Position)
        company_marks_stored.save()
        return HttpResponseRedirect(reverse('complete',args=(m_r.pk,)))
    else:
        count+=1
        ques_audio=gTTS(questions1[count-1])
        file_loc='static/'+str(count-1)+'.mp3'
        file_name=str(count-1)+'.mp3'
        ques_audio.save(file_loc)
        return render(request,'Interview.html',{'questions1':questions1[count-1],'c':count,'file_name':file_name,'company':company})

def user_login(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if(user):
            if(user.is_active):
                login(request,user)
                user_test=user
                return HttpResponseRedirect(reverse('welcome'))
            else:
                return HttpResponse("ACCOUNT IS NOT ACTIVE")
        else:
            print("someone tried to access account unauthenically and failed")
            print("Username {} and password {}".format(username,password))
            return HttpResponse("invalid login details")
    else:
        return render(request,'Login.html',{})
