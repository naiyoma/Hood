# Neighbourhood
#### This is an application that allows users to join and create Neighbourhoods,08/10/2018 
#### By Aurelia Naiyoma
## Description
This application allows its users to do the following

- Sign in with the application to start using.
- Set up a profile about me and a general location and my neighborhood name.
- Find a list of different businesses in my neighborhood.
- Find Contact Information for the health department and Police authorities near my neighborhood.
- Create Posts that will be visible to everyone in my neighborhood.
- Change My neighborhood when I decide to move out.
- Only view details of a single neighborhood.
## Setup/Installation Requirements
# installations required
- python version should be 3.6
-Django version 1.11 `pip install django==1.11`
- Additionally, you’ll need to make sure you have pip available. You can check this by running:
- `pip --Version`
- Install Pipenv `pip install --user pipenv`
- install virtualenv and then test it
- `python3.6 pip install --user --upgrade pip`
- `python3.6 -m virtualenv env`
- `source env/bin/activate`

Inorder to clone , follow the procedure below;
- On GitHub, navigate to the main page of the repository.
- Under the repository name, click Clone or downlonload.
- click the paste button.
- Open Terminal.
- Change the current working directory to the location where  -  you want the cloned directory to be made.
- Type git clone, and then paste the URL you copied in Step 2.
- git clone` https://github.com/naiyoma/hood.git`
`Press Enter`.

#install dependancies
- install dependancies that will create an environment for the app to run 
`pip3 install -r requirements.txt`
#creating a database
- `psql`
- `CREATE DATABASE neighbourhood;`
- connect to the database `\c neighbourhood;`
- check if tables have been created `\dt`

#Run migrations
- `python3.6 manage.py migrate`
- `python3.6 manage.py makemigrations neighbourhoods`

#Running the app
- `python3.6 manage.py runserver`
- Open terminal on ` localhost:8000`

#testing
- `python3.6 manage.py test `

#SPECIFICATIONS
| Behaviour | Input | Output |

| Display Posts| *On the Landing Page*| user can view different Posts|
| Posts expand | * On the Landing Page*| user can click on an Posts to view more details|
| As An Admin Sign in| * On The Admin Dashboard*| Post Posts,and Businesses|
| As A User   | *On Profile Page| Edit Profile Page|

## Technologies Used
- HTML
- CSS
- Python
- Django
- Postgres
- javascript
- Heroku

## Support and contact details
- lankas.aurelia@gmail.com
- 0702781830

# Known Bugs
- the website does not function well on explorer

### License
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
Copyright (c) {2018} **{By Aurelia Naiyoma}**

##live link to Heruko
https://jirani-254.herokuapp.com/
