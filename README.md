### Description:
Проект сервиса API для YaTube.
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
Migrate:
```bash
python3 manage.py migrate
```
Run the project:
```bash
python3 manage.py runserver
```
### Request examples:
#### version 1.0

**GET** request for a list of **posts**:

```bash
/api/v1/posts/
```

**POST** request for a specific **post**:

```bash
/api/v1/posts/
```

**GET** request for a specific **post**:

```bash
/api/v1/posts/1/
```

**PUT** request for update a specific **post**:

```bash
/api/v1/posts/1/
```

**PATCH** request for a specific **post**:

```bash
/api/v1/posts/1/
```

**DELETE** request for a specific **post**:

```bash
/api/v1/posts/1/
```

**GET** request for a list of **comments** of a specific post:

```bash
/api/v1/posts/1/comments/
```

**POST** request for a specific **comment**:

```bash
/api/v1/posts/1/comments/
```

**GET** request for a specific **comment**:

```bash
/api/v1/posts/1/comments/1/
```

**PUT** request for a specific **comment**:

```bash
/api/v1/posts/1/comments/1/
```

**PATCH** request for a specific **comment**:

```bash
/api/v1/posts/1/comments/1/
```

**DELETE** request for a specific **comment**:

```bash
/api/v1/posts/1/comments/1/
```

**GET** request for a list of **groups**:

```bash
/api/v1/groups/
```

**GET** request for a specific **group**:

```bash
/api/v1/groups/1/
```

**GET** request for a list of **followings** of an authorized user:

```bash
/api/v1/follow/
```

**POST** request for a **following** of a specific author:

```bash
/api/v1/follow/
```

**POST** request for a **JWT-token** creation:

```bash
/api/v1/jwt/create/
```

**POST** request for a **JWT-token** refreshing:

```bash
/api/v1/jwt/refresh/
```

**POST** request for a **JWT-token** verification:

```bash
/api/v1/jwt/verify/
```

### Author
Dmitrii Pugachev
