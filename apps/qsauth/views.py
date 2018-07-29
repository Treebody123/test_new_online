from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import login,logout
from .forms import LoginForm
from django.contrib import messages
from django.shortcuts import redirect,reverse
from django.contrib.auth import authenticate

# Create your views here.


class LoginView(View):
    def get(self,request):
        return render(request,'auth/login.html')

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                if remember:
                    # 如果设置过期时间为None，那么就会使用默认的过期时间
                    # 默认的过期时间是2个礼拜，也就是14天
                    request.session.set_expiry(None)
                else:
                    # 如果设置过期时间为0，那么浏览器关闭以后就会结束
                    request.session.set_expiry(0)
                # 如果登录成功，让他跳转到首页
                return redirect(reverse('cms:index'))
            else:
                messages.info(request,'Username/Password is not correct！')
                return redirect(reverse('qsauth:login'))
        else:
            messages.info(request,'Username/Password is not correct！')
            return redirect(reverse('qsauth:login'))

def logout_view(request):
    logout(request)
    return redirect('/')