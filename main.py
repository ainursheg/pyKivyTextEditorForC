from kivy.app import App                         # Importing all neccessary libs

from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.codeinput import CodeInput
from kivy.uix.textinput import TextInput

from pygments.lexers import CLexer

from os import system, popen

class TextEditorApp(App):

    def newFile(self, args):
        try:
            with open(self.nameF.text, "w") as file:
                result = "New file created"
        except FileNotFoundError:
            result = "File not found!"
        finally:
            self.check.text = result
    
    def openFile(self, args):
        try:
            with open(self.nameF.text) as file:
                self.code.text = file.read()
        except FileNotFoundError:
            self.check.text = "File not found!"
                
    def compileFile(self, args, result = ""):
        try:
            with open(self.nameF.text, "w") as file:
                file.write(self.code.text)
        except FileNotFoundError:
            result = "Error: file not found!"
        else:
            system("gcc %s"%(self.nameF.text))
            for string in popen("./a.out"):
                result += string
        finally:
            self.check.text = result

    def saveFile(self, args):
        try:
            with open(self.nameF.text, "w") as file:
                result = "Success: file saved!"
                file.write(self.code.text)
        except FileNotFoundError:
            result = "Error: file not found!"
        finally:
            self.check.text = result


    def build(self):                            # GUI Interface
        root = BoxLayout(
            orientation = "vertical")

        butn = GridLayout(
            cols = 4, size_hint = [1,.07])

        self.nameF = TextInput(
            text = "", size_hint = [1,.1],
            background_color = [1,1,1,.5])
        root.add_widget(self.nameF)

        buttonNew = Button(
            text = 'New File', on_press = self.newFile)
        butn.add_widget(buttonNew)

        buttonOpen = Button(
            text = 'Open File', on_press = self.openFile)
        butn.add_widget(buttonOpen)

        buttonCompile = Button(
            text = 'Compile file', on_press = self.compileFile)
        butn.add_widget(buttonCompile)

        buttonSave = Button(
            text = 'Save File', on_press = self.saveFile)
        butn.add_widget(buttonSave)

        root.add_widget(butn)

        self.code = CodeInput(
            text = "", lexer = CLexer())
        root.add_widget(self.code)

        self.check = TextInput(
            text = "", size_hint = [1,.3],
            background_color = [1,1,1,.5])
        root.add_widget(self.check)

        return root

if __name__ == '__main__':
    TextEditorApp().run()