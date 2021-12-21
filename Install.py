from os import system as S
S('apt update && apt upgrade -y')
S('apt install python -y')
S('pip install --upgrade pip')
S('pip install faker')
S('apt install requests wget')
S('python prank')