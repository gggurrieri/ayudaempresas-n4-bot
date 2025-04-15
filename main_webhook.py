
import os
import random
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes
from calificador_n4 import calificar_url_n4

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

bot = Bot(token=TELEGRAM_TOKEN)
application = Application.builder().token(TELEGRAM_TOKEN).build()

cantidad_urls_a_calificar = 10
TODAS_LAS_URLS_N4 = [
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url1",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url2",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url3",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url4",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url5",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url6",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url7",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url8",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url9",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url10",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url11",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url12",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url13",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url14",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url15",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url16",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url17",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url18",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url19",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url20",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url21",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url22",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url23",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url24",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url25",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url26",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url27",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url28",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url29",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url30",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url31",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url32",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url33",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url34",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url35",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url36",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url37",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url38",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url39",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url40",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url41",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url42",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url43",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url44",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url45",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url46",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url47",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url48",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url49",
    "https://ayudaempresas.galicia.ar/AyudajuridicaSPA/ini/n4/url50",
]

async def ejecutar_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    urls_seleccionadas = random.sample(TODAS_LAS_URLS_N4, cantidad_urls_a_calificar)
    resultado_mensaje = []

    for url in urls_seleccionadas:
        resultado = calificar_url_n4(url)
        resultado_texto = f"🔗 {url}\n" + "\n".join([f"- {k}: {v}" for k, v in resultado.items()])
        resultado_mensaje.append(resultado_texto)

    final = "\n\n".join(resultado_mensaje)
    await update.message.reply_text(f"✅ Resultado de calificación de {cantidad_urls_a_calificar} URLs:\n\n{final}")

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
        else:
            await update.message.reply_text("Usá `/activar <cantidad>`\nEj: `/activar 5`", parse_mode="Markdown")
            return

        await update.message.reply_text(f"🔄 Calificando {cantidad_urls_a_calificar} URLs N4...")
        await ejecutar_bot(update, context)

    except ValueError:
        await update.message.reply_text("⚠️ Número inválido. Usá `/activar 5`")

application.add_handler(CommandHandler("activar", activar))

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
