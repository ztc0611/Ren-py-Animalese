############################################################################################
### Animalese/Animal Crossing style speech generation for Ren'py
############################################################################################
### Large thank you to Henry of harryishuman for the original version of this code!
### Modified for use in Ren'py by CoolerMudkip/Zach Coleman from Lemmasoft Fourms
############################################################################################

init python:

    #Needed Libraries for use. If this is being imported into your project, do not forget to copy over the pydub folder!
    import pydub
    import os, math, sys, random, string, re
    from pydub import AudioSegment
    from pydub import effects
    from pydub.playback import play

    TEMP_FILE_NAME = config.gamedir+"/audio/temp_garble.ogg"

    #List of letters/Diagraphs. This only works for english sounds by default but could be modified to include Spanish/etc sounds.
    letter_graphs = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
        "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6",
        "7", "8", "9"
    ]
    digraphs = [
        "ch", "sh", "ph", "th", "wh"
    ]

    dots = "dot"

    #Builds the sentence when given a sentence and a character's name using their speech garble.
    def build_sentence(sentence, name):

        #If the player isn't skipping and the voice volume setting isn't 0/muted, then generate the text sounds.
        if renpy.get_skipping() == None and preferences.volumes['voice'] > 0:
            sentence_wav = AudioSegment.empty()
            sentence = sentence.lower()
            sentence = replace_swear_words(sentence)
            sentence = replace_parentheses(sentence)
            sentence = replace_numbers(sentence)
            i = 0
            while (i < len(sentence)):
                char = None
                if (i < len(sentence)-1) and ((sentence[i] + sentence[i+1]) in digraphs):
                    char = sentence[i] + sentence[i+1]
                    i+=1
                elif sentence[i] in letter_graphs:
                    char = sentence[i]
                elif sentence[i] in string.punctuation:
                    char = dots
                i+=2

                if char != None:
                    new_segment = AudioSegment.from_wav(config.gamedir+"/audio/beeps/"+name+"/{}.wav".format(char))
                    sentence_wav += new_segment

            sentence_wav = change_playback_speed(sentence_wav, voice)
            sentence_wav.export(config.gamedir+"/audio/output.wav", format="wav")

    #Replaces swear words with a "dot" sound effect. Can be disabled by commenting out line 36.
    def replace_swear_words(sentence):
        swear_words = ["fuck", "shit", "piss", "crap", "bugger", "hell", "damn", "dick", "bastard", "asshole"]
        for word in swear_words:
            sentence = sentence.replace(word, "*"*len(word))
        return sentence

    #makes text in parentheses also be dot noises. This is inpsired by how text works in Animal Crossing.
    def replace_parentheses(sentence):
        while "(" in sentence or ")" in sentence:
            start = sentence.index("(")
            end = sentence.index(")")
            sentence = sentence[:start] + "*"*(end-start) + sentence[end+1:]
        return sentence

    #Replaces numbers with their spoken equivilent.
    def replace_numbers(sentence):
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        for word in numbers:
            if word == "1":
                sentence = sentence.replace(word, "one")
            if word == "2":
                sentence = sentence.replace(word, "two")
            if word == "3":
                sentence = sentence.replace(word, "three")
            if word == "4":
                sentence = sentence.replace(word, "four")
            if word == "5":
                sentence = sentence.replace(word, "five")
            if word == "6":
                sentence = sentence.replace(word, "six")
            if word == "7":
                sentence = sentence.replace(word, "seven")
            if word == "8":
                sentence = sentence.replace(word, "eight")
            if word == "9":
                sentence = sentence.replace(word, "nine")
            if word == "0":
                sentence = sentence.replace(word, "zero")
        return sentence

    #Speeds up the playback to make it sound more garbled and less decipherable.
    def change_playback_speed(sound, speed_change):
        export = sound.speedup(6.0, 200, 30)
        return export
