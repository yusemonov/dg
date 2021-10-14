from django.contrib import admin
from cfdns.models import *
from dolphin.models import *
from farming.models import *
from fbprofiles.models import *
from idgenerator.models import *
from gologin_app.models import GoProfiles
from indigo.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
import tablib


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
    list_display = ['status', 'name', 'user_id', ]
    list_filter = ['status', ]


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


class GoProfilesAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'role',
        'id',
        'notes',
        'browserType',
        'lockEnabled',
        'timezone',
        'navigator',
        'geolocation',
        'canBeRunning',
        'os',
        'proxy',
        'proxyType',
        'folders',
        'sharedEmails',
        'shareId',
        'createdAt',
        'updatedAt',
        'lastActivity',

    ]
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


class FarmSheetsResource(resources.ModelResource):

    class Meta:
        model = FarmSheets
        skip_unchanged = True
        report_skipped = True
        # fields = ('f_name', 'creditals', 'phone',
        #           'login_password', 'profile_url', 'dob')
        export_order = ['status', 'f_name', 'creditals', 'phone',
                        'login_password', 'profile_url', 'dob', 'bm_ur']
        exclude = ('invite_to_bm')
        # import_id_fields = ('creditals')


class FarmSheetsAdmin(ImportExportModelAdmin):
    resource_class = FarmSheetsResource

    list_display = ['status', 'f_name', 'creditals',
                    'phone', 'login_password', 'profile_url', 'dob', 'bm_ur']
    # list_display_links = ['status', 'f_name', 'creditals',
    #                       'phone', 'login_password', 'profile_url', 'dob', 'bm_ur']


def get_status():
    value = FarmSheets.objects.all()
    print(value)


admin.site.register(FarmSheets, FarmSheetsAdmin)
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
admin.site.register(GoProfiles, GoProfilesAdmin)
admin.site.register(FarmStages)
admin.site.register(AccountFarming, AccountFarmingAdmin)
admin.site.site_header = 'a13 PowerTool'
admin.site.site_title = 'a13 PowerTool'
create_id.short_description = "Create id"
admin.site.add_action(create_id)
