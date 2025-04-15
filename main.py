
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

# Config
TELEGRAM_TOKEN = '7641381058:AAGY2TXG9ZOLfq5Rql3ai0Ff0Jak_hf2dHY'
CHAT_ID_AUTORIZADO = '5171106537'  # reemplazar con tu chat ID

# Variable para guardar cuántas URLs se deben calificar
cantidad_urls_a_calificar = 5  # por defecto

# Lista simulada de URLs N4 (reemplazar con las reales que se extraen de la web)
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
    global cantidad_urls_a_calificar

    urls_seleccionadas = random.sample(TODAS_LAS_URLS_N4, cantidad_urls_a_calificar)

    mensaje = f"🔔 URLs N4 calificadas hoy ({cantidad_urls_a_calificar}):\n" + "\n".join(urls_seleccionadas)

    await context.bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=mensaje)

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
            await update.message.reply_text("Por favor usá `/activar <cantidad>`\nEj: `/activar 7`", parse_mode="Markdown")
            return

        await update.message.reply_text(f"✅ Bot activado. Se calificarán {cantidad_urls_a_calificar} URLs N4.")
        await ejecutar_bot(update, context)

    except ValueError:
        await update.message.reply_text("⚠️ Por favor ingresá un número válido. Ejemplo: `/activar 10`", parse_mode="Markdown")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("activar", activar))
    app.run_polling()
