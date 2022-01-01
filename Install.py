from os import system as S
S('apt update && apt upgrade -y')
S('apt install wget python -y')
S('pip install --upgrade pip')
S('pip install faker')
S('pip install requests')
S('python prank')
