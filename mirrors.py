from inspect import currentframe, getframeinfo


# Public Mirrors

# Universities
# https://mirrors.cernet.edu.cn/site
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
        'comments': ''
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
        'comments': ''
    },
    'hit': {
        'name': '哈尔滨工业大学',
        'url': 'https://mirrors.hit.edu.cn',
        'special': {},
        'comments': ''
    },
    'iscas': {
        'name': 'ISCAS',  # 中科院
        'url': 'https://mirror.iscas.ac.cn/',
        'special': {},
        'comments': ''
    },
    'lzu': {
        'name': '兰州大学',
        'url': 'https://mirror.lzu.edu.cn',
        'special': {},
        'comments': ''
    },
    'neusoft': {
        'name': '大连东软信息学院',
        'url': 'https://mirrors.neusoft.edu.cn',
        'special': {},
        'comments': ''
    },
    'nju': {
        'name': '南京大学',  # 南京大学
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
        'name': '上海科技大学',
        'url': 'https://mirrors.shanghaitech.edu.cn',
        'special': {},
        'comments': ''
    },
    'sjtu': {
        'name': '上交 sjtu',  # 上海交通大学,
        'url': 'https://mirror.sjtu.edu.cn',
        'special': {},
        'comments': '与 sjtug 互补'
    },
    'sjtug': {
        'name': '上交 sjtug',  # 上海交通大学,
        'url': 'https://mirrors.sjtug.sjtu.edu.cn',
        'special': {},
        'comments': '与 sjtu 互补'
    },
    'sustech': {
        'name': '南方科技大学',
        'url': 'https://mirrors.sustech.edu.cn',
        'special': {},
        'comments': ''
    },
    'tuna': {
        'name': '清华大学 TUNA',  # 清华大学
        'url': 'https://mirrors.tuna.tsinghua.edu.cn',
        'special': {},
        'comments': ''
    },
    'ustc': {
        'name': '中科大 USTC',  # 中国科学技术大学
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
        'name': '中大 Matrix',
        'url': 'https://mirrors.matrix.moe',
        'special': {},
        'comments': '内网 [FS](mirrors.py#L{})'.format(getframeinfo(currentframe()).lineno - 7)
    },
    'zju': {
        'name': '浙江大学',
        'url': 'https://mirrors.zju.edu.cn',
        'special': {},
        'comments': ''
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
    '163': {
        'name': '网易',
        'url': 'https://mirrors.163.com',
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
