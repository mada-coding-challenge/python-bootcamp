echo "create project..."
django-admin startproject src .
touch src/README.md
python3 -m venv venv 
source venv/bin/activate
pip3 install requests 
pip3 list 
pip3 freeze > requirements.txt 
pip3 install -r requirements.txt
echo "project created successfully"