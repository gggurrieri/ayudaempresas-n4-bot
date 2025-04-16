
import os
import random
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes
from calificador_n4 import calificar_url_n4
from detectar_urls_n4 import detectar_urls_n4

TELEGRAM_TOKEN = os.getenv("7641381058:AAGY2TXG9ZOLfq5Rql3ai0Ff0Jak_hf2dHY")
WEBHOOK_URL = os.getenv("https://ayudaempresas-n4-bot.onrender.com")

bot = Bot(token="5171106537")
application = Application.builder().token(TELEGRAM_TOKEN).build()

cantidad_urls_a_calificar = 10
ARCHIVO_URLS = "urls_n4_reales.txt"
URL_N4_POR_DEFECTO = "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/como-transfiero-entre-cuentas-propias"

def cargar_urls_n4():
    if not os.path.exists(ARCHIVO_URLS):
        return []
    with open(ARCHIVO_URLS, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

async def ejecutar_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    urls_disponibles = cargar_urls_n4()
    if not urls_disponibles:
        await update.message.reply_text("⚠️ No hay URLs N4 disponibles. Ejecutá /actualizar_urls primero.")
        return

    seleccionadas = random.sample(urls_disponibles, min(cantidad_urls_a_calificar, len(urls_disponibles)))
    resultado_mensaje = []

    for url in seleccionadas:
        resultado = calificar_url_n4(url)
        resultado_texto = f"🔗 {url}\n" + "\n".join([f"- {k}: {v}" for k, v in resultado.items()])
        resultado_mensaje.append(resultado_texto)

    final = "\n\n".join(resultado_mensaje)
    await update.message.reply_text(f"✅ Resultado de calificación de {len(seleccionadas)} URLs:\n\n{final}")

async def activar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global cantidad_urls_a_calificar
    try:
        if context.args:
            cantidad = int(context.args[0])
            if 1 <= cantidad <= 50:
                cantidad_urls_a_calificar = cantidad
            else:
                await update.message.reply_text("⚠️ Elegí un número entre 1 y 50.")
                return
        await update.message.reply_text(f"🔄 Calificando {cantidad_urls_a_calificar} URLs N4...")
        await ejecutar_bot(update, context)
    except ValueError:
        await update.message.reply_text("⚠️ Número inválido. Usá `/activar 5`")

async def actualizar_urls(update: Update, context: ContextTypes.DEFAULT_TYPE):
    base_url = context.args[0] if context.args else URL_N4_POR_DEFECTO
    await update.message.reply_text("🔍 Buscando URLs N4 desde:" + base_url)
    try:
        urls_encontradas = detectar_urls_n4(base_url)
        await update.message.reply_text(f"✅ Se guardaron {len(urls_encontradas)} URLs N4.")
    except Exception as e:
        await update.message.reply_text(f"❌ Error al detectar URLs: {e}")

application.add_handler(CommandHandler("activar", activar))
application.add_handler(CommandHandler("actualizar_urls", actualizar_urls))

flask_app = Flask(__name__)

@flask_app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    application.update_queue.put_nowait(update)
    return "ok"

@flask_app.route("/", methods=["GET"])
def home():
    return "Bot N4 webhook activo!"

async def main():
    await application.bot.set_webhook(url=WEBHOOK_URL + "/webhook")

import asyncio
asyncio.run(main())
