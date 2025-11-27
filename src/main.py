from textnode import TextNode, TextType


def main():
    res = TextNode("this is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(res)


if __name__ == "__main__":
    main()
