import requests
from django.conf import settings

def enviar_notificacao_telegram(texto):
    """
    Envia mensagem simples para o Telegram
    """
    print("🚀 ENVIANDO NOTIFICAÇÃO...")
    print(f"📝 Texto: {texto}")
    
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    
    dados = {
        'chat_id': settings.TELEGRAM_CHAT_ID,
        'text': texto
    }
    
    try:
        resposta = requests.post(url, json=dados, timeout=10)
        print(f"📱 Status: {resposta.status_code}")
        
        if resposta.status_code == 200:
            print("✅ SUCESSO! Mensagem enviada!")
            return True
        else:
            print(f"❌ ERRO: {resposta.text}")
            return False
            
    except Exception as e:
        print(f"❌ EXCEÇÃO: {e}")
        return False

def notificar_autor_criado(autor):
    """
    Notifica quando um autor for criado
    """
    print(f"🔔 AUTOR CRIADO: {autor.nome}")
    
    mensagem = f"🎉 Novo autor: {autor.nome}\nEmail: {autor.email}"
    
    return enviar_notificacao_telegram(mensagem)