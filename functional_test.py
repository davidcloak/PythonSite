from selenium import webdriver
import unittest
#make sure website and server are working
#big picture testing
class RegisterTest(unittest.TestCase):
    def setUp(self):
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.headless=True
        self.browser = webdriver.Firefox(options=fireFoxOptions)
        self.browser.get('http://127.0.0.1:8000')
    
    def tearDown(self):
         self.browser.quit()

    def test_title(self):
        self.assertIn('Welcome Page', self.browser.title, 'Wrong Title')

    def makeUser(self):
        createUserBtn = self.browser.find_element_by_id('createUser')
        createUserBtn.click()

        #Form Page
        first = self.browser.find_element_by_id('firstName')
        last = self.browser.find_element_by_id('lastName')
        email = self.browser.find_element_by_id('email')
        password = self.browser.find_element_by_id('password')

        first.send_keys('David')
        last.send_keys('Cloak')
        email.send_keys('email@email.com')
        password.send_keys('thePassword')

        confermBtn = self.browser.find_element_by_id('submit')
        confermBtn.click()

    def testMakeUser(self):
        self.makeUser()

        #Confermaiton Page
        self.assertIn('David Cloak', self.browser.find_element_by_id('name').text, 'Name Not Found')
        self.assertIn('email@email.com', self.browser.find_element_by_id('email').text, 'Email Not Found')
        self.assertIn('XXXXXXXXXXX', self.browser.find_element_by_id('password').text, 'Password Not Found')

        returnHomeBtn = self.browser.find_element_by_id('home')
        returnHomeBtn.click()

        #Home Page
        self.assertIn('David', self.browser.find_element_by_id('user').text, 'Name Not Found')



class LoginTest(unittest.TestCase):
    def setUp(self):
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.headless=True
        self.browser = webdriver.Firefox(options=fireFoxOptions)
        self.browser.get('http://127.0.0.1:8000')
    
    def tearDown(self):
         self.browser.quit()


    #to unsure the user is made before hand since I am not
    #using a database yet
    def makeUser(self):
        createUserBtn = self.browser.find_element_by_id('createUser')
        createUserBtn.click()

        #Form Page
        first = self.browser.find_element_by_id('firstName')
        last = self.browser.find_element_by_id('lastName')
        email = self.browser.find_element_by_id('email')
        password = self.browser.find_element_by_id('password')

        first.send_keys('David')
        last.send_keys('Cloak')
        email.send_keys('email@email.com')
        password.send_keys('thePassword')

        confermBtn = self.browser.find_element_by_id('submit')
        confermBtn.click()


    def testLogin(self):
        self.makeUser()
        self.browser.get('http://127.0.0.1:8000')

        loginBtn = self.browser.find_element_by_id('login')
        loginBtn.click()

        email = self.browser.find_element_by_id('email')
        password = self.browser.find_element_by_id('password')
        email.send_keys('email@email.com')
        password.send_keys('thePassword')

        confermBtn = self.browser.find_element_by_id('submit')
        confermBtn.click()

        #Home Page
        self.assertIn('David', self.browser.find_element_by_id('user').text, 'Name Not Found')


class GameTest(unittest.TestCase):
    def setUp(self):
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.headless=True
        self.browser = webdriver.Firefox(options=fireFoxOptions)
        self.browser.get('http://127.0.0.1:8000')
    
    def tearDown(self):
         self.browser.quit()

    #to unsure the user is made before hand since I am not
    #using a database yet
    def makeUser(self):
        createUserBtn = self.browser.find_element_by_id('createUser')
        createUserBtn.click()

        #Form Page
        first = self.browser.find_element_by_id('firstName')
        last = self.browser.find_element_by_id('lastName')
        email = self.browser.find_element_by_id('email')
        password = self.browser.find_element_by_id('password')

        first.send_keys('David')
        last.send_keys('Cloak')
        email.send_keys('email@email.com')
        password.send_keys('thePassword')

        confermBtn = self.browser.find_element_by_id('submit')
        confermBtn.click()

    def testGameSecond(self):
        self.makeUser()

        #puts us on home page
        self.browser.get('http://127.0.0.1:8000/Home')

        #goes to game
        gameLink = self.browser.find_element_by_id('gamebtn')
        gameLink.click()

        firstList = self.browser.find_element_by_id('options')
        self.assertIn('Shall you adventure into the woods?', firstList.text, 'First Option not found')
        self.assertIn('Shall you adventure into the sea?', firstList.text, 'Second Option not found')
        self.assertIn('Shall you adventure into the cave?', firstList.text, 'Third Option not found')

        gameLink = self.browser.find_element_by_id('second')
        gameLink.click()

        secondList = self.browser.find_element_by_id('options')
        self.assertIn('Capture the Squid', secondList.text, 'First Option not found')
        self.assertIn('Flee', secondList.text, 'Second Option not found')
        self.assertIn('Kill and have him for supper', secondList.text, 'Third Option not found')

        gameLink = self.browser.find_element_by_id('second')
        gameLink.click()

        self.assertIn('Trying to run attracted the squids attention and it came and ate everyone on board.', self.browser.find_element_by_id('endMessage').text, 'End Message missing')

    def testGameFirst(self):
        self.makeUser()

        #puts us on home page
        self.browser.get('http://127.0.0.1:8000/Home')

        #goes to game
        gameLink = self.browser.find_element_by_id('gamebtn')
        gameLink.click()

        firstList = self.browser.find_element_by_id('options')
        self.assertIn('Shall you adventure into the woods?', firstList.text, 'First Option not found')
        self.assertIn('Shall you adventure into the sea?', firstList.text, 'Second Option not found')
        self.assertIn('Shall you adventure into the cave?', firstList.text, 'Third Option not found')

        gameLink = self.browser.find_element_by_id('first')
        gameLink.click()

        secondList = self.browser.find_element_by_id('options')
        self.assertIn('Run', secondList.text, 'First Option not found')
        self.assertIn('Stand your ground!', secondList.text, 'Second Option not found')
        self.assertIn('Throw a rock at it.', secondList.text, 'Third Option not found')

        gameLink = self.browser.find_element_by_id('second')
        gameLink.click()

        self.assertIn('What were you think standing your grand you have no armor or weapons to defend yourself? He ate you in short.', self.browser.find_element_by_id('endMessage').text, 'End Message missing')

    def testGameThird(self):
        self.makeUser()

        #puts us on home page
        self.browser.get('http://127.0.0.1:8000/Home')

        #goes to game
        gameLink = self.browser.find_element_by_id('gamebtn')
        gameLink.click()

        firstList = self.browser.find_element_by_id('options')
        self.assertIn('Shall you adventure into the woods?', firstList.text, 'First Option not found')
        self.assertIn('Shall you adventure into the sea?', firstList.text, 'Second Option not found')
        self.assertIn('Shall you adventure into the cave?', firstList.text, 'Third Option not found')

        gameLink = self.browser.find_element_by_id('third')
        gameLink.click()

        secondList = self.browser.find_element_by_id('options')
        self.assertIn('Become one with the bats', secondList.text, 'First Option not found')
        self.assertIn('Play dead', secondList.text, 'Second Option not found')
        self.assertIn('You are deathly afraid of bats.', secondList.text, 'Third Option not found')

        gameLink = self.browser.find_element_by_id('second')
        gameLink.click()

        self.assertIn('Most bats are not human eaters. But these bats know a free meal when they see it and ate what they thought was long dead.', self.browser.find_element_by_id('endMessage').text, 'End Message missing')


class StyleAndLayoutTest(unittest.TestCase):

    def setUp(self):
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.headless=True
        self.browser = webdriver.Firefox(options=fireFoxOptions)
        self.browser.get('http://127.0.0.1:8000')
    
    def tearDown(self):
         self.browser.quit()

    def testIndexPage(self):
        self.browser.set_window_size(1024, 768)

        buttons = self.browser.find_element_by_id('buttons')
        self.assertAlmostEqual(
            buttons.location['x'] + buttons.size['width'] / 2,
            512,
            delta=10
        )

    def testConferm(self):
        self.browser.get('http://127.0.0.1:8000/Conferm')

        self.browser.set_window_size(1024, 768)

        context = self.browser.find_element_by_id('context')
        self.assertAlmostEqual(
            context.location['x'] + context.size['width'] / 2,
            512,
            delta=10
        )

    def testGamePage(self):
        self.browser.get('http://127.0.0.1:8000/Game')
        self.browser.set_window_size(1024, 768)

        items = self.browser.find_element_by_id('context')
        self.assertAlmostEqual(
            items.location['x'] + items.size['width'] / 2,
            512,
            delta=10
        )

        self.browser.get('http://127.0.0.1:8000/Game')
        
        background = self.browser.find_element_by_id('background').value_of_css_property('background-color')
        self.assertEquals("rgb(0, 0, 0)", background, "Background color is incorrect.")

        backgroundImg = self.browser.find_element_by_id('image').value_of_css_property('background-image')
        self.assertEquals('url("http://127.0.0.1:8000/static/images/Welcome.jpg")', backgroundImg, "Image is incorrect. Welcome")

        gameLink = self.browser.find_element_by_id('first')
        gameLink.click()

        background = self.browser.find_element_by_id('background').value_of_css_property('background-color')
        self.assertEquals("rgb(0, 0, 0)", background, "Background color is incorrect. Forsest")

        backgroundImg = self.browser.find_element_by_id('image').value_of_css_property('background-image')
        self.assertEquals('url("http://127.0.0.1:8000/static/images/Forest.jpg")', backgroundImg, "Image is incorrect. Forest")

        self.browser.get('http://127.0.0.1:8000/Game')
        gameLink = self.browser.find_element_by_id('second')
        gameLink.click()

        background = self.browser.find_element_by_id('background').value_of_css_property('background-color')
        self.assertEquals("rgb(0, 0, 0)", background, "Background color is incorrect. Sea")

        backgroundImg = self.browser.find_element_by_id('image').value_of_css_property('background-image')
        self.assertEquals('url("http://127.0.0.1:8000/static/images/Sea.jpg")', backgroundImg, "Image is incorrect. Sea")

        self.browser.get('http://127.0.0.1:8000/Game')
        gameLink = self.browser.find_element_by_id('third')
        gameLink.click()

        background = self.browser.find_element_by_id('background').value_of_css_property('background-color')
        self.assertEquals("rgb(0, 0, 0)", background, "Background color is incorrect. Cave")

        backgroundImg = self.browser.find_element_by_id('image').value_of_css_property('background-image')
        self.assertEquals('url("http://127.0.0.1:8000/static/images/Cave.jpg")', backgroundImg, "Image is incorrect. Cave")

    def testGameEndPage(self):
        self.browser.get('http://127.0.0.1:8000/GameEnd')
        self.browser.set_window_size(1024, 768)

        context = self.browser.find_element_by_id('context')
        self.assertAlmostEqual(
            context.location['x'] + context.size['width'] / 2,
            512,
            delta=10
        )

        background = self.browser.find_element_by_id('background').value_of_css_property('background-color')
        self.assertEquals("rgb(0, 0, 0)", background, "Background color is incorrect.")

        endScreen = self.browser.find_element_by_id('endMessage').value_of_css_property('color')
        self.assertEquals("rgb(255, 0, 0)", endScreen, "Color of text is incorrect.")

if __name__ == '__main__':
    #calls the class if it is not instantiated elsewhere
    unittest.main()

