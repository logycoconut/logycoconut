> 参考了netcan大神的[个人主页](https://github.com/netcan/netcan)并加以改造

### 更新最近五条博客

* 通过`requests`库请求网页

* `xpath`语法分析网页并获取数据

* 写入`README`文件中

### 定时触发更新

* 利用`Github Actions`的定时任务

* 具体配置可以看仓库中的`update.yml`文件

### 关于配置文件中的`GITHUB_TOKEN`

在`Settings / Developer settings / Personal access tokens`中申请一个个人令牌, 命名为`GITHUB_TOKEN`, 它的作用域仅限于`repo`

这样我们就有一个可以对仓库进行操作的令牌, 确保actions可以运行

*一开始我以为还需要在仓库中的` Settings / Secrets`中配置环境变量, 后来不配也可以正常工作, 也许是在`Personal access tokens`中申请的令牌是全局的 ? ( 存疑 )*