# werewolfGame 
##### created by medyg

## 开发环境
* [python3.5.2](https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe) + [Tornado](http://www.tornadoweb.org/en/stable/)

## 本地运行
1. 使用visual studio打开WerewolfGame.sln或终端运行指令`python werewolvesGame.py`  
2. 浏览器访问`localhost:8888`

- - -  
## 项目框架
- 文件`application.py`：这个文件的核心任务是完成`tornado.web.Application()`的实例化  
- 文件`url.py`：在这个文件中记录项目中所有URL和映射的类，即完成`application.py`中`handlers=[...]`的功能  
- 文件`werewolvesGame.py`：这是项目的入口文件，里面包含`if __name__ == "__main__"`，从这里启动项目和服务  
- 目录`handler`：存放`.py`文件，即所谓各种请求处理类（当然，如果更大一些的项目，可能还要分配给别的目录来存储这种东西）  
- 目录`optsql`：存放操作数据库的文件，比如各种读取或者写入数据库的类或函数，都放在这里面的某些文件中  
- 目录`static`：存放静态文件，就是上文说的比如`CSS，JS，img`等，为了更清晰，在这个目录里面，还可建立子目录  
- 目录`views`：存放`.html`的模板（在更大型的项目中，可能会设计多个目录来存放不同的模板，或者在里面再有子目录进行区分）  
本框架参考自[Tornado静态路径以及一个项目框架](https://segmentfault.com/a/1190000000743589)  

# 在线狼杀MC，建设中
