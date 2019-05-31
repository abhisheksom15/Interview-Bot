from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)

    phone_number=models.IntegerField()

    date_of_birth=models.CharField(max_length=15)

    Address=models.CharField(max_length=200)

    school_10th=models.CharField(max_length=100)

    percentage_10th=models.IntegerField()

    school_12th=models.CharField(max_length=100)

    percentage_12th=models.IntegerField()
    Btech='B.tech'
    Bsc='B.sc'
    BCA='BCA'
    MCA='MCA'
    BBA='BBA'
    BE='B.E'
    NONE='None'
    CSE='Computer science'
    IT='Information technology'
    CE='Computer engineering'
    MATH='Mathematics'
    ML='Machine learning'
    ECE='Electronics and communication'

    grad_choices=((Btech,'B.tech'),(Bsc,'B.sc'),(BCA,'BCA'),(MCA,'MCA'),(BBA,'BBA'),(BE,'B.E'),(NONE,'None'))
    graduation=models.CharField(choices=grad_choices,max_length=7)

    branch_choices=((CSE,'Computer science'),(IT,'Information technology'),(CE,'Computer engineering'),(MATH,'Mathematics'),(ML,'Machine learning'),(ECE,'Electronics and communication'),(NONE,'None'))
    branch_graduation=models.CharField(choices=branch_choices,max_length=30)
    Cplusplus='C++'
    C='C'
    JAVA='JAVA'
    Csharp='C#'
    NET='.NET'
    PYTHON='PYTHON'
    JS='JavaScript'
    HTML='HTML'
    CSS='CSS'
    DBMS='Database'
    NETWORK='Networking'
    CLOUD='Cloud'
    AND='Android'
    AI='AI'
    DATASCIENCE='Data science'

    technical_choices=((Cplusplus,'C++'),(C,'C'),(JAVA,'JAVA'),(Csharp,'C#'),(NET,'.NET'),(PYTHON,'PYTHON'),(JS,'JavaScript'),(HTML,'HTML'),(CSS,'CSS'),(DBMS,'Database'),(NETWORK,'Networking'),(CLOUD,'Cloud'),(AND,'Android'),(ML,'ML'),(AI,'AI'),(DATASCIENCE,'Data science'))

    technical_skills_and_language=models.CharField(choices=technical_choices,max_length=15)

    Other_skills=models.CharField(choices=technical_choices,blank=True,max_length=15)
    Reading_books='Reading books'
    reading_novels='reading novels'
    Cooking='Cooking'
    Movies='Watching Movies'
    Badminton='Playing Badminton'
    Cricket='Playing Cricket'
    Football='Playing football'
    basketball='Playing basketball'
    Chess='Playing Chess'
    GYM='Going Gym'
    Music='listening Music'
    Dance='Dancing'

    hob_choices=((Reading_books,'Reading books'),(reading_novels,'reading novels'),(Cooking,'Cooking'),(Movies,'Watching Movies'),(Badminton,'Playing Badminton'),(Cricket,'Playing Cricket'),(Football,'Playing football'),(basketball,'Playing basketball'),(Chess,'Playing Chess'),(GYM,'Going Gym'),(Music,'listening Music'),(Dance,'Dancing'))
    Main_Hobbies=models.CharField(choices=hob_choices,max_length=25)

    Other_Hobbies=models.CharField(choices=hob_choices ,blank=True,max_length=25)

    achievement=models.CharField(max_length=100,blank=True)

    Project_Done=models.CharField(max_length=100,blank=True)

    profile_picture=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
class questions(models.Model):
    Reading_books='Reading books'
    reading_novels='reading novels'
    Cooking='Cooking'
    Movies='Watching Movies'
    Badminton='Playing Badminton'
    Cricket='Playing Cricket'
    Football='Playing football'
    basketball='Playing basketball'
    Chess='Playing Chess'
    GYM='Going Gym'
    Music='listening Music'
    Dance='Dancing'
    Cplusplus='C++'
    C='C'
    JAVA='JAVA'
    Csharp='C#'
    NET='.NET'
    PYTHON='PYTHON'
    JS='JavaScript'
    HTML='HTML'
    CSS='CSS'
    DBMS='Database'
    NETWORK='Networking'
    CLOUD='Cloud'
    AND='Android'
    AI='AI'
    DATASCIENCE='Data science'
    ML='Machine learning'

    HR='HR'
    TECHNICAL='TECHNICAL'
    QUESTION_TYPE=((HR,'HR'),(TECHNICAL,'TECHNICAL'))
    Question_Type=models.CharField(choices=QUESTION_TYPE,max_length=10)
    GK='GK'
    Concept="Concept"
    cat_choice=((Concept,"Concept"),(HR,'HR'),(TECHNICAL,'TECHNICAL'),(GK,'GK'),(Reading_books,'Reading books'),(reading_novels,'reading novels'),(Cooking,'Cooking'),(Movies,'Watching Movies'),(Badminton,'Playing Badminton'),(Cricket,'Playing Cricket'),(Football,'Playing football'),(basketball,'Playing basketball'),(Chess,'Playing Chess'),(GYM,'Going Gym'),(Music,'listening Music'),(Dance,'Dancing'),(Cplusplus,'C++'),(C,'C'),(JAVA,'JAVA'),(Csharp,'C#'),(NET,'.NET'),(PYTHON,'PYTHON'),(JS,'JavaScript'),(HTML,'HTML'),(CSS,'CSS'),(DBMS,'Database'),(NETWORK,'Networking'),(CLOUD,'Cloud'),(AND,'Android'),(ML,'ML'),(AI,'AI'),(DATASCIENCE,'Data science'))
    Category=models.CharField(choices=cat_choice,max_length=50)
    Difficulty_level=models.PositiveSmallIntegerField()
    Question=models.CharField(max_length=256)
    Answer=models.CharField(max_length=512)

    def __str__(self):
        return self.Question
class result_user(models.Model):
    user_result=models.OneToOneField(User,on_delete=models.CASCADE)
    marks=models.CharField(max_length=2048)
    date_of_exam= models.DateTimeField(auto_now_add=True)
    quest_list=models.CharField(max_length=2048,default="")
    exam_name=models.CharField(max_length=256)
    def __str__(self):
         return self.user_result.username
class company_post(models.Model):
    Company_name=models.CharField(max_length=256)
    Position=models.CharField(max_length=256)
    Difficulty_level=models.PositiveIntegerField()
    salary_in_rupees=models.PositiveIntegerField()
    min_experience_in_years=models.PositiveIntegerField()
    Discreption=models.CharField(max_length=512)
    def __str__(self):
        return self.Company_name
class company_marks(models.Model):
    user_name=models.ForeignKey(result_user,on_delete=models.CASCADE)
    Company_name=models.ForeignKey(company_post,on_delete=models.CASCADE)
    cm_marks=models.PositiveSmallIntegerField()
    cm_position=models.CharField(max_length=256)
    def __str__(self):
        return self.user_name.user_result.username
