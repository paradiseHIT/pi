# pi
## 背景
家里有树莓派，可以利用这个树莓派做bt下载，同时供应天猫魔盒做视频服务器，主要依赖的几个服务samba, transmission

## 过程
### os安装，支持无屏无键盘
1.烧录img，参看官方文档，我安装的是lite版本，需要一个读sd卡的读卡器，烧录好以后在sd卡一级目录下创建ssh文件，为了无屏无键盘远程可以自动开启ssh服务

### 基本包安装
安装工具
``` sudo apt-get install vim python-pip  ntfs-3g  samba samba-common-bin ntpdate transmission-daemon -y ```
调整时间
``` tzselect ```

### 硬盘挂载
3.挂载自己的硬盘 sudo modprobe fuse && mount /dev/sda1 /mnt/xxxx
4.修改fstab，每次重启自动挂载
/dev/sda1 /mnt/segate ntfs-3g defaults,noexec,umask=0000 0 0
sudo mount -a

6.samba
修改samba配置文件并启动samba服务
sudo vim /etc/samba/smb.conf
最后添加
[raspberrypi]
    # 说明信息
    comment = NAS Storage
    # 可以访问的用户
    valid users = pi
    # 共享文件的路径,raspberry pi 会自动将连接到其上的外接存储设备挂载到/media/pi/目录下。
    path = /mnt/segate
    # 可被其他人看到资源名称（非内容）
    browseable = yes
    public = yes
    # 可写
    writable = yes
    # 新建文件的权限为 664
    create mask = 0664
    # 新建目录的权限为 775
    directory mask = 0775

增加用户，这个用户必须是已经存在
sudo smbpasswd -a pi
重启服务
sudo /etc/init.d/samba restart

7.transmission配置

blocklist参考了techjawab的github：
"blocklist-url": "http://list.iblocklist.com/?list=ydxerpxkpcfqjaybcssw&fileformat=p2p&archiveformat=gz",
设置下载目录为用户目录下的Downloads文件夹：
"download-dir": "/home/pi/Downloads",
设置未下载完成数据存放地点为Downloads文件夹：
"incomplete-dir": "/home/pi/Downloads",
设置Web登陆密码为：raspberry
"rpc-password": "raspberry",
设置Web登陆用户名：transmission
"rpc-username": "transmission",
允许Web登陆：（设置为true）
"utp-enabled": true
设置完成之后，保存setting.json文件，重新启动transmission服务：
sudo service transmission-daemon reload

