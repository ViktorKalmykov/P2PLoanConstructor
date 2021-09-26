from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons
from kivymd.font_definitions import fonts

KV = '''
#https://stackoverflow.com/questions/65698145/kivymd-tab-name-containing-icons-and-text
# this import will prevent disappear tabs through some clicks  
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts

# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)
    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color
<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"
    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height
        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/kivy-icon-256.png"
    MDLabel:
        text: "P2P Loans Constructor"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]
    MDLabel:
        text: "by Viktor Kalmykov, Biscuit Team"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]
    ScrollView:
        DrawerList:
            id: md_list
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "P2P Loans Constructor"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["star-outline", lambda x: app.on_star_click()]]
                        md_bg_color: 0, 0, 0, 1                    
                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)
                        height: "48dp"
                        tab_indicator_anim: False
                        background_color: 0.1, 0.1, 0.1, 1 
                    
                        Tab:
                            id: tab1
                            name: 'tab1'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['calculator-variant']}[/size][/font] Input"
                    
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"
                              
                                BoxLayout:
                                    orientation: 'horizontal'
                                  
                                    MDIconButton:
                                        icon: "calendar-month"
                                      
                                    MDTextField:
                                        hint_text: "Start date"
                                      
                                BoxLayout:
                                    orientation: 'horizontal'
                                  
                                    MDIconButton:
                                        icon: "cash"
                                      
                                    MDTextField:
                                        hint_text: "Loan"
                                      
                                BoxLayout:
                                    orientation: 'horizontal'
                                  
                                    MDIconButton: 
                                        icon: "clock-time-five-outline"
                                      
                                    MDTextField:
                                        hint_text: "Months"
                                      
                                BoxLayout:
                                    orientation: "horizontal"
                                  
                                    MDIconButton:
                                        icon: "bank"   
                                      
                                    MDTextField:
                                        hint_text: "Interest, %"
                                      
                                    MDTextField:
                                        id: payment_type
                                        hint_text: "Payment type"
                                        on_focus: if_self.focus: app.menu.open()
                           
                        Tab:
                            id: tab2
                            name: 'tab2'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-pie']}[/size][/font] Portfolio composition"
                    
                        Tab:
                            id: tab3
                            name: 'tab3'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-bar-stacked']}[/size][/font] Payments forecast"
                    
                        Tab:
                            id: tab4
                            name: 'tab4'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-box-plus-outline']}[/size][/font] Duration"
                    
                        Tab:
                            id: tab5
                            name: 'tab5'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['checkbox-marked-outline']}[/size][/font] Summary"
                    
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                id: content_drawer
'''


class Tab(MDFloatLayout, MDTabsBase):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class P2PLoansConstructorApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    def on_start(self):
        icons_item_menu_lines = {
            "account-cog-outline": "My Account",
            "hand-okay": "My Grade",
            "head-lightbulb-outline": "Buscuit Bot",
            "alpha": "Market Screener",
            "beta": "About",
            "search-web": "Biscuit.com",
        }
        icons_item_menu_tabs = {
            "calculator-variant": "Input",
            "table-large": "Table",
            "chart-areaspline": "Payments",
            "chart-pie": "Portfolio composition",
            "book-open-variant": "Summary"
        }
        for icon_name in icons_item_menu_lines.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item_menu_lines[icon_name])
            )

        # To auto generate tabs
        # for icon_name, name_tab in icons_item_menu_tabs.items():
        #   self.root.ids.tabs.add_widget(
        #       Tab(
        #           text=f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons[icon_name]}[/font][/ref] {name_tab}"
        #       )
        #   )

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        print("tab clicked! "+tab_text)

    def on_star_click(self):
        pass

P2PLoansConstructorApp().run()

