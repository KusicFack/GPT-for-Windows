from GPT import *
from tabform import *
from SP_Window import *
from CreateDialog import *
from PySide6.QtCore import QThread, QTimer, Signal
from PySide6.QtWidgets import QMessageBox, QInputDialog, QSystemTrayIcon
from PySide6.QtGui import QGuiApplication
import openai, time, os, copy, base64, winsound

pic1 = ('GPT_ICO.png', b'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Uk0AAHomAACAhAAA+gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAAKOUExURQAAAP///xCjfw+jf/z9/fT6+e749vf8+/X6+aPbzrDg1bjj2c7s5djv6uL08OHz7+f18gCddwCcdACcdQCbdACbdQGddwKeeAOeeASfeQSeeAWfeQagegafegegegegewefegigewmhfAmgewqhewqhfAuhfAuhfQyhfAyhfQ2ifQ2ifg6jfg6jfw6ifg+jfg+ifhCkgBGkgBGjfxKkgBKkgRKjgBOkgBSlgRSkgRWlgRamgxemghelghimghimgxmlghqnhBqmhBunhBumgxyohR2ohR6phx6ohh+phx+ohSKqiSOriiOqiSesiymsjCqtjSuujSytji6vjzGwkTKwkTWxkzaykzezlDexkzizlTiylDmzlDmzlTy0lj20lz60lz+1mD+0l0G2mkK2mkO3m0S3mkW3m0e4nEe4nUi4nUu6nk27oE67oFK9o1K8olO9o1S9o1e+pVi+pVq/plzAqGLDq2HCqmHCq2PDq2LCq2TDrGfFrWbErWfErWrGr2zGsG3HsW7HsXDIsnLJs3XKtXbKtnnMuHjLtnvMuH7Oun/Oun7NuoHPvILPvIPPvIbQvojSv4nSwIzSwY3TwpHVxJPWxZLVxJLVxZHUw5PVxZXWxpnXyKDbzKHbzaTczqXczqfd0Kjd0Kzf0q7g1K3f07Dg1Lbj2LXi17fj2MLn3sPo38Xo38fp4crq4svr48/s5dHt5tbv6djw6tfv6eX18eT08PL6+Pn9/ACbcwCacgCZcQCYbwCYcACXbQCWbACWbWjFrXzNuK7g07Xj183r49Pu59zy7ODz7uL07+Hz7uj38+f28uX08O759u349ez39On38+j28uf18e/59u749fP6+Pr9/Pj9+////yV/HpkAAADadFJOU/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8AgwWs3gAAAAlwSFlzAAALEwAACxMBAJqcGAAAAjlJREFUKJFjvMnAwBAk/PU8Ayow5H67joGBgeHmTUUmJh0mDKDDxKR68ybDTQdmTDkIYDa5ycJwiAEX+P+bgdH0LE5pBgZGZgPWN3CeOhu32EdkWUuWN9fhHHEFTY47v5lZOK/ATP/OyARXK53pc/+P9K2N/++8ev0fJghzpr5I4Y468b3VjOwXeMoVYL5hZoSoUv0WHHnE9rG4tj37gdAIoQvfUHRrmcy/fsM7aStPmFiy5YEs1hBVqHaIoo85edM+/zC6tU6oz+/athWrbKEegEirGJsEPWZh/vn1/synSWUTfjIx/kaW/i73YC8Hwx9GnTsZVq27jCYEfGeFSLNAyK9RKn85eP4cdot6VyR0Sr5fVU3iCgMDAwPE5XK7VqvO53CWuNnAosa8dgXrWo8f5z4jdF8WPdYxaZLywbmf/vp8vXF6zuQP/H+R7GZgZNkqvtac+/py74c/7zP87NJ+yoIszcAiWLguaKNWvchTTo3HLHEfjgohOY2B90JLtn2Z/skf0gmfmcW8v3f+uMGAcBrD+3dVEesfPbAv/LFc67Pshbl3hF8gSzN8v8lpGuITrSWrs3SNjv7muy+gboJZzij+Ipxp/ZoPcp9fdbLAIpyB2QiqjuGLzoN7wj9ZpRctZL0GkzVk9HoCV8rAoPv+JwPXI3haYLRieXEVIctwmQEF/P/CcBNnMmdi0rvJxOCozYADMHIyMN5kcH36n/E/ptx/BoXtDIw3GRgYoll/YWRB9o/rGBgYAHmcxMcgGRBZAAAAAElFTkSuQmCC')
pic2 = ('user.png', b'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Uk0AAHomAACAhAAA+gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAADVUExURQAAAP////7+/v39/fv7+/j4+PX19fT09PPz8+/v7+np6ebm5uLi4t7e3tPT09DQ0M3NzcbGxsHBwby8vK2traqqqpeXl5OTk4eHh4ODg4CAgH19fXFxcW1tbWtra2lpaWhoaGdnZ2ZmZmNjY15eXlxcXFtbW1lZWVhYWFZWVlVVVVRUVE9PTz09PTw8PDs7Ozo6Ojg4ODU1NTIyMi8vLywsLCsrKyoqKigoKCQkJCMjIyIiIiAgIBkZGRcXFxYWFhAQEA8PDw4ODgoKCgkJCQMDA////9j2Sj0AAABHdFJOU/////////////////////////////////////////////////////////////////////////////////////////////8Ax5xWbwAAAAlwSFlzAAASdAAAEnQB3mYfeAAAAOJJREFUKJG1k0FLw0AQhd/bTQwxTWO0EBDr3VNR8NAKmqLsj67gyYMXf4fWU6oIRULiwZBskt0cWnyXYeebmZ0Hu1QAVjBJAaCywKpAWSEAJYboP4ut00OWH0SPttpFLOlMUgtdjkmSx/dNSmpYrgEA2+CjTum+P6u4gRE7VRyb8fkf92LLbmeSpH+hZdq+L98Kd/pixLNMUIpS5EVZnrx2B197bDRKu6u9/2i1319dHOmjXL+LE52Hzz1XV4f11dFNjwLzJCBJEZ7eGYwBuM1ywjt6MvTupr3euRhqV+DwF/wFxX4jBtkSOT0AAAAASUVORK5CYII=')

def pic_check(pic):
    if not os.path.exists('./{}'.format(pic[0])):
        imgdata = base64.b64decode(pic[1])
        with open('./{}'.format(pic[0]), 'wb') as f:
            f.write(imgdata)

class mythread(QThread): #处理对话请求，并返回请求结果或错误信息
    text = Signal(str)
    end = Signal()
    system_answer = Signal()
    error = Signal(str)
    start = Signal()
    def __init__(self):
        super().__init__()
        self.user_text = ''
        self.ID = ''
        self.role = ''
        self.systemsetting = ''
        self.reminder = ''
        self.model = ''

    def receive(self, text, ID, model, setting_tuple):
            self.user_text = text
            self.ID = ID
            self.model = model
            self.role, self.systemsetting, self.reminder = setting_tuple

    def run(self):
        try:
            if self.role == 'system':
                self.system_answer.emit()
            else:
                self.start.emit()
                if self.systemsetting and self.reminder:
                    answer = openai.ChatCompletion.create(
                        model=self.model,
                        messages=[
                            {"role": "system", "content": self.systemsetting},
                            {"role": "user", "content": self.user_text},
                            {"role": "assistant", "content": self.reminder}
                        ],
                        stream=True,
                        user=self.ID
                    )
                elif self.systemsetting or self.reminder:
                    if self.systemsetting:
                        answer = openai.ChatCompletion.create(
                            model=self.model,
                            messages=[
                                {"role": 'system', "content": self.systemsetting},
                                {"role": self.role, "content": self.user_text}
                            ],
                            stream=True,
                            user=self.ID
                        )
                    else:
                        answer = openai.ChatCompletion.create(
                            model=self.model,
                            messages=[
                                {"role": 'assistant', "content": self.reminder},
                                {"role": self.role, "content": self.user_text}
                            ],
                            stream=True,
                            user=self.ID
                        )
                else:
                    answer = openai.ChatCompletion.create(
                        model=self.model,
                        messages=[
                            {"role": self.role, "content": self.user_text}
                        ],
                        stream=True,
                        user=self.ID
                    )
                for chunk in answer:
                    try:
                        content = chunk.choices[0]['delta']['content']
                        self.text.emit(content)
                    except Exception:
                        pass
                self.end.emit()
        except Exception as e:
            self.error.emit(str(e))

class loginthread(QThread):  #处理登录，分别对自动登录和手动登录进行请求
    login_exception = Signal(str)
    login = Signal()
    def __init__(self):
        super().__init__()
        self.key = ''

    def receive(self, parent, key):
        self.parent = parent
        self.key = key

    def run(self):
        try:
            openai.api_key = self.key
            models = openai.Model.list()
            self.parent.Statelabel.setText('当前状态：已连接至OpenAI')
            self.parent.actionlongin.setEnabled(False)
            self.login.emit()
        except Exception as e:
            self.login_exception.emit(str(e))

class soundthread(QThread):
    def __init__(self):
        super().__init__()
        self.category = ''

    def run(self):
        winsound.PlaySound(self.category, winsound.SND_ALIAS)

class statusbarthread(QThread):
    load1 = Signal()
    load2 = Signal()
    load3 = Signal()
    stop = Signal()

    def __init__(self):
        super().__init__()

    def run(self):
        while not self.isInterruptionRequested():
            self.load1.emit()
            time.sleep(1)
            self.load2.emit()
            time.sleep(1)
            self.load3.emit()
            time.sleep(1)
        self.stop.emit()

class createdialog(QDialog,Ui_CreateDialog):
    a = Signal(dict)
    def __init__(self, parent, models):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(':/icos/GPT_ICO.ico'))
        self.value = {}
        self.comboBox.addItems(models)
        self.HelpButton.clicked.connect(self.help)
        self.buttonBox.accepted.connect(self.settings)
        self.buttonBox.rejected.connect(self.close)
        self.parentpos = parent.frameGeometry()
        self.move(self.parentpos.x()+(self.parentpos.width()-self.width())/2, self.parentpos.y()+(self.parentpos.height()-self.height())/2)


    def settings(self):
        self.value['model'] = self.comboBox.currentText()
        self.value['continue'] = self.ContinueSwitch.isChecked()
        self.a.emit(self.value)

    def help(self):
        QMessageBox.information(self, '关于模型与连续对话', '模型：<br>·gpt-3.5-turbo：即GPT3.5，目前最通用的ChatGPT版本，最大支持4096token，数据记录截止至2021.9<br>·gpt-3.5-turbo-16k：最大支持16384token（长对话推荐），价格略高，其余与前者相同<br><br>连续对话：<br>可以自动保存对话历史记录，但根据模型选择可进行的对话字数有限，超过后对话不可再进行')

class tab(QWidget,Ui_Tab):  #每一个对话的单独界面，作为tab添加至主窗口的tabwidget中
    a = Signal(str,str,str,tuple)
    b = Signal(str)
    e = Signal(str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for i in ['user', 'system', 'assistant']:
            self.MessageType.addItem(i)
        self.all_text = r'''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <script src="file:///./MathJax/tex-mml-chtml.js" id="MathJax-script" async></script>
                <script>
                    window.MathJax = {
                      tex: {
                        inlineMath: [ ["$", "$"], ["\\\\(","\\\\)"] ],
                        displayMath: [ ["$$","$$"], ["\\[", "\\]"] ],
                        processEscapes: true,
                        noundefined: {
                          color: "red",
                          background: "#FFEEEE",
                          size: "90%"
                        },
                        macros: {
                          href: "{}"
                        },
                        autoload: {
                          color: [],
                          colorv2: ['color']
                        },
                        packages: {'[+]': ['noerrors']}
                      },
                      options: {
                        ignoreHtmlClass: "tex2jax_ignore|dno",
                        processHtmlClass: 'tex2jax_process'
                      },
                      loader: {
                        load: ['[tex]/noerrors']
                      }
                    };
                </script>
                <style>
                    img{
                        width:30px;
                        height:30px;
                    }
                    div{
                    word-wrap:break-word;
                    word-break:break-all;
                    overflow:hidden;
                    }
                    #left{
                        width:10%;
                        float: left;
                    }
                    #right{
                        width:90%;
                        float: right;
                    }
                </style>
                <script language="javascript">
                    window.location="#bottom"
                </script>
            </head>
            <body>
            <div id = "main" style="background:#f0f0f0">
                <br><br>
                <div id="left" align="center"><img src="file:///./GPT_ICO.png"/></div>
                <div id="right">您好，请问您有什么问题？</div>
                <br><br><br>
            </div><a name="bottom">'''
        self.buffer = r'''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <style>
                    img{
                        width:30px;
                        height:30px;
                    }
                    div{
                    word-wrap:break-word;
                    word-break:break-all;
                    overflow:hidden;
                    }
                    #left{
                        width:10%;
                        float: left;
                    }
                    #right{
                        width:90%;
                        float: right;
                    }
                </style>
                <script language="javascript">
                    window.location="#bottom"
                </script>
            </head>
            <body>
            <div id = "main" style="background:#f0f0f0">
                <br><br>
                <div id="left" align="center"><img src="file:///./GPT_ICO.png"/></div>
                <div id="right">您好，请问您有什么问题？</div>
                <br><br><br>
            </div><a name="bottom">'''
        self.output_text = r'''
                <!DOCTYPE html>
                <html>
                    <head>
                        <meta charset="UTF-8">
                        <script type="text/javascript" id="MathJax-script" async
                          src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
                        </script>
                        <script>
                            window.MathJax = {
                              tex: {
                                inlineMath: [ ["$", "$"], ["\\\\(","\\\\)"] ],
                                displayMath: [ ["$$","$$"], ["\\[", "\\]"] ],
                                processEscapes: true,
                                noundefined: {
                                  color: "red",
                                  background: "#FFEEEE",
                                  size: "90%"
                                },
                                macros: {
                                  href: "{}"
                                },
                                autoload: {
                                  color: [],
                                  colorv2: ['color']
                                },
                                packages: {'[+]': ['noerrors']}
                              },
                              options: {
                                ignoreHtmlClass: "tex2jax_ignore|dno",
                                processHtmlClass: 'tex2jax_process'
                              },
                              loader: {
                                load: ['[tex]/noerrors']
                              }
                            };
                        </script>
                        <style>
                            img{
                                width:30px;
                                height:30px;
                            }
                            div{
                            word-wrap:break-word;
                            word-break:break-all;
                            overflow:hidden;
                            }
                            #left{
                                width:10%;
                                float: left;
                            }
                            #right{
                                width:90%;
                                float: right;
                            }
                        </style>
                        <script language="javascript">
                            window.location="#bottom"
                        </script>
                    </head>
                    <body>
                    <div id = "main" style="background:#f0f0f0">
                        <br><br>
                        <div id="left" align="center">AI</div>
                        <div id="right">您好，请问您有什么问题？</div>
                        <br><br><br>
                    </div>'''
        self.SendButton.clicked.connect(self.sendMessage)
        self.MessageType.currentIndexChanged.connect(self.rolechange)
        self.CheckContent.clicked.connect(lambda: self.settings(self.systemsetting, self.reminder))
        self.model = ''
        self.keephistory = ''
        self.history = '这是对话历史： \n'
        self.wrod = 0
        self.wordmax = 0
        self.user = ''
        self._user = ''
        self.role = 'user'
        self.systemsetting = ''
        self.reminder = ''
        self.answer = ''
        self.change = False
        self.thread = mythread()
        self.thread.text.connect(self.delta_handle)
        self.thread.start.connect(self.initpage)
        self.thread.end.connect(self.end_handle)
        self.thread.system_answer.connect(self.system_handle)
        self.thread.error.connect(self.e)
        self.thread.error.connect(self.bad_answer)
        self.a.connect(self.thread.receive)
        self.timer = QTimer()
        self.timer.timeout.connect(self.pageshow)

    def sendMessage(self):
        self.change = True
        if self.SendText.toPlainText():
            self.SendButton.setEnabled(False)
            self.MessageType.setEnabled(False)
            self.user_text = self.SendText.toPlainText()
            if self.keephistory:
                self.history += ('用户:'+ self.user_text + '\n')
                self.word = len(self.history) - 8
                self.WordStatistic.setText(str(self.word) + '/' + str(self.wordmax))
            self.SendText.clear()
            self.all_text = self.all_text[:len(self.all_text) - 17]
            self.buffer = self.buffer[:len(self.buffer) - 17]
            if self.role == 'user':
                self.showtext = '''<div id = "main"><br><br><div id="left" align="center"><img src="file:///./user.png"></div><div id="right">''' + self.user_text + '''</div><br><br><br></div><div id = "main" style="background:#f0f0f0"><br><br><div id="left" align="center"><img src="file:///./GPT_ICO.png"></div><div id="right"><br><br><br><a name="bottom">'''
                self.output_showtext = '''<div id = "main"><br><br><div id="left" align="center">您</div><div id="right">''' + self.user_text + '''</div><br><br><br></div><div id = "main" style="background:#f0f0f0"><br><br><div id="left" align="center">AI</div><div id="right">'''
                self.all_text += self.showtext
                self.buffer += self.showtext
                self.output_text += self.output_showtext
                if self.keephistory:
                    self.reminder = self.history
            elif self.role == 'system':
                self.showtext = '''<div id = "main"><br><br><div id="left" align="center"><img src="file:///./user.png"></div><div id="right" style="color:#FF0000">[系统命令]''' + self.user_text + '''</div><br><br><br></div><div id = "main" style="background:#f0f0f0"><br><br><div id="left" align="center"><img src="file:///./GPT_ICO.png"></div><div id="right"><br><br><br><a name="bottom">'''
                self.output_showtext = '''<div id = "main"><br><br><div id="left" align="center">您</div><div id="right" style="color:#FF0000">[系统命令]''' + self.user_text + '''</div><br><br><br></div><div id = "main" style="background:#f0f0f0"><br><br><div id="left" align="center">AI</div><div id="right">'''
                self.all_text += self.showtext
                self.buffer += self.showtext
                self.output_text += self.output_showtext
            else:
                self.showtext = '''<div id = "main"><br><br><div id="left" align="center"><img src="file:///./user.png"></div><div id="right" style="color:#00AA00">[助手命令]''' + self.user_text + '''</div><br><br><br></div><div id = "main" style="background:#f0f0f0"><br><br><div id="left" align="center"><img src="file:///./GPT_ICO.png"></div><div id="right"><br><br><br><a name="bottom">'''
                self.output_showtext = '''<div id = "main"><br><br><div id="left" align="center">您</div><div id="right" style="color:#FF0000">[助手命令]''' + self.user_text + '''</div><br><br><br></div><div id = "main" style="background:#f0f0f0"><br><br><div id="left" align="center">AI</div><div id="right">'''
                self.all_text += self.showtext
                self.buffer += self.showtext
                self.output_text += self.output_showtext
            self.a.emit(self.user_text, self.user, self.model, (self.role, self.systemsetting, self.reminder))
            self.b.emit('响应中...')
            self.TextShow.setHtml(self.all_text, QUrl('file:///./'))
            self.all_text = self.all_text[:len(self.all_text)-29]
            self.buffer = self.buffer[:len(self.buffer) - 29]
            self.thread.start()
        else:
            QMessageBox.warning(self, '提示', '您未进行输入', QMessageBox.StandardButton.Yes,QMessageBox.StandardButton.Yes)

    def initpage(self):
        self.bufferback = copy.copy(self.buffer)
        self.timer.start(500)

    def pageshow(self):
        self.showbuffer = copy.copy(self.buffer)
        self.showbuffer += '<br><br><br><a name="bottom">'
        self.TextShow.setHtml(self.showbuffer, QUrl('file:///./'))

    def rolechange(self):
        self.role = self.MessageType.currentText()
    def delta_handle(self, delta):
        self.answer += delta
        self.buffer += delta

    def end_handle(self):
        self.b.emit('')
        self.timer.stop()
        self.all_text += self.answer + '<br><br><br></div></div><a name="bottom">'
        self.output_text += self.answer + '<br><br><br></div></div>'
        if self.keephistory:
            self.history += ('你:' + self.answer + '\n')
            self.word = len(self.history) - 8
            self.WordStatistic.setText(str(self.word) + '/' + str(self.wordmax))
            if self.word >= self.wordmax:
                self.SendButton.setEnabled(False)
        self.buffer += '<br><br><br></div></div><a name="bottom">'
        self.TextShow.setHtml(self.all_text, QUrl('file:///./'))
        if self.role == 'assistant':
            self.reminder = self.answer
        self.answer = ''
        self.SendButton.setEnabled(True)
        self.MessageType.setEnabled(True)

    def system_handle(self):
        self.b.emit('')
        self.systemsetting = self.user_text
        self.all_text += '系统设置成功！<br><br><br></div></div><a name="bottom">'
        self.buffer += '系统设置成功！<br><br><br></div></div><a name="bottom">'
        self.output_text += '系统设置成功！<br><br><br></div></div>'
        self.TextShow.setHtml(self.all_text, QUrl('file:///./'))
        self.SendButton.setEnabled(True)
        self.MessageType.setEnabled(True)
    def bad_answer(self):
        self.timer.stop()
        if self.keephistory:
            self.history += ('你:似乎发生了错误，我无法回答您的问题。\n')
            self.word = len(self.history) - 8
            self.WordStatistic.setText(str(self.word) + '/' + str(self.wordmax))
        self.bufferback += '似乎发生了错误，我无法回答您的问题。<br><br><br></div></div><a name="bottom">'
        self.all_text += '似乎发生了错误，我无法回答您的问题。<br><br><br></div></div><a name="bottom">'
        self.output_text += '似乎发生了错误，我无法回答您的问题。<br><br><br></div></div>'
        self.buffer = self.bufferback
        self.answer = ''
        self.TextShow.setHtml(self.all_text, QUrl('file:///./'))

    def settings(self, setting, reminder):
        self.dialog = QDialog(self)
        self.dialog.resize(800, 50)
        self.dialog.setWindowTitle('设置与提示')
        self.dialog.setWindowModality(Qt.WindowModality.NonModal)
        point = QPoint((QGuiApplication.primaryScreen().size().width()-800)//2, (QGuiApplication.primaryScreen().size().height()-50)//2)
        self.dialog.move(point)
        self.layout = QVBoxLayout()
        self.sys_label = QLabel('系统设置')
        self.sys_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.sys_content = QLineEdit()
        self.sys_content.setText(setting)
        self.sys_content.setReadOnly(True)
        self.sys_button = QPushButton('删除设置')
        if not setting:
            self.sys_button.setEnabled(False)
        self.sys_button.clicked.connect(self.delete_1)
        self.layout_1 = QHBoxLayout()
        for i in [self.sys_label,self.sys_content,self.sys_button]:
            self.layout_1.addWidget(i)
        self.layout_1.setStretch(0, 1)
        self.layout_1.setStretch(1, 10)
        self.layout_1.setStretch(2, 1)
        self.ass_label = QLabel('助手命令')
        self.ass_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ass_content = QLineEdit()
        self.ass_content.setText(reminder)
        self.ass_content.setReadOnly(True)
        self.ass_button = QPushButton('删除设置')
        if not reminder:
            self.ass_button.setEnabled(False)
        self.ass_button.clicked.connect(self.delete_2)
        self. layout_2 = QHBoxLayout()
        for i in [self.ass_label,self.ass_content,self.ass_button]:
            self.layout_2.addWidget(i)
        self.layout_2.setStretch(0, 1)
        self.layout_2.setStretch(1, 10)
        self.layout_2.setStretch(2, 1)
        self.layout.addLayout(self.layout_1)
        self.layout.addLayout(self.layout_2)
        self.dialog.setLayout(self.layout)
        self.dialog.exec()

    def delete_1(self):
        option = QMessageBox.warning(self.dialog,'删除设置','您确定删除吗？',QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No,QMessageBox.StandardButton.No)
        if option == 16384:
            self.sys_content.clear()
            self.systemsetting = ''
            self.sys_button.setEnabled(False)
        elif option == 65536:
            pass

    def delete_2(self):
        option = QMessageBox.warning(self.dialog, '删除设置', '您确定删除吗？', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if option == 16384:
            self.ass_content.clear()
            self.reminder = ''
            self.ass_button.setEnabled(False)
        elif option == 65536:
            pass

class window(Ui_MainWindow, QMainWindow):  #程序主窗口，主要负责tabwidget的维护和菜单栏动作的响应
    key = Signal(QMainWindow,str)
    start = Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.NewChat.setEnabled(False)
        self.actionlongin.setEnabled(False)
        self.actionshift.setEnabled(False)
        self.dir = os.getcwd()
        self.tabs = {}
        self.model_list = ['gpt-3.5-turbo','gpt-3.5-turbo-16k']
        self.loginthread = loginthread()
        self.key.connect(self.loginthread.receive)
        self.loginthread.login.connect(self.login_ok)
        self.loginthread.login_exception.connect(self.login_bad)
        self.statusbartimer = statusbarthread()
        self.statusbartimer.load1.connect(self.loading1)
        self.statusbartimer.load2.connect(self.loading2)
        self.statusbartimer.load3.connect(self.loading3)
        self.start.connect(self.loginthread.start)
        self.start.connect(self.statusbartimer.start)
        self.soundthread = soundthread()
        self.detect()
        self.tabcount = self.ChatTabs.count()
        self.ChatTabs.tabCloseRequested.connect(self.tab_close)
        self.actionabout.triggered.connect(self.about)
        self.actionlongin.triggered.connect(self.login)
        self.actionDelete.triggered.connect(lambda: self.restart(self.ChatTabs.currentWidget()))
        self.actionexport.triggered.connect(lambda: self.output(self.ChatTabs.currentWidget()))
        self.actionshift.triggered.connect(self.shift)
        self.NewChat.clicked.connect(self.newtab)


    def ShowWindow(self):
        global WindowModel
        WindowModel = 0
        self.show()

    def shift(self):
        global SP_DashBoard
        SP_DashBoard.trigger()

    def detect(self):
        try:
            with open(self.dir + '\\OpenAI.key', 'r+') as f:
                key = f.readlines()[0]
            self.key.emit(self, key)
            self.start.emit()
        except Exception:
            self.soundthread.category = 'SystemHand'
            self.soundthread.start()
            QMessageBox.warning(self, '自动登录失败', '没有有效的OpenAI.key' , QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.Yes)
            self.actionlongin.setEnabled(True)

    def login(self):
        try:
            with open(self.dir +'\\OpenAI.key', 'r+') as f:
                key = f.readlines()[0]
            self.actionlongin.setEnabled(False)
            self.key.emit(self, key)
            self.start.emit()
        except Exception:
            text, ok = self._input(self)
            self.statusbar.showMessage('登录中...', 0)
            if text and ok:
                self.actionlongin.setEnabled(False)
                with open(self.dir + '\\OpenAI.key', 'w') as f:
                    f.write(text)
                self.key.emit(self, text)
                self.start.emit()
            else:
                self.soundthread.category = 'SystemHand'
                self.soundthread.start()
                QMessageBox.warning(self, '提示', '用户取消或未输入', QMessageBox.StandardButton.Yes,QMessageBox.StandardButton.Yes)
                self.statusbar.showMessage('登录失败', 0)

    def login_ok(self):
        self.statusbartimer.stop.connect(self.SB_ok)
        self.statusbartimer.requestInterruption()
        if self.tabcount < 3:
            self.NewChat.setEnabled(True)
        else:
            self.NewChat.setEnabled(False)
        self.actionlongin.setEnabled(False)
        self.actionshift.setEnabled(True)
        global SP_DashBoard
        SP_DashBoard.setEnabled(True)
        self._continue()
        self.soundthread.category = 'SystemAsterisk'
        self.soundthread.start()
        QMessageBox.information(self, '登录成功', '已连接至OpenAI', QMessageBox.StandardButton.Yes,QMessageBox.StandardButton.Yes)

    def SB_ok(self):
        self.statusbar.showMessage('登录成功', 0)
        self.statusbartimer.stop.disconnect(self.SB_ok)

    def login_bad(self,e):
        self.statusbartimer.stop.connect(self.SB_bad)
        self.statusbartimer.requestInterruption()
        self.soundthread.category = 'SystemHand'
        self.soundthread.start()
        QMessageBox.critical(self, '登录失败', 'error content:\n' + e, QMessageBox.StandardButton.Yes,QMessageBox.StandardButton.Yes)
        self.actionlongin.setEnabled(True)
        self.actionshift.setEnabled(False)
        global SP_DashBoard
        SP_DashBoard.setEnabled(False)
        self.NewChat.setEnabled(False)

    def SB_bad(self):
        self.statusbar.showMessage('登录失败', 0)
        self.statusbartimer.stop.disconnect(self.SB_bad)

    def restart(self, chattab):
        chattab.all_text = r'''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <script src="file:///./MathJax/tex-mml-chtml.js" id="MathJax-script" async></script>
                <script>
                    window.MathJax = {
                      tex: {
                        inlineMath: [ ["$", "$"], ["\\\\(","\\\\)"] ],
                        displayMath: [ ["$$","$$"], ["\\[", "\\]"] ],
                        processEscapes: true,
                        noundefined: {
                          color: "red",
                          background: "#FFEEEE",
                          size: "90%"
                        },
                        macros: {
                          href: "{}"
                        },
                        autoload: {
                          color: [],
                          colorv2: ['color']
                        },
                        packages: {'[+]': ['noerrors']}
                      },
                      options: {
                        ignoreHtmlClass: "tex2jax_ignore|dno",
                        processHtmlClass: 'tex2jax_process'
                      },
                      loader: {
                        load: ['[tex]/noerrors']
                      }
                    };
                </script>
                <style>
                    img{
                        width:30px;
                        height:30px;
                    }
                    div{
                    word-wrap:break-word;
                    word-break:break-all;
                    overflow:hidden;
                    }
                    #left{
                        width:10%;
                        float: left;
                    }
                    #right{
                        width:90%;
                        float: right;
                    }
                </style>
                <script language="javascript">
                    window.location="#bottom"
                </script>
            </head>
            <body>
            <div id = "main" style="background:#f0f0f0">
                <br><br>
                <div id="left" align="center"><img src="file:///./GPT_ICO.png"/></div>
                <div id="right">您好，请问您有什么问题？</div>
                <br><br><br>
            </div><a name="bottom">'''
        chattab.buffer = r'''
                <!DOCTYPE html>
                <html>
                    <head>
                        <meta charset="UTF-8">
                        <style>
                            img{
                                width:30px;
                                height:30px;
                            }
                            div{
                            word-wrap:break-word;
                            word-break:break-all;
                            overflow:hidden;
                            }
                            #left{
                                width:10%;
                                float: left;
                            }
                            #right{
                                width:90%;
                                float: right;
                            }
                        </style>
                        <script language="javascript">
                            window.location="#bottom"
                        </script>
                    </head>
                    <body>
                    <div id = "main" style="background:#f0f0f0">
                        <br><br>
                        <div id="left" align="center"><img src="file:///./GPT_ICO.png"/></div>
                        <div id="right">您好，请问您有什么问题？</div>
                        <br><br><br>
                    </div><a name="bottom">'''
        chattab.answer = ''
        chattab.systemsetting = ''
        chattab.reminder = ''
        chattab.SendText.clear()
        chattab.history = '这是对话历史： \n'
        chattab.word = 0
        chattab.change = False
        chattab.WordStatistic.setText('')
        chattab.TextShow.setHtml(chattab.all_text, QUrl('file:///./'))
        chattab.user = time.asctime()
        chattab.MessageType.setCurrentIndex(0)
        chattab.SendButton.setEnabled(True)
        chattab.MessageType.setEnabled(True)

    def output(self,chattab):
        if not chattab.change:
            self.soundthread.category = 'SystemHand'
            self.soundthread.start()
            QMessageBox.warning(self,'导出失败','您未进行过对话',QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.Yes)
        else:
            self.statusbar.showMessage('导出对话中...',0)
            if os.path.exists(self.dir + '\\dialog history'):
                pass
            else:
                os.mkdir(self.dir + '\\dialog history')
            with open(self.dir + '\\dialog history\\dialog_' + chattab._user + '.html', 'w', encoding='utf-8') as f:
                f.write(chattab.output_text)
            self.soundthread.category = 'SystemAsterisk'
            self.soundthread.start()
            QMessageBox.information(self, '导出成功', '已成功导出', QMessageBox.StandardButton.Yes,QMessageBox.StandardButton.Yes)
            self.statusbar.clearMessage()

    def newtab(self):
        self.dialog = createdialog(self, self.model_list)
        self.dialog.a.connect(self.createtab)
        self.dialog.show()

    def createtab(self, value):
        try:
            create_time = str(time.time())
            self.tabs[create_time] = tab()
            self.ChatTabs.addTab(self.tabs[create_time], value['model'])
            self.tabs[create_time].b.connect(self.SB_handle)
            self.tabs[create_time].TextShow.setHtml(self.tabs[create_time].all_text, QUrl('file:///./'))
            self.tabs[create_time].user = time.asctime()
            self.tabs[create_time]._user = create_time
            self.tabs[create_time].model = value['model']
            self.tabs[create_time].keephistory = value['continue']
            if value['continue']:
                if value['model'] == 'gpt-3.5-turbo':
                    self.tabs[create_time].wordmax = 4096
                else:
                    self.tabs[create_time].wordmax = 16384
                self.tabs[create_time].MessageType.hide()
                self.tabs[create_time].CheckContent.hide()
                self.tabs[create_time].horizontalLayout.setStretch(0, 0)
                self.tabs[create_time].horizontalLayout.setStretch(1, 8)
                self.tabs[create_time].horizontalLayout.setStretch(2, 1)
            self.tabs[create_time].e.connect(self.thread_error)
            self.tabcount = self.ChatTabs.count()
            self.ChatTabs.setCurrentIndex(self.tabcount-1)
            if self.tabcount >= 3:
                self.NewChat.setEnabled(False)
            del self.dialog
        except Exception:
            pass

    def tabchange(self):
        self.ChatTabs.setCurrentIndex(-1)

    def tab_close(self, index):
        del_tab = self.ChatTabs.widget(index)
        self.ChatTabs.removeTab(index)
        del self.tabs[del_tab._user]
        self.tabcount = self.ChatTabs.count()
        if not self.actionlongin.isEnabled():
            self.NewChat.setEnabled(True)

    def SB_handle(self,string):
        if string:
            self.statusbar.showMessage(string,0)
        else:
            self.statusbar.clearMessage()

    def thread_error(self,string):
        self.soundthread.category = 'SystemHand'
        self.soundthread.start()
        QMessageBox.critical(self, '错误', 'error content:\n' + string, QMessageBox.StandardButton.Yes,QMessageBox.StandardButton.Yes)
        self.Statelabel.setText('当前状态：未连接至OpenAI')
        self.actionlongin.setEnabled(True)
        self.actionshift.setEnabled(False)
        global SP_DashBoard
        SP_DashBoard.setEnabled(False)
        self.NewChat.setEnabled(False)
        self.statusbar.clearMessage()
        for i in self.tabs:
            self.tabs[i].SendButton.setEnabled(False)
            self.tabs[i].MessageType.setEnabled(False)

    def loading1(self):
        self.statusbar.showMessage('登录中.', 1000)

    def loading2(self):
        self.statusbar.showMessage('登录中..', 1000)

    def loading3(self):
        self.statusbar.showMessage('登录中...', 1000)
    def _continue(self):
        try:
            for i in self.tabs:
                self.tabs[i].SendButton.setEnabled(True)
                self.tabs[i].MessageType.setEnabled(True)
        except Exception:
            pass

    def about(self):
        QMessageBox.information(self, '关于GPT for Windows 3.3', '''这是一款利用OpenAI的API与ChatGPT实现交互的本地应用。<br><br>该项目主要功能如下：<br>（1）可以实现多对话同步进行和快速导出对话记录(html文件)<br>（2）可以实现自动登录（会在当前目录下生成一个.key文件来保存您的登录秘钥）<br>（3）支持对数学、物理公式的显示与导出支持<br>（4）支持对话模型的选择<br>（5）增加‘‘悬浮模式’’，置顶小窗便于查询<br>（6）现在支持手控长对话、连续对话两种对话类型<br><br>项目开发人员：库斯科Fack<br>项目网址：<a href='https://github.com/KusicFack/GPT-for-Windows'>https://github.com/KusicFack/GPT-for-Windows''' ,
                                QMessageBox.StandardButton.Yes,QMessageBox.StandardButton.Yes)

    @staticmethod
    def _input(widget):
        text, ok = QInputDialog.getText(widget, '登录', '请输入OpenAI API Key: ')
        return text, ok

class SP_Window(Ui_Form, QWidget):
    a = Signal(str, str, str, tuple)
    b = Signal(str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(':/icos/GPT_ICO.ico'))
        self.AnswerShow.hide()
        self.setMinimumSize(600, 50)
        self.setMaximumSize(800, 50)
        self.ClearButton.setEnabled(False)
        self.SendButton.clicked.connect(self.SendMessage)
        self.ClearButton.clicked.connect(self.Clear)
        self.delta = ''
        self.answer = r'''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <script src="file:///./MathJax/tex-mml-chtml.js" id="MathJax-script" async></script>
                <script>
                    window.MathJax = {
                      tex: {
                        inlineMath: [ ["$", "$"], ["\\\\(","\\\\)"] ],
                        displayMath: [ ["$$","$$"], ["\\[", "\\]"] ],
                        processEscapes: true,
                        noundefined: {
                          color: "red",
                          background: "#FFEEEE",
                          size: "90%"
                        },
                        macros: {
                          href: "{}"
                        },
                        autoload: {
                          color: [],
                          colorv2: ['color']
                        },
                        packages: {'[+]': ['noerrors']}
                      },
                      options: {
                        ignoreHtmlClass: "tex2jax_ignore|dno",
                        processHtmlClass: 'tex2jax_process'
                      },
                      loader: {
                        load: ['[tex]/noerrors']
                      }
                    };
                </script>
                <style>
                div{
                word-wrap:break-word
                word-break:break_all
                overflow:hidden;
                }
                </style>
                <script language="javascript">
                window.location="#bottom"
                </script>
            </head>
            <body>
                <a name="bottom">'''
        self.buffer = r'''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <style>
                div{
                word-wrap:break-word
                word-break:break_all
                overflow:hidden;
                }
                </style>
                <script language="javascript">
                window.location="#bottom"
                </script>
            </head>
            <body>
                <a name="bottom">'''
        self.timer = QTimer()
        self.timer.timeout.connect(self.pageshow)
        self.thread = mythread()
        self.thread.text.connect(self.delta_handle)
        self.thread.start.connect(self.init_handle)
        self.thread.end.connect(self.end_handle)
        self.thread.error.connect(self.bad_answer)
        self.a.connect(self.thread.receive)

    def ShowWindow_SP(self):
        global WindowModel
        WindowModel = 1
        self.show()

    def SendMessage(self):
        if self.QuestionEdit.text():
            self.answer = r'''
                    <!DOCTYPE html>
                    <html>
                        <head>
                            <meta charset="UTF-8">
                            <script src="file:///./MathJax/tex-mml-chtml.js" id="MathJax-script" async></script>
                            <script>
                                window.MathJax = {
                                  tex: {
                                    inlineMath: [ ["$", "$"], ["\\\\(","\\\\)"] ],
                                    displayMath: [ ["$$","$$"], ["\\[", "\\]"] ],
                                    processEscapes: true,
                                    noundefined: {
                                      color: "red",
                                      background: "#FFEEEE",
                                      size: "90%"
                                    },
                                    macros: {
                                      href: "{}"
                                    },
                                    autoload: {
                                      color: [],
                                      colorv2: ['color']
                                    },
                                    packages: {'[+]': ['noerrors']}
                                  },
                                  options: {
                                    ignoreHtmlClass: "tex2jax_ignore|dno",
                                    processHtmlClass: 'tex2jax_process'
                                  },
                                  loader: {
                                    load: ['[tex]/noerrors']
                                  }
                                };
                            </script>
                            <style>
                            div{
                            word-wrap:break-word
                            word-break:break_all
                            overflow:hidden;
                            }
                            </style>
                            <script language="javascript">
                            window.location="#bottom"
                            </script>
                        </head>
                        <body>
                            <a name="bottom">'''
            self.buffer = r'''
                    <!DOCTYPE html>
                    <html>
                        <head>
                            <meta charset="UTF-8">
                            <style>
                            div{
                            word-wrap:break-word
                            word-break:break_all
                            overflow:hidden;
                            }
                            </style>
                            <script language="javascript">
                            window.location="#bottom"
                            </script>
                        </head>
                        <body>
                            <a name="bottom">'''
            self.delta = ''
            self.SendButton.setEnabled(False)
            self.ClearButton.setEnabled(False)
            self.QuestionEdit.setEnabled(False)
            self.user_text = self.QuestionEdit.text()
            self.a.emit(self.user_text, '', 'gpt-3.5-turbo', ('user', '', ''))
            self.thread.start()
        else:
            QMessageBox.warning(self, '提示', '您未进行输入', QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.Yes)

    def init_handle(self):
        self.setMinimumSize(600, 200)
        self.setMaximumSize(800, 600)
        self.AnswerShow.show()
        self.timer.start(500)
        self.answer = self.answer[:len(self.answer) - 17]
        self.buffer = self.buffer[:len(self.buffer) - 17]
        self.answer += '<div><p>'
        self.buffer += '<div><p>'
        self.AnswerShow.setHtml(self.buffer, QUrl('file:///./'))

    def pageshow(self):
        self.showbuffer = copy.copy(self.buffer) + '<a name="bottom">'
        self.AnswerShow.setHtml(self.showbuffer, QUrl('file:///./'))

    def delta_handle(self, delta):
        self.delta += delta
        self.buffer += delta

    def end_handle(self):
        self.timer.stop()
        self.delta += '</p></div><a name="bottom">'
        self.answer += self.delta
        self.AnswerShow.setHtml(self.answer, QUrl('file:///./'))
        self.SendButton.setEnabled(True)
        self.ClearButton.setEnabled(True)
        self.QuestionEdit.setEnabled(True)

    def bad_answer(self,e):
        global CP_DashBoard, my_window
        CP_DashBoard.trigger()
        self.AnswerShow.hide()
        self.setMinimumSize(600, 50)
        self.setMaximumSize(800, 50)
        self.QuestionEdit.clear()
        self.QuestionEdit.setEnabled(True)
        self.SendButton.setEnabled(True)
        self.ClearButton.setEnabled(True)
        self.b.connect(my_window.thread_error)
        self.b.emit(e)

    def Clear(self):
        self.AnswerShow.hide()
        self.answer = r'''
                            <!DOCTYPE html>
                            <html>
                                <head>
                                    <meta charset="UTF-8">
                                    <script src="file:///./MathJax/tex-mml-chtml.js" id="MathJax-script" async></script>
                                    <script>
                                        window.MathJax = {
                                          tex: {
                                            inlineMath: [ ["$", "$"], ["\\\\(","\\\\)"] ],
                                            displayMath: [ ["$$","$$"], ["\\[", "\\]"] ],
                                            processEscapes: true,
                                            noundefined: {
                                              color: "red",
                                              background: "#FFEEEE",
                                              size: "90%"
                                            },
                                            macros: {
                                              href: "{}"
                                            },
                                            autoload: {
                                              color: [],
                                              colorv2: ['color']
                                            },
                                            packages: {'[+]': ['noerrors']}
                                          },
                                          options: {
                                            ignoreHtmlClass: "tex2jax_ignore|dno",
                                            processHtmlClass: 'tex2jax_process'
                                          },
                                          loader: {
                                            load: ['[tex]/noerrors']
                                          }
                                        };
                                    </script>
                                    <style>
                                    div{
                                    word-wrap:break-word
                                    word-break:break_all
                                    overflow:hidden;
                                    }
                                    </style>
                                    <script language="javascript">
                                    window.location="#bottom"
                                    </script>
                                </head>
                                <body>
                                    <a name="bottom">'''
        self.buffer = r'''
                            <!DOCTYPE html>
                            <html>
                                <head>
                                    <meta charset="UTF-8">
                                    <style>
                                    div{
                                    word-wrap:break-word
                                    word-break:break_all
                                    overflow:hidden;
                                    }
                                    </style>
                                    <script language="javascript">
                                    window.location="#bottom"
                                    </script>
                                </head>
                                <body>
                                    <a name="bottom">'''
        self.QuestionEdit.clear()
        self.AnswerShow.setHtml('')
        self.setMinimumSize(600, 50)
        self.setMaximumSize(800, 50)

if __name__ == '__main__':

    def GlobalShow(num):
        if num == 0:
            global my_window
            my_window.showNormal()

        elif num == 1:
            global my_sp_window
            my_sp_window.showNormal()

    def StateChange1():
        global CP_DashBoard, SP_DashBoard
        CP_DashBoard.setEnabled(True)
        CP_DashBoard.setCheckable(True)
        CP_DashBoard.setChecked(False)
        SP_DashBoard.setChecked(True)
        SP_DashBoard.setEnabled(False)

    def StateChange2():
        global CP_DashBoard, SP_DashBoard
        SP_DashBoard.setEnabled(True)
        SP_DashBoard.setCheckable(True)
        SP_DashBoard.setChecked(False)
        CP_DashBoard.setChecked(True)
        CP_DashBoard.setEnabled(False)

    def click(reason):
        if reason == QSystemTrayIcon.Context:
            pass
        elif reason == QSystemTrayIcon.Trigger or QSystemTrayIcon.DoubleClick:
            global GlobalShow, WindowModel
            GlobalShow(WindowModel)

    pic_check(pic1)
    pic_check(pic2)
    a = QApplication()
    a.setQuitOnLastWindowClosed(False)
    WindowModel = 0
    my_window = window()
    my_sp_window = SP_Window()

    showwindowaction = QAction('显示')
    quitaction = QAction('退出')
    DashBoard = QMenu('切换视图')
    CP_DashBoard = QAction('标准视图')
    CP_DashBoard.setCheckable(True)
    CP_DashBoard.setChecked(True)
    CP_DashBoard.setEnabled(False)
    CP_DashBoard.triggered.connect(my_window.ShowWindow)
    CP_DashBoard.triggered.connect(my_sp_window.hide)
    CP_DashBoard.triggered.connect(StateChange2)
    SP_DashBoard = QAction('悬浮视图')
    SP_DashBoard.setCheckable(True)
    SP_DashBoard.triggered.connect(my_sp_window.ShowWindow_SP)
    SP_DashBoard.triggered.connect(my_window.hide)
    SP_DashBoard.triggered.connect(StateChange1)
    DashBoard.addAction(CP_DashBoard)
    DashBoard.addAction(SP_DashBoard)
    showwindowaction.triggered.connect(lambda:GlobalShow(WindowModel))
    quitaction.triggered.connect(QApplication.quit)
    TrayIconMenu = QMenu()
    TrayIconMenu.addAction(showwindowaction)
    TrayIconMenu.addSeparator()
    TrayIconMenu.addMenu(DashBoard)
    TrayIconMenu.addSeparator()
    TrayIconMenu.addAction(quitaction)
    TrayIcon = QSystemTrayIcon(QIcon(':/icos/GPT_ICO.ico'))
    TrayIcon.setToolTip('GPT for Windows 3.3')
    TrayIcon.setContextMenu(TrayIconMenu)
    TrayIcon.activated.connect(click)
    TrayIcon.show()

    my_window.show()
    a.exec()