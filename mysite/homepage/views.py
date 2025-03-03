from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    return render(request, 'homepage/index.html')

def send_feedback(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')  
        user_message = request.POST.get('message')  

        if user_email and user_message:
            try:
                
                email_body = f"Message from: {user_email}\n\n{user_message}"

                
                send_mail(
                    subject="New Hire Me Request",  
                    message=email_body,  
                    from_email='baginski.oleksii@gmail.com', 
                    recipient_list=['baginski.oleksii@gmail.com'],  
                    fail_silently=False,
                )
                
                messages.success(request, "Message sent! I will reply to you as soon as possible.")
            except Exception as e:
                
                messages.error(request, f"An error occurred: {e}")
        else:
            
            messages.error(request, "Please fill in all fields.")

        return redirect('home')  

    return redirect('home')