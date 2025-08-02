from interface import create_interface

if __name__ == "__main__":
    print("🚀 Launching AI Chat Assistant")
    demo = create_interface()
    demo.launch(share=False, server_port=7862)
