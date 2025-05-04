import datetime
import re
import hashlib
import os
import bcrypt 
#Warning!! download it first
class Person:
  person_id=None#it will be added by either using a random generator or using SERIAL or AUTO_INCREMENT in db
  fname='john'
  lname='doe'
  email='johndoe@example.com'
  password='secret hashed password'
  phone_num= '2041889'
  birthdate=datetime.datetime.strptime('1889-4-20', "%Y-%m-%d")#Hail hitler
  age=0 
  
  def  __init__(self,person_id,fname,lname,password,phone_num,birthdate,age,email):
      fname_check,fname_msg= self.check_name(fname)
      lname_check,lname_msg=self.check_name(lname)
      email_check,email_msg= self.check_email(email)
      phone_num_check,phone_msg =self.check_phone_num(phone_num)
      birthdate_check,birthdate_msg= self.check_birthdate(birthdate)
      age_check,age_msg=self.check_age(age,birthdate)
      #I'm supposed to check that id won't be repeated in the db then I will add it either using SERIAL or a customized id but, for now I will add it as it is.
      self.person_id=person_id
      if fname_check:
        #add to database here
        self.fname= fname
        
      else:
        raise ValueError(fname_msg)
        #print(fname_msg)
        
      if lname_check:
        #add to database here
        self.lname=lname
        
      else:
        raise ValueError(lname_msg)
        #print(lname_msg)
        
      
          
      if phone_num_check:
    
        #add to database here
          self.phone_num= phone_num
          
      else:
        raise ValueError(phone_msg)
          #print(phone_msg)
          
      if birthdate_check:
    
        #add to database here
          self.birthdate=birthdate
          
      else:
        raise ValueError(birthdate_msg)
        #print(birthdate_msg)
      if email_check:
        self.email=email
        #add to database
      else:
        raise ValueError(email_msg)
        #print(email_msg)
      pass_check,pass_msg=self.check_password(password,fname,lname,email,birthdate)
      if pass_check:
        #hash the password using pepper and salt
        #I will add the password temporary as a plain text
         self.password=password
        #add to database here
          
      else:
          raise ValueError(pass_msg)
          #print(pass_msg)
      
      if age_check:
    
        #add to database here
            self.age=age
      else:
            raise ValueError(age_msg)
            #print(age_msg)
          
        
        
        
  def calculate_age(self,birthdate):
    today = datetime.datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day)) #newer version
    #return datetime.datetime.today().year-self.birthdate.year #my old version
  
  def check_age(self,age,birthdate):
    if type(age) != int:
      return False, f'Enter an integer.{age} is not allowed'
    if age <-1 or age >100 or type(age) != int:
      return False, f'Enter a reasonable number. its impossible to be {age} years old '
    elif age <8:
      return False, f'too young to join my app. wait  {8-age} years to be able to register!'
    elif(age != self.calculate_age(birthdate)):
      return False,'inconsistent date and age!!'
    else:
      return True, f'Welcome to my app, you are {age} years old, have fun!!'
    
  def check_name(self,name):
    if re.fullmatch(r'[a-zA-Z]+',name) and 3<=len(name)<=20:
      return True,'valid name'
    else:
      return False, 'Invalid name. Please enter name of length between 3 and 20 and avoid using symbols and numbers'
    
  def check_password(self,password,fname,lname,birthdate,email):
    if re.fullmatch(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$',password) and fname.lower() not in password.lower() and lname.lower() not in password.lower() and f'{birthdate.year}' not in password and email.lower() not in password.lower():
      return True, 'valid password'
    else:
      return False, "Password should not include your name, email, or birth year and it should contain at least one lower case character, one upper case character, one symbol and one number." 
  def check_phone_num(self,phone_num):
    if len(phone_num) == 11 and phone_num.startswith("01") and re.fullmatch(r'\d{11}',phone_num):
      return True,'valid phone number'
    else:
      return False, "invalid phone number"
    
    
  def check_birthdate(self,birthdate):
    if birthdate > datetime.datetime.today():
     return False, 'Invalid: birthdate in the future.'
    elif (datetime.datetime.today().year - birthdate.year) > 100:
     return False, 'Too old to register!'

    else:
      return True ,'Valid date'
    
  def check_email(self,email):
    if re.fullmatch(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',email):
      return True,'valid email'
    else:
      return False, 'Invalid email!!'


class User(Person):
  joined_groups=None
  assigned_therapistID=None
  lowest_mode_streak=5
  
  
  def  __init__(self,person_id,fname,lname,password,phone_num,birthdate,age,email,joined_groups=[],assigned_therapistID=None,lowest_mode_streak=5):
      super().__init__(person_id,fname,lname,password,phone_num,birthdate,age,email)
      jgs_check,jgs_msg= self.check_joined_groups(joined_groups)
      atID_check,atID_msg=self.check_assigned_therapistID(assigned_therapistID)
      lms_check,lms_msg=self.check_lowest_mode_streak(lowest_mode_streak)
      if jgs_check:
        self.joined_groups= joined_groups
      else:
        raise ValueError(jgs_msg)
      
      if atID_check:
        self.assigned_therapistID=assigned_therapistID
      else:
        raise ValueError(atID_msg)
      
      if lms_check:
      
        self.lowest_mode_streak=lowest_mode_streak
      else:
        raise ValueError(lms_msg)
  def check_joined_groups(self,groups):
          return True,"valid groups"
          #we need db manager before implementing this method
  def check_assigned_therapistID(self,assigned_therapistID):
        if assigned_therapistID==None:
          return True, "Therabist not set yet"
        return True, "valid therapist id"#we need db manager before implementing this method
  def check_lowest_mode_streak(self,lowest_mode_streak):
        if not isinstance(lowest_mode_streak, int):
              return False, "Lowest mode streak must be an integer"
        if lowest_mode_streak < 3 or lowest_mode_streak >365:
              return False, "Lowest mode streak must be at least 3 and less than or equal 365"
        return True, "Valid lowest mode streak"
class Therapist:
  pass
pepper='Itz4just3a2pepper'#It will be stored in env file for security purposes
class Security_algorithms:
  """in this class we will add encryption, hashing and other algorithms that will be used in the security of the project"""
  
  @staticmethod
  #sha265
  def hash_using_sha265(self,string):
    return hashlib.sha256(string.encode())
  
  #sha265 but in hexa decimal format
  @staticmethod
  def hash_using_sha265_HexV(self,string):
    return hashlib.sha256(string.encode()).hexdigest()
  #sha512
  @staticmethod
  def hash_using_sha512(self,string):
    return hashlib.sha512(string.encode())
  #sha512 but in hexadecimal format
  @staticmethod
  def hash_using_sha512_HexV(self,string):
    return hashlib.sha512(string.encode()).hexdigest()
  
  @staticmethod
  def hash_using_sha265_salt(string,salt=None):
    if not salt:
      salt = os.urandom(16)#I used it to generate 16 byte long salt
      pass_salt = salt + string.encode('utf-8')
    hashed = hashlib.sha256(pass_salt).hexdigest()
    return salt, hashed
    #return hashlib.sha256(string.encode()).hexdigest()
  @staticmethod
  def verify_pass_using_sha256(password,salt,hashed):
    #hashed is the password in the db
    #salt is the salt that was used in hashing the password
    #password is the password that we want to verify
    return True if hashlib.sha256(salt+password.encode('utf-8')).hexdigest() == hashed else False
    
    
  #methods using bcrypt
  @staticmethod
  def hash_password_with_salt(password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    #generate salt and deal with it internally which make it more advanced than hashlib
    return hashed
  @staticmethod
  def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)#it will verify it
  
  @staticmethod
  def hash_password_with_pepper(password):
    peppered = (password + pepper).encode('utf-8')
    hashed = bcrypt.hashpw(peppered, bcrypt.gensalt())
    return hashed
  
  @staticmethod
  def verify_password_with_pepper(password, hashed):
    peppered = (password + pepper).encode('utf-8')
    return bcrypt.checkpw(peppered, hashed)

  
#print(bcrypt.hashpw('hello'.encode('utf-8'), bcrypt.gensalt()))