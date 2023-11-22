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
| [中科大 USTC](https://mirrors.ustc.edu.cn) | 高校 | 24.55 | 77.09 KB/s | 16.93 MB/s | 16/16 | 100.00 | 1 |  |
| [北京外国语大学](https://mirrors.bfsu.edu.cn) | 高校 | 40.21 | 56.52 KB/s | 19.41 MB/s | 16/16 | 96.94 | 2 |  |
| [ISCAS](https://mirror.iscas.ac.cn/) | 高校 | 41.53 | 40.24 KB/s | 20.91 MB/s | 14/16 | 94.13 | 3 |  |
| [南方科技大学](https://mirrors.sustech.edu.cn) | 高校 | 7.71 | 77.05 KB/s | 5.55 MB/s | 14/16 | 93.04 | 4 |  |
| [华为](https://repo.huaweicloud.com) | 商业 | 10.44 | 38.26 KB/s | 2.98 MB/s | 16/16 | 91.93 | 5 | 主站域名不同 |
| [西北农林科技大学](https://mirrors.nwafu.edu.cn) | 高校 | 42.38 | 58.80 KB/s | 21.16 MB/s | 7/16 | 89.74 | 6 |  |
| [重庆邮电大学](https://mirrors.cqupt.edu.cn) | 高校 | 34.29 | 67.09 KB/s | 8.43 MB/s | 14/16 | 88.69 | 7 |  |
| [腾讯](https://mirrors.tencent.com) | 商业 | 12.37 | 29.69 KB/s | 7.36 MB/s | 12/16 | 85.65 | 8 |  |
| [中大 Matrix](https://mirrors.matrix.moe) | 高校 | 3.01 | 3.72 KB/s | 2.95 MB/s | 16/16 | 84.60 | 9 | 内网 [FS](mirrors.py#L132) |
| [清华大学 TUNA](https://mirrors.tuna.tsinghua.edu.cn) | 高校 | 36.95 | 40.74 KB/s | 2.73 MB/s | 16/16 | 80.81 | 10 |  |
| [南京大学](https://mirrors.nju.edu.cn) | 高校 | 38.26 | 42.42 KB/s | 2.81 MB/s | 16/16 | 80.60 | 11 |  |
| [浙江大学](https://mirrors.zju.edu.cn) | 高校 | 38.31 | 45.20 KB/s | 2.68 MB/s | 15/16 | 80.20 | 12 |  |
| [上海科技大学](https://mirrors.shanghaitech.edu.cn) | 高校 | 36.26 | 65.29 KB/s | 2.81 MB/s | 11/16 | 80.01 | 13 |  |
| [阿里](https://mirrors.aliyun.com) | 商业 | 26.99 | 39.90 KB/s | 828.73 KB/s | 14/16 | 79.48 | 14 |  |
| [上交 sjtu](https://mirror.sjtu.edu.cn) | 高校 | 34.44 | 38.48 KB/s | 3.50 MB/s | 13/16 | 79.02 | 15 | 与 sjtug 互补 |
| [重庆大学](https://mirrors.cqu.edu.cn) | 高校 | 34.36 | 30.06 KB/s | 3.62 MB/s | 12/16 | 77.90 | 16 |  |
| [上交 sjtug](https://mirrors.sjtug.sjtu.edu.cn) | 高校 | 34.81 | 29.85 KB/s | 2.76 MB/s | 13/16 | 76.97 | 17 | 与 sjtu 互补 |
| [北京理工大学](https://mirror.bit.edu.cn) | 高校 | 36.27 | 58.67 KB/s | 4.36 MB/s | 7/16 | 75.63 | 18 |  |
| [西安交通大学](https://mirrors.xjtu.edu.cn) | 高校 | 51.93 | 41.50 KB/s | 2.80 MB/s | 14/16 | 74.77 | 19 |  |
| [哈尔滨工业大学](https://mirrors.hit.edu.cn) | 高校 | 55.24 | 40.90 KB/s | 2.81 MB/s | 15/16 | 74.69 | 20 |  |
| [北京交通大学](https://mirror.bjtu.edu.cn) | 高校 | 39.00 | 57.80 KB/s | 1.27 MB/s | 9/16 | 73.71 | 21 |  |
| [北京邮电大学](https://mirrors.bupt.edu.cn) | 高校 | 36.48 | 52.98 KB/s | 2.81 MB/s | 7/16 | 73.27 | 22 |  |
| [首都在线](https://mirrors.yun-idc.com) | 商业 | 42.56 | 43.93 KB/s | 4.36 MB/s | 6/16 | 70.82 | 23 |  |
| [兰州大学](https://mirror.lzu.edu.cn) | 高校 | 60.75 | 40.22 KB/s | 2.76 MB/s | 12/16 | 69.97 | 24 |  |
| [大连东软信息学院](https://mirrors.neusoft.edu.cn) | 高校 | 52.89 | 38.83 KB/s | 2.72 MB/s | 8/16 | 68.71 | 25 |  |
| [网易](https://mirrors.163.com) | 商业 | 60.53 | 18.39 KB/s | 916.33 KB/s | 10/16 | 61.56 | 26 |  |
| [南京邮电大学](https://mirrors.njupt.edu.cn) | 高校 | 36.85 | 0 B/s | 0 B/s | 0/16 | 51.94 | 27 |  |
| [搜狐](https://mirrors.sohu.com) | 商业 | Failed | 0 B/s | 0 B/s | 6/16 | 30.99 | 28 |  |
