from django.test import TestCase
from .models import Neighbourhood,Profile,Post,Business
# Create your tests here.

# Create your tests here.
#profile test
class ProfileTestClass(TestCase):
     #set Up method
    def setUp(self):
        self.naiyoma = Profile(id=9000,username = 'naiyoma')
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.naiyoma,Profile))
    #testing save method
    def test_save_method(self):
        self.naiyoma.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    #testing for deleting method
    def test_delete_method(self):
        self.naiyoma.save_profile()
        self.naiyoma.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)
    #testing for update caption
    def test_update_metod(self):
        self.naiyoma.save_profile()
        self.naiyoma.update_description()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)
    #testing for creatinging post    
    def test_creation_method(self):
        self.naiyoma.create_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)     
class PostTestClass(TestCase):
    #set Up method
    def setUp(self):
        self.image = Post(image = 'cool')
    #test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Post))
    def test_save_method(self):
        self.image.save_image()
        image = Post.objects.all()
        self.assertTrue(len(image) > 0)
    #testing for deleting method
    def test_delete_method(self):
        self.image.save_image()
        self.image.delete_image()
        image = Post.objects.all()
        self.assertTrue(len(image) > 0)
    #testing for update caption
    def test_update_metod(self):
        self.image.save_image()
        self.image.update_caption()
        image = Post.objects.all()
        self.assertTrue(len(image) > 0)
    #testing for creatinging post    
    def test_creation_method(self):
        self.image.create_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0) 
class BusinessTestClass(TestCase):
    #set up method
    def setUp(self):
        self.business = Business(id=9000,business_name= 'naiyoma')
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))
    #testing for saving    
    def test_save_method(self):
        self.business.save_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)
    #testing for deleting method
    def test_delete_method(self):
        self.business.save_business()
        self.business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)
    #testing for update caption
    def test_update_metod(self):
        self.business.save_business()
        self.business.update_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)
    # #testing for creatinging post    
    # def test_creation_method(self):
    #     self.business.create_business()
    #     business = Business.objects.all()
    #     self.assertTrue(len(Business) > 0) 
#testing neighbourhood
class NeighbourhoodTestClass(TestCase):
    #set up method
    def setUp(self):
        self.neighbourhood = Neighbourhood(id=9000,neighbourhood_name= 'naiyoma')
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))        
    #testing for saving    
    def test_save_method(self):
        self.neighbourhood.save_neighbourhood()
        neighbourhood = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhood) > 0)
    #testing for deleting method
    def test_delete_method(self):
        self.neighbourhood.save_neighbourhood()
        self.neighbourhood.delete_neighbourhood()
        neighbourhood = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhood) < 1)    
    #testing for update caption
    def test_update_metod(self):
        self.neighbourhood.save_neighbourhood()
        self.neighbourhood.update_neighbourhood()
        neighbourhood = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhood) > 0)
    #testing for creatinging post    
    def test_creation_method(self):
        self.neighbourhood.create_neighbourhood()
        neighbourhood = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhood) > 0)    