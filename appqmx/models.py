from django.db import models

# Create your models here.
import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.views.decorators.http import condition

import appqmx.models


class YhxT(models.Model):
    """用户信息"""
    SEX_CHOICE = (
        ('0', '男'),
        ('1', '女'),
    )
    stu_UxtimE = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    stu_UxnuM = models.BigIntegerField(primary_key=True, verbose_name="账号")
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    stu_UxpwD = models.CharField(max_length=32, verbose_name="密码")
    stu_UxnamE = models.CharField(max_length=32, verbose_name="姓名")
    stu_UxmZ = models.CharField(max_length=32, verbose_name="民族")
    stu_UxxB = models.CharField(max_length=10, choices=SEX_CHOICE, verbose_name='性别', default='男')
    stu_Uxphone = models.CharField(max_length=11, unique=True, verbose_name="手机号码")
    stu_UxzY = models.CharField(max_length=32, verbose_name="专业", blank=True)
    stu_UxjG = models.CharField(max_length=32, verbose_name="籍贯", blank=True)
    stu_UxsR = models.DateField(max_length=32, verbose_name="生日", blank=True)

    # 就职日期    #  是否在职  # 离职日期
    class Meta:
        # 末尾不加s
        db_table = 'YhxT'
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.stu_UxnamE


def khgetohtid():
    last_khid = KhxT.objects.all().order_by('stk_KhiD').last()
    if not last_khid:
        return 'YQ' + '0000001'
    KhiD_no = last_khid.stk_KhiD
    KhiD_int = int(KhiD_no.split('YQ')[-1])
    new_KhiD_int = KhiD_int + 1
    new_invoice_no = 'YQ000000' + str(new_KhiD_int)
    return new_invoice_no


class KhxT(models.Model):
    """客户信息"""

    LB_CHOICE = (
        ('0', 'A'), ('1', 'B'), ('2', 'C'), ('3', 'D'), ('4', 'E'), ('5', 'F'), ('6', 'G'))
    stk_KhiD = models.CharField(primary_key=True, max_length=11, default=khgetohtid, verbose_name="客户编号")
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    stk_KhaecnamE = models.CharField(max_length=25, verbose_name="企业名称")
    stk_KhjbnamE = models.CharField(max_length=32, verbose_name="经办人")
    stk_KhjbdH = models.CharField(max_length=32, verbose_name="电话联系方式")
    stk_KhdZ = models.CharField(max_length=32, verbose_name="企业地址")
    stk_KhlxnamE = models.CharField(max_length=32, verbose_name="联系人", blank=True)
    stk_KhlxdH = models.CharField(max_length=32, verbose_name="电话联系方式", blank=True)
    stk_KhsydZ = models.CharField(max_length=32, verbose_name="设备使用地址", blank=True)
    stk_KhlB = models.CharField(max_length=32, choices=LB_CHOICE, verbose_name="客户类别")
    # stk_KhlB = models.CharField(max_length=32, choices=LB_CHOICE, verbose_name="客户类别")

    class Meta:
        # 末尾不加s
        db_table = 'KhxT'
        verbose_name = '客户信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.stk_KhaecnamE


class KhlB(models.Model):
    """客户类别表"""
    stk_KbiD = models.BigIntegerField(primary_key=True, verbose_name="类别")
    stk_KbxQ = models.CharField(max_length=32, verbose_name="详情")

    class Meta:
        # 末尾不加s
        db_table = 'KhlB'
        verbose_name = '客户类别表"'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.stk_KbiD


class jhxT(models.Model):
    """机号别表"""
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    jhb_pM = models.CharField(max_length=32, verbose_name="品名")
    jhb_xH = models.CharField(max_length=32, verbose_name="型号")
    jhb_JxiD = models.CharField(max_length=32, verbose_name="机号")
    jhb_delete = models.BooleanField(default=False)

    class Meta:
        # 末尾不加s
        db_table = 'jhxT'
        verbose_name = '机号别表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s' % (self.jhb_JxiD)


class JbxT(models.Model):
    """基本信息"""
    stj_JbkhM = models.CharField(max_length=32, default='福建省云启智创科技有限公司', verbose_name="开户名")
    stj_JbkhH = models.CharField(max_length=32, verbose_name="开户行")
    stj_JbyhzH = models.CharField(max_length=32, verbose_name="账号")
    stj_JbjbnamE = models.CharField(max_length=32, verbose_name="经办人")
    stj_JbjbPN = models.CharField(max_length=11, verbose_name="联系电话")
    stj_JbbZ = models.CharField(max_length=255, verbose_name="备注")

    class Meta:
        # 末尾不加s
        db_table = 'JbxT'
        verbose_name = '基本信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.stj_JbkhM


def htgetohtid():
    last_invoice = HtxT.objects.all().order_by('sth_HtID').last()
    todaytime = datetime.datetime.now()
    if not last_invoice:
        return "HT" + todaytime.strftime('%Y%m%d') + '00001'
    invoice_no = last_invoice.sth_HtID
    invoice_int = int(invoice_no.split('HT')[-1])
    new_invoice_int = invoice_int + 1
    new_invoice_no = 'HT' + str(new_invoice_int)
    return new_invoice_no


class HtxT(models.Model):
    SEX_CHOICE = (
        ('0', '月'),
        ('1', '季'),
    )
    sth_HtID = models.CharField(primary_key=True, max_length=32, default=htgetohtid, verbose_name="合同编号")
    sth_HtqssJ = models.DateField(auto_now_add=True, verbose_name="合同记录起始时间")
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    sth_HtyfnamE = models.ForeignKey(KhxT, on_delete=models.CASCADE, verbose_name="客户名称")
    sth_HtjfnamE = models.CharField(max_length=32, default='福建省云启智创科技有限公司', verbose_name="甲方名称")
    sth_HtjH = models.ManyToManyField(to=jhxT, verbose_name='机号')
    # sth_HtjH = models.CharField(max_length=10, verbose_name="机号")
    sth_HtfwdZ = models.CharField(max_length=32, verbose_name="服务地点")
    sth_HtyJ = models.DecimalField(max_digits=7, decimal_places=0, verbose_name="押金金额")
    sth_HtjbfwF = models.DecimalField(max_digits=7, decimal_places=0, verbose_name="基本费")
    sth_HtbyC = models.DecimalField(max_digits=7, decimal_places=0, verbose_name="包印彩")
    sth_HtbyH = models.DecimalField(max_digits=7, decimal_places=0, verbose_name="包印黑")
    sth_HtczhjE = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="超张黑金")
    sth_HtczcjE = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="超张彩金")
    sth_HtcblX = models.CharField(max_length=10, choices=SEX_CHOICE, default='月', verbose_name="抄表类型")
    sth_HtqysJ = models.DateField(verbose_name="合同生效时间")
    sth_HtjzsJ = models.DateField(verbose_name="合同到期时间")
    sth_HtczzqS = models.CharField(max_length=32, verbose_name="总期数", blank=True, default=12)
    HtzlsC = models.FileField(upload_to='static/images/yyzz/', verbose_name="合同资料上传", blank=True)
    Ht_delete = models.BooleanField(default=False, verbose_name="可抄表")

    class Meta:
        # 末尾不加s
        db_table = 'HtxT'
        verbose_name = '合同信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s' % self.sth_HtID




class CbxT(models.Model):
    """抄表系统"""
    stc_CbqC = models.CharField(max_length=10, verbose_name="抄表期次")
    stc_CbaecnamE = models.CharField(max_length=32, verbose_name="抄表客户信息")
    stc_CbsycbsJ = models.CharField(max_length=32, verbose_name="上月抄表时间", blank=True)
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    stc_CbbccbsJ = models.CharField(max_length=32, verbose_name="本月抄表时间")
    stc_Htbh = models.CharField(max_length=32, verbose_name="合同编号", default=None, blank=True, null=True)
    stc_CbH = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="本月黑",default=0, blank=True, null=True)
    stc_CbC = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="本月彩",default=0, blank=True, null=True)
    stc_CbsH = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="上月黑",default=0, blank=True, null=True)
    stc_CbsC = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="上月彩",default=0, blank=True, null=True)
    stc_CbsjH = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="实际黑",default=0, blank=True, null=True)
    stc_CbsjC = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="实际彩",default=0, blank=True, null=True)
    stc_CbczhjE = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="超张黑金额",default=0, blank=True, null=True)
    stc_CbczcjE = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="超张彩金额",default=0, blank=True, null=True)
    stc_CbbyhJ = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="本机合计",default=0, blank=True, null=True)
    stc_CbxH = models.CharField(max_length=32, verbose_name="型号", null=True)
    stc_CbjH = models.CharField(max_length=32, verbose_name="机号", null=True)

    class Meta:
        db_table = 'CbxT'
        verbose_name = '抄表系统'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.stc_CbqC


class CbxTProxy(CbxT):
    class Meta:
        proxy = True
        verbose_name = '未抄表数据'
        verbose_name_plural = verbose_name