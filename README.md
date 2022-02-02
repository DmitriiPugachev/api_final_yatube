### Description:
API for YaTube.
#### You can:
  * get, create, update and delete posts;
  * get an information about groups;
  * get, create, update and delete posts comments;
  * get a list of favorites and add a specific author in favorites.
#### Techs:
  * requests==2.26.0
  * django==2.2.6
  * djangorestframework==3.12.4
  * djangorestframework-simplejwt==4.7.2
  * djoser==2.1.0
  * pillow==8.3.1
### How to run the project:
Clone the repo and go to its directory:
```bash
git clone https://github.com/DmitriiPugachev/api_final_yatube.git
```
```bash
cd api_final_yatube
```
Create and activate a virtual environment:
```bash
python3 -m venv env
```
```bash
source env/bin/activate
```
Install and upgrade pip in the environment:
```bash
python3 -m pip install --upgrade pip
```
Install dependencies from ```requirements.txt```:
```bash
pip install -r requirements.txt
```
Create a ```.env``` file in the root directory and fulfill it like in an ```example.env``` file.

Migrate:
```bash
python3 manage.py migrate
```
Run the project:
```bash
python3 manage.py runserver
```
### Links
[redoc and examples of all possible requests](http://127.0.0.1:8000/redoc/) this link is for local usage

[admin account](http://127.0.0.1:8000/admin/)  this link is for local usage
### Author
Dmitrii Pugachev
