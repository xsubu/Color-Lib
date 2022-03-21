# color functionality 
# written using Python 3

# The MIT License (MIT)
#
# Copyright (c) Lumos AI LLC
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import colorsys
import numpy as np

# convert list to tuple
def convert(list):
    return tuple(list)


def rgb2hex(val):
    """
    Takes tuple and converts to hex value.
    """
    conversion = '#%02x%02x%02x' % val
    return conversion


def hex2rgb(val):
    """
    Takes hex string and converts to rgb tuple.
    """
    hexNum = val.strip('#')
    hexLen = len(hexNum)
    conversion = tuple(int(hexNum[i:i+hexLen//3], 16) for i in range(0, hexLen, hexLen//3))
    return conversion

def complimentary(hexval):
    """
    Takes hex value converts to rgb tuple and produces complimentary color.
    """
    val = hex2rgb(hexval)
    #value has to be 0 < x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #get hue changes at 150 and 210 degrees
    deg_180_hue = h + (180.0 / 360.0)
    color_180_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_180_hue, l, s)))
    return color_180_rgb

# split complementary color
# A split-complementary color scheme is a three-color combination that consists of a base color and two colors that are 150  degrees and 210 degrees apart from the base color respectively

def splitComplimentary(hexval):
    """
    Takes hex value converts to rgb tuple and produces list of split complimentary colors.
    """
    val = hex2rgb(hexval)
    #value has to be 0 x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #get hue changes at 150 and 210 degrees
    deg_150_hue = h + (150.0 / 360.0)
    deg_210_hue = h + (210.0 / 360.0)
    #convert to rgb
    color_150_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_150_hue, l, s)))
    color_210_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_210_hue, l, s)))
    return [color_150_rgb, color_210_rgb]


# Analogous Color
# Analogous color schemes are created by pairing one main color with the two colors directly next to it on the color wheel. We can specify the angle between the main color and the other two colors

def analogous(hexval, d):
    """
    Takes hex value and angle (out of 100) converts to rgb tuple and produces list of analogous colors)
    """
    val = hex2rgb(hexval)
    analogous_list = []
    #set color wheel angle
    d = d /360.0
    #value has to be 0 <span id="mce_SELREST_start" style="overflow:hidden;line-height:0;"></span>&lt; x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #rotate hue by d
    h = [(h+d) % 1 for d in (-d, d)]
    for nh in h:
        new_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(nh, l, s)))
        analogous_list.append(new_rgb)
    return analogous_list

# Triadic Color
# Triadic colors are a combination of three colors that consists of a main color and two colors that are 120 degrees and 240 degrees apart from the main color respectively
def triadic(hexval):
    """
    Takes hex value converts to rgb tuple and produces list of triadic colors.
    """
    val = hex2rgb(hexval)
    #value has to be 0 < x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #get hue changes at 120 and 240 degrees
    deg_120_hue = h + (120.0 / 360.0)
    deg_240_hue = h + (240.0 / 360.0)
    #convert to rgb
    color_120_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_120_hue, l, s)))
    color_240_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_240_hue, l, s)))
    return [color_120_rgb, color_240_rgb]

# Tetradic Color
# Tetradic colors are four-color combination that consists of a main color and three colors that are 90 degrees, 180 degrees, and 270 degrees apart from the main color respectively
def tetradic(hexval):
    """
    Takes hex value converts to rgb tuple and produces list of tetradic colors.
    """
    val = hex2rgb(hexval)
    #value has to be 0 <span id="mce_SELREST_start" style="overflow:hidden;line-height:0;"></span>&lt; x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #get hue changes at 120 and 240 degrees
    deg_60_hue = h + (60.0 / 360.0)
    deg_180_hue = h + (180.0 / 360.0)
    deg_240_hue = h + (240.0 / 360.0)
    #convert to rgb
    color_60_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_60_hue, l, s)))
    color_180_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_180_hue, l, s)))
    color_240_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_240_hue, l, s)))
    return [color_60_rgb, color_180_rgb, color_240_rgb]


# identification of color names
import re
re_color = re.compile('#([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})')
from math import sqrt

def color_to_rgb(color):
    return tuple(int(x, 16) / 255.0 for x in re_color.match(color).groups())

def similarity(color1, color2):
    """Computes the pearson correlation coefficient for two colors. The result
    will be between 1.0 (very similar) and -1.0 (no similarity)."""
    c1 = color_to_rgb(color1)
    c2 = color_to_rgb(color2)

    s1 = sum(c1)
    s2 = sum(c2)
    sp1 = sum(map(lambda c: pow(c, 2), c1))
    sp2 = sum(map(lambda c: pow(c, 2), c2))
    sp = sum(map(lambda x: x[0] * x[1], zip(c1, c2)))

    try:
            computed = (sp - (s1 * s2 / 3.0)) / sqrt((sp1 - pow(s1, 2) / 3.0) * (sp2 - pow(s2, 2) / 3.0))
    except:
            computed = 0
    
    return computed


color_names = {'#b0bf1a': 'acid green', '#c9ffe5': 'aero blue', '#b284be': 'african violet', '#edeae0': 'alabaster', '#f0f8ff': 'alice blue', '#c46210': 'alloy orange', '#efdecd': 'almond', '#e52b50': 'amaranth', '#f19cbb': 'amaranth pink', '#ab274f': 'amaranth purple', '#d3212d': 'amaranth red', '#3b7a57': 'amazon', '#ffbf00': 'amber', '#9966cc': 'amethyst', '#a4c639': 'android green', '#cd9575': 'antique brass', '#665d1e': 'antique bronze', '#915c83': 'antique fuchsia', '#841b2d': 'antique ruby', '#faebd7': 'antique white', '#8db600': 'apple green', '#fbceb1': 'apricot', '#7fffd4': 'aquamarine', '#d0ff14': 'arctic lime', '#4b5320': 'army green', '#8f9779': 'artichoke', '#b2beb5': 'ash gray', '#87a96b': 'asparagus', '#ff9966': 'atomic tangerine', '#a52a2a': 'auburn', '#fdee00': 'aureolin', '#007fff': 'azure', '#89cff0': 'baby blue', '#a1caf1': 'baby blue eyes', '#fefefa': 'baby powder', '#fae7b5': 'banana mania', '#da1884': 'barbie pink', '#7c0a02': 'barn red', '#9f8170': 'beaver', '#f5f5dc': 'beige', '#ffe4c4': 'bisque', '#3d2b1f': 'bistre', '#cae00d': 'bitter lemon', '#fe6f5e': 'bittersweet', '#000000': 'black', '#3d0c02': 'black bean', '#1b1811': 'black chocolate', '#3b2f2f': 'black coffee', '#54626f': 'black coral', '#3b3c36': 'black olive', '#bfafb2': 'black shadows', '#ffebcd': 'blanched almond', '#318ce7': 'bleu de france', '#ace5ee': 'blizzard blue', '#faf0be': 'blond', '#660000': 'blood red', '#0000ff': 'blue', '#a2a2d0': 'blue bell', '#5dadec': 'blue jeans', '#126180': 'blue sapphire', '#5072a7': 'blue yonder', '#0d98ba': 'blue-green', '#8a2be2': 'blue-violet', '#3c69e7': 'bluetiful', '#de5d83': 'blush', '#79443b': 'bole', '#e3dac9': 'bone', '#006a4e': 'bottle green', '#87413f': 'brandy', '#cb4154': 'brick red', '#66ff00': 'bright green', '#d891ef': 'bright lilac', '#ff55a3': 'brilliant rose', '#fb607f': 'brink pink', '#004225': 'british racing green', '#cd7f32': 'bronze', '#88540b': 'brown', '#af6e4d': 'brown sugar', '#7bb661': 'bud green', '#f0dc82': 'buff', '#deb887': 'burlywood', '#a17a74': 'burnished brown', '#cc5500': 'burnt orange', '#e97451': 'burnt sienna', '#8a3324': 'burnt umber', '#bd33a4': 'byzantine', '#536872': 'cadet', '#5f9ea0': 'cadet blue', '#91a3b0': 'cadet grey', '#006b3c': 'cadmium green', '#ed872d': 'cadmium orange', '#e30022': 'cadmium red', '#fff600': 'cadmium yellow', '#a3c1ad': 'cambridge blue', '#efbbcc': 'cameo pink', '#ffff99': 'canary', '#ff0800': 'candy apple red', '#592720': 'caput mortuum', '#c41e3a': 'cardinal', '#00cc99': 'caribbean green', '#960018': 'carmine', '#ffa6c9': 'carnation pink', '#b31b1b': 'carnelian', '#56a0d3': 'carolina blue', '#ed9121': 'carrot orange', '#00563f': 'castleton green', '#c95a49': 'cedar chest', '#ace1af': 'celadon', '#2f847c': 'celadon green', '#246bce': 'celtic blue', '#de3163': 'cerise', '#007ba7': 'cerulean', '#2a52be': 'cerulean blue', '#6d9bc3': 'cerulean frost', '#f7e7ce': 'champagne', '#f1ddcf': 'champagne pink', '#36454f': 'charcoal', '#232b2b': 'charleston green', '#e68fac': 'charm pink', '#ffb7c5': 'cherry blossom pink', '#954535': 'chestnut', '#a8516e': 'china rose', '#aa381e': 'chinese red', '#856088': 'chinese violet', '#ffb200': 'chinese yellow', '#ffa700': 'chrome yellow', '#98817b': 'cinereous', '#cd607e': 'cinnamon satin', '#9fa91f': 'citron', '#7f1734': 'claret', '#0047ab': 'cobalt blue', '#d2691e': 'cocoa brown', '#b9d9eb': 'columbia blue', '#8c92ac': 'cool grey', '#b87333': 'copper', '#ad6f69': 'copper penny', '#cb6d51': 'copper red', '#996666': 'copper rose', '#ff3800': 'coquelicot', '#ff7f50': 'coral', '#893f45': 'cordovan', '#6495ed': 'cornflower blue', '#fff8dc': 'cornsilk', '#2e2d88': 'cosmic cobalt', '#fff8e7': 'cosmic latte', '#ffbcd9': 'cotton candy', '#81613c': 'coyote brown', '#fffdd0': 'cream', '#dc143c': 'crimson', '#f5f5f5': 'cultured', '#00b7eb': 'cyan (process)', '#58427c': 'cyber grape', '#f56fa1': 'cyclamen', '#654321': 'dark brown', '#5d3954': 'dark byzantium', '#26428b': 'dark cornflower blue', '#008b8b': 'dark cyan', '#b8860b': 'dark goldenrod', '#013220': 'dark green', '#1a2421': 'dark jungle green', '#bdb76b': 'dark khaki', '#534b4f': 'dark liver', '#8b008b': 'dark magenta', '#4a5d23': 'dark moss green', '#556b2f': 'dark olive green', '#ff8c00': 'dark orange', '#9932cc': 'dark orchid', '#03c03c': 'dark pastel green', '#301934': 'dark purple', '#8b0000': 'dark red', '#e9967a': 'dark salmon', '#8fbc8f': 'dark sea green', '#3c1414': 'dark sienna', '#8cbed6': 'dark sky blue', '#483d8b': 'dark slate blue', '#2f4f4f': 'dark slate gray', '#177245': 'dark spring green', '#00ced1': 'dark turquoise', '#9400d3': 'dark violet', '#00703c': 'dartmouth green', '#da3287': 'deep cerise', '#b94e48': 'deep chestnut', '#004b49': 'deep jungle green', '#ff1493': 'deep pink', '#ff9933': 'deep saffron', '#00bfff': 'deep sky blue', '#4a646c': 'deep space sparkle', '#7e5e60': 'deep taupe', '#2243b6': 'denim blue', '#edc9af': 'desert sand', '#696969': 'dim gray', '#1e90ff': 'dodger blue', '#d71868': 'dogwood rose', '#00009c': 'duke blue', '#efdfbb': 'dutch white', '#e1a95f': 'earth yellow', '#555d50': 'ebony', '#1b1b1b': 'eerie black', '#614051': 'eggplant', '#f0ead6': 'eggshell', '#1034a6': 'egyptian blue', '#7df9ff': 'electric blue', '#6f00ff': 'electric indigo', '#ccff00': 'electric lime', '#bf00ff': 'electric purple', '#6c3082': 'eminence', '#1b4d3e': 'english green', '#b48395': 'english lavender', '#ab4b52': 'english red', '#cc474b': 'english vermillion', '#563c5c': 'english violet', '#00ff40': 'erin', '#96c8a2': 'eton blue', '#801818': 'falu red', '#b53389': 'fandango', '#de5285': 'fandango pink', '#e5aa70': 'fawn', '#4d5d53': 'feldgrau', '#4f7942': 'fern green', '#6c541e': 'field drab', '#ff5470': 'fiery rose', '#ce2029': 'fire engine red', '#e95c4b': 'fire opal', '#b22222': 'firebrick', '#e25822': 'flame', '#eedc82': 'flax', '#0063dc': 'flickr blue', '#fb0081': 'flickr pink', '#a2006d': 'flirt', '#fffaf0': 'floral white', '#15f4ee': 'fluorescent blue', '#856d4d': 'french bistre', '#0072bb': 'french blue', '#fd3f92': 'french fuchsia', '#9efd38': 'french lime', '#d473d4': 'french mauve', '#fd6c9e': 'french pink', '#c72c48': 'french raspberry', '#f64a8a': 'french rose', '#77b5fe': 'french sky blue', '#8806ce': 'french violet', '#cc397b': 'fuchsia purple', '#c74375': 'fuchsia rose', '#e48400': 'fulvous', '#dcdcdc': 'gainsboro', '#e49b0f': 'gamboge', '#007f66': 'generic viridian', '#f8f8ff': 'ghost white', '#6082b6': 'glaucous', '#ab92b3': 'glossy grape', '#a57c00': 'gold', '#85754e': 'gold fusion', '#996515': 'golden brown', '#fcc200': 'golden poppy', '#ffdf00': 'golden yellow', '#daa520': 'goldenrod', '#676767': 'granite gray', '#a7f432': 'green lizard', '#6eaea1': 'green sheen', '#1164b4': 'green-blue', '#009966': 'green-cyan', '#adff2f': 'green-yellow', '#a99a86': 'grullo', '#2a3439': 'gunmetal', '#e9d66b': 'hansa yellow', '#3fff00': 'harlequin', '#da9100': 'harvest gold', '#ff7a00': 'heat wave', '#df73ff': 'heliotrope', '#f0fff0': 'honeydew', '#006db0': 'honolulu blue', '#ff1dce': 'hot magenta', '#ff69b4': 'hot pink', '#355e3b': 'hunter green', '#138808': 'india green', '#cd5c5c': 'indian red', '#e3a857': 'indian yellow', '#4b0082': 'indigo', '#00416a': 'indigo dye', '#5a4fcf': 'iris', '#f4f0ec': 'isabelline', '#b2ffff': 'italian sky blue', '#fffff0': 'ivory', '#00a86b': 'jade', '#a50b5e': 'jazzberry jam', '#f4ca16': 'jonquil', '#bdda57': 'june bud', '#29ab87': 'jungle green', '#4cbb17': 'kelly green', '#3ab09e': 'keppel', '#e8f48c': 'key lime', '#e79fc4': 'kobi', '#354230': 'kombu green', '#512888': 'ksu purple', '#d6cadd': 'languid lavender', '#26619c': 'lapis lazuli', '#a9ba9d': 'laurel green', '#cf1020': 'lava', '#fff0f5': 'lavender blush', '#c4c3d0': 'lavender gray', '#7cfc00': 'lawn green', '#fffacd': 'lemon chiffon', '#cca01d': 'lemon curry', '#fdff00': 'lemon glacier', '#f6eabe': 'lemon meringue', '#fff44f': 'lemon yellow', '#545aa7': 'liberty', '#add8e6': 'light blue', '#f08080': 'light coral', '#93ccea': 'light cornflower blue', '#e0ffff': 'light cyan', '#c8ad7f': 'light french beige', '#fafad2': 'light goldenrod yellow', '#b0b0b0': 'light gray', '#d3d3d3': 'light gray', '#90ee90': 'light green', '#fed8b1': 'light orange', '#c5cbe1': 'light periwinkle', '#ffb6c1': 'light pink', '#ffa07a': 'light salmon', '#20b2aa': 'light sea green', '#87cefa': 'light sky blue', '#778899': 'light slate gray', '#b0c4de': 'light steel blue', '#ffffe0': 'light yellow', '#c8a2c8': 'lilac', '#32cd32': 'lime green', '#195905': 'lincoln green', '#faf0e6': 'linen', '#6ca0dc': 'little boy blue', '#674c47': 'liver', '#987456': 'liver chestnut', '#6699cc': 'livid', '#ffbd88': 'macaroni and cheese', '#cc3336': 'madder lake', '#ff00ff': 'magenta', '#9f4576': 'magenta haze', '#aaf0d1': 'magic mint', '#f8f4ff': 'magnolia', '#c04000': 'mahogany', '#fbec5d': 'maize', '#6050dc': 'majorelle blue', '#0bda51': 'malachite', '#979aaa': 'manatee', '#f37a48': 'mandarin', '#fdbe02': 'mango', '#ff8243': 'mango tango', '#74c365': 'mantis', '#880085': 'mardi gras', '#eaa221': 'marigold', '#e0b0ff': 'mauve', '#ef98aa': 'mauvelous', '#47abcc': 'maximum blue', '#30bfbf': 'maximum blue green', '#acace6': 'maximum blue purple', '#5e8c31': 'maximum green', '#d9e650': 'maximum green yellow', '#733380': 'maximum purple', '#d92121': 'maximum red', '#a63a79': 'maximum red purple', '#fafa37': 'maximum yellow', '#f2ba49': 'maximum yellow red', '#73c2fb': 'maya blue', '#66ddaa': 'medium aquamarine', '#0000cd': 'medium blue', '#e2062c': 'medium candy apple red', '#af4035': 'medium carmine', '#ba55d3': 'medium orchid', '#9370db': 'medium purple', '#3cb371': 'medium sea green', '#7b68ee': 'medium slate blue', '#00fa9a': 'medium spring green', '#48d1cc': 'medium turquoise', '#f8b878': 'mellow apricot', '#f8de7e': 'mellow yellow', '#febaad': 'melon', '#d3af37': 'metallic gold', '#0a7e8c': 'metallic seaweed', '#9c7c38': 'metallic sunburst', '#e4007c': 'mexican pink', '#7ed4e6': 'middle blue', '#8dd9cc': 'middle blue green', '#8b72be': 'middle blue purple', '#4d8c57': 'middle green', '#acbf60': 'middle green yellow', '#8b8680': 'middle grey', '#d982b5': 'middle purple', '#e58e73': 'middle red', '#a55353': 'middle red purple', '#ffeb00': 'middle yellow', '#ecb176': 'middle yellow red', '#702670': 'midnight', '#191970': 'midnight blue', '#ffc40c': 'mikado yellow', '#ffdae9': 'mimi pink', '#e3f988': 'mindaro', '#f5e050': 'minion yellow', '#3eb489': 'mint', '#f5fffa': 'mint cream', '#98ff98': 'mint green', '#bbb477': 'misty moss', '#ffe4e1': 'misty rose', '#8da399': 'morning blue', '#30ba8f': 'mountain meadow', '#997a8d': 'mountbatten pink', '#18453b': 'msu green', '#c54b8c': 'mulberry', '#ffdb58': 'mustard', '#317873': 'myrtle green', '#d65282': 'mystic', '#ad4379': 'mystic maroon', '#f6adc6': 'nadeshiko pink', '#ffdead': 'navajo white', '#000080': 'navy blue', '#4666ff': 'neon blue', '#39ff14': 'neon green', '#d7837f': 'new york pink', '#727472': 'nickel', '#4f42b5': 'ocean blue', '#48bf91': 'ocean green', '#cc7722': 'ochre', '#43302e': 'old burgundy', '#cfb53b': 'old gold', '#fdf5e6': 'old lace', '#796878': 'old lavender', '#c08081': 'old rose', '#848482': 'old silver', '#808000': 'olive', '#b5b35c': 'olive green', '#9ab973': 'olivine', '#353839': 'onyx', '#a8c3bc': 'opal', '#b784a7': 'opera mauve', '#ff7f00': 'orange', '#ff9f00': 'orange peel', '#f5bd1f': 'orange-yellow', '#da70d6': 'orchid', '#f2bdcd': 'orchid pink', '#841617': 'ou crimson red', '#2d383a': 'outer space (crayola)', '#ff6e4a': 'outrageous orange', '#800020': 'oxblood', '#002147': 'oxford blue', '#1ca9c9': 'pacific blue', '#006600': 'pakistan green', '#682860': 'palatinate purple', '#bcd4e6': 'pale aqua', '#9bc4e2': 'pale cerulean', '#fadadd': 'pale pink', '#78184a': 'pansy purple', '#ffefd5': 'papaya whip', '#e63e62': 'paradise pink', '#50c878': 'paris green', '#dea5a4': 'pastel pink', '#536878': "payne's grey", '#ffe5b4': 'peach', '#ffdab9': 'peach puff', '#d1e231': 'pear', '#b768a2': 'pearly purple', '#ccccff': 'periwinkle', '#1c39bb': 'persian blue', '#00a693': 'persian green', '#32127a': 'persian indigo', '#d99058': 'persian orange', '#f77fbe': 'persian pink', '#cc3333': 'persian red', '#fe28a2': 'persian rose', '#ec5800': 'persimmon', '#8ba8b7': 'pewter blue', '#000f89': 'phthalo blue', '#123524': 'phthalo green', '#2e2787': 'picotee blue', '#c30b4e': 'pictorial carmine', '#fddde6': 'piggy pink', '#01796f': 'pine green', '#2a2f23': 'pine tree', '#ffc0cb': 'pink', '#fc74fd': 'pink flamingo', '#ffddf4': 'pink lace', '#d8b2d1': 'pink lavender', '#f78fa7': 'pink sherbet', '#93c572': 'pistachio', '#e5e4e2': 'platinum', '#8e4585': 'plum', '#5946b2': 'plump purple', '#5da493': 'polished pine', '#86608e': 'pomp and power', '#be4f62': 'popstar', '#ff5a36': 'portland orange', '#b0e0e6': 'powder blue', '#f58025': 'princeton orange', '#701c1c': 'prune', '#003153': 'prussian blue', '#df00ff': 'psychedelic purple', '#cc8899': 'puce', '#ff7518': 'pumpkin', '#6a0dad': 'purple', '#9678b6': 'purple mountain majesty', '#4e5180': 'purple navy', '#fe4eda': 'purple pizzazz', '#9c51b6': 'purple plum', '#9a4eae': 'purpureus', '#436b95': 'queen blue', '#e8ccd7': 'queen pink', '#a6a6a6': 'quick silver', '#8e3a59': 'quinacridone magenta', '#ff355e': 'radical red', '#242124': 'raisin black', '#e30b5d': 'raspberry', '#915f6d': 'raspberry glace', '#b3446c': 'raspberry rose', '#d68a59': 'raw sienna', '#826644': 'raw umber', '#ff33cc': 'razzle dazzle rose', '#e3256b': 'razzmatazz', '#8d4e85': 'razzmic berry', '#663399': 'rebecca purple', '#ff0000': 'red', '#fd3a4a': 'red salsa', '#ff5349': 'red-orange', '#e40078': 'red-purple', '#c71585': 'red-violet', '#a45a52': 'redwood', '#002387': 'resolution blue', '#777696': 'rhythm', '#004040': 'rich black', '#444c38': 'rifle green', '#00cccc': 'robin egg blue', '#8a7f80': 'rocket metallic', '#838996': 'roman silver', '#ff007f': 'rose', '#f9429e': 'rose bonbon', '#9e5e6f': 'rose dust', '#674846': 'rose ebony', '#e32636': 'rose madder', '#ff66cc': 'rose pink', '#aa98a9': 'rose quartz', '#c21e56': 'rose red', '#905d5d': 'rose taupe', '#ab4e52': 'rose vale', '#65000b': 'rosewood', '#d40000': 'rosso corsa', '#bc8f8f': 'rosy brown', '#7851a9': 'royal purple', '#ce4676': 'ruber', '#d10056': 'rubine red', '#e0115f': 'ruby', '#a81c07': 'rufous', '#80461b': 'russet', '#679267': 'russian green', '#32174d': 'russian violet', '#b7410e': 'rust', '#da2c43': 'rusty red', '#8b4513': 'saddle brown', '#ff7800': 'safety orange', '#eed202': 'safety yellow', '#f4c430': 'saffron', '#bcb88a': 'sage', '#fa8072': 'salmon', '#ff91a4': 'salmon pink', '#c2b280': 'sand', '#967117': 'sand dune', '#f4a460': 'sandy brown', '#507d2a': 'sap green', '#0f52ba': 'sapphire', '#cba135': 'satin sheen gold', '#ff2400': 'scarlet', '#ff91af': 'schauss pink', '#ffd800': 'school bus yellow', '#2e8b57': 'sea green', '#59260b': 'seal brown', '#fff5ee': 'seashell', '#ffba00': 'selective yellow', '#704214': 'sepia', '#8a795d': 'shadow', '#778ba5': 'shadow blue', '#009e60': 'shamrock green', '#8fd400': 'sheen green', '#d98695': 'shimmering blush', '#5fa778': 'shiny shamrock', '#fc0fc0': 'shocking pink', '#882d17': 'sienna', '#c0c0c0': 'silver', '#acacac': 'silver chalice', '#c4aead': 'silver pink', '#bfc1c2': 'silver sand', '#cb410b': 'sinopia', '#ff3855': 'sizzling red', '#ffdb00': 'sizzling sunrise', '#007474': 'skobeloff', '#87ceeb': 'sky blue', '#cf71af': 'sky magenta', '#6a5acd': 'slate blue', '#708090': 'slate gray', '#299617': 'slimy green', '#c84186': 'smitten', '#100c08': 'smoky black', '#fffafa': 'snow', '#893843': 'solid pink', '#757575': 'sonic silver', '#1d2951': 'space cadet', '#807532': 'spanish bistre', '#0070b8': 'spanish blue', '#d10047': 'spanish carmine', '#989898': 'spanish gray', '#009150': 'spanish green', '#e86100': 'spanish orange', '#f7bfbe': 'spanish pink', '#e60026': 'spanish red', '#00ffff': 'spanish sky blue', '#4c2882': 'spanish violet', '#007f5c': 'spanish viridian', '#a7fc00': 'spring bud', '#87ff2a': 'spring frost', '#00ff7f': 'spring green', '#23297a': "st. patrick's blue", '#007bb8': 'star command blue', '#4682b4': 'steel blue', '#cc33cc': 'steel pink', '#5f8a8b': 'steel teal', '#fada5e': 'stil de grain yellow', '#e4d96f': 'straw', '#914e75': 'sugar plum', '#ffcc33': 'sunglow', '#e3ab57': 'sunray', '#cf6ba9': 'super pink', '#a83731': 'sweet brown', '#d2b48c': 'tan', '#f28500': 'tangerine', '#e4717a': 'tango pink', '#fb4d46': 'tart orange', '#483c32': 'taupe', '#8b8589': 'taupe gray', '#d0f0c0': 'tea green', '#f4c2c2': 'tea rose', '#f88379': 'tea rose', '#008080': 'teal', '#367588': 'teal blue', '#cf3476': 'telemagenta', '#e2725b': 'terra cotta', '#d8bfd8': 'thistle', '#de6fa1': 'thulian pink', '#fc89ac': 'tickle me pink', '#0abab5': 'tiffany blue', '#dbd7d2': 'timberwolf', '#eee600': 'titanium yellow', '#ff6347': 'tomato', '#00755e': 'tropical rain forest', '#2d68c4': 'true blue', '#1c05b3': 'trypan blue', '#3e8ede': 'tufts blue', '#deaa88': 'tumbleweed', '#40e0d0': 'turquoise', '#00ffef': 'turquoise blue', '#a0d6b4': 'turquoise green', '#8a9a5b': 'turtle green', '#fad6a5': 'tuscan', '#6f4e37': 'tuscan brown', '#7c4848': 'tuscan red', '#a67b5b': 'tuscan tan', '#c09999': 'tuscany', '#8a496b': 'twilight lavender', '#66023c': 'tyrian purple', '#ff6fff': 'ultra pink', '#3f00ff': 'ultramarine', '#4166f5': 'ultramarine blue', '#635147': 'umber', '#ffddca': 'unbleached silk', '#5b92e5': 'united nations blue', '#ffff66': 'unmellow yellow', '#014421': 'up forest green', '#7b1113': 'up maroon', '#ae2029': 'upsdell red', '#afdbf5': 'uranian blue', '#664228': 'van dyke brown', '#f3e5ab': 'vanilla', '#f38fa9': 'vanilla ice', '#c5b358': 'vegas gold', '#c80815': 'venetian red', '#43b3ae': 'verdigris', '#e34234': 'vermilion', '#d9381e': 'vermilion', '#a020f0': 'veronica', '#8f00ff': 'violet', '#324ab2': 'violet-blue', '#f75394': 'violet-red', '#40826d': 'viridian', '#009698': 'viridian green', '#9f1d35': 'vivid burgundy', '#00ccff': 'vivid sky blue', '#ffa089': 'vivid tangerine', '#9f00ff': 'vivid violet', '#ceff00': 'volt', '#004242': 'warm black', '#f5deb3': 'wheat', '#ffffff': 'white', '#a2add0': 'wild blue yonder', '#d470a2': 'wild orchid', '#ff43a4': 'wild strawberry', '#fc6c85': 'wild watermelon', '#a75502': 'windsor tan', '#722f37': 'wine', '#673147': 'wine dregs', '#ff007c': 'winter sky', '#56887d': 'wintergreen dream', '#c9a0dc': 'wisteria', '#c19a6b': 'wood brown', '#738678': 'xanadu', '#eeed09': 'xanthic', '#0c020f': 'xiketic', '#0f4d92': 'yale blue', '#ffff00': 'yellow', '#ffae42': 'yellow orange', '#fff700': 'yellow sunshine', '#9acd32': 'yellow-green', '#0014a8': 'zaffre'}

def getColorName(color):
    # provide a hex value and get the name of the color
    sim = [(similarity(color, c), name) for c, name in color_names.items()]
    return max(sim, key=lambda x: x[0])[1]