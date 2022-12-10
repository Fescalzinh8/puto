# Bot token.
BOT_TOKEN = 5732913004:AAEKg06U5vYFhmGMADLzQ1K2fMFoRw8degQ""

# Telegram API ID and Hash. This is NOT your bot token and shouldn't be changed.
API_ID = 11989670
API_HASH = "b55182231af29c5ab4d79af384ac7336"

# CHAT DE ERROS
LOG_CHAT = -1001520108802

# LOGS DE COMPRAS E ADD SALDO
ADMIN_CHAT = -1001520108802

# CHAT DE COMPRAS PARA CLIENTE
CLIENT_CHAT = -1001520108802
# Quantas atualiza��es podem ser tratadas em paralelo.
# N�o use valores altos para servidores low-end.
WORKERS = 20

# Os administradores podem acessar o painel e adicionar novos materiais ao bot.
ADMINS = [5193376857, 1853137977]

# Sudoers t�m acesso total ao servidor e podem executar comandos.
SUDOERS = [5193376857]

# All sudoers should be admins too
ADMINS.extend(SUDOERS)

GIFTERS = []
