echo "create project..."
touch README.md
python3 -m venv venv 
pip3 install requests 
pip3 list 
pip3 freeze > requirements.txt 
pip3 install -r requirements.txt
source venv/bin/activate
pip3 install django
django-admin startproject product
echo "project created successfully"