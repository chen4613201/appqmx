"""
Django settings for YQZCCC project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#fl+q3%*lw(jc2pht=(qwr+#nj4k$0p7sk+ir+xzo*&lga_#7*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appqmx.apps.AppqmxConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoProject1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoProject1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'yqzccc',
    #     'USER': 'root',
    #     'PASSWORD': '123456',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    #     'OPTIONS': {
    #         "init_command": "SET foreign_key_checks = 0;",
    #     },
    # }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_I10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# SIMPLEUI_LOGO = 'http://qungz.photo.store.qq.com/qun-qungz/pgXWi*1gjoDCagh.kCq.Tw!!/V5bCQAyMjE4NTcwMzXpZgFiNbL1Ag
# !!/800?w5=362&h5=354&rf=viewer_421' SIMPLEUI_INDEX = 'https://www.baidu.com' 隐藏右侧SimpleUI广告链接
SIMPLEUI_HOME_INFO = False
SIMPLEUI_LOADING = False  # 显示加载遮罩层
SIMPLEUI_CONFIG = {
    # 是否使用系统默认菜单，自定义菜单时建议关闭。
    'system_keep': False,

    # 用于菜单排序和过滤, 不填此字段为默认排序和全部显示。空列表[] 为全部不显示.
    'menu_display': ['抄表系统', '合同管理', '客户管理', '设备管理', '考勤管理', '运维数据待', '基本配置'],

    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时刷新展示菜单内容。
    # 一般建议关闭。
    'dynamic': False,
    'menus': [
        {
            'appqmx': 'auth',
            'name': '权限认证',
            'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': '用户列表',
                    'icon': 'fa fa-user',
                    'url': 'auth/user/'
                },
                {
                    'name': '用户组',
                    'icon': 'fa fa-users',
                    'url': 'auth/group/'
                }
            ]
        },
        {
            'name': '基本配置',
            'icon': 'fa fa-tasks',
            'models': [
                {
                    'name': '基本配置',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': 'appqmx/jbxt/',
                    'icon': 'fa fa-feather-alt'
                },
            ]
        },
        {
            'name': '运维数据待',
            'icon': 'fa fa-tasks',
            'models': [
                {
                    'name': '待完善',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    # 'url': '/admin/tasks/task/',
                    'icon': 'fa fa-feather-alt'
                },
            ]
        },
        {
            'name': '考勤管理',
            'icon': 'fa fa-tasks',
            'models': [
                {
                    'name': '待完善',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    # 'url': '/admin/tasks/task/',
                    'icon': 'fa fa-feather-alt'
                },
            ]
        },
        {
            'name': '客户管理',
            'icon': 'fa fa-tasks',
            'models': [
                {
                    'name': '客户录入',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': 'appqmx/khxt/',
                    'icon': 'fa fa-feather-alt'
                },
                {
                    'name': '历史记录',
                    'icon': 'fa fa-history',
                    # 'url': 'auth/group/'
                }
            ]
        },
        {
            'name': '合同管理',
            'icon': 'fa fa-tasks',
            'models': [
                {
                    'name': '合同录入',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': 'appqmx/htxt/',
                    'icon': 'fa fa-feather-alt'
                },
                {
                    'name': '历史记录',
                    'icon': 'fa fa-users',
                    # 'url': 'auth/group/'
                }
            ]
        },
        {
            'name': '抄表系统',
            'icon': 'fa fa-tasks',
            'models': [{
                'name': '已抄表数据',
                # 注意url按'/admin/应用名小写/模型名小写/'命名。
                'url': 'appqmx/cbxt/',
                'icon': 'fa fa-feather-alt'
            },
            {
                'name': '未抄表数据',
                # 注意url按'/admin/应用名小写/模型名小写/'命名。
                'url': 'appqmx/cbxtproxy/',
                'icon': 'fa fa-feather-alt'
            },
            {
                'name': '历史记录',
                'icon': 'fa fa-history',
                # 'url': 'auth/group/'
            }
            ]
        },
        {
            'name': '设备管理',
            'icon': 'fa fa-tasks',
            'models': [{
                'name': '设备录入',
                # 注意url按'/admin/应用名小写/模型名小写/'命名。
                'url': 'appqmx/jhxt/',
                'icon': 'fa fa-feather-alt'
            },
            {
                'name': '历史记录',
                'icon': 'fa fa-history',
                # 'url': 'auth/group/'
            }
            ]
        },
    ]
}

# SIMPLEUI_LOGO = 'http://qungz.photo.store.qq.com/qun-qungz/pgXWi*1gjoDCagh.kCq.Tw!!/V5bCQAyMjE4NTcwMzXpZgFiNbL1Ag
# !!/800?w5=362&h5=354&rf=viewer_421' SIMPLEUI_INDEX = 'https://www.baidu.com' 隐藏右侧SimpleUI广告链接
SIMPLEUI_HOME_INFO = False
SIMPLEUI_LOADING = False  # 显示加载遮罩层
# 1、最近动作
# 隐藏：
# SIMPLEUI_HOME_ACTION = False
# 显示：
# SIMPLEUI_HOME_ACTION = True
# 2、快速操作
# 隐藏：
SIMPLEUI_HOME_QUICK = False
# 显示：
# SIMPLEUI_HOME_QUICK = True
# 3、关闭登录页粒子动画
SIMPLEUI_LOGIN_PARTICLES = False
# 使用分析
SIMPLEUI_ANALYSIS = False
# 设置默认主题，指向主题css文件名。红色风格
SIMPLEUI_DEFAULT_THEME = 'e-red.css'
SIMPLEUI_HOME_ICON = 'fa fa-user'
# simpleui 是否以脱机模式加载静态资源
SIMPLEUI_STATIC_OFFLINE = True