- # 常用的Linux Command

## 日常

- 查看历史命令行记录：`history`or`!$`

- 回到上一个工作路径：`cd -`

- 展示进程树（p:pid）：`pstree -p`

- 查看路径文件信息：`ls -lh`|`-h`表示文件大小用KB等表示

- 查看系统运行时间等：`uptime [-psV]`

- 前后翻页查看文件：`less`| 通过`page up down`翻页

- 使用 `alias` 来创建常用命令的快捷形式。例如：`alias ll='ls -latr'` 创建了一个新的命令别名 `ll`

- `vim less more`查看文件都可以用`/keywords`来查询关键字，`n`来查找下一个

- 打包文件：

  ```
  tar -zcvf 打包压缩后的文件名 要打包的文件  
  参数说明：z：调用gzip压缩命令进行压缩; c：打包文件; v：显示运行过程; f：指定文件名;  
  示例：  tar -zcvf a.tar file1 file2,...      //多个文件压缩打包
  ```

- 解压文件：

  ```
    tar -zxvf a.tar                      //解包至当前目录
    tar -zxvf a.tar -C /usr------        //指定解压的位置
    unzip test.zip             //解压*.zip文件 
    unzip -l test.zip          //查看*.zip文件的内容 
  ```

- 查找文件目录下包含`numpy`的内容：`find . -type f -name "*" | xargs grep "numpy"`

- `xargs` 是一个强大的命令行工具，它可以从标准输入读取数据，并将它们作为命令行参数传递给其他命令。

  在 Linux 系统中，许多命令都无法直接处理大量的输入参数，或者无法读取大量文件。这时，你就可以使用 `xargs` 来帮忙。通常，我们会与 `find`、`grep`、`cat` 等命令结合使用 `xargs`。

  下面是一个简单的例子：使用 `find` 命令找到所有的 `.txt` 文件，然后用 `xargs` 将这些文件作为参数传给 `rm` 命令进行删除：

  bash

  ```bash
  find . -name "*.txt" | xargs rm
  ```

- 服务器之间文件交换：`scp /opt/data.txt  192.168.1.101:/opt/ ` | 将本地opt目录下的data文件发送到192.168.1.101服务器的opt目录下

- 反转查找：`grep -v`