# fofa-info
fofa.info批量API爬取

## **功能：**

1.将账号和API写入保存到配置文件，自动读取

2.查询语法输入

3.可设置查询数量

4.爬取状态码为200的URL



## **注意：**

1.配置文件（fofakey.txt）

​	账号和API将保存到配置文件中。

​	若当前目录下不存在fofakey.txt，将自动创建。

​	若fofakey.txt为空，脚本会自动需要使用者输入账号和API，并保存在fofakey.txt中，以便以后直接读取。

​	fofakey.txt第一行保存fofa账号，第二行保存API。

2.查询的数量

​	默认为100，可设置查询数量

​	设置的查询数量未必是最准确的数量

​	比如：查询到的数量为100，用户输入的数量为10，肯定只会输出10个

​				查询到的数量为10，用户输入的数量为100，最终也只会输出10个

​	查询到的具体数量将输出显示

3.结果保存

​	最终结果会以txt的形式保存

​	保存名称用户自己设置，回车默认为文件名称为当前时间的值

4.爬取

​	前面查询到了具体数量

​	这里会对每个URL进行状态码读取

​	对重状态码为200的URL及端口将会写入保存到文件



## **安装：**

`pip3 install requests`



`python3 fofainfo.py`



![image-20220731115111279](https://github.com/ice0bear14h/fofa-info/blob/master/image-20220731115111279.png)

![image-20220731115423358](https://github.com/ice0bear14h/fofa-info/blob/master/image-20220731115423358.png)
