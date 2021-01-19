from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from webApp.models import User
from webApp.forms import UserForm

# Create your views here.

content= {}
content['model'] = User("", "","", "", "")
content['position'] = 0

Options = {
    "1":{'intro':'Hello '+content['model'].fName, 'one':'Shall you adventure into the woods?', 'two':'Shall you adventure into the sea?', 'three':'Shall you adventure into the cave?', 'image':'Welcome.jpg'},
    "21":{'intro':'You see a cyclops. What shall you do?', 'one':'Run', 'two':'Stand your ground!', 'three':'Throw a rock at it.', 'image':'Forest.jpg'},
    "211":'Running away you tripped and broke you neck.',
    "212":'What were you think standing your grand you have no armor or weapons to defend yourself? He ate you in short.',
    "213":'Think you wanted to play catch the cyclops picks up what he thinks to be an approprate rock and throws it to you. It was not an approprate sized rock.',
    "22":{'intro':'Setting sail onto the sea you see a giant squid what do you do?', 'one':'Capture the Squid', 'two':'Flee', 'three':'Kill and have him for supper', 'image':'Sea.jpg'},
    "221":'While trying to capture the squid it broke your boat and it sunk leaving you to die at sea.',
    "222":'Trying to run attracted the squids attention and it came and ate everyone on board.',
    "223":'You successfully kill and cooked the squid. But... the meat was not good and everyone who ate it died of food poisoning.',
    "23":{'intro':'You get surrounded by bats what do you do', 'one':'Become one with the bats', 'two':'Play dead', 'three':'You are deathly afraid of bats.', 'image':'Cave.jpg'},
    "231":'Well thats odd you became a bat. But were not used to using ecolocation and flew into a wall and broke your neck.',
    "232":'Most bats are not human eaters. But these bats know a free meal when they see it and ate what they thought was long dead.',
    "233":'You have a heart attack.'
}

def LogoutPage(request):
    if request.method == 'POST':
        content['model'] = User("", "","", "", "")
        return render(request, 'start.html')
    else:
        return render(request, 'logout.html')

def TestPage(request):
    all_users = User.objects.all()

    email = 'cloak.david@gmail.com'
    password = 'Password123'

    theUser = User.objects.filter(email__contains=email)
    theUser = theUser.filter(password__contains=password)

    return render(request, 'test.html', {'all' : all_users})

def StartPage(request):
    return render(request, 'start.html')

def FormPage(request):
        return render(request, 'createUser.html')

def ConPage(request):
    if request.method == 'POST':
        addUser = UserForm(request.POST)
        if addUser.is_valid:
            addUser.save()

        p = addUser.__getitem__('password').value()
        p = request.POST.get('password')
        password = ''

        if p != None:
            for i in range(0, len(p)):
                password += 'X'

        # content['model'] = User('',
        #     str(addUser.__getitem__('fName').value()),
        #     str(addUser.__getitem__('lName').value()),
        #     str(addUser.__getitem__('email').value()),
        #     password)

        return render(request, 'conferm.html', {'context' : content['model']})
    else:
        return render(request, 'conferm.html', {'context' : content['model']})

def HomePage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        theUser = User.objects.filter(email__contains=email)
        theUser = theUser.filter(password__contains=password)
        try:
            if theUser.first().email == email:
                content['model'] = theUser.first()
        except:
            content['model'] = User(' ', 'fname', 'lname', 'email', 'password')

        if content['model'].email == email:
            return render(request, 'home.html', {'context' : content['model']})
        else:
            return render(request, 'login.html', content)
    return render(request, 'home.html', {'context' : content['model']})

def LoginPage(request):
    return render(request, 'login.html', content)

def GamePage(request):
    if request.method == 'POST':
        if content['position'] == 0:
            page = request.POST.get('choose')
            content['gamelists'] = Options['2'+page]
            content['position'] = page
            return render(request, 'Game.html', content)
        else:
            page = request.POST.get('choose')
            content['gamelists'] = Options['2'+content['position']+page]
            content['position'] = 0
            return render(request, 'GameEnd.html', content)
    else:
        content['gamelists'] = Options['1']
        content['position'] = 0
        return render(request, 'Game.html', content)
    
def GameEndPage(request):
    content['gamelists'] = "You shouldn't be here yet!"+content['model'].fName
    content['position'] = 0
    return render(request, 'GameEnd.html', content)

def MarioGamePage(request):
    return render(request, 'index.html')