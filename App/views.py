from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth,Group
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile,Post,Comment,Message,FollowersCount,Chat,LikePost,Favourite_post,Notifications,Group_comment
from itertools import chain
import random
from django.db.models import Q
from django.http import HttpResponse,JsonResponse
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from twilio.rest import Client
from decouple import config
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
@login_required(login_url='welcome_page')
def indexs(request):
    posts = Post.objects.all()
    user_profile = Profile.objects.get(user=request.user)
    favourites =Favourite_post.objects.filter(name=request.user)

    # Get feed only for people user following
    user_following_list = []
    feed = []

    #people user following
    user_following = FollowersCount.objects.filter(follower = request.user.username)


    # User post
    user_posts = Post.objects.filter(user=request.user.username)


    #make the user verified if the followers have reached 100
    if FollowersCount.objects.filter(user=Post.user) == 100:
        user_profile.is_verified = True

    # is a user is verified verify all his posts
    user_post_profile = Post.objects.all()

    # Post of People user not following
    #post_of_not_users = Post.objects.all().exclude()

    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_list = Post.objects.filter(user=usernames)

        # Incase users don't have a post

        #feed.append(post_of_not_users)
        feed.append(feed_list)

    feed.append(user_posts)
    feed_list = list(chain(*feed))

    return render(request, 'indexs.html', {'user_profile':user_profile,'post':feed_list,'favourites':favourites})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
<<<<<<< HEAD

=======
        
>>>>>>> de1ee6a44f834efd78a7cc3a2b70f6b2159b744c
        #Strip all white spaces
        username = username.strip()
        email = email.strip()
        password = password.strip()
        password2 = password2.strip()
<<<<<<< HEAD

=======
        
>>>>>>> de1ee6a44f834efd78a7cc3a2b70f6b2159b744c
        if password == password2 :
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save();
<<<<<<< HEAD

=======
                
                send_mail(
                    'Welcome Message',
                    'Hi welcome to runschoolhub. We are happy to have you',
                    [settings.EMAIL_HOST_USER],
                    email,
                    fail_silently=False
                )
                 
>>>>>>> de1ee6a44f834efd78a7cc3a2b70f6b2159b744c
                return redirect('login')
        else:
            messages.info(request,'Password not the same')
            return redirect('register')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
<<<<<<< HEAD

        #Strip all white spaces
        username = username.strip()
        password = password.strip()

=======
        
        #Strip all white spaces
        username = username.strip() 
        password = password.strip()   
>>>>>>> de1ee6a44f834efd78a7cc3a2b70f6b2159b744c
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('indexs')
        else:
            messages.info(request, 'Credentials are Invalid')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def setting(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        if request.FILES.get('profile_image') == None:
            profile_image = user_profile.profileimage
            nickname = request.POST['nickname']
            bio = request.POST['bio']
            faculty = request.POST['faculty']


            user_profile.profileimage = profile_image
            user_profile.nickname =  nickname
            user_profile.bio = bio
            user_profile.faculty = faculty
            user_profile.save();

            post = Post.objects.filter(user=request.user)
            for post in post:
                post.profileimage = profile_image
                post.save()


        else:
            profileimage = request.FILES.get('profile_image')
            nickname = request.POST['nickname']
            bio = request.POST['bio']
            faculty = request.POST['faculty']

            user_profile.profileimage = profileimage
            user_profile.nickname = nickname
            user_profile.bio = bio
            user_profile.faculty = faculty
            user_profile.save();


            post = Post.objects.filter(user=request.user)
            for post in post:
                post.profileimage = profileimage
                post.save()



    return render(request, 'setting.html', {'user_profile':user_profile})

@login_required(login_url='login')
def profile(request,pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    post = Post.objects.filter(user=pk)
    post_len = len(post)
    follower = request.user.username
    user = pk


    if FollowersCount.objects.filter(follower=follower, user=user).first():
        text= 'Unfollow'
    else:
        text = 'follow'

    user_followers = len(FollowersCount.objects.filter(user=pk))
    user_following = len(FollowersCount.objects.filter(follower=pk))


    context = {
        'user_profile':user_profile,
        'post':post,
        'post_len':post_len,
        'text':text,
        'user_followers':user_followers,
        'user_following':user_following
    }
    return render(request, 'profile.html', context)

@login_required(login_url='login')
def upload(request):
    user_profile =  Profile.objects.get(user = request.user)
    if request.method == 'POST':
        user = request.user.username
        caption = request.POST['caption']
        profileimage = request.POST['profile_image']
        videos = request.FILES.getlist('video')
        images = request.FILES.getlist('image')
        audios = request.FILES.getlist('audio')
        pdfs = request.FILES.getlist('pdf')
<<<<<<< HEAD


        for video in videos:
            video = Post.objects.create(video=video, caption=caption, profileimage=profileimage, user=user)
        for image in images:
            images = Post.objects.create(image=image, caption=caption, profileimage=profileimage, user=user)
        for audio in audios:
            audio = Post.objects.create(audio=audio, caption=caption, profileimage=profileimage, user=user)
        for pdf in pdfs:
            pdf = Post.objects.create(pdf=pdf, caption=caption, profileimage=profileimage, user=user)
=======
        
        
        if images or videos or audios or pdfs:
            for video in videos:
                video = Post.objects.create(video=video, caption=caption, profileimage=profileimage, user=user)
            for image in images:
                images = Post.objects.create(image=image, caption=caption, profileimage=profileimage, user=user)
            for audio in audios:
                audio = Post.objects.create(audio=audio, caption=caption, profileimage=profileimage, user=user)
            for pdf in pdfs:
                pdf = Post.objects.create(pdf=pdf, caption=caption, profileimage=profileimage, user=user)
        else:
            caption = Post.objects.create(caption=caption, profileimage=profileimage, user=user)
>>>>>>> de1ee6a44f834efd78a7cc3a2b70f6b2159b744c



    return render(request, 'upload.html', {'user_profile':user_profile})

@login_required(login_url='login')
def comment(request):
    # Get user profile profile
    user_profile =  Profile.objects.get(user = request.user)
    if request.method == 'POST':
        name = request.POST['name']
        ids = request.POST['ids']
        # posts = request.POST['post']
        # post = Post.objects.get(caption=posts)
        comment = request.POST['comment']
        profileimage = request.POST['profile_image']

        comments = Comment.objects.create(comment=comment,name=name, ids=ids, profileimage =profileimage )
        comments.save()
        # Increase the number of commenters
        post = Post.objects.get(id=ids)
        post.no_of_commenters = post.no_of_commenters + 1
        post.save()

    return HttpResponse(comments.comment)
        # Redirect to the post
        # return redirect('/'+'post/'+str(post.id))

@login_required(login_url='login')
def like_post(request):
    if request.method == 'POST':
        name =  request.POST['name']
        ids =  request.POST['ids']

        #Get the post the user is liking and if he has already liked delete the like
        post = Post.objects.get(id=ids)
        if LikePost.objects.filter(name=name, ids=ids).exists():
            like = LikePost.objects.get(name=name, ids=ids)
            like.delete()
            post.no_of_likes = post.no_of_likes - 1
            post.save()


        else:
            like = LikePost.objects.create(name=name, ids=ids)
            like.save()
            post.no_of_likes = post.no_of_likes + 1
            post.save()

        return HttpResponse(post.no_of_likes)


@login_required(login_url='login')
def post(request, pk):
    user_profile =  Profile.objects.get(user = request.user)
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(ids=pk)
    return render(request, 'post.html', {'post':post, 'user_profile':user_profile})

def getComments(request, pk):
    comments = Comment.objects.filter(ids=pk)
    return JsonResponse({'comments':list(comments.values())})


@login_required(login_url='login')
def delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('/')

@login_required(login_url='login')
def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']
<<<<<<< HEAD

=======
        
        # Deletes follower if it already exists
>>>>>>> de1ee6a44f834efd78a7cc3a2b70f6b2159b744c
        if FollowersCount.objects.filter(follower=follower, user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower, user=user)
            delete_follower.delete()
            
            # Delete Chat model if it exists
            delete_chat1 = Chat.objects.filter(follower=follower, user=user).first() 
            delete_chat2 = Chat.objects.filter(follower=user, user=follower).first()
            delete_chat1.delete()
            delete_chat2.delete()
            
            return HttpResponse('Follow')
        # Creates folllower if it does not exists
        else:
            new_follower = FollowersCount.objects.create(follower=follower, user=user)
<<<<<<< HEAD
            new_follower.save()
            return HttpResponse('Unfollow')

@login_required(login_url='login')
=======
            new_follower.save() 
            
            #Gets user profile
            user_object = User.objects.get(username=user)
            user_profile = Profile.objects.get(user = user_object)
            
            follower_object = User.objects.get(username=follower)
            follower_profile = Profile.objects.get(user = follower_object)
            
            print(user_profile.id_user)
            print(follower_profile.id_user)
            # Create chat models
            new_chat1 = Chat.objects.create(follower=follower, user=user, user_profile_img=user_profile.profileimage, follower_profile_img=follower_profile.profileimage , id_user=user_profile.id_user, id_follower=follower_profile.id_user)
            new_chat2 = Chat.objects.create(follower=user, user=follower, follower_profile_img=user_profile.profileimage, user_profile_img=follower_profile.profileimage, id_user=follower_profile.id_user, id_follower=user_profile.id_user)
            new_chat1.save()
            new_chat2.save()
            return HttpResponse('Unfollow')
        
  


@login_required(login_url='login')       
>>>>>>> de1ee6a44f834efd78a7cc3a2b70f6b2159b744c
def search_user(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    if request.method == 'POST':
        user = request.POST['user']

        username_object = User.objects.filter(username__icontains=user)


        username_profile = []
        username_profile_list = []

        for users in username_object:
             username_profile.append(users.id)

        for ids in username_profile:
            profile_lists =  Profile.objects.filter(id_user = ids)
            username_profile_list.append(profile_lists)

        username_profile_list  = list(chain(*username_profile_list))
        return render(request, 'suggestions.html', {'username_profile_list':username_profile_list, 'user_profile':user_profile})
    else:
        user = request.user
        user_details = Profile
    # user suggestiions starts, suggests users in the same department
        #user_faculty = Profile.objects.get(faculty = user)
        #same_profile_object = Profile.objects.filter(faculty__icontains=user)

        user_following = FollowersCount.objects.filter(follower = request.user.username)

        all_user = User.objects.all()
        people_user_following = []
        for user in user_following:
            user_list = User.objects.get(username=user.user)
            people_user_following.append(user_list)
        new_suggestions_list = [x for x in list(all_user) if (x not in list(people_user_following))]
        current_user = User.objects.filter(username=request.user.username)
        final_suggestions = [x for x in list(new_suggestions_list) if (x not in list(current_user))]
        random.shuffle(final_suggestions)


        usernames_profile = []
        usernames_profile_list = []

        users_profile = Profile.objects.get(user=user_object)

        for users in final_suggestions:
            usernames_profile.append(users.id)

        for ids in usernames_profile:
            profiles_lists =  Profile.objects.filter(id_user = ids)
            usernames_profile_list.append(profiles_lists)

        suggestions_usernames_profile_list  = list(chain(*usernames_profile_list))


        return render(request, 'suggestions.html', {'suggestions_usernames_profile_list':suggestions_usernames_profile_list, 'user_profile':user_profile})

@login_required(login_url='login')
def search(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_search = request.POST['search']
        check_caption = Post.objects.filter(caption__icontains = user_search)


        return render(request, 'search.html',{'check_caption':check_caption, 'user_search':user_search, 'user_profile':user_profile})
    else:
        return redirect('/')

@login_required(login_url='login')
def favourite_post(request,pk):

    name = request.user
    post = Post.objects.get(id=pk)
    if Favourite_post.objects.filter(name=request.user, file=post).first():
        text = 'Remove favourites'
    else:
        text = 'Add favourites'

    if post.image:
        if Favourite_post.objects.filter(file=post.image, name=name).first():
            delete_post =  Favourite_post.objects.get(file=post.image, name=name)
            delete_post.delete()
            return redirect('/')
        else:
            save_post = Favourite_post.objects.create(file=post.image, name=name)
            save_post.save()
            return redirect('/')

    if post.video:
        if Favourite_post.objects.filter(file=post.video, name=name).first():
            delete_post =  Favourite_post.objects.get(file=post.video, name=name)
            delete_post.delete()
            return redirect('/')
        else:
            save_post = Favourite_post.objects.create(file=post.video, name=name)
            save_post.save()
            return redirect('/')

    if post.pdf:
        if Favourite_post.objects.filter(file=post.pdf, name=name).first():
            delete_post =  Favourite_post.objects.get(file=post.pdf, name=name)
            delete_post.delete()
            return redirect('/')
        else:
            save_post = Favourite_post.objects.create(file=post.pdf, name=name)
            save_post.save()
            return redirect('/')

    if post.audio:
        if Favourite_post.objects.filter(file=post.audio, name=name).first():
            delete_post =  Favourite_post.objects.get(file=post.audio, name=name)
            delete_post.delete()
            return redirect('/')
        else:
            save_post = Favourite_post.objects.create(file=post.audio, name=name)
            save_post.save()
            return redirect('/')

@login_required(login_url='login')
def favourites(request):
    user_profile = Profile.objects.get(user=request.user)
    favourites = Favourite_post.objects.filter(name = request.user)

    return render(request,'favourites.html', {'favourites':favourites})

@login_required(login_url='login')
def view_groups(request):
    user_profile = Profile.objects.get(user=request.user)
    group = Group.objects.all()
    return render(request, 'view_groups.html', {'group':group, 'user_profile':user_profile})

@login_required(login_url='login')
def create_group(request):
    if request.method == 'POST':
        group_name = request.POST['group_name']
        group_pic = request.FILES.get('group_pic')
        if Group.objects.filter(name=group_name).exists():
            messages.info(request, 'Group Name Already Exists')
            return redirect('view_groups')
        else:
            group = Group.objects.create(name=group_name)
            return redirect('view_groups')
    else:
        return redirect('view_groups')


@login_required(login_url='login')
def join_group(request):
    if request.method == 'POST':
        user = request.POST['user']
        group = request.POST['group']
        get_group = Group.objects.get(name= group)
        join_group = get_group.user_set.add(user)
        return redirect('view_groups')
    else:
        return redirect('view_groups')

@login_required(login_url='login')
def search_group(request):
    group = Group.objects.all()
    if request.method == 'POST':
        group_name = request.POST['group_name']
        result = Group.objects.filter(name__icontains=group_name)
        return render(request, 'view_groups.html', {'result':result})
    else:
        return render(request, 'view_groups.html',{'group':group})

@login_required(login_url='login')
def group_chat(request,pk):
    get_group = Group.objects.get(name= pk)
    user_profile =  Profile.objects.get(user = request.user)

    return render(request, 'group_chat.html', {'get_group':get_group, 'user_profile':user_profile})

@login_required(login_url='login')
def group_chat_comment(request):
    if request.method == 'POST':
        name = request.POST['name']
        ids = request.POST['ids']
        comment = request.POST['comment']
        group_name = request.POST['group_name']
        profileimage = request.POST['profile_image']

        comments = Group_comment.objects.create(name=name,ids=ids,comment=comment,profileimage=profileimage,group_name=group_name)
        comments.save()
    return HttpResponse(comments.comment)

@login_required(login_url='login')
def get_group_comments(request,pk):
    comments = Group_comment.objects.filter(group_name=pk)
    return JsonResponse({'comments':list(comments.values())})

<<<<<<< HEAD
def view_chats(request):
    users = Profile.objects.exclude(user=request.user)
    user = Profile.objects.exclude(user=request.user)
    for user in user:
        print(user.user)

        # user_id =  user_id.id_user

        # messages = Message.objects.filter(Q(senderId = user_id)|Q(receiverId = user_id))

        # print(messages)

        return render(request, 'view_chats.html', {'users': users, 'messages':messages})
    return render(request, 'view_chats.html', {'users': users})
=======
@login_required(login_url='login')
def view_chats(request):    
    user_profile = Profile.objects.get(user=request.user)    
    # Get the list of Chat objects where the logged-in user is the follower
    chat_friends = Chat.objects.filter(follower=request.user.username)

    # Use a dictionary to store unique chat friends by user
    unique_chat_friends = {}
    
    for chat in chat_friends:
        # Only add if user is not already in the dictionary
        if chat.user not in unique_chat_friends:
            unique_chat_friends[chat.user] = chat

    # Convert dictionary values back to a list
    unique_chat_friends_list = list(unique_chat_friends.values())

    print(unique_chat_friends_list)  # Prints the unique chat objects
    return render(request, 'view_chats.html', {'chat_friends': unique_chat_friends_list, 'user_profile':user_profile})

>>>>>>> de1ee6a44f834efd78a7cc3a2b70f6b2159b744c



@login_required(login_url='login')
def chat(request,user_id):
    print(user_id)
    receiver_profile = Profile.objects.get(id_user=user_id)
    user_profile =  Profile.objects.get(user = request.user)
    print(receiver_profile)
    return render(request, 'chat.html', {'user_profile':user_profile,'receiver_profile':receiver_profile})

# To send message in a chat
@login_required(login_url='login')
def send_chat_message(request):
<<<<<<< HEAD
    if request.method == 'POST':
        print(request.POST)
=======
    if request.method == 'POST':  
>>>>>>> de1ee6a44f834efd78a7cc3a2b70f6b2159b744c
        sender = request.POST['sender']
        receiver = request.POST['receiver']
        profile_image = request.POST['profile_image']
        message = request.POST['message']
        receiverId =  request.POST['receiverId']
        senderId =  request.POST['senderId']

          # Initialize variables for image and video
        image = request.FILES.get('image', None)  # Get image from the request if available
        video = request.FILES.get('video', None)  # Get video from the request if available

        # Base message creation (no image or video)

        messages = Message.objects.create(
            sender=sender,
            receiver=receiver,
            senderId=senderId,
            receiverId=receiverId,
            profileimage=profile_image,
            message=message
        )
        chat_friends = Chat.objects.filter(Q(follower=request.user.username, user=receiver)|Q(follower=receiver, user=request.user.username))
        print(chat_friends)
        if message:
            for friend in chat_friends:
                friend.last_message = str(messages)
                friend.save()
        
        # If image is provided, update the message with the image
        if image:
            fs = FileSystemStorage()
<<<<<<< HEAD
            filename = fs.save('Chat_Image/' + str(image), image)
=======
            filename = fs.save('Chat_Image/' + str(image), image) 
>>>>>>> de1ee6a44f834efd78a7cc3a2b70f6b2159b744c
            image_path = fs.url(filename)
            messages.image = image_path
            messages.save()
            for friend in chat_friends:
                friend.last_message = 'Sent a photo'
                friend.save()

        # If video is provided, update the message with the video
        if video:
            fs = FileSystemStorage()
            filename = fs.save('Chat_Image'+ str(video), video)
            video_path = fs.url(filename)
            messages.video = video_path
            messages.save()
<<<<<<< HEAD

=======
            for friend in chat_friends:
                friend.last_message = 'Sent a video'
                friend.save()
            
>>>>>>> de1ee6a44f834efd78a7cc3a2b70f6b2159b744c
    return HttpResponse('Message sent')

# Get the messages in the chat using id
@login_required(login_url='login')
def get_chat_message(request,pk):
    users = Profile.objects.exclude(Q(user=request.user)|Q(user=request.user))
    user = request.user

    # This is to filter the chat which the sender or receiver has an id
    messages = Message.objects.filter(Q(senderId = pk)|Q(receiverId = pk)).exclude(~Q(sender=user),~Q(receiver=user))
    for message in messages:
        print(message.image)

    return JsonResponse({'messages':list(messages.values())})


@login_required(login_url='login')
def course_outlines(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'courses.html', {'user_profile':user_profile})

# @login_required(login_url='login')
# def favourite_post(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         ids = request.POST['ids']
#         post = Post.objects.get(id=ids)

#         if post.image:
#             if Favourite_post.objects.filter(file=post.image, name=name).first():
#                 delete_post =  Favourite_post.objects.get(file=post.image, name=name)
#                 delete_post.delete()
#                 return HttpResponse('Addfavourites')
#             else:
#                 save_post = Favourite_post.objects.create(file=post.image, name=name)
#                 save_post.save()
#                 return HttpResponse('Remove favourites')

#         if post.video:
#             if Favourite_post.objects.filter(file=post.video, name=name).first():
#                 delete_post =  Favourite_post.objects.get(file=post.video, name=name)
#                 delete_post.delete()
#                 return HttpResponse('Add favourites')
#             else:
#                 save_post = Favourite_post.objects.create(file=post.video, name=name)
#                 save_post.save()
#                 return HttpResponse('Remove favourites')

#         if post.pdf:
#             if Favourite_post.objects.filter(file=post.pdf, name=name).first():
#                 delete_post =  Favourite_post.objects.get(file=post.pdf, name=name)
#                 delete_post.delete()
#                 return HttpResponse('Add favourites')
#             else:
#                 save_post = Favourite_post.objects.create(file=post.pdf, name=name)
#                 save_post.save()
#                 return HttpResponse('Remove favourites')

#         if post.audio:
#             if Favourite_post.objects.filter(file=post.audio, name=name).first():
#                 delete_post =  Favourite_post.objects.get(file=post.audio, name=name)
#                 delete_post.delete()
#                 return HttpResponse('Add favourites')
#             else:
#                 save_post = Favourite_post.objects.create(file=post.audio, name=name)
#                 save_post.save()
#                 return HttpResponse('Remove favourites')

# Handles Student emmergency
@login_required(login_url='login')
def student_emergency(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        body = request.POST['message']
        account_sid = 'AC9753a1bd05b961528a8ecc63a3ba4166'
        auth_token = '91e7266a55e8353b4e038ea056c697d0'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_= '+18042698851',
            body = body,
            to = '+2348072846035'
        )

    return render(request, 'student_emergency.html', {'user_profile':user_profile})

@login_required(login_url='login')
def notifications(request):
    user_profile = Profile.objects.get(user=request.user)
    notifications =  Notifications.objects.all()
    return render(request, 'notifications.html', {'user_profile':user_profile, 'notifications':notifications})

def welcome_page(request):
    return render(request, 'welcome_page.html')