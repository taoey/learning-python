## Typroa中markdown图片转存到七牛图床

现在只开发单个文章的脚本

开发思路：
- 匹配文章中的URL
- 上传对应的图片，返回对应七牛中图片的位置
- 替换文章中的URL，在指定的git仓库生成处理后的文档
- 提交git

参考资料：
- [使用 Python 操作 Git 版本库 - GitPython](https://www.cnblogs.com/baiyangcao/p/gitpython.html)
- [七牛云python官方文档](https://developer.qiniu.com/kodo/sdk/1242/python)