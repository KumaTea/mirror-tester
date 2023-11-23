# Mirror Tester
镜像源速度测试脚本

为选择困难症提供最好的镜像

## 评分标准

| 项目 | 权重 |
| --- | --- |
| 小文件速度 | 48 |
| 大文件速度 | 36 |
| Ping | 10 |
| 丰富度 | 6 |

## 测试结果示例
* 时间：2023-11-22
* 位置：广东
* 网络：中国移动
* 带宽：200 Mbps (25 M/s)

| 镜像 | 类型 | Ping | 小文件 | 大文件 | 丰富度 | 总分 | 排名 | 备注 |
| --- | --- | --: | --: | --: | --: | --: | --- | --- |
| [南方科技大学](https://mirrors.sustech.edu.cn) | 高校 | 7.52 | 83.29 KB/s | 14.56 MB/s | 14/16 | 100.00 | 1 |  |
| [中科大 USTC](https://mirrors.ustc.edu.cn) | 高校 | 24.32 | 67.37 KB/s | 17.88 MB/s | 15/16 | 99.39 | 2 |  |
| [华为](https://repo.huaweicloud.com) | 商业 | 11.02 | 158.78 KB/s | 3.11 MB/s | 15/16 | 99.37 | 3 | 主站域名不同 |
| [北京外国语大学](https://mirrors.bfsu.edu.cn) | 高校 | 40.50 | 59.55 KB/s | 20.69 MB/s | 16/16 | 96.59 | 4 |  |
| [ISCAS](https://mirror.iscas.ac.cn/) | 高校 | 42.09 | 38.29 KB/s | 18.04 MB/s | 14/16 | 92.19 | 5 |  |
| [腾讯](https://mirrors.tencent.com) | 商业 | 10.41 | 32.96 KB/s | 11.61 MB/s | 11/16 | 89.73 | 6 |  |
| [西北农林科技大学](https://mirrors.nwafu.edu.cn) | 高校 | 42.52 | 57.10 KB/s | 21.05 MB/s | 7/16 | 88.24 | 7 |  |
| [首都在线](https://mirrors.yun-idc.com) | 商业 | 42.33 | 45.00 KB/s | 20.22 MB/s | 6/16 | 85.54 | 8 |  |
| [阿里](https://mirrors.aliyun.com) | 商业 | 26.57 | 34.03 KB/s | 7.19 MB/s | 14/16 | 84.16 | 9 |  |
| [中大 Matrix](https://mirrors.matrix.moe) | 高校 | 2.93 | 3.32 KB/s | 2.49 MB/s | 16/16 | 83.84 | 10 | 内网 [FS](mirrors.py#L132) |
| [浙江大学](https://mirrors.zju.edu.cn) | 高校 | 30.77 | 45.58 KB/s | 2.61 MB/s | 15/16 | 81.74 | 11 |  |
| [清华大学 TUNA](https://mirrors.tuna.tsinghua.edu.cn) | 高校 | 36.63 | 45.61 KB/s | 2.70 MB/s | 16/16 | 81.09 | 12 |  |
| [南京大学](https://mirrors.nju.edu.cn) | 高校 | 38.19 | 50.08 KB/s | 2.81 MB/s | 16/16 | 80.99 | 13 |  |
| [重庆邮电大学](https://mirrors.cqupt.edu.cn) | 高校 | 35.53 | 59.01 KB/s | 2.92 MB/s | 13/16 | 80.10 | 14 |  |
| [上海科技大学](https://mirrors.shanghaitech.edu.cn) | 高校 | 36.67 | 58.36 KB/s | 2.82 MB/s | 11/16 | 77.85 | 15 |  |
| [重庆大学](https://mirrors.cqu.edu.cn) | 高校 | 34.25 | 45.92 KB/s | 3.20 MB/s | 12/16 | 77.69 | 16 |  |
| [上交 sjtu](https://mirror.sjtu.edu.cn) | 高校 | 34.54 | 37.83 KB/s | 3.01 MB/s | 12/16 | 76.90 | 17 | 与 sjtug 互补 |
| [上交 sjtug](https://mirrors.sjtug.sjtu.edu.cn) | 高校 | 35.58 | 34.90 KB/s | 2.77 MB/s | 12/16 | 75.25 | 18 | 与 sjtu 互补 |
| [北京理工大学](https://mirror.bit.edu.cn) | 高校 | 36.42 | 48.59 KB/s | 4.41 MB/s | 6/16 | 73.07 | 19 |  |
| [北京邮电大学](https://mirrors.bupt.edu.cn) | 高校 | 36.53 | 55.22 KB/s | 2.81 MB/s | 7/16 | 72.99 | 20 |  |
| [哈尔滨工业大学](https://mirrors.hit.edu.cn) | 高校 | 55.16 | 38.60 KB/s | 2.81 MB/s | 14/16 | 72.81 | 21 |  |
| [西安交通大学](https://mirrors.xjtu.edu.cn) | 高校 | 52.00 | 39.43 KB/s | 2.81 MB/s | 13/16 | 72.52 | 22 |  |
| [兰州大学](https://mirror.lzu.edu.cn) | 高校 | 60.62 | 35.99 KB/s | 2.75 MB/s | 12/16 | 68.48 | 23 |  |
| [大连东软信息学院](https://mirrors.neusoft.edu.cn) | 高校 | 52.64 | 40.46 KB/s | 0 B/s | 8/16 | 63.69 | 24 |  |
| [北京交通大学](https://mirror.bjtu.edu.cn) | 高校 | 63.04 | 44.20 KB/s | 2.48 MB/s | 7/16 | 62.47 | 25 |  |
| [网易](https://mirrors.163.com) | 商业 | 63.30 | 13.86 KB/s | 0 B/s | 9/16 | 56.99 | 26 |  |
| [南京邮电大学](https://mirrors.njupt.edu.cn) | 高校 | 36.99 | 0 B/s | 0 B/s | 0/16 | 51.38 | 27 |  |
| [搜狐](https://mirrors.sohu.com) | 商业 | Failed | 0 B/s | 0 B/s | 5/16 | 28.07 | 28 |  |
