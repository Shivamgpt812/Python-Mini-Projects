import pywhatkit as pw

txt= """Python is a high-level programming language known for its simplicity and readability. It's widely used for various purposes such as web development, data analysis, artificial intelligence, scientific computing, and more """

pw.text_to_handwriting(txt,"demo1.png",[0,0,138])
print("END")