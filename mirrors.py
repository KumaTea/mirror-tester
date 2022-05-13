# Public Mirrors

# Universities
universities = {
    'bfsu': {
        'name': '北京外国语大学',
        'url': 'https://mirrors.bfsu.edu.cn',
        'special': {}
    },
    'bit': {
        'name': '北京理工大学',
        'url': 'https://mirror.bit.edu.cn',
        'special': {}
    },
    'bjtu': {
        'name': '北京交通大学',
        'url': 'https://mirror.bjtu.edu.cn',
        'special': {}
    },
    'bupt': {
        'name': '北京邮电大学',
        'url': 'https://mirrors.bupt.edu.cn',
        'special': {}
    },
    'cqu': {
        'name': '重庆大学',
        'url': 'https://mirrors.cqu.edu.cn',
        'special': {}
    },
    'cqupt': {
        'name': '重庆邮电大学',
        'url': 'https://mirrors.cqupt.edu.cn',
        'special': {}
    },
    'dgut': {
        'name': '东莞理工学院',
        'url': 'https://mirrors.dgut.edu.cn',
        'special': {}
    },
    'hit': {
        'name': '哈尔滨工业大学',
        'url': 'https://mirrors.hit.edu.cn',
        'special': {}
    },
    'lzu': {
        'name': '兰州大学',
        'url': 'https://mirror.lzu.edu.cn',
        'special': {}
    },
    'neusoft': {
        'name': '大连东软信息学院',
        'url': 'https://mirrors.neusoft.edu.cn',
        'special': {}
    },
    'nju': {
        'name': 'NJU Mirror',  # 南京大学
        'url': 'https://mirrors.nju.edu.cn',
        'special': {}
    },
    'njupt': {
        'name': '南京邮电大学',
        'url': 'https://mirrors.njupt.edu.cn',
        'special': {}
    },
    'nwafu': {
        'name': '西北农林科技大学',
        'url': 'https://mirrors.nwafu.edu.cn',
        'special': {}
    },
    'shanghaitech': {
        'name': 'Geekpie',
        'url': 'https://mirrors.shanghaitech.edu.cn',
        'special': {}
    },
    'sjtu': {
        'name': 'sjtu',  # 上海交通大学,
        'url': 'https://mirror.sjtu.edu.cn',
        'special': {}
    },
    'sjtug': {
        'name': 'sjtug',  # 上海交通大学,
        'url': 'https://mirrors.sjtug.sjtu.edu.cn',
        'special': {}
    },
    'tuna': {
        'name': 'TUNA',  # 清华大学
        'url': 'https://mirrors.tuna.tsinghua.edu.cn',
        'special': {}
    },
    'ustc': {
        'name': 'USTC',  # 中国科学技术大学
        'url': 'https://mirrors.ustc.edu.cn',
        'special': {
            'kernel': 'kernel.org'
        }
    },
    'xjtu': {
        'name': '西安交通大学',
        'url': 'https://mirrors.xjtu.edu.cn'
    }
}

commercials = {
    'aliyun': {
        'name': '阿里',
        'url': 'https://mirrors.aliyun.com',
        'special': {}
    },
    'tencent': {
        'name': '腾讯',
        'url': 'https://mirrors.tencent.com',
        'special': {}
    },
    'huawei': {
        'name': '华为',
        'url': 'https://repo.huaweicloud.com',
        'special': {}
    },
    'cn99': {
        'name': 'CN99',
        'url': 'https://mirrors.cn99.com',
        'special': {}
    },
    '163': {
        'name': '网易',
        'url': 'https://mirrors.163.com',
        'special': {}
    },
    'cnnic': {
        'name': 'CNNIC',
        'url': 'https://mirrors.cnnic.cn',
        'special': {}
    },
    'sohu': {
        'name': '搜狐',
        'url': 'https://mirrors.sohu.com',
        'special': {}
    },
    'yun-idc': {
        'name': '首都在线',
        'url': 'https://mirrors.yun-idc.com',
        'special': {}
    },
}

all_mirrors = universities | commercials

# Dismissed mirrors
# 同步镜像过少
# 不向公网开放
dismissed = [
    'dlut'
    'hust'
]
