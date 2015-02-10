# -*- coding: utf8 -*-

def color(colorname, str):
    colors = {
        'clear': '\033[0m',
        'black': '\033[40m',
        'red': '\033[41m',
        'green': '\033[42m',
        'yellow': '\033[43m',
        'blue': '\033[44m',
        'purple': '\033[45m',
        'cyan': '\033[46m',
        'white': '\033[47m'
        }

    return colors[colorname] + str + colors['clear']
