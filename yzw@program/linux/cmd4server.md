## cmd连接服务器

```cmd
ssh username@ip
```

## cmd下载上传文件至服务器

### stfp连接服务器

```cmd
sftp username@ip
```

## 下载上传

### 下载单文件

```cmd
get filepath localpath
```

**or**

先进入本地待保存目录和服务器文件路径，再执行

```cmd
get filename
```

### 下载多文件

```cmd
get -r filepath localpath
```

### 恢复下载

```
reget -r filepath localpath
```

### 上传文件

使用`put`命令，命令格式和下载格式一样

## 路径展示

### 服务器路径

```
pwd
```

### 本地路径

```
lpwd
```

### 进入本地路径

```
lcd
```

### 展示本地路径

```
lls
```

## 其他

### 退出sftp

```
exit or quit or bye
```

### 全屏

```
Alt + enter
```

