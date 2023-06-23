# GPT-for-Windows
利用PySide6实现的与OpenAI通信的Windwos本地客户端，您只需要提供OpenAI key就可以如在网站上一样正常使用。

## 使用说明
### 一、使用步骤
<br>1.秘钥登录：第一次打开应用会要求用户输入自己的秘钥登录，登录成功后会在程序目录下生成.key文件保存秘钥。以后再次打开时程序会使用.key文件自动登录🌐<br><br>
2.新建对话：点击右上“新建对话”按钮，选择您需要的模型，便可创建您的对话；在3.3版本中，还可以勾选“启用连续对话”选项开启保持历史记录的连续对话模式。鉴于对内存的占用控制，程序设定为最多只能同时进行三个对话💬<br><br>
3.开始对话：尽情地享受和ChatGPT的聊天时光吧😊<br><br>
### 二、其他操作
<br>1.秘钥更改：如果用户需要更改秘钥，只需删除程序在其目录下保存的.key文件，然后重新打开程序登录即可🔑<br><br>
2.对话保存：程序提供了对话记录导出操作，切换到需要保存的对话页面，点击菜单栏“对话>>导出当前对话”，程序会在其目录下创建一个名为“dialog history”文件夹，您所导出的对话会以html格式储存在里面📥<br><br>
3.重置对话：程序提供了对话重置操作，切换到需要重置的对话页面，点击菜单栏“对话>>重置当前对话”，当前页面的对话会被重置为未开始对话的初始状态🔄<br><br>
4.对话控制：对于手控长对话模式，系统提供了三种对话角色：“user”、“reminder”、“system”。<br><br> “user”角色用于提出您的问题，ChatGPT会根据“reminder”、“system”的提示和设定做出回答<br>“reminder”角色也是提出您的问题，但其回答结果会被保留，并作为记录提示在后续对话中使用<br>“system”角色用于提出您对于ChatGPT的设定（例如扮演什么角色等要求），其不会传输给ChatGPT回答，而是直接作为设置在后续对话中影响ChatGPT回答<br>详细角色介绍请参阅OpenAI官方文档对于[角色消息的介绍](https://platform.openai.com/docs/guides/gpt/chat-completions-api)<br><br>“reminder”、“system”可点击左下角“查看对话设置”按钮查看，并可以手动删除；重复进行的“reminder”、“system”角色对话会覆盖前一次设定🕹️<br><br>
### 三、注意事项
<br>1.网络连接：由于GWF的存在，目前ChatGPT无法在中国大陆内使用。本程序仅是利用OpenAI的官方API进行进行对话，因此如需使用还请自备方法科学上网🚀<br><br>
2.
