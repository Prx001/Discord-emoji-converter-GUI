import PySimpleGUI as psg
import pyperclip
# Defining two themes for GUI window
psg.LOOK_AND_FEEL_TABLE["OneDark"] = {"BACKGROUND": "#282C34", #Plain dark=#3C3F41 #Too dark=#222222
"TEXT": "#8f96a5", #White=F5F5F5 #Too dark=#606671
"INPUT": "#282C34",
"TEXT_INPUT": "#F5F5F5",
"SCROLL": "#c7e78b",
"BUTTON": ("#222222", "#F5F5F5"),
"PROGRESS": ("#01826B", "#D0D0D0"),
"BORDER": 1, "SLIDER_DEPTH": 0, "PROGRESS_DEPTH": 0,
}
psg.LOOK_AND_FEEL_TABLE["Dark1"] = {"BACKGROUND": "#3C3F41", #222222 #282C34
"TEXT": "#F5F5F5", #F5F5F5
"INPUT": "#3C3F41",
"TEXT_INPUT": "#F5F5F5",
"SCROLL": "#c7e78b",
"BUTTON": ("#222222", "#F5F5F5"),
"PROGRESS": ("#01826B", "#D0D0D0"),
"BORDER": 1, "SLIDER_DEPTH": 0, "PROGRESS_DEPTH": 0,
}
# Store in-GUI-used images (Base64)
closeWidget_base64 = b'iVBORw0KGgoAAAANSUhEUgAAAC4AAAAgCAYAAABts0pHAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsIAAA7CARUoSoAAAAEqSURBVFhHY9TQMf3PMAQB0xB0M9jJow6nd8yNhvhoiBMZAqNJhciAopqy0RCnWlASadBoiLc1VTGYGmrhDC9NVTmGSX2tRIYnYWVUC/H16zcw1NXVYHU8yNHt7a0MmzZtIewiIlUwi4hJNxCpFq+yZy9eM9y5dR3seBAN4oMAzNFTpkxj2HPgODWsAptBNYeDDEN3PD8vJzikqe1okF2MtGiPg9I6KOT//v1LE0fTrFn75csXsKOZmZkZPn78SLXkgWwQ1TInzFDkNN3U1IIzw1LqG6qmcfSMiCvDUupoqmZOXKUHrRxPtaSSmZmOMyOePn+NAZRscnKyqBHYYDNoUqpQzXV4DKJaiNPDsTQtVejlgdEQp1dIw+wZDfHRECcyBEaTCpEBRTVlALKgfL7ljyqDAAAAAElFTkSuQmCC'
closeWidget2_base64 = b'iVBORw0KGgoAAAANSUhEUgAAAC4AAAAgCAIAAADi0d0QAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAACsSURBVFhH7dTBCcMwEETRdCZcgsnZpAGT0uy7OlAHAjXjBYMI6zkoOzk4MPBPSw6PaPAjpekmiYISBSUKShSUKKj/p2zbviwvd7Tm+ZlzdsfBghRztNacxhy11nV9fx7Hiz+Q05AOi9pK1/AOi53tqeEdFks5/4/rbgJRlP4u/aXcD74qTnH74DVBCtwpqQlS7DsGd2qOUoo7DsbO9oeJghIFJQpKFNRtKGk6ALcweKOL0/IEAAAAAElFTkSuQmCC'
# defining reference dictionary
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
# Complete reference dictionary using a for loop
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for ch in string:
    ch = ch.lower()
    emoji = ":regional_indicator_" + ch + ":"
    discord[ch] = emoji
discord[" "] = " "
# Creating main GUI window
psg.theme("OneDark")
layout = [  [psg.Button("", image_data=closeWidget_base64, button_color=(psg.theme_background_color(),psg.theme_background_color()), border_width=0, key="EXIT")],
            [psg.Text("Enter your text here"), psg.InputText(key="TEXT -IN-")],
            [psg.Text("Click 'Convert' to get the emoji for Discord!")],
            [psg.Button("Convert"), psg.Button("Exit")] ]
window = psg.Window("Discord emoji converter", layout, no_titlebar=True, grab_anywhere=True, element_justification="right")
# Run GUI loop
while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED or event == "Exit" or event == "EXIT":
        break
    if event == "Convert":
        # Convert process
        ready = str(values["TEXT -IN-"]).lower()
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
                # In case of error
                psg.theme("Dark1")
                layout_error0 = [  [psg.Button("", image_data=closeWidget2_base64, button_color=(psg.theme_background_color(),psg.theme_background_color()), border_width=0, key="EXIT")],
                                  [psg.Text("One of the characters you entered doesn't have Discord emoji!")],
                                  [psg.Button("OK")] ]
                window_error0 = psg.Window("Error", layout_error0, no_titlebar=True, grab_anywhere=True, element_justification="right")
                while True:
                    button_error0, values_error0 = window_error0.read()
                    if button_error0 == psg.WIN_CLOSED or button_error0 == "OK" or button_error0 == "EXIT":
                        break
                window_error0.close()
                continue
        elif len(ready) == 1:
            try:
                emoji1 = discord[ready]
            except KeyError:
                # In case of error
                psg.theme("Dark1")
                layout_error1 = [  [psg.Button("", image_data=closeWidget2_base64, button_color=(psg.theme_background_color(),psg.theme_background_color()), border_width=0, key="EXIT")],
                                  [psg.Text("The text you entered doesn't have Discord emoji!")],
                                  [psg.Button("OK")] ]
                window_error1 = psg.Window("Error", layout_error1, no_titlebar=True, grab_anywhere=True, element_justification="right")
                while True:
                    button_error1, values_error1 = window_error1.read()
                    if button_error1 == psg.WIN_CLOSED or button_error1 == "OK" or button_error1 == "EXIT":
                        break
                window_error.close()
                continue
        # Result window
        psg.theme("Dark1")
        layout1 = [  [psg.Button("", image_data=closeWidget2_base64, button_color=(psg.theme_background_color(),psg.theme_background_color()), border_width=0, key="EXIT")],
                     [psg.Text("Emoji for Discord:"), psg.InputText(emoji1)],
                     [psg.Text("Click on the 'Copy' and copy all then paste them in Discord!")],
                     [psg.Button("OK"), psg.Button("Copy")] ]
        window1 = psg.Window("Discord emoji", layout1, no_titlebar=True, grab_anywhere=True, element_justification="right")
        while True:
            event1, values1 = window1.read()
            if event1 == psg.WIN_CLOSED or event1 == "OK" or event1 == "EXIT":
                break
            if event1 == "Copy":
                # Copy the text
                pyperclip.copy(emoji1)
                # Success window
                psg.theme("OneDark")
                layout_copied = [  [psg.Button("", image_data=closeWidget_base64, button_color=(psg.theme_background_color(),psg.theme_background_color()), border_width=0, key="EXIT")],
                                   [psg.Text("Emoji text copied successfully!\nNow you can paste it directly into Discord!")],
                                   [psg.Button("OK")] ]
                window_copied = psg.Window("", layout_copied, no_titlebar=True, grab_anywhere=True, element_justification="right")
                while True:
                    event_copied, values_copied = window_copied.read()
                    if event_copied == psg.WIN_CLOSED or event_copied == "OK" or event_copied == "EXIT":
                        window_copied.close()
                        break
        window1.close()
        continue
window.close()