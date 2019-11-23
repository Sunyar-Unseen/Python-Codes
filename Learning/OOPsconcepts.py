class User():
    def __init__(self,firstn,lastn):
        self.firstn = firstn
        self.lastn = lastn
       

yaten_user =User("Yatendra", "Singh")
shiv_user = User("Shivam","Gupta")

print(yaten_user.firstn,shiv_user.firstn)

  #  def set_name():
    
   # def get_name():

class YTUser():
    def __init__(self,fn,ln,product):
        self.first_name = fn
        self.last_name = ln
        g_product = product

g_user = YTUser("Gandharva","Singh","YouTube")
d_user = YTUser("Dexter","Gupta","Youtube")

print(g_user.first_name,d_user.first_name)

class sum_two():
    def __init__(self,a,b):
        self.a =a
        self.b =b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b



x = sum_two(40,50)

print(x.add())
print(x.sub())
print(x.mul())
print(x.div())

class GoogleUser():
    def __init__(self,username,password,dob):
        self.username = username
        self.password = password
        self.dob = dob
class YTUser(GoogleUser):
    def __init__(self,username,password,dob,fav_genere):
        super().__init__(username,password,dob)
        self.fav_genere = fav_genere

a_user = GoogleUser("Yaten","F***","01/01/2000") 

yt_user = YTUser("FN","LN","01/01/2001",["Music","Cartoon"])

print(yt_user.dob,yt_user.fav_genere)