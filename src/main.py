import sys

from chatbot import Chatbot
from pdf_reader import PDFReader


def main():
    chatbot = Chatbot()
    pdf_reader = PDFReader()

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            break

        if user_input.lower().startswith("upload"):
            _, pdf_path = user_input.split()
            pdf_reader.upload(pdf_path)
            print("PDF uploaded successfully.")
            continue

        response = chatbot.respond(user_input, pdf_reader.get_text())
        print("ChatGPT: ", response)

if __name__ == "__main__":
    main()
