import pyperclip
import whois
import webbrowser
import art
from colorama import init
from colorama import Fore

def create_mail(domain, lang = "en", open = False):
    domain_registrator = whois.whois(domain)["registrar"]
    if domain_registrator is None:
        domain_registrator = "Domain registrar"
    try:
        email = whois.whois(domain)["emails"][0]
    except TypeError:
        email = "type@email.here"
    if lang == "en":
        print(f"Email: {email}")
        print()
        print(subject := f"Subject: Report of Phishing site {domain}")
        print()
        print(mail := f"""Dear {domain_registrator},

I am writing to inform you of a phishing site that is registered under your domain name registry. The site in question is {domain}, which is designed to deceive users into disclosing their personal information and login credentials.

As a concerned internet user, I feel obligated to report this fraudulent activity to you and request your immediate action to resolve this issue. I believe you have the power to take prompt action and ensure that this malicious site is taken down as soon as possible.""")
        pyperclip.copy(mail)
        print(Fore.GREEN + "\nСообщение скопировано в буфер обмена!")
        if open == True:
            webbrowser.open(f"mailto:{email}?subject={subject}&body={mail}", new=2)
    elif lang == "ru":
        print(f"Email: {email}")
        print()
        print(subject := f"Тема: Сообщение о фишинговом сайте {domain}")
        print()
        print(mail := f"""Уважаемый {domain_registrator},

Я пишу вам, чтобы сообщить вам о фишинговом сайте, зарегистрированном в вашем реестре доменных имен. Речь идет о сайте {domain}, который предназначен для того, чтобы обманом заставить пользователей раскрыть свою личную информацию и учетные данные для входа.

Как обеспокоенный пользователь Интернета, я чувствую себя обязанным сообщить вам об этой мошеннической деятельности и потребовать от вас немедленных действий для решения этой проблемы. Я считаю, что у вас есть возможность принять незамедлительные меры и гарантировать, что доменное имя этого сайта будет разделегировано как можно скорее.""")
        pyperclip.copy(mail)
        print(Fore.GREEN + "\nСообщение скопировано в буфер обмена!")
        if open == True:
            webbrowser.open(f"mailto:{email}?subject={subject}&body={mail}", new=2)
    else:
        print("Некорректный язык!")

if __name__ == "__main__":
    init(autoreset=True)
    print(Fore.GREEN + art.text2art("taked0wn", font="small"))
    domain = input(Fore.RED + "Введите доменное имя фиш-сайта: ")
    lang = input(Fore.RED + "Выберите язык для письма (en/ru): ")
    open_in_mail_client = input(Fore.RED + "Нужно ли открыть окно в почтовом клиенте (y/N): ")
    if open_in_mail_client.lower() == "y":
        open_in_mail_client = True
    else:
        open_in_mail_client = False
    print()
    create_mail(domain, lang, open_in_mail_client)
