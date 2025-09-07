from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivymd.uix.textfield import MDTextField


Window.size=(400, 600)
Builder.load_string("""
<Main>:
    Screen:
        RelativeLayout:
            canvas:
                Rectangle:
                    source: "file_image//blaci22.jpg"
                    size: self.size
                    pos: self.pos
            MDFloatLayout:
                MDTextField:
                    id: text_input
                    mode: 'round'
                    size_hint: None, None
                    size: 260, 50
                    pos_hint: {"center_x": 0.51, "center_y": 0.8}
                    font_size: 24
                    multiline: False
                    

                
                GridLayout
                    rows: 5
                    cols: 4
                    pos_hint: {"center_x": 0.7, "center_y": 0.2}
                    spacing:15
                    icon_size: 75
                    MDIconButton:
                        id: clear
                        icon : "backspace-outline"
                        md_bg_color: "white"
                        md_bg_color: "#a6a6a6"
                        icon_size: 30
                        on_press: text_input.text = text_input.text[:-1]
                        
                        
                    
                    MDIconButton:
                        icon : "contrast"
                        md_bg_color: "white"
                        md_bg_color: "#a6a6a6"
                        icon_size: 30
                    
                    MDIconButton:
                        icon : "percent-outline"
                        md_bg_color: "white"
                        md_bg_color: "#a6a6a6"
                        icon_size: 30
                        on_press: text_input.text +="//"
                        
                    
                    MDIconButton:
                        icon : "division"
                        md_bg_color: "white"
                        icon_size: 30
                        on_press: text_input.text +="/"
                        md_bg_color: "#e0b038" 
                        
                    # اجزاء رياصيات
                        
                    
                    
                    
                    MDIconButton:
                        icon : "numeric-7"
                        md_bg_color: "white"
                        icon_size: 30
                        on_press: text_input.text +="7"
            
                    
                    MDIconButton:
                        icon : "numeric-8"
                        md_bg_color: "white"
                        icon_size: 30
                        on_press: text_input.text +="8"
                    
                    MDIconButton:
                        icon : "numeric-9"
                        md_bg_color: "white"
                        icon_size: 30
                        on_press: text_input.text +="9"
                    
                    MDIconButton:
                        icon : "close"
                        md_bg_color: "white"
                        icon_size: 30
                        on_press: text_input.text +="*"
                        md_bg_color: "#e0b038" 
                        
                    
                    MDIconButton:
                        icon : "numeric-6"
                        md_bg_color: "white"
                        icon_size: 30
                        on_press: text_input.text +="6"
            
                    
                    MDIconButton:
                        icon : "numeric-5"
                        md_bg_color: "white"
                        icon_size: 30
                        on_press: text_input.text +="5"
                    
                    MDIconButton:
                        icon : "numeric-4"
                        md_bg_color: "white"
                        icon_size: 30
                        on_press: text_input.text +="4"
                    
                    MDIconButton:
                        icon : "minus"
                        md_bg_color: "white"
                        icon_size: 30
                        on_press: text_input.text +="-"
                        md_bg_color: "#e0b038" 
                        
                    
                    MDIconButton:
                        icon : "numeric-3"
                        md_bg_color: "white"
                        icon_size: 30
                        on_press: text_input.text +="3"
                        
            
                    
                    MDIconButton:
                        icon : "numeric-2"
                        md_bg_color: "white"
                        icon_size: 30
                        on_press: text_input.text +="2"
                    
                    MDIconButton:
                        icon : "numeric-1"
                        md_bg_color: "white"
                        icon_size: 30
                        on_press: text_input.text +="1"
                        
                    
                    MDIconButton:
                        icon : "plus"
                        md_bg_color: "white"
                        icon_size: 30
                        on_press: text_input.text +="+"
                        md_bg_color: "#e0b038" 
                        
                        
                    
          
                    
                    MDIconButton:
                        icon : "calculator"
                        md_bg_color: "white"
                        icon_size: 30
                        
                        
            
                    
                    MDIconButton:
                        icon : "numeric-0"
                        md_bg_color: "white"
                        icon_size: 30
                        on_press: text_input.text +="0"
                        
                    
                    MDIconButton:
                        icon : "circle-small"
                        md_bg_color: "white"
                        icon_size: 30
                        on_press: text_input.text +="."

                    MDIconButton:
                        icon : "equal"
                        md_bg_color: "white"
                        icon_size: 30
                        font_size: 30
                        on_press: text_input.text =str(eval(text_input.text))
                        
                        md_bg_color: "#e0b038" 
                    
          
                   
                    



""")
class Main(Screen):
    def clear(self):
        self.ids.clear

class Name(MDApp):
    def build(self):
        cal=Screen()
        cal.add_widget(Main(name="Main"))
        
        return cal

Name().run()