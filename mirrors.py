# Public Mirrors

# Universities
universities = {
    'bfsu': {
        'name': '北京外国语大学',
        'url': 'https://mirrors.bfsu.edu.cn',
        'special': {},
        'comments': ''
    },
    'bit': {
        'name': '北京理工大学',
        'url': 'https://mirror.bit.edu.cn',
        'special': {},
        'comments': '禁 Ping'
    },
    'bjtu': {
        'name': '北京交通大学',
        'url': 'https://mirror.bjtu.edu.cn',
        'special': {},
        'comments': ''
    },
    'bupt': {
        'name': '北京邮电大学',
        'url': 'https://mirrors.bupt.edu.cn',
        'special': {},
        'comments': ''
    },
    'cqu': {
        'name': '重庆大学',
        'url': 'https://mirrors.cqu.edu.cn',
        'special': {},
        'comments': ''
    },
    'cqupt': {
        'name': '重庆邮电大学',
        'url': 'https://mirrors.cqupt.edu.cn',
        'special': {},
        'comments': '禁 Ping'
    },
    'dgut': {
        'name': '东莞理工学院',
        'url': 'https://mirrors.dgut.edu.cn',
        'special': {},
        'comments': '禁 Ping'
    },
    'hit': {
        'name': '哈尔滨工业大学',
        'url': 'https://mirrors.hit.edu.cn',
        'special': {},
        'comments': ''
    },
    'lzu': {
        'name': '兰州大学',
        'url': 'https://mirror.lzu.edu.cn',
        'special': {},
        'comments': '禁 Ping'
    },
    'neusoft': {
        'name': '大连东软信息学院',
        'url': 'https://mirrors.neusoft.edu.cn',
        'special': {},
        'comments': ''
    },
    'nju': {
        'name': 'NJU Mirror',  # 南京大学
        'url': 'https://mirrors.nju.edu.cn',
        'special': {},
        'comments': ''
    },
    'njupt': {
        'name': '南京邮电大学',
        'url': 'https://mirrors.njupt.edu.cn',
        'special': {},
        'comments': ''
    },
    'nwafu': {
        'name': '西北农林科技大学',
        'url': 'https://mirrors.nwafu.edu.cn',
        'special': {},
        'comments': ''
    },
    'shanghaitech': {
        'name': 'Geekpie',
        'url': 'https://mirrors.shanghaitech.edu.cn',
        'special': {},
        'comments': ''
    },
    'sjtu': {
        'name': 'sjtu',  # 上海交通大学,
        'url': 'https://mirror.sjtu.edu.cn',
        'special': {},
        'comments': ''
    },
    'sjtug': {
        'name': 'sjtug',  # 上海交通大学,
        'url': 'https://mirrors.sjtug.sjtu.edu.cn',
        'special': {},
        'comments': ''
    },
    'tuna': {
        'name': 'TUNA',  # 清华大学
        'url': 'https://mirrors.tuna.tsinghua.edu.cn',
        'special': {},
        'comments': ''
    },
    'ustc': {
        'name': 'USTC',  # 中国科学技术大学
        'url': 'https://mirrors.ustc.edu.cn',
        'special': {
            'kernel': 'kernel.org'
        },
        'comments': ''
    },
    'xjtu': {
        'name': '西安交通大学',
        'url': 'https://mirrors.xjtu.edu.cn',
        'special': {},
        'comments': ''
    },
    'sysu': {
        # This mirror should be excluded
        # since it only opens to its
        # internal networks, but it's joined
        # here to act as a failsafe test.
        # INDEX_POINT_SYSU
        'name': 'SYSU Matrix',
        'url': 'https://mirrors.matrix.moe',
        'special': {},
        # 'comments': '内网 [FS](mirrors.py#L{})'.format(open('mirrors.py', 'r', encoding='utf-8').read()[:open('mirrors.py', 'r', encoding='utf-8').read().index('INDEX_POINT_SYSU')].count('\n'))
        'comments': '内网 [FS](mirrors.py#L{})'.format((f := open('mirrors.py', 'r', encoding='utf-8')).read()[:(f.close() or (g := open('mirrors.py', 'r', encoding='utf-8')).read().index('INDEX_POINT_SYSU'))].count('\n') + (g.close() or 0))
    },
}

commercials = {
    'aliyun': {
        'name': '阿里',
        'url': 'https://mirrors.aliyun.com',
        'special': {},
        'comments': ''
    },
    'tencent': {
        'name': '腾讯',
        'url': 'https://mirrors.tencent.com',
        'special': {},
        'comments': ''
    },
    'huawei': {
        'name': '华为',
        'url': 'https://repo.huaweicloud.com',
        'special': {},
        'comments': '主站域名不同'
    },
    'cn99': {
        'name': 'CN99',
        'url': 'https://mirrors.cn99.com',
        'special': {},
        'comments': ''
    },
    '163': {
        'name': '网易',
        'url': 'https://mirrors.163.com',
        'special': {},
        'comments': ''
    },
    'cnnic': {
        'name': 'CNNIC',
        'url': 'https://mirrors.cnnic.cn',
        'special': {},
        'comments': ''
    },
    'sohu': {
        'name': '搜狐',
        'url': 'https://mirrors.sohu.com',
        'special': {},
        'comments': ''
    },
    'yun-idc': {
        'name': '首都在线',
        'url': 'https://mirrors.yun-idc.com',
        'special': {},
        'comments': ''
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
