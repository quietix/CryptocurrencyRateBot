from telebot.types import Update
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from src.apply_config_changes import bot
from django.template import loader
from django.shortcuts import render, redirect
from django.apps import apps
from . import handlers


@csrf_exempt
def handle_request(request):
    if request.method == "POST":
        try:
            update = Update.de_json(request.body.decode('utf-8'))
            bot.process_new_updates([update])
            bot.add_message_handler({"/start": handlers.start,
                                     "/help": handlers.help,
                                     "/register": handlers.register,
                                     "/menu": handlers.register})
        except Exception as e:
            print(str(e))
        return HttpResponse('', status=200)
    else:
        return Http404


@csrf_exempt
def admin(request):
    if request.method == "POST":

        if "email" in request.POST and "password" in request.POST:
            email = request.POST.get("email", "")
            password = request.POST.get("password", "")

            admins = apps.get_model('tg_bot_app', 'Admin').objects.all()
            for admin in admins:
                if admin.email == email and admin.password == password:
                    users = apps.get_model('tg_bot_app', 'User').objects.all()
                    accounts = apps.get_model('tg_bot_app', 'Account').objects.all()

                    return render(request, "tg_bot_app/admin_main.html", {"users": users, "accounts": accounts})
            return redirect("/admin/")

        elif "user_id_to_delete" in request.POST:
            try:
                user_id_to_delete = request.POST.get("user_id_to_delete", "")
                user = apps.get_model('tg_bot_app', 'User').objects.get(user_id=user_id_to_delete)
                user.delete()
            except Exception as e:
                print(e)
            finally:
                users = apps.get_model('tg_bot_app', 'User').objects.all()
                accounts = apps.get_model('tg_bot_app', 'Account').objects.all()
                return render(request, "tg_bot_app/admin_main.html", {"users": users, "accounts": accounts})

        elif "account_id_to_delete" in request.POST:
            try:
                account_id_to_delete = request.POST.get("account_id_to_delete", "")
                account = apps.get_model('tg_bot_app', 'Account').objects.get(account_id=account_id_to_delete)
                account.delete()
            except Exception as e:
                print(e)
            finally:
                users = apps.get_model('tg_bot_app', 'User').objects.all()
                accounts = apps.get_model('tg_bot_app', 'Account').objects.all()
                return render(request, "tg_bot_app/admin_main.html", {"users": users, "accounts": accounts})

        elif "add_account_button" in request.POST:
            return render(request, "tg_bot_app/add_account.html")

        elif "go_back_button" in request.POST:
            users = apps.get_model('tg_bot_app', 'User').objects.all()
            accounts = apps.get_model('tg_bot_app', 'Account').objects.all()
            return render(request, "tg_bot_app/admin_main.html", {"users": users, "accounts": accounts})

        elif "user_id_added" in request.POST and "phone_added" in request.POST:
            from .modules.db_manager import DBManager
            db_manager = DBManager()

            user_id = request.POST.get("user_id_added", "")
            phone = request.POST.get("phone_added", "")

            try:
                db_manager.add_account(user_id, phone)

                users = apps.get_model('tg_bot_app', 'User').objects.all()
                accounts = apps.get_model('tg_bot_app', 'Account').objects.all()
                return render(request, "tg_bot_app/admin_main.html", {"users": users, "accounts": accounts})

            except Exception as e:
                print(e)

                users = apps.get_model('tg_bot_app', 'User').objects.all()
                accounts = apps.get_model('tg_bot_app', 'Account').objects.all()
                return render(request, "tg_bot_app/admin_main.html", {"users": users, "accounts": accounts})


    else:
        return render(request, "tg_bot_app/admin_auth.html")