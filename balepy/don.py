__title__: str = 'balepy'
__version__: str = '1.3.5'
__license__: str = 'MIT license'
__author__: str = 'Mamad Mehrabi Rad'
__url__: str = 'https://github.com/OnlyRad/balepy'
__author_email__: str = 'mohammadmehrabi175@gmail.com'
__description__: str = 'Optimal and practical module for building API bots in bale messengers'

def welcome(text, time: float = 0.035):
    from time import sleep
    try:
        from rich import print as Print
        Print(text)
    except ModuleNotFoundError:
        for char in text:
            print(char, end='', flush=True)
            sleep(float(time))
    print()
welcome(f"{__title__} -> {__version__}\nGithub: {__url__}")