
init python:

    #Generate seperate audio channel from voice for beeps.
    renpy.music.register_channel(name='beeps', mixer='voice')

    #Character callback that generates the sound.
    def e(event, **kwargs):
        if event == "show": #When the text is shown
            build_sentence(_last_say_what, "eileen")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end": #When the text is finished displaying or you open a menu.
            renpy.sound.stop(channel="beeps")

    #Example of an alternate character callback
    def e2(event, **kwargs):
        if event == "show": #When the text is shown
            build_sentence(_last_say_what, "eileen2")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end": #When the text is finished displaying or you open a menu.
            renpy.sound.stop(channel="beeps")

define e = Character("Eileen", callback=e)
define e2 = Character("Eileen", callback=e2)


label start:

    scene bg room
    show eileen happy

    e "Hello, welcome to the Ren'py \"Animalese\" textgarble generator!"
    e "Importing these scripts and files into your VN can allow you to produce this effect!"
    "..."
    e2 "The E and A sounds of this voice is different, for an example of how to make a second set of voice samples."
    e2 "Try making your own samples for different characters in your own projects!"

    return
