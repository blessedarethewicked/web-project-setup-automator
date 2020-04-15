import os
import shlex, subprocess
import shutil

full_auto_mode = True

print('what is the name of the Web project:')
# user inputs the name
project_name = input()
#make a new directory with the name that 
#the user picked
try:
	os.mkdir(project_name)
except:
	print('error:')
	print('you didnt type anyhing or ')
	print('you have already got a project with that name')
	print('please  try another name')
	exit()
#get the current workiing directory
working_dir = os.getcwd()
#make the path of a new directory
working_dir_name = working_dir.replace('\\auto web setup','')
#move out of the working directory 
os.chdir(working_dir_name)
current_working_dir = os.getcwd()
print(current_working_dir)
#make the project directory 
os.mkdir(project_name)
project_dir = current_working_dir + '\\' +  project_name
#move to the new directory
os.chdir(project_dir)

# check that pip is working 
subprocess.run("pip --version")

#try and install a virtualenv
try:
	subprocess.run("pip install virtualenv")
	print('>>>> pip install virtualenv')
except:
	print('failed to install virtualenv')
#try and set up the env folder	
try:
	subprocess.run("virtualenv env")
	print('>>>> virtualenv env')
except:
	print('failed to set up the env folder')
#try and activate the env
try:
	os.system("env\\Scripts\\activate")
	print(">>>> env\Scripts\activate")
except:
	full_auto_mode = False
	print('failed to activate the env \n')
	print('full auto mode is now off')
	
#try annd install flask 
try:
	subprocess.run("pip install flask flask-sqlalchemy")
	print('>>>> pip install flask flask-sqlalchemy')
except:
	print('failed to install flask flask-sqlalchemy ')

	

	
# make copies first
#copy the static folder
original_static = working_dir +"\\static"
target_static = working_dir +"\\temp\\static"
shutil.copytree(original_static, target_static)
print('>>>> copy the static folder')

#copy the templates folder
original_templates = working_dir +"\\templates"
target_templates = working_dir +"\\temp\\templates"
shutil.copytree(original_templates, target_templates)
print('>>>> copy the templates folder')

 
#copy the app.py file
original_app = working_dir + "\\app.py"
target_app = working_dir +"\\temp"
shutil.copy(original_app, target_app)
print('>>>> copy the app.py file')


#move the copies 	
#the destination folder
destination = project_dir
#the source folder for the static folder
static_source = target_static #working_dir +"\\temp\\static"
#copy command
dest = shutil.move(static_source, destination, copy_function = shutil.copytree)
#the source folder for the templates folder
templates_source = target_templates #working_dir +"\\temp\\templates"
#copy command
dest = shutil.move(templates_source, destination, copy_function = shutil.copytree)
# the source file for the app.py
app_source = target_app + "\\app.py"
dest = shutil.move(app_source, destination, copy_function = shutil.copy)
print('>>>> moving the copies')

#setting perimeters

#check is the full_auto_mode is True
if full_auto_mode:
	print('>>>> full auto mode')
	try:
		os.system("set flask = app.py")
		print('>>>> flask = app.py')
	except:
		print('failed to set up the env folder')
	try:
		os.system("flask run")
		print('>>>> flask run')
	except:
		print('failed to set flask to run')
	try:
		os.system("FLASK_ENV=development")
		print('>>>> FLASK_ENV=development')
	except:
		print("failed ot set the debug mode on")	
	
else:
	print("######################################################### \n")
	print("commands that you have to type to finish  of the set up")
	print("set flask = app.py")
	print("")
