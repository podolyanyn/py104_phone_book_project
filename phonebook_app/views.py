from django.shortcuts import render


def index(request):
    return render(request, 'phonebook_app/index.html')


def login(request):
    pass


def register():
    pass


def logout():
    pass


def add_contact(request):
    return render(request, 'phonebook_app/add_contact.html')


def contact_detail(request):
    return render(request, 'phonebook_app/contact_detail.html')


def edit_contact(request):
    return render(request, 'phonebook_app/edit_contact.html')


def delete_contact(request):
    return render(request, 'phonebook_app/delete_contact.html')


def contact_list(request):
    return render(request, 'phonebook_app/contact_list.html')


def search_contact(request):
    pass
