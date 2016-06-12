from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from core.forms import UserEditForm, UserFinancialSettingsForm
from core.models import UserFinancialSettings


@login_required
def home(request):
    print "IP Address for debug-toolbar: " + request.META['REMOTE_ADDR']
    return redirect('users_list')


class UserListView(ListView):
    model = get_user_model()
    template_name = 'users/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(UserListView, self).get_context_data(*args, **kwargs)
        context['userfinancialsettings_list'] = UserFinancialSettings.objects.all()
        return context


@login_required
def edit_user(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    try:
        userfinancial = UserFinancialSettings.objects.get(user_id=user_id)
    except Exception, e:
        userfinancial = None

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=user, prefix='user')
        if user_form.prefix in request.POST:
            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'Successfully updated user account.')
            else:
                messages.error(request, 'There was an error, please check your input.')

        userfinancial_form = UserFinancialSettingsForm(request.POST, instance=userfinancial, prefix='financial')
        if userfinancial_form.prefix in request.POST:
            if userfinancial_form.is_valid():
                userfinancial = userfinancial_form.save(commit=False)
                userfinancial.user_id = user_id
                userfinancial.save()
                messages.success(request, 'Successfully updated user financial settings.')
            else:
                messages.error(request, 'There was an error, please check your input.')

        return redirect('users_list')

    # if request.method == 'POST':
    #     user_form = UserEditForm(request.POST, instance=user)
    #     if user_form.is_valid():
    #         user_form.save()

    #         messages.success(request, 'Successfully updated user account.')
    #         return redirect('users_list')
    else:
        user_form = UserEditForm(instance=user, prefix='user')
        userfinancial_form = UserFinancialSettingsForm(instance=userfinancial, prefix='financial')

    return render(request, 'users/edit.html', {
        'user' : user,
        'form' : user_form,
        'financial' : userfinancial_form,
    })
