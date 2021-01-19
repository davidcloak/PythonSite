from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
import webApp.views


# Create your tests here.
class StartPageTest(TestCase):

    def test_uses_index_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'start.html')

    def test_StartPage_returns_correct_html(self):
        request = HttpRequest()
        response = webApp.views.StartPage(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Welcome Page</title>', html)
        self.assertTrue(html.endswith('</html>'))


class FormPageTest(TestCase):

    def test_uses_createUser_template(self):
        response = self.client.get('/Form')
        self.assertTemplateUsed(response, 'createUser.html')

    def test_FormPage_returns_correct_html(self):
        request = HttpRequest()
        response = webApp.views.FormPage(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Create A User</title>', html)
        self.assertTrue(html.endswith('</html>'))

class ConfermPageTest(TestCase):

    def test_uses_Conferm_template(self):
        response = self.client.get('/Conferm')
        self.assertTemplateUsed(response, 'conferm.html')

    def test_ConfermPage_returns_correct_html(self):
        request = HttpRequest()
        response = webApp.views.ConPage(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Confermation</title>', html)
        self.assertTrue(html.endswith('</html>'))

class HomePageTest(TestCase):

    def test_uses_Home_template(self):
        response = self.client.get('/Home')
        self.assertTemplateUsed(response, 'home.html')

    def test_HomePage_returns_correct_html(self):
        request = HttpRequest()
        response = webApp.views.HomePage(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Home Page</title>', html)
        self.assertTrue(html.endswith('</html>'))

class LoginPageTest(TestCase):
    
    def test_uses_Login_template(self):
        response = self.client.get('/Login')
        self.assertTemplateUsed(response, 'login.html')

    def test_LoginPage_returns_correct_html(self):
        request = HttpRequest()
        response = webApp.views.LoginPage(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>User Login</title>', html)
        self.assertTrue(html.endswith('</html>'))

class GamePageTest(TestCase):
    
    def test_uses_Game_template(self):
        response = self.client.get('/Game')
        self.assertTemplateUsed(response, 'Game.html')

    def test_GamePage_returns_correct_html(self):
        request = HttpRequest()
        response = webApp.views.GamePage(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Text Game</title>', html)
        self.assertTrue(html.endswith('</html>'))

class GameEndPageTest(TestCase):
    
    def test_uses_GameEnd_template(self):
        response = self.client.get('/GameEnd')
        self.assertTemplateUsed(response, 'GameEnd.html')

    def test_GameEndPage_returns_correct_html(self):
        request = HttpRequest()
        response = webApp.views.GameEndPage(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Game Over</title>', html)
        self.assertTrue(html.endswith('</html>'))

class MarioGame(TestCase):
    
    def test_uses_MarioGame_template(self):
        response = self.client.get('/Mario')
        self.assertTemplateUsed(response, 'index.html')

    def test_MarioGamePage_returns_correct_html(self):
        request = HttpRequest()
        response = webApp.views.MarioGamePage(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Mario Knock Off</title>', html)
        self.assertTrue(html.endswith('</html>'))

class Logout(TestCase):
    
    def test_uses_Logout_template(self):
        response = self.client.get('/Logout')
        self.assertTemplateUsed(response, 'logout.html')

    def test_LogoutPage_returns_correct_html(self):
        request = HttpRequest()
        response = webApp.views.LogoutPage(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Log Out</title>', html)
        self.assertTrue(html.endswith('</html>'))

class UserLogin(TestCase):
    pass