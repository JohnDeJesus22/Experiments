from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder


runTouchApp(Builder.load_string('''

ActionBar:
    pos_hint: {'top': 1}
    ActionView:
        use_separator: True
        ActionPrevious:
            title: 'Action Bar'
            with_previous: False
        ActionOverflow:
        ActionButton:
            text: 'Btn 1'
            icon: 'atlas://data/images/defaulttheme/audio-volume-high'
        ActionButton:
            text: 'Btn 2'
            icon: 'data:image/jpeg;base64,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'
        ActionToggleButton:
            text: 'Read'
        ActionToggleButton:
            text: 'To be Read'
            state: 'down'
        
        ActionGroup:
            text: 'G1'
            ActionButton:
                text: 'Btn 1'
                icon: 'atlas://data/images/defaulttheme/audio-volume-high'
            ActionButton:
                text: 'Btn 2'
            ActionButton:
                text: 'Btn 3'  
'''))
