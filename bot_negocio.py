from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/bot_negocio', methods=['POST'])
def responder_cliente():
    # 1. Extract the message securely from JSON
    mensaje_recibido = extract_message(request)
    
    # 2. Clean the user's message
    mensaje_cliente = clean_message(mensaje_recibido)
    
    # 3. Classify and respond based on the message
    return classify_and_respond(mensaje_cliente)

def extract_message(request):
    """Extract message from request."""
    try:
        if request.is_json:
            return request.get_json().get("message", "")
        return request.data.decode('utf-8') or ""
    except Exception as e:
        print(f"Error extracting message: {e}")
        return ""

def clean_message(mensaje):
    """Clean the user's message for processing."""
    return str(mensaje).strip().lower().replace(".", "").replace(",", "")

def classify_and_respond(mensaje_cliente):
    """Classify the client's message and generate appropriate response."""
    if re.match(r'^[1-5]$', mensaje_cliente):
        return handle_menu_option(mensaje_cliente)
    return mostrar_menu_principal()  # Defaults to welcome menu for invalid inputs

def handle_menu_option(option):
    """Handle the selected menu option."""
    respuestas = {
        "1": response_horarios_ingreso(),
        "2": response_precios_unitarios(),
        "3": response_paquetes_promocionales(),
        "4": response_como_llegar(),
        "5": response_restaurante()
    }
    return generar_respuesta(respuestas[option])

def response_horarios_ingreso():
    return (
        "📍 *Saqsayki - Tu mejor experiencia*\n"
        "🕒 *HORARIOS E INGRESO*\n\n"
        "📅 Lunes a domingo (incluyendo feriados)\n"
        "⏰ 9:30 a.m. a 5:30 p.m.\n\n"
        "🎟️ *Precios de ingreso:*\n"
        "• Adultos: S/ 7.00\n"
        "• Niños: S/ 4.00\n\n"
        "✅ *El ingreso incluye:*\n"
        "• Mano Gigante del Inca\n"
        "• Bosque Encantado de los Duendes\n"
        "• Mano de Choclo de Oro\n"
        "• Trilogía Andina\n"
        "• Diversos miradores turísticos\n\n"
        "💬 Escriba *menu* para volver al inicio"
    )

def response_precios_unitarios():
    return (
        "💰 *PRECIOS UNITARIOS DE JUEGOS*\n\n"
        "🌊 *Juegos Acuáticos*\n"
        "• Caminata en línea — S/ 5.00\n"
        "• Puente acuático — S/ 5.00\n"
        "• Tirolesa acuática — S/ 8.00\n"
        "• Puente aéreo — S/ 8.00\n\n"
        "⛰️ *Juegos de Altura*\n"
        "• Columpio Extremo 'Vuelo del Cóndor' — S/ 20.00\n"
        "• Circuito de 21 obstáculos extremos — S/ 20.00\n\n"
        "💬 Escriba *menu* para volver al inicio"
    )

def response_paquetes_promocionales():
    return (
        "🎒 *PAQUETES PROMOCIONALES*\n\n"
        "💦 *Paquete Acuático — S/ 25.00*\n"
        "• Entrada al parque\n"
        "• Puente acuático\n"
        "• Caminata en línea\n"
        "• Tirolesa acuática\n"
        "• Puente aéreo\n\n"
        "🧗 *Paquete Aventurero — S/ 35.00*\n"
        "• Entrada al parque\n"
        "• Columpio extremo\n"
        "• Circuito de 21 obstáculos\n"
        "• Puente acuático\n\n"
        "🔥 *Paquete Full — S/ 45.00*\n"
        "• Entrada al parque\n"
        "• Columpio extremo\n"
        "• Circuito de 21 obstáculos\n"
        "• Tirolesa acuática\n"
        "• Caminata en línea\n"
        "• Puente aéreo\n"
        "• Puente acuático\n\n"
        "💬 Escriba *menu* para volver al inicio"
    )

def response_como_llegar():
    return (
        "📍 *CÓMO LLEGAR A SAQSAYKI*\n\n"
        "🏃‍♂️‍➡️ Nos encontramos aproximadamente a 30 minutos a pie desde la Chicana Grande.\n\n"
        "🚕 En taxi podrás llegar en aproximadamente 15 minutos desde Chicana Grande.\n\n"
        "🗺️ *Google Maps:*\n"
        "https://maps.app.goo.gl/xrwjZyXT2iBeMiUr9\n\n"
        "📞 *Taxis recomendados:*\n"
        "• 926 050 769\n"
        "• 991 972 382\n\n"
        "🏍️ *Tours en cuatrimoto:*\n"
        "• 942 208 931\n\n"
        "💬 Escriba *menu* para volver al inicio"
    )

def response_restaurante():
    return jsonify({
        "replies": [
            {
                "message": (
                    "🍽️ *CARTA DEL RESTAURANTE SAQSAYKI*\n\n"
                    "Aquí está nuestra carta completa con todos nuestros platillos.\n\n"
                    "📌 *Nota:* Solo realizamos reservas para días festivos y eventos especiales.\n\n"
                    "¿Tienes alguna consulta? Escríbenos sin problema, estamos para ayudarte.\n\n"
                    "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                    "💬 Escriba *menu* para volver al inicio"
                ),
                "image": "https://i.ibb.co/6w2zX9q/carta-ejemplo.jpg" 
            }
        ]
    })

def mostrar_menu_principal():
    """Show the main menu to the user."""
    texto = (
        "¡Buenas noches! ✨\n\n"
        "Bienvenido(a) al *Parque Temático Saqsayki*\n\n"
        "Vive una experiencia única llena de aventura, diversión y naturaleza.\n\n"
        "📌 *Seleccione una opción escribiendo el número:*\n\n"
        "1️⃣ Horarios e ingreso\n"
        "2️⃣ Precios unitarios de juegos\n"
        "3️⃣ Paquetes promocionales\n"
        "4️⃣ Cómo llegar\n"
        "5️⃣ Restaurante 🍽️ (Ver carta completa)\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "💡 Ingrese una de las opciones\n\n"
        "📌 *Comandos:* Escriba *menu* para ver este mensaje nuevamente\n\n"
        "📍 Saqsayki - Tu mejor experiencia"
    )
    return generar_respuesta(texto)

def generar_respuesta(texto_mensaje):
    """Generate a JSON response with the provided message."""
    return jsonify({"replies": [{"message": texto_mensaje}]})

if __name__ == '__main__':
    app.run(debug=True)  # Run in debug mode for development
