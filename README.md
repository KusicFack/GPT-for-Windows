# GPT-for-Windows
利用PySide6实现的与OpenAI通信的Windows本地客户端，支持Windows10/11。您只需要提供OpenAI key就可以如在网站上一样正常使用ChatGPT。

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
<br>1.网络连接：由于著名的[GFW](https://baike.c114.com.cn/view.asp?id=23004-44A3EE4E)的存在，目前ChatGPT无法在中国大陆内使用。本程序仅是利用OpenAI的官方API进行进行对话，因此如需使用还请自备方法科学上网🚀<br><br>
2.对话错误：在对话中可能会遇到对话卡住、对话报错等状况，这可能是科学方法不稳定亦或是OpenAI本身API的问题，还请重试提问或者重置对话来解决❌<br><br>
3.回答偏离：在对话过程中可能会遇到ChatGPT“偏题”回答，这可能是ChatGPT本身存在的不定时“抽风”现象，也可能是因为一些其他未知因素（例如对话记录格式等）导致。请您重新使用更加细致、准确的语言描述您的问题🤔<br><br>
4.连续对话：每一个对话模型都有一次提问可处理的[token](https://platform.openai.com/docs/guides/gpt/managing-tokens)数量上限。token数量取决于您的问题和对话设置（或者是对话历史记录）。显然，保留历史记录的连续对话token数量会随着对话的进行而增多，最后token数量会超过其处理上限。因此程序设置了连续对话的字数最大值，一旦字数超越最大值后程序便不允许再进行对话。各模型的最大token支持详见[OpenAI官方文档](https://platform.openai.com/docs/models/models)🔝<br><br>
5.对话收费：您将会被依据每次提问的token数量收取一定费用，当您的OpenAI账户上金额归零后可能无法再使用ChatGPT。请注意，本程序不会收取您的费用，您的费用全权由OpenAI计算收取。收费标准详见[OpenAI模型价目表](https://openai.com/pricing)💰<br><br>
## 写在最后
<br>本程序的创建更新是作者一人在课余期间完成的，因此更新较为佛系🕊️。由于作者并非计软网专业，只是一个乐于折腾的业余Python爱好者，因此本程序并不完美，可能会有一些莫名奇妙的BUG产生（尽管作者已经尽力实践避坑）😳，还请您在issue中及时提供建议和反馈便于作者进一步改进。作者真心希望这个程序能够帮助到您，也希望您在使用之余能给作者一个小小的Star🌟支持，或者关注作者[bilibili](https://space.bilibili.com/349868513)。您的支持是作者的不懈动力🙏
