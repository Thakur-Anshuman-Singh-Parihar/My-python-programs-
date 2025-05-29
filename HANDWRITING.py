import pywhatkit as pwk
paragraph = """Handwriting is the act or skill of writing by hand, using a writing instrument such as a pen or pencil."""
pwk.text_to_handwriting(paragraph,"firt_notes.png",[0,0,138])
print("end")