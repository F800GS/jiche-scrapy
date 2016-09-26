# jiche-scrapy
最基础的scrapy使用

存在问题：  
1，错字，少打括号，spider中 item=JicheItem（） 括号少打；  
2，使用xpsth不熟练，在最终的response中提取不到有效数据，调用response.text将response转换为unicode格式文档，然后使用正则表达式提取数据  
3，各个方法返回值的类型需要注意  
