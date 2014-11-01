Android中使用ant进行多渠道打包
================

### 1. 「[这篇][1]」文章有比较详细的介绍

## 2. 我遇到的问题
### 2.1
第一个问题是上面的实例是多工程的，我的项目是多【源码包】的，也就是说我的项目中除了src这个源代码文件夹之外，还有其他的源代码文件夹，
比如volley,photoview，这样打包的时候volley,photoview这些源代码包中的类就会找不到。Google之后，解决方案是：
在local.properties中加入
source.dir=src;photoview;volley
这样第一个问题就解决了

### 2.2
AndroidManifest.xml中的UMENG_CHANNEL替换时出错，要注意的是下面的代码一定要在一行中，并且android:name要在前面
<meta-data android:name="UMENG_CHANNEL" android:value="360"  />
比如如果是下面这样就会替换失败
<meta-data android:name="UMENG_CHANNEL"
 android:value="360"  />
 或者下面这样也会失败
 <meta-data android:value="360" android:name="UMENG_CHANNEL"  />
 
 具体原因可以在build.xml中找到这里
 <replaceregexp
		    encoding="utf-8"
		    file="AndroidManifest.xml"
		    flags="s"
		    match='android:name="UMENG_CHANNEL".+android:value="([^"]+)"'
		    replace='android:name="UMENG_CHANNEL" android:value="${channel}"'/>
上面的作用就是替换渠道，做法是在AndroidManifest.xml文件查找
android:name="UMENG_CHANNEL".+android:value="([^"]+)"
的字符串，然后替换成
android:name="UMENG_CHANNEL" android:value="${channel}"
的字符串

### 2.3
打包加入混淆时出现
taskdef class proguard.ant.ProGuardTask cannot be found 
的错误
在「[这里][2]」找到解决办法
	2.3.1 在「[这里][3]」下载proguard
	2.3.2 解压放到{sdk.dir}/tools目录中，并把文件夹重命名为proguard
	2.3.3 重试
	
### 2.4
如果你的proguard文件中同时加了
-libraryjars libs/fastjson-1.1.26-android.jar
和包对于的class的
-keep class com.alibaba.fastjson.**{*;}
那么打包的时候就会提示说加入了两次fastjson-1.1.26-android.jar
解决办法把
-libraryjars libs/fastjson-1.1.26-android.jar
去掉

[1]: http://my.oschina.net/liucundong/blog/333301
[2]: http://stackoverflow.com/questions/24451331/taskdef-class-proguard-ant-proguardtask-cannot-be-found-using-the-classloader-an
[3]: http://proguard.sourceforge.net/
 