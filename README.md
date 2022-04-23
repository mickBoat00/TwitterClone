# TwitterClone

A simple social media app in Django, to learn the process of creating popular social media apps like Twitter

#### Current features of the app
- Create, Read, Update, Delete CRUD operations on posts
- Like Retweet, Comment on Post
- Show list of the number of people on Liked or Retweeted the post
- User login System


To install
1. clone the repository
  ```
  git clone 
  ```
3. Create a virtual environment
  Use the command in the base diretory of the cloned project. Use the command
  ```
  python3 -m venv venv 
  ```
  
3. Activate the virtual environment. Use this commmand for linux /Mac users 
  ```
   source venv/bin/activate
  ```
   
5. Install the requirements
  ```
   pip install -r requirements.txt
  ```
4. Make sure to run your server with an ip of 0.0.0.0 because it is the only ALLOWED HOST
  ```
   python manage.py runserver 0:8000
  ```
  
  To run test
   - Run this command in your terminal
  ```
  pytest
  ```
  
