
import wikipedia
import wx
import pyttsx3
import speech_recognition as sr
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
                          pos=wx.DefaultPosition, size=wx.Size(450, 100),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
                                wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                          title="Assistant Wikipedia")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
                            label="Veuillez effectuer une recherche dans Wikipedia")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400, 30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):

                question=self.txt.GetValue()

                nombre=0
                if question is "":
                            print("erreur")
                else:

                    wikipedia.set_lang("fr")

                    nbpages=wikipedia.search(question)
                    for i in nbpages:
                      nombre = nombre + 1
                    if nombre > 0:
                        wiki = wikipedia.summary(question, sentences=2)

                        print(wiki)
                        engine = pyttsx3.init()
                        engine.say(wiki)
                        engine.runAndWait()
                    else:
                        engine = pyttsx3.init()
                        engine.say("Aucune page trouvée")
                        engine.runAndWait()



if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()