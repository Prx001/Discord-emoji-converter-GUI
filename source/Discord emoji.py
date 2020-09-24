import PySimpleGUI as psg

discord = {
    "0": ":zero:",
    "1": ":one:",
    "2": ":two:",
    "3": ":three:",
    "4": ":four:",
    "5": ":five:",
    "6": ":six:",
    "7": ":seven:",
    "8": ":eight:",
    "9": ":nine:",
    }
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for ch in string:
    ch = ch.lower()
    emoji = ":regional_indicator_" + ch + ":"
    discord[ch] = emoji
discord[" "] = " "

psg.theme('DarkAmber')
layout = [  [psg.Text('Your text'), psg.InputText()],
            [psg.Text('Click convert to get the emoji for Discord')],
            [psg.Button('Convert'), psg.Button('Exit')] ]

window = psg.Window('Discord emoji converter', layout)
while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED or event == 'Exit':
        break
    if event == "Convert":
        ready = str(values[0]).lower()
        box = []
        if len(ready) > 1:
            for ch1 in ready:
                box.append(ch1)
            try:
                for ch in box:
                    index = box.index(ch)
                    emoji = discord[ch] + " "
                    box[index] = emoji
                emoji1 = "".join(box)
            except KeyError:
                psg.theme("DarkAmber")
                layout_error = [  [psg.Text("One of the characters you entered doesn't have Discord emoji!")],
                                  [psg.Button("OK")] ]
                window_error = psg.Window("Error", layout_error)
                while True:
                    button_error, values = window_error.read()
                    if button_error == psg.WIN_CLOSED or button_error == "OK":
                        break
                window_error.close()
                continue
        elif len(ready) == 1:
            try:
                emoji1 = discord[ready]
            except KeyError:
                psg.theme("DarkAmber")
                layout_error = [  [psg.Text("The text you entered doesn't have Discord emoji!")],
                                  [psg.Button("OK")] ]
                window_error = psg.Window("Error", layout_error)
                while True:
                    button_error, values = window_error.read()
                    if button_error == psg.WIN_CLOSED or button_error == "OK":
                        break
                window_error.close()
                continue
        psg.theme("DarkAmber")
        layout1 = [  [psg.Text("Emoji for Discord:"), psg.InputText(emoji1)],
                     [psg.Text("Click on the text and copy all then paste them in Discord!")],
                     [psg.Button("OK")] ]
        window1 = psg.Window("Discord emoji", layout1)
        while True:
            key, values = window1.read()
            if key == psg.WIN_CLOSED or key == "OK":
                break
        window1.close()
        continue

window.close()