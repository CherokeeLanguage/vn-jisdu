
style window:
    left_padding 200
    right_padding 200
style quick_button_text:
    size 34
    #color '#000000'
style button_text:
    size 34
    color '#000000'
style label_text:
    size 34
    color '#000000'
style action_editor_button_text:
    size 20
    color '#000000'

image rabbit = "images/characters/lapin-300px.png"
image coyote = "images/characters/coyote--300px.png"
image wolf = "images/characters/wolf-2--300px.png"
image bear = "images/characters/grizzly-bear--300px.png"

image side rabbit:
    "images/portraits/p_Jisdu.png"
    xzoom -1.0
        
image side coyote:
    "images/portraits/p_Coyote.png"
    xzoom -1.0
        
image side wolf:
    "images/portraits/p_Wolf.png"
    xzoom -1.0
        
image side bear:
    "images/portraits/p_Bear.png"
    xzoom -1.0
    
image bg_scene_mountains:
    "images/landscapes/bg_main.png"
    
image bg_scene_rabbit:
    "images/landscapes/spring-thaw-2400px.png"
    alpha 1.0

image bg_scene_trees_under:
    "images/landscapes/trees-colorized-002-2400px.png"
    
image bg_scene_trees_over:
    "images/landscapes/trees-colorized-002-2400px-overlay.png"
    
image prop_tree_limb:
    "images/trees/perpaola-ramo-800px.png"
    
init python:
    renpy.music.register_channel("sfx1", "sfx", False)
    renpy.music.register_channel("sfx2", "sfx", False)
    
image white = Solid((255, 255, 255, 255))

label start:
    jump choose_language
    
label choose_language:
    scene white with fade
        
    menu:
        "ᏣᎳᎩ":
            $ renpy.change_language(None)
            define rabbit = Character('ᏥᏍᏚ',  show_two_window=False, image="rabbit")
            define coyote = Character('ᏩᏯ ᎤᏍᏗ', show_two_window=False, image="coyote")
            define wolf = Character('ᏩᎭᏯ', show_two_window=False, image="wolf")
            define bear = Character('ᏲᎾ ᎡᏆ', show_two_window=False, image="bear")
            
        "English":
            $ renpy.change_language("english")
            define rabbit = Character('Rabbit',  show_two_window=False, image="rabbit")
            define coyote = Character('Coyote', show_two_window=False, image="coyote")
            define wolf = Character('Wolf', show_two_window=False, image="wolf")
            define bear = Character('Bear', show_two_window=False, image="bear")
            
    jump scene_coyote

label scene_coyote:
    
    scene bg_scene_mountains onlayer master with fade:
        xpos -2.73
        
    "ᏌᏊ ᎢᏳᏩᎦᏘ"
                
    
    show coyote onlayer master:
        xoffset 74 yoffset 415 xzoom -1.0 alpha 0
        linear 0.5 alpha 1
    
        
    "ᎠᎪᏗ ᎡᎯ ᏩᏯ ᎤᏍᏗ ᎤᎴᏁᎢ."
    
    
    show rabbit onlayer master:
        xoffset 1115 yoffset 459 alpha 0
        linear 0.5 alpha 1
        
    "ᎤᏰᎶᎢᏍᏗ ᎤᎪᎮᎢᏃ, ᎦᎷᎦ ᏥᏍᏚ."
    
    coyote "Ꭷ! ᏥᏍᏚ! ᎦᏙᎲ ᎭᏗᏟ?"
    rabbit "ᎦᎵᏘᎠ!"
        
    show rabbit onlayer master:
        linear 0.2 xoffset -120 yoffset 459 
    
    "ᎤᎶᏎᎢ. ᏭᏕᎵᏤᎢ."
    "ᏩᏯ ᎤᏍᏗ ᎤᏬᏞᎢ."
    "ᏩᏯ ᎤᏍᏗ ᎤᏪᎵᏎᎢ,"
    coyote "ᎪᎱᏍᏗ ᎤᏲᎢ ᎤᎵᏍᏓᏁᎸᎢ. ᏯᏆᎵᏍᏓᏁᎭ ᏍᏊ!"
    "ᎾᎯᏳ ᏩᏯ ᎤᏍᏗ ᏍᏊ ᎤᎴᏅᎮᎢ ᎤᎵᏘᏍᏗ."
    
    show coyote onlayer master:
        xzoom 1.0
        linear 0.4 xoffset -259 yoffset 415 
    
    "ᎤᏪᏅᏎᎢ ᎠᎴ ᎤᏪᏅᏎᎢ."
    
    hide rabbit
    hide coyote
    
    jump scene_wolf

label scene_wolf:
    
    scene bg_scene_mountains onlayer master with fade:
        xpos -2.73 xoffset 1066

    "ᎤᎿ ᎤᏍᏗ ᎢᎪᏗ ᎨᏎᎢ."    
    show wolf:
        xoffset 30 yoffset 411 xzoom -1 alpha 0
        linear 0.5 alpha 1
        
    "ᎤᎿ ᏩᏯ ᎨᏎᎢ."        
    "ᏩᏯ ᎤᎪᎮᎢᏃ, ᎦᎷᎦ ᏩᏯ ᎤᏍᏗ."
    show coyote:
        xoffset 953 yoffset 419 alpha 0
        linear 0.5 alpha 1
        
    "ᎤᎷᏤᎢ ᏩᏯᏃ ᎤᏛᏛᎮᎢ,"
    wolf "ᎦᏙᎲ ᎭᏗᏟ?"
    coyote "ᎦᎵᏘᎠ!"
    
    show coyote:
        linear 0.2 xoffset -250 yoffset 419 
    
    "ᏩᏯ ᎤᏍᏗ ᎤᎶᏎᎢ."
    "ᏩᎭᏯ ᎤᏬᏞᎢ."
    "ᏩᎭᏯ ᎤᏪᎵᏎᎢ,"
    wolf "ᎪᎱᏍᏗ ᎤᏲᎢ ᎤᎵᏍᏓᏁᎸᎢ. ᏯᏆᎵᏍᏓᏁᎭ ᏍᏊ!"
    "ᎾᎯᏳ ᏩᏯ ᎤᎴᏅᎮᎢ ᎤᎵᏘᏍᏗ."
    
    show wolf:
        xzoom 1
        linear .4 xoffset -455 yoffset 411 
        
    "ᎤᏪᏅᏎᎢ ᎠᎴ ᎤᏪᏅᏎᎢ."
    hide coyote
    hide wolf
    
label scene_bear:
    
    scene bg_scene_mountains onlayer master with fade:
        xpos -2.73 xoffset 2*1066
    
    "ᎤᎿ ᎤᏍᏗ ᎢᎪᏗ ᎨᏎᎢ."
    
    
    show bear onlayer master:
        xoffset 34 yoffset 323 alpha 0
        linear 0.5 alpha 1
        
    
    "ᎤᎿ ᏲᎾ ᎡᏆ ᎨᏎᎢ."
    "ᏲᎾ ᎡᏆ ᎤᎪᎮᎢᏃ, ᎦᎷᎦ ᏩᏯ."
    show wolf:
        xoffset 909 yoffset 415 alpha 0.0
        linear 0.5 alpha 1.0
        
    "ᎤᎷᏤᎢ ᎠᎴ ᏲᎾ ᎡᏆ ᎤᏛᏛᎮᎢ,"
    bear "ᏃᏊ ᎦᏙᎲ ᎭᏗᏟ?"
    wolf "ᎦᎵᏘᎠ!"
    
    show wolf onlayer master:
        linear 0.25 xoffset -412 yoffset 415 
    "ᏩᏯ ᎤᎶᏎᎢ."
    "ᏲᎾ ᎡᏆ ᎤᏍᏗ ᎤᎴᏁᎢ."
    "ᏲᎾ ᎡᏆ ᎤᏪᎵᏎᎢ,"
    bear "ᎪᎱᏍᏗ ᎤᏲᎢ ᎤᎵᏍᏓᏁᎸᎢ. ᏯᏆᎵᏍᏓᏁᎭ ᏍᏊ!"
    "ᎾᎯᏳ ᏲᎾ ᎡᏆ ᎤᎴᏅᎮᎢ ᎤᎵᏘᏍᏗ."
    
    show bear onlayer master:
        xzoom -1.0 
        linear 0.25 xoffset -503 yoffset 323 
        
    "ᎤᏪᏅᏎᎢ ᎠᎴ ᎤᏪᏅᏎᎢ."
    hide wolf
    hide bear
    
label scene_all:
    
    scene bg_scene_mountains onlayer master with fade:
        xpos -2.73 xoffset 3*1066
        
    "ᎤᎿ ᎢᎪᏗ ᎨᏎᎢ."
    
    show bear onlayer master:
        xzoom -1.0 alpha 0
        xanchor -0.02 xoffset 795 yoffset 306 
        linear 0.5 alpha 1
        
    "ᎤᎷᏤᎢ."
    "ᎤᎿ ᏚᎪᎮᎢ."
    "ᏚᏃᏞᎢ."
        
    show wolf onlayer master:
        xoffset 30 yoffset 472 xzoom -1.0 
        alpha 0
        linear 0.5 alpha 1
    "ᏩᎭᏯ."
    
    show coyote onlayer master:
        xoffset 454 yoffset 354 xzoom -1.0 
        alpha 0
        linear 0.5 alpha 1
        
    "ᏩᏯ ᎤᏍᏗ."
    
    show rabbit onlayer master:
        xoffset 607 yoffset 481 xzoom -1.0 
        alpha 0
        linear 0.5 alpha 1
    "ᎠᎴ ᏥᏍᏚ."
    
    "ᏲᎾ ᎡᏆ ᏩᎭᏯ ᎤᏛᏛᎮᎢ,"
    
    show coyote:
        linear 0.5 alpha .4
    show rabbit:
        linear 0.5 alpha .4
    
    bear "ᏃᏊ, ᎦᏙᎲ ᎤᎵᏘᏒᎢ? ᎤᎿ Ꮭ ᎪᎱᏍᏗ ᏱᎨᏒᎢ ᏣᎵᏘᏍᏗ."
    wolf "ᎤᎴᏁᎢ. ᎠᎩᎪᎲᎢ ᎦᎷᎦ ᎠᎪᏘ ᎡᎯ ᏩᏯ. ᎯᎳᏴᎢ ᎤᎷᏨᎢ, ᎠᎦᏛᏅᎢ, 'ᏃᏊ ᎦᏙᎲ ᎭᏗᏟ?' ᎤᏛᏛᎲᎢ 'ᎦᎵᏘᎠ!'"
        
    show wolf:
        linear .5 alpha .4
    show coyote:
        linear 0.5 alpha 1
        
    bear "ᏂᎯᎾ? ᎦᏙᎲ ᎤᎵᏘᏎᎢ?"
    coyote "ᎤᎿ ᎤᎴᏁᎢ. ᎯᎳᏴᎢ ᏥᏍᏚ ᎤᎷᏨᎢ, ᎠᏆᏛᏛᎲᎢ, 'ᏃᏊ, ᎦᏙᎲ?', ᎤᏛᏅᎢᏃ, 'ᎦᎵᏘᎠ.'"
    
    show coyote:
        linear 0.5 alpha .4
    show rabbit:
        linear 0.5 alpha 1
    
    bear "ᏃᏊ ᏂᎯ. ᏃᏊ ᎦᏙᎲ ᎤᎵᏘᏎᎢ?"
    rabbit "ᏚᏩᏂᎦᏢ..."
    
label scene_rabbit:
    scene bg_scene_rabbit:
        zoom 0.55
    show bg_scene_trees_under onlayer master:
        subpixel True xpos None ypos None xanchor None yanchor None xoffset 620 yoffset 280 xzoom 1.0 zoom 0.2 rotate None     
    show rabbit onlayer master:
        subpixel True xpos None ypos None xanchor None yanchor None xoffset 947 yoffset 576 zoom 0.40 rotate None 
    show bg_scene_trees_over onlayer master:
        subpixel True xpos None ypos None xanchor None yanchor None xoffset 620 yoffset 280 zoom 0.2 rotate None 
    $camera_move(2785, -2666, 1138, 0, duration=0)
    with fade
        
    $camera_move(2785, 1995, 1138, 0, duration=3)
    pause(3)
    $camera_move(3495, 3026, 1620, 0, duration=2)
    pause(1.9)        
    show rabbit onlayer master:
        linear .5 subpixel True xpos None ypos None xanchor None yanchor None xoffset 920 yoffset 576 zoom 0.4 rotate None 
        
    rabbit "ᏚᏩᏂᎦᏢᎢ ᏓᎩᏍᏗᎬᎢ ..." with dissolve
    
    show prop_tree_limb:
        zoom 0.05 alpha 0
    
    play sfx1 "audio/267891__kangaroovindaloo__spooky-wind-2.ogg"
    extend " ᎤᏰᎶᎢᏍᏗ ᎤᏃᎸᏅᎢ!"
    rabbit " ᎤᏅᏥ ᎤᎶᏒᎢ."
    rabbit "ᎾᎯᏳ ᎤᏩᏂᎦᏢᎢ ᎤᎶᏒᎢ ... ᎠᎴ ᎦᏚ ᎠᏴ ᏱᎨᏒᎢ!"
    
    play sfx2 "audio/183451__corkscr3w__wood-crack-4.ogg"
    pause (1.1)
        
    show prop_tree_limb onlayer master:
        alpha 1.0
        xoffset 938 yoffset 501 zoom 0.12
        linear 0.2 xoffset 938 yoffset 620
    pause (0.2)
    
    play sound "audio/9509__petenice__whoosh.wav"
    show rabbit onlayer master:
        linear .2 subpixel True xpos None ypos None xanchor None yanchor None xoffset 778 yoffset 576 zoom 0.4 rotate None 
    
    rabbit "ᎾᎯᏳᏃ ᎠᏆᎵᏘᏒᎢ ..."
    
    stop sfx1 fadeout 2
    stop sfx2 fadeout 2
    
    jump scene_theend
    
label scene_theend:
    
    scene bg_scene_mountains onlayer master with fade:
        xpos -2.73 xoffset 3*1066
    show bear onlayer master:
        xzoom -1.0 alpha 0
        xanchor -0.02 xoffset 795 yoffset 306 
        linear 0.5 alpha 1
    show wolf onlayer master:
        xoffset 30 yoffset 472 xzoom -1.0 
        alpha 0
        linear 0.5 alpha 1
    show coyote onlayer master:
        xoffset 454 yoffset 354 xzoom -1.0 
        alpha 0
        linear 0.5 alpha 1
    show rabbit onlayer master:
        xoffset 607 yoffset 481 xzoom -1.0 
        alpha 0
        linear 0.5 alpha 1
    rabbit "ᎤᏰᎸᏗ ᎠᏆᏛᏅᎢ, 'ᎦᎵᏘᎠ'"
    "ᎾᎯᏳ ᎤᏂᏰᏘᏎᎢ."
    "ᎾᎯᏳ ᎤᎵᏍᏆᏛᎢ."
    show bear onlayer master:
        linear 1.0 alpha 0        
    show wolf onlayer master:
        linear 1.0 alpha 0        
    show coyote onlayer master:
        linear 1.0 alpha 0        
    show rabbit onlayer master:
        linear 1.0 alpha 0
    pause(1.0)
    scene black with fade
    pause(1.0)
    return
return