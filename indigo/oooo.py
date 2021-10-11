# -*- coding: utf-8 -*-
from cfdns.models import *
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.core import serializers
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from dolphin.models import *
from farming.models import *
from fbprofiles.models import *
from idgenerator.models import *
from django.urls import path


from indigo.models import *
import pickle

# Действия администратора


def create_id(model, request, queryset):
    opts = Doc._meta.get_fields()

    print(opts)


@admin.action(description='Загрузить в дельфин')
def dolphin_loader(modeladmin, request, queryset):
    queryset.update(is_add_dolphin=True)


class AccountsFacebookAdmin(admin.ModelAdmin):
    list_display = ['fb_verbname', 'fb_fname', 'fb_lname', 'fb_login',
                    'fb_pass', 'fb_dob', 'fb_eaab', ]


class ListsProxyAdmin(admin.ModelAdmin):
    list_display = ['ip', 'protocol', 'anonymity',
                    'country', 'city', 'is_valid']
    readonly_fields = ['ip', 'protocol', 'anonymity',
                       'country', 'city', 'is_valid']
    search_fields = ("country__startswith", )
    list_filter = ('anonymity', 'protocol')
    list_per_page = 10


class IndigoProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'browser', 'network', 'notes', 'is_add', 'uuid']
    # actions = [export_as_json]


class DolphinInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_id',)


class ProfileCreditationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'token', 'certtoken')


class DomainsAdmin(admin.ModelAdmin):
    list_display = ('cf_id', 'name', 'status', 'paused', 'type', 'development_mode', 'name_servers_1', 'name_servers_2', 'original_name_servers',
                    'original_registrar', 'original_dnshost', 'modified_on', 'created_on', 'activated_on', 'meta', 'owner', 'account', 'permissions')
    readonly_fields = ('cf_id', 'name', 'status', 'owner', 'account')
    list_filter = ('owner',)


class AccountFarmingAdmin(admin.ModelAdmin):
    list_display = ('farmer', 'fb_account')


class DocAdmin(admin.ModelAdmin):
    list_display = ['typedoc', 'country',
                    'surname', 'given_name', 'passport_number', 'genre', 'nationality', 'birth_date', 'personal_number', 'locations', 'data_start',
                    'exp_date', 'issuing', 'get_exif_info']
    actions = [create_id]


class DolphinLoaderAdmin(admin.ModelAdmin):
    list_display = ['cookies', 'login', 'password', 'email', 'comments',
                    'is_add_dolphin', 'is_add_indigo', 'is_add_gologin']
    readonly_fields = ['is_add_dolphin', 'is_add_indigo', 'is_add_gologin']
    actions = [dolphin_loader]

# @admin.register(DolphinLoader)
# class DolphinLoaderAdmin(admin.ModelAdmin):
#     change_list_template = "admin/monitor_change_list.html"

#     def get_urls(self):
#         urls = super(DolphinLoaderAdmin, self).get_urls()
#         custom_urls = [
#             path('check_token/', self.check_token, name='check_token')
#             ]
#         return custom_urls + urls

#     def check_token_btmp(self, request):
#         check_token = TokenCheck()
#         count = check_token.import_data()
#         self.message_user(request, f"создано {count} новых записей")
#         return HttpResponseRedirect("../")


admin.site.register(DolphinLoader, DolphinLoaderAdmin)
admin.site.register(Domains, DomainsAdmin)
admin.site.register(ProfileCreditations, ProfileCreditationsAdmin)
admin.site.register(AccountsFacebook, AccountsFacebookAdmin)
admin.site.register(ListsProxy, ListsProxyAdmin)
admin.site.register(IndigoProfile, IndigoProfileAdmin)
admin.site.register(DolphinInfo, DolphinInfoAdmin)
admin.site.register(DolphinPermissions)
admin.site.register(Cookies)
admin.site.register(Doc, DocAdmin)
admin.site.register(Gologin)
admin.site.register(FarmStages)
admin.site.register(AccountFarming, AccountFarmingAdmin)
admin.site.site_header = 'a13 PowerTool'
admin.site.site_title = 'a13 PowerTool'
create_id.short_description = "Create id"
admin.site.add_action(create_id)
# admin.site.add_action(make_published, 'export_selected')
# admin.site.add_action(export_as_json)
# admin.site.register(Farm, FarmAdmin)
# @admin.action(description='Создать профили в индиго')
# def export_as_json(modeladmin, request, queryset):
#     opts = modeladmin.model._meta
#     fields = [field for field in opts.get_fields(
#     ) if not field.many_to_many and not field.one_to_many]
#     for obj in queryset:
#         # for field in fields:
#         name = obj.name
#         browser = obj.browser
#         os = obj.os
#         notes = obj.notes
#         # value = getattr(obj, field.name)
#     body = {
#         "name": name,
#         "browser": browser,
#         "os": os,
#         "notes": notes,
#     }
#     headers = {
#         'accept': 'application/json',
#         'Content-Type': 'application/json'
#     }
#     url = 'http://localhost.multiloginapp.com:45000/api/v2/profile'
#     # json_data = json.dumps(body)
#     request = requests.post(url, data=json.dumps(body), headers=headers)
#     out = request.json()
#     res = out['uuid']
#     u = IndigoProfile.objects.get(name=body['name'])
#     u.uuid = res
#     u.is_add = True
#     u.save()


# class FarmAdmin(admin.ModelAdmin):
#     list_display = ('farmer', 'get_farm_stages', 'get_accounts_facebook',)
#     list_display_links = ('farmer', 'get_accounts_facebook',)


# @admin.display(description='Аккаунт фб')
# def get_accounts_facebook(self, obj):
#     return format(obj.accounts_facebook)

# @admin.display(description='Стадия Фарма')
# def get_farm_stages(self, obj):
#     return format(obj.farm_stages)
# @admin.action(description='Get dns', permissions=['change'])
# def make_published(self, request, queryset):
#     cf = CloudFlare.CloudFlare(
#         email='whitetech.lp@gmail.com', token='ff029fbbc9b791bac44bba34f88b3738bea3f')
#     zones = cf.zones.get()
#     for zone in zones[0:20]:

#         name = zone.get('name')
#         status = zone.get('status')
#         paused = zone.get('paused')
#         type = zone.get('type')
#         development_mode = zone.get('development_mode')
#         name_servers = zone.get('name_servers')
#         original_name_servers = zone.get('original_name_servers')
#         original_registrar = zone.get('original_registrar')
#         original_dnshost = zone.get('original_dnshost')
#         modified_on = zone.get('modified_on')
#         created_on = zone.get('created_on')
#         activated_on = zone.get('activated_on')
#         meta = zone.get('meta')
#         owner = zone.get('owner')
#         account = zone.get('account')
#         permissions = zone.get('permissions')
#         updated = queryset.update(name=name)
#         self.message_user(request, updated, messages.SUCCESS)
