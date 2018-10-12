```
$ git svn clone "svn url" -r"version number":HEAD -A "username file" --no-metadata -s --ignore-refs=refs/remotes/"branch name" “local path”
$ cp -Rf .git/refs/remotes/tags/* .git/refs/tags/
$ rm -Rf .git/refs/remotes/tags
$ cp -Rf .git/refs/remotes/* .git/refs/heads/
$ rm -Rf .git/refs/remotes
$ git remote add origin "git repo url"
$ git push -u origin --all （推送并关联所有分支）
$ git push origin --tags （推送所有标签）
$ git svn --version （查看git和svn版本号）
$ git svn info （查看远程svn库信息）
$ git svn rebase （更新远程svn库）
$ git svn dcommit （提交到远程svn库）
```
>1. 第一条命令的最基本命令为：git svn clone "svn url"
>2. **-r"version number":HEAD**：例（-r12:HEAD）表示从指定版本开始克隆到最新版。因为svn是按每一个提交进行拉取，当提交过多时克隆时间可长达几小时甚至上天。
>3. **-A "username file"**：例（-A username.txt）表示映射svn提交人到git提交人。这个操作非常重要，否则svn的提交信息将全部写入到git的全局用户名下。这条命令也可以写成*--authors-file="username file"*。操作方法如下：
>  1. 在要克隆的目录下新建txt文件。
>  2. 每个提交人为1行，例**```jack=smith<smith@test.com>```**，左边为svn提交人，右边为git平台的提交账户名和邮箱。
>4. **--no-metadata**：禁止导出svn附加信息。具体是什么效果暂未测试出来。
>5. **-s**：非常重要的命令，表示将svn结构和git结构一一对应。
>  1. svn的标准目录结构为“trunk（主分支）”，“branches（其它分支）”，“tags（标签）”。
>  2. 如果使用*-s*命令，则可以将trunk对应到master，branches对应到其它分支，tags对应到标签。
>  3. 如果不适用*-s*命令，则默认将svn所有文件导入到git的master分支，忽略svn的branches和tags。
>  4. 如果svn为非标结构，则可以手动对应，命令为*-T "trunk name"* or *--trunk="trunk name"*，*-b "branches name"* or *--branches="branches name"*，*-t "tags name"* or *--tags="tags name"*。*-s*命令也可以写为*--stdlayout*。
>  5. 目录结构如图所示，也可查看[此处](http://www.cnmiss.cn/?p=296)：
 >6. **--ignore-refs=refs/remotes/"branch name"**：（例：--ignore-refs=refs/remotes/dev），表示忽略dev分支，如果路径不同则需要更改路径。
>7. 第2~5条命令分别表示将远程svn的标签转换为本地git真正的标签，删除远程svn标签，将远程svn的分支转换为本地git真正的分支，删除远程svn分支，如果路径不同则需要更改路径。
>8. 如果是在线导入svn库，则需要考虑以下几个问题：
  1. 正常来讲只允许导入公有svn库，因为私有库只能允许成员or站内用户克隆。如果要允许导入私有库，可能需要输入仓库所有者的帐号和密码，所以导入选项需增加**用户名**和**密码**字段，但是非必填（私有库克隆未测试过，因为同类产品只允许导入公有库）。
  2. 如果svn库是标准结构，则导入时可采用*-s*命令来一一对应，再用cp -Rf命令来转换分支和标签。但如果不是标准结构，由于系统不知道用户是怎么划分其svn的trunk，branches，tags结构的，正常情况下则只能将svn所有文件导入到git的master分支里，自动忽略branches和tags。不过可以增加字段让用户在线填入，告知系统要如何对应结构，所以需增加字段为**trunk="输入主干目录名"**，**branches="输入分支目录名"**，**tags="输入标签目录名"**。
  3. 由于svn和git的提交人机制不同，因此还需要映射提交人关系，否则svn的所有提交人信息都将纳入git的全局用户名下。所以需有多少个svn提交人就增加增加多少字段为**```svn用户=git用户<git用户邮箱>```**
  4. 由于svn拉取代码是按版本一个个拉取，加上其采用http传输协议，若版本较多则非常耗时，长达几小时甚至上天。所以导入时，远程git库是没法进行任何操作的，且若远程svn库做了任何改动，那么新的改动也无法导入远程git库。
  5. ***总结：手动克隆远程svn库到本地，按需修改后再推到远程git库更加方便灵活，远程svn库有任何改动也可以本地更新后再推到远程git库***。