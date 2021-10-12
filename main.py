# pip install kivy
# pip install kivymd
# pip install https://github.com/kivymd/KivyMD/archive/3274d62.zip
from calendar import calendar

from kivy.graphics import Color, Rectangle, Line, Ellipse
from random import random as r

from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

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

from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock

from kivymd.uix.picker import MDDatePicker
import datetime
import calendar

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
                                        id: start_date
                                        hint_text: "Start date"
                                        on_focus: if self.focus: app.date_dialog.open()
                                        color_mode: 'custom'
                                        line_color_focus: 0, 0, 0, 1
                                        text_color: 0, 0, 0, 1
                                        current_hint_text_color: 0, 0, 0, 1
                                        text_hint_color: 0, 0, 1, 1

                                    MDTextField:
                                        hint_text: "Start date"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "cash"

                                    MDTextField:
                                        id: loan
                                        hint_text: "Loan"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton: 
                                        icon: "clock-time-five-outline"

                                    MDTextField:
                                        id: months
                                        hint_text: "Months"

                                BoxLayout:
                                    orientation: "horizontal"

                                    MDIconButton:
                                        icon: "bank"   

                                    MDTextField:
                                        id: interest
                                        hint_text: "Interest rate, %"

                                    MDTextField:
                                        id: payment_type
                                        hint_text: "Payment type"
                                        on_focus: if self.focus: app.menu.open()
                                MDSeparator:
                                    height: "1dp"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    AnchorLayout:
                                        anchor_x: 'center'

                                        MDRectangleFlatIconButton:
                                            icon: "android"
                                            text: "BUTTON1"
                                            adaptive_width: True
                                            on_release: app.calc_table(*args)

                                    AnchorLayout:
                                        anchor_x: 'center'

                                        MDRectangleFlatIconButton:
                                            icon: "android"
                                            text: "BUTTON2"
                                            theme_text_color: "Custom"
                                            text_color: 1, 1, 1, 1
                                            line_color: 0, 0, 0, 1
                                            icon_color: 1, 0, 0, 1
                                            md_bg_color: 0, 0, 0, 1
                                            on_release: app.share_it(*args)

                                    AnchorLayout:
                                        anchor_x: 'center'

                                        Button:
                                            text: "Test Ok"
                                            size_hint_y: .5
                                            background_color: (0.1, 0.1, 0.1, 1.0)
                                            
                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"
                                    
                                    MDLabel:
                                        text: "Payment"
                                        
                                    MDTextField:
                                        id: payment_label
                                        hint_text: ""
                                        disabled: True
                                BoxLayout:
                                    orientation: "horizontal"
                                    padding: "10dp"
                                    
                                    MDLabel:
                                        text: "Total interest"
                                        
                                    MDTextField:
                                        id: overpayment_loan_label
                                        hint_text: ""
                                        disabled: True
                                        
                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"
                                    
                                    MDLabel:
                                        text: "Total payments"
                                        
                                    MDTextField:
                                        id: total_amount_of_payments_label
                                        hint_text: ""
                                        disabled: True
                                        
                                BoxLayout:
                                    orientation: "horizontal"
                                    padding: "10dp"
                                    
                                    MDLabel:
                                        text: "Effective %"
                                        
                                    MDTextField:
                                        id: effective_interest_rate_label
                                        hint_text: ""
                                        disabled: True
                                        text_hint_color:[0, 0, 1, 1]
                                        
                        Tab:
                            id: tab2
                            name: 'tab2'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-bar-stacked']}[/size][/font] Payments forecast"   

                            ScrollView:
                                BoxLayout:
                                    orientation: 'vertical'
                                    id: calc_data_table
                                    
                            MDFloatingActionButton:
                                icon: "email-outline"
                                pos: 20, 20 
                                on_release: app.show_confirmation_dialog()


                        Tab:
                            id: tab3
                            name: 'tab3'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-pie']}[/size][/font] Portfolio composition"

                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"
                                
                                
                                BoxLayout:
                                    orientation: 'vertical'
                                    padding: "10dp"
                                    size_hint_x: 1
                                    size_hint_y: None
                                    height: 50

                                    canvas: 
                                        Color: 
                                            rgba: 0.2, 0.2, 0.2, 0.1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos

                                    MDLabel:
                                        text: "Payment"
                                        halign: "center"
                                        font_style: "H5"
                                        height: "48dp"

                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"
                                id: graph

                                canvas:
                                    Color:
                                        rgba: 1, 1, 1, 1
                                    Rectangle:
                                        size: self.size
                                        pos: self.pos


                            BoxLayout:
                                orientation: 'horizontal'
                                padding: "10dp"
                                size_hint_x: 1
                                size_hint_y: None
                                height: 50

                                MDIcon:
                                    icon: "checkbox-blank"
                                    halign: "right"
                                    color: 0, 0, 1, 1

                                MDLabel: 
                                    text: "Interest"
                                    halign: "left"
                                    font_style: "H6"
                                    height: "48dp"

                                MDIcon:
                                    icon: "checkbox-blank"
                                    halign: "right"
                                    color: 1, 0, 0, 1

                                MDLabel:
                                    text: "Principal"
                                    halign: "left"
                                    font_style: "H6"
                                    height: "48dp" 

                        Tab:
                            id: tab4
                            name: 'tab4'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-box-plus-outline']}[/size][/font] Duration"

                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"

                                BoxLayout:
                                    orientation: 'vertical'
                                    padding: "10dp"
                                    size_hint_x: 1
                                    size_hint_y: None
                                    height: 50

                                    canvas:
                                        Color:
                                            rgba: 0.2, 0.2, 0.2, 0.1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos

                                    MDLabel:
                                        text: "Total payments"
                                        halign: "center"
                                        font_style: "H5"
                                        height: "48dp"   

                                BoxLayout:
                                    orientation: 'vertical'
                                    padding: "10dp"
                                    id: chart

                                    canvas:
                                        Color:
                                            rgba: 1, 1, 1, .6
                                        Rectangle: 
                                            size: self.size
                                            pos: self.pos

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"
                                    size_hint_x: 1
                                    size_hint_y: None
                                    height: 50

                                    MDIcon:
                                        icon: "checkbox-blank"
                                        halign: "right"
                                        color: 0, 0, 1, 1

                                    MDLabel:
                                        text: "Interest"
                                        halign: "left"
                                        font_style: "H6"
                                        height: "48dp"

                                    MDIcon:
                                        icon: "checkbox-blank"
                                        halign: "right"
                                        color: 1, 0, 0, 1

                                    MDLabel:
                                        text: "principal"
                                        halign: "left"
                                        font_style: "H6"
                                        height: "48dp"  

                        Tab:
                            id: tab5
                            name: 'tab5'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['checkbox-marked-outline']}[/size][/font] Summary"

        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                id: content_drawer
                
<ContentDialogSend>
    orientation: 'vertical'
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"
    
    MDTextField:
        hint_text: "Email"
        
    MDTextField:
        hint_text: "Message"
'''


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab'''

class ContentDialogSend(BoxLayout):
    pass

def next_month_date(d):
    _year = d.year + (d.month // 12)
    _month = 1 if (d.month // 12) else d.month + 1
    next_month_len = calendar.monthrange(_year, _month)[1]
    next_month = d
    if d.day > next_month_len:
        next_month = next_month.replace(day=next_month_len)
    next_month = next_month.replace(year=_year, month=_month)
    return next_month


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


class ItemColor(BoxLayout):
    text = StringProperty()
    color = ListProperty()


def show_canvas_stress(wid):
    with wid.canvas:
        for x in range(10):
            Color(r(), 1, 1, mode='hsv')
            Rectangle(pos=(r() * wid.width + wid.x, r() * wid.height + wid.y), size=(20, 20))


def draw_graph(wid, start_date, loan, months, interest, payment_type):
    with wid.canvas:
        Color(.2, .2, .2, 1)
        Line(rectangle=(wid.x, wid.y, wid.width, wid.height), width=1)
    graph_height = wid.height
    delta_width = wid.width / months

    percent = interest / 100 / 12
    monthly_payment = loan * (percent + percent / ((1 + percent) ** months - 1))

    debt_end_month = loan
    for i in range(0, months):
        repayment_of_interest = debt_end_month * percent
        repayment_of_loan_body = monthly_payment - repayment_of_interest
        debt_end_month = debt_end_month - repayment_of_loan_body
        delta_height_interest = int(repayment_of_interest * graph_height / monthly_payment)
        delta_height_loan = int(repayment_of_loan_body * graph_height / monthly_payment)
        # print("####: ", delta_height_loan, delta_height_loan)
        # print(monthly_payment, repayment_of_interest, repayment_of_loan_body, debt_end_month)
        with wid.canvas:
            Color(1, 0, 0, 1)
            Rectangle(pos=(wid.x + int(i * delta_width), wid.y), size=(int(delta_width), delta_height_loan))
            Color(0, 0, 1, 1)
            Rectangle(pos=(wid.x + int(i * delta_width), wid.y + delta_height_loan),
                      size=(int(delta_width), delta_height_interest))


def draw_chart(wid, total_amount_of_payments, loan):
    interest_chart = ((total_amount_of_payments - loan) * 360) / total_amount_of_payments
    circle_width = wid.width
    center_x = 0
    center_y = wid.height // 2 - circle_width // 2
    if (wid.width > wid.height):
        circle_width = wid.height
        center_x = wid.width // 2 - circle_width // 2
        center_y = 0
    # print(wid.x, wid.y)
    with wid.canvas:
        Color(0, 0, 1, 1)
        Ellipse(pos=(wid.x + center_x, wid.y + center_y), size=(circle_width, circle_width),
                angle_start=360 - int(interest_chart), angle_end=360)
        Color(1, 0, 0, 1)
        Ellipse(pos=(wid.x + center_x, wid.y + center_y), size=(circle_width, circle_width), angle_start=0,
                angle_end=360 - int(interest_chart))


def share(title, text):
    from kivy import platform

    print(platform)

class P2PLoansConstructorApp(MDApp):
    dialog = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.theme_cls.primary_palette = "Brown"
        self.theme_cls.primary_hue = "A100"
        self.data_for_calc_is_changed = True

        self.screen = Builder.load_string(KV)
        # https://kivymd.readthedocs.io/en/latest/components/menu/?highlight=MDDropItem#center-position
        # menu_items = [{"icon": "git", "text": f"Item (i)"} for i in range(5)]
        menu_items = [{"icon": "format-text-rotation-angle-up", "text": "annuity"},
                      {"icon": "format-text-rotation-angle-down", "text": "differentiated"}]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.payment_type,
            items=menu_items,
            position="auto",
            width_mult=4,
        )
        self.menu.bind(on_release=self.set_item)

        self.date_dialog = MDDatePicker(
            callback=self.get_date,
            background_color=(0.1, 0.1, 0.1, 1.0),
        )

    def set_item(self, instance_menu, instance_menu_item):
        def set_item(interval):
            self.screen.ids.payment_type.text = instance_menu_item.text
            instance_menu.dismiss()

        Clock.schedule_once(set_item, 0.5)

    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''
        print(date)
        self.screen.ids.start_date.text = date.strftime("%d-%m-%Y")  # str(date)

    def build(self):
        self.theme_cls.theme_style = "Light"  # "Dark" # "Light"
        # return Builder.load_string(KV)
        return self.screen

    def on_start(self):
        self.screen.ids.start_date.text = datetime.date.today().strftime("%d-%m-%Y")
        self.screen.ids.loan.text = "1000"
        self.screen.ids.months.text = "12"
        self.screen.ids.interest.text = "12"
        self.screen.ids.payment_type.text = "annuity"

        loan = self.screen.ids.loan.text
        months = self.screen.ids.months.text
        interest = self.screen.ids.interest.text
        loan = float(loan)
        months = int(months)
        interest = float(interest)
        percent = interest / 100 / 12
        monthly_payment = loan * (percent + percent / ((1 + percent) ** months - 1))
        total_amount_of_payments = monthly_payment * months
        overpayment_loan = total_amount_of_payments - loan
        effective_interest_rate = ((total_amount_of_payments / loan - 1) / (months / 12)) * 100

        self.screen.ids.payment_label.text = str(round(monthly_payment, 2))
        self.screen.ids.total_amount_of_payments_label.text = str(round(total_amount_of_payments, 2))
        self.screen.ids.overpayment_loan_label.text = str(round(overpayment_loan, 2))
        self.screen.ids.effective_interest_rate_label.text = str(round(effective_interest_rate, 2))

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
            "chart-areaspline": "Portfolio composition",
            "chart-pie": "Payments",
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
            self, *args):
        '''Called when switching tabs.
                :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
                :param instance_tab: <__main__.Tab object>;
                :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
                :param tab_text: text or name icon of tab;
                '''

        #print("tab clicked! " + tab_text)
        if self.data_for_calc_is_changed:
            self.calc_table(self, args)
            self.data_for_calc_is_changed = False
        pass

    def on_star_click(self):
        pass

    def calc_table(self, *args):
        print("button1 pressed")
        start_date = self.screen.ids.loan.text
        loan = self.screen.ids.loan.text
        months = self.screen.ids.months.text
        interest = self.screen.ids.interest.text
        payment_type = self.screen.ids.payment_type.text
        print(start_date + " " + loan + " " + months + " " + payment_type)
        start_date = datetime.datetime.strptime(self.screen.ids.start_date.text, "%d-%m-%Y").date()
        loan = float(loan)
        months = int(months)
        interest = float(interest)

        row_data_for_tab = []
        percent = interest / 100 / 12
        monthly_payment = loan * (percent + percent / ((1 + percent) ** months - 1))

        debt_end_month = loan
        for i in range(0, months):
            repayment_of_interest = debt_end_month * percent
            repayment_of_loan_body = monthly_payment - repayment_of_interest
            debt_end_month = debt_end_month - repayment_of_loan_body
            print(monthly_payment, repayment_of_interest, repayment_of_loan_body, debt_end_month)
            row_data_for_tab.append(
                [i + 1, start_date.strftime("%d-%m-%Y"), round(monthly_payment, 2), round(repayment_of_interest, 2),
                 round(repayment_of_loan_body, 2), round(debt_end_month, 2)])
        total_amount_of_payments = monthly_payment * months
        overpayment_loan = total_amount_of_payments - loan
        effective_interest_rate = ((total_amount_of_payments / loan - 1) / (months / 12))
        #print(total_amount_of_payments, overpayment_loan, effective_interest_rate)

        start_date = next_month_date(start_date)

        # show_canvas_stress(self.screen.ids.graph)
        show_canvas_stress(self.screen.ids.chart)

        self.screen.ids.graph.canvas.clear()
        draw_graph(self.screen.ids.graph, start_date, loan, months, interest, payment_type)

        self.screen.ids.chart.canvas.clear()
        draw_chart(self.screen.ids.chart, total_amount_of_payments, loan)

        data_tables = MDDataTable(
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("B,,-", dp(10)),
                ("Date", dp(20)),
                ("Payment", dp(20)),
                ("Interest", dp(20)),
                ("Principal", dp(20)),
                ("Debt", dp(20)),
            ],
            row_data=row_data_for_tab,
        )
        self.screen.ids.calc_data_table.clear_widgets()
        self.screen.ids.calc_data_table.add_widget(data_tables)

        pass

    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Share it:",
                type="custom",
                content_cls=ContentDialogSend(),
                buttons=[
                    MDFlatButton(
                        text="Cancel", text_color=self.theme_cls.primary_color
                    ),
                    MDFlatButton(
                        text="SEND", text_color=self.theme_cls.primary_color
                    ),
                ],
            )
        self.dialog.open()

    def share_it(self, *args):
        share("title_share", "this content to share!")

P2PLoansConstructorApp().run()

