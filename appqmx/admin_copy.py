# Register your models here.
import datetime

from django.contrib import admin
from django.db import connections

from appqmx.models import KhxT, HtxT, YhxT, CbxT, jhxT
from django.contrib import messages
from django.utils.translation import ngettext
# from django.forms.widgets import


# class CbxTInline(admin.TabularInline):
#     model = CbxT
#
#
# class HtxTInline(admin.TabularInline):
#     # Score 必须是models.py中的模型名称,大小写必须要匹配.这个模型为子表,以便可以被父表编辑
#     model = HtxT
#     # 默认显示条目的数量
#     # extra = 5


class HtxTAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ("user",)
        form = super(HtxTAdmin, self).get_form(request, obj, **kwargs)
        return form

    list_display = (
        'sth_HtID', 'sth_HtyfnamE', 'sth_HtqysJ', 'sth_HtjzsJ', 'sth_HtxH', 'sth_HtjH', 'sth_HtyJ', 'sth_HtjbfwF',
        'sth_HtbyH', 'sth_HtbyC', 'sth_HtczhjE', 'sth_HtczcjE', 'sth_HtcblX', 'sth_HtczzqS', 'HtzlsC')
    readonly_fields = ('sth_HtjfnamE',)
    search_fields = ['sth_HtID', 'stc_CbaecnamE']
    autocomplete_fields = ['sth_HtyfnamE']
    form_layout = ['Ht_delete']
    # 只读
    fields = ('sth_HtID', ('sth_HtyfnamE', 'sth_HtfwdZ'), 'sth_HtpM', ('sth_HtxH', 'sth_HtjH'),
              ('sth_HtyJ', 'sth_HtjbfwF'), ('sth_HtbyH', 'sth_HtbyC'), ('sth_HtczhjE', 'sth_HtczcjE'),
              ('sth_HtqysJ', 'sth_HtjzsJ'), ('sth_HtcblX', 'sth_HtczzqS'), 'HtzlsC')
    actions = ['add_cb']

    def get_queryset(self, request):
        qs = super(HtxTAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    @admin.action(description='生成抄表')
    def add_cb(self, request, queryset):
        ht_list = queryset.values()
        for ht in ht_list:
            # print(ht)
            kh_info = KhxT.objects.filter(stk_KhiD=ht['sth_HtyfnamE_id']).values('stk_KhaecnamE')
            # hc_jhxT = HtxT.objects.filter(sth_HtyfnamE=kh_id).values('sth_HtczhjE', 'sth_HtczcjE', 'sth_HtbyH',
            #                                                          'sth_HtbyC', 'sth_HtjbfwF')
            ht_info = HtxT.objects.filter(sth_HtID=ht['sth_HtID']).values('sth_HtID', 'sth_HtyfnamE', 'user_id', 'sth_HtjH', 'sth_HtxH')
            kh_name = list(kh_info)[0]['stk_KhaecnamE']
            kh_user = list(ht_info)[0]['user_id']
            ht_jH = list(ht_info)[0]['sth_HtjH']
            ht_xH = list(ht_info)[0]['sth_HtxH']
            cb_info = CbxT.objects.filter(stc_CbjH=ht_jH).values('stc_CbqC')

            if not cb_info:
                for i in range(1, int(ht['sth_HtczzqS']) + 1):
                    CbxT.objects.create(stc_CbaecnamE=kh_name, stc_CbqC=i, user_id=kh_user, stc_CbxH=ht_xH,
                                    stc_CbjH=ht_jH)

    add_cb.icon = 'fas el-icon-check'
    add_cb.type = 'primary'


class KhxTAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ("user",)
        form = super(KhxTAdmin, self).get_form(request, obj, **kwargs)
        return form

    list_display = (
        'stk_KhiD', 'stk_KhaecnamE', 'stk_KhjbnamE', 'stk_KhjbdH', 'stk_KhdZ', 'stk_KhlxnamE', 'stk_KhlxdH',
        'stk_KhsydZ', 'stk_KhlB')
    fields = (('stk_KhiD', 'stk_KhaecnamE'), ('stk_KhjbnamE', 'stk_KhjbdH', 'stk_KhdZ'),
              ('stk_KhlxnamE', 'stk_KhlxdH', 'stk_KhsydZ'), 'stk_KhlB',)
    search_fields = ('stk_KhaecnamE', 'stk_KhlB')

    def get_queryset(self, request):
        qs = super(KhxTAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


# class HtxTInline(admin.ModelAdmin):
#   fields = (('sth_HtyfnamE', 'sth_HtqysJ',), 'sth_HtjzsJ',)


# class CbxTInfo(admin.ModelAdmin):
#     def pub_date(self):
#
#
#
#     pub_date.short_description = '发布日期'


class CbxTAdmin(admin.ModelAdmin):
    model = HtxT

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        # export_exec_widget = FileUploadWidget()
        self.exclude = ("user",)
        form = super(CbxTAdmin, self).get_form(request, obj, **kwargs)
        return form

    list_display = (
        'stc_CbqC', 'stc_CbaecnamE', 'stc_CbsycbsJ', 'stc_CbH', 'stc_CbC', 'stc_CbsH', 'stc_CbsC',
        'stc_CbsjH', 'stc_CbsjC', 'stc_CbczhjE', 'stc_CbczcjE', 'stc_CbbyhJ', 'stc_CbbccbsJ', 'stc_CbxH', 'stc_CbjH')
    search_fields = ('stc_CbjH', 'stc_CbaecnamE', 'stc_CbxH')
    list_editable = ['stc_CbC', 'stc_CbH']
    actions = ['gen_cb_data', 'delete_all_data']
    list_filter = ['stc_CbqC']

    def get_queryset(self, request):
        qs = super(CbxTAdmin, self).get_queryset(request)
        id_list = []
        query_result = None
        if request.user.is_superuser:
            with connections['default'].cursor() as cursor:
                cursor.execute('select min(id) from CbxT group by stc_CbjH,stc_CbbccbsJ')
                idlist = cursor.fetchall()
                for item in idlist:
                    id_list.append(item[0])
                query_result = CbxT.objects.filter(id__in=id_list)
            # with connections['default'].cursor() as cursor:
            #     cursor.execute('select min(id) from CbxT group by stc_CbjH,stc_CbbccbsJ')
            #     idlist = cursor.fetchall()
            #     for item in idlist:
            # query_result = CbxT.objects.all()
            # for item in query_result:
            #     # if item['stc_CbH'] != None and item['stc_CbH'] != '' and item['stc_CbC'] != '' and item['stc_CbC'] != None:
            #     pass
            return query_result
        return qs.filter(user=request.user)

    # fields = (('stc_CbqC', 'stc_CbaecnamE'), 'stc_CbsycbsJ', ('stc_CbsH', 'stc_CbsC'), ('stc_CbH', 'stc_CbC'),
    #           ('stc_CbsjH', 'stc_CbsjC'), ('stc_CbczhjE', 'stc_CbczcjE'), 'stc_CbbyhJ')
    # autocomplete_fields = ['stc_CbaecnamE']
    # list_editable = ['stc_CbH', 'stc_CbC']
    # search_fields = ('stc_CbaecnamE__stk_KhaecnamE',)

    @admin.action(description='生成数据')
    def gen_cb_data(self, request, queryset):
        cb_list = queryset.values()
        todaytime = datetime.date.today()
        # print(cb_list)
        for cb in cb_list:
            cb_previous_id = int(cb['stc_CbqC']) - 1
            if cb_previous_id >= 0:
                previous_cb_info = CbxT.objects.filter(stc_CbqC=cb_previous_id).values('stc_CbH', 'stc_CbC', 'stc_CbsH',
                                                                                       'stc_CbsC', 'stc_CbbccbsJ')
                kh_id_res = KhxT.objects.filter(stk_KhaecnamE=cb['stc_CbaecnamE']).values('stk_KhiD')
                kh_id = list(kh_id_res)[0]['stk_KhiD']
                hc_info = HtxT.objects.filter(sth_HtyfnamE=kh_id).values('sth_HtczhjE', 'sth_HtczcjE', 'sth_HtbyH',
                                                                         'sth_HtbyC', 'sth_HtjbfwF')

                hc_jg = list(hc_info)[0]['sth_HtczhjE']
                cc_jg = list(hc_info)[0]['sth_HtczcjE']
                by_h = list(hc_info)[0]['sth_HtbyH']
                by_c = list(hc_info)[0]['sth_HtbyC']
                ht_jbf = list(hc_info)[0]['sth_HtjbfwF']

                if cb_previous_id == 0:
                    previous_h_num = 0
                else:
                    previous_h_num = list(previous_cb_info)[0]['stc_CbH']
                if cb_previous_id == 0:
                    previous_c_num = 0
                else:
                    previous_c_num = list(previous_cb_info)[0]['stc_CbC']
                previous_c_sj = todaytime
                current_h_num = cb['stc_CbH']
                current_c_num = cb['stc_CbC']
                sj_h = int(current_h_num) - int(previous_h_num)
                sj_c = int(current_c_num) - int(previous_c_num)

                if sj_h > by_h:
                    diff_num = sj_h - by_h
                    hc_je = diff_num * hc_jg
                else:
                    hc_je = 0
                if sj_c > by_c:
                    diff_num = sj_c - by_c
                    cc_je = diff_num * cc_jg
                else:
                    cc_je = 0
                told_je = ht_jbf + cc_je + hc_je
                queryset.update(stc_CbsjH=sj_h, stc_CbsjC=sj_c, stc_CbsH=previous_h_num,
                                stc_CbsC=previous_c_num, stc_CbczhjE=hc_je,
                                stc_CbczcjE=cc_je, stc_CbbyhJ=told_je, stc_CbbccbsJ=previous_c_sj, user='1')

    @admin.action(description='删除所有数据')
    def delete_all_data(self, request, queryset):
        # qs = super(CbxTAdmin, self).get_queryset(request)
        all_data = CbxT.objects.all()
        all_data.delete()
        # all_data.commit()

    # delete_all_data.icon = 'fas el-icon-check'
    delete_all_data.type = 'primary'
    gen_cb_data.icon = 'fas el-icon-check'
    gen_cb_data.type = 'primary'


# class CbxtfBAdmin(admin.ModelAdmin):
# list_display = ('dis_level',)
# form_layout = ('sth_ HtjzsJ', 'sth_HtqysJ', 'sth_HtczzqS', 'HtzlsC', 'Ht_delete')


admin.site.register(KhxT, KhxTAdmin)  # 将表在admin中注册
admin.site.register(HtxT, HtxTAdmin)
admin.site.register(YhxT)
admin.site.register(CbxT, CbxTAdmin)
admin.site.register(jhxT)
# admin.site.register(user)
admin.site.site_header = '云启智创ERP测试版'  # 设置header
admin.site.site_title = '云启智创ERP'  # 设置title
admin.site.index_title = '云启智创ERP'
SIMPLEUI_HOME_TITLE = '云启智创ERP'

# SIMPLEUI_DEFAULT_ICON = False
# 服务器信息 隐藏
SIMPLEUI_HOME_INFO = False
