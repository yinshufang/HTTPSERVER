httpserver

前端

功能：提供给用户直接使用

要求：良好的用户体验

        更全面的功能

        很好的和后端进行交互

        有良好的跨平台性

        有一定的优化

后端：

功能：逻辑处理

        算法实现

        磁盘交互（数据库  静态文件处理）

要求: 健壮性，安全性

        并发性能和处理速度

        架构合理便于维护扩展

网站后端

httpserver  +  WebFrame

第三版

    功能：

    httpserver：

        获取http请求

        解析httpserver请求

        将请求发送给 WebFrame

        从WebFrame接收反馈数据

        将数据组织为Response格式发送给客户端

    WebFrame：

        从httpserver接收具体请求

        根据请求进行逻辑处理和数据处理

            *静态页面

            *逻辑数据

        将需要的数据反馈给httpserver

    升级点：1，采用httpserver和应用处理分离的模式

                2，降低了耦合度

                3，原则上httpserver可以搭配任意的WebFrame



项目结构：

                |----   httpserver|---HttpServer.py(主程序）

project-----|                     |--settings（httpserver配置）

                |                                  

                |----  WebFrame|----static（存放静态页面）

                                       | --views.py（应用处理）

                                       |  --urls.py(存放路由）

                                       |-- settings(框架配置）

                                       |--  WebFrame.py（主程序代码）​
