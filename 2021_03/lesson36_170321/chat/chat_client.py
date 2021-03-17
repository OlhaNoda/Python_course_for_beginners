from PyQt5 import QtCore, QtWidgets
import ui_chat_client
import ui_chat_connect
import sys
import socket


class ReceiveThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self, client_socket):
        super(ReceiveThread, self).__init__()
        self.client_socket = client_socket

    def run(self):
        while True:
            message = self.client_socket.recv(1024)
            message = message.decode()
            self.signal.emit(message)


class Client:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.init_ui()
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def init_ui(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.connectWidget = QtWidgets.QWidget(self.mainWindow)
        self.chatWidget = QtWidgets.QWidget(self.mainWindow)
        self.chatWidget.setHidden(True)
        self.chat_ui = ui_chat_client.Ui_Form()
        self.chat_ui.setupUi(self.chatWidget)
        self.chat_ui.pushButton.clicked.connect(self.send_message)
        self.connect_ui = ui_chat_connect.Ui_Form()
        self.connect_ui.setupUi(self.connectWidget)
        self.connect_ui.pushButton.clicked.connect(self.button_connect_clicked)
        self.mainWindow.setGeometry(QtCore.QRect(1100, 20, 320, 500))
        self.mainWindow.show()

    def button_connect_clicked(self):
        nickname = self.connect_ui.nameTextEdit.toPlainText()
        if self.connect(self.host, self.port, nickname):
            self.connectWidget.setHidden(True)
            self.chatWidget.setVisible(True)
            self.recv_thread = ReceiveThread(self.client_sock)
            self.recv_thread.signal.connect(self.show_message)
            self.recv_thread.start()

    def show_message(self, message):
        self.chat_ui.textBrowser.append(message)

    def connect(self, host, port, nickname):
        self.client_sock.connect((host, port))
        self.client_sock.send(nickname.encode())
        return True

    def send_message(self):
        message = self.chat_ui.textEdit.toPlainText()
        self.chat_ui.textBrowser.append("я: " + message)
        self.client_sock.send(message.encode())
        self.chat_ui.textEdit.clear()


if __name__ == "__main__":
    chat_host = '127.0.0.1'
    chat_port = 65432
    app = QtWidgets.QApplication(sys.argv)
    chat_client = Client(chat_host, chat_port)
    sys.exit(app.exec())
