from win10toast import ToastNotifier


def hunting(element, procura):
    toaster = ToastNotifier()

    for item in element:
        if procura.upper() in item.text.upper():
            print("Encontrei o tópico : " + (item.text.replace("\t", "")).replace("\n", ""))
            print("https://www.promobit.com.br/" + item.attrs['href'])
            toaster.show_toast("Achei!", item.text, duration=10)