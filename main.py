import pywhatkit
import winsdk.windows.devices.geolocation as wdg
import asyncio
import tkinter as tk

# Async function to get coordinates
async def getCoords():
    locator = wdg.Geolocator()
    pos = await locator.get_geoposition_async()
    return [pos.coordinate.point.position.latitude, pos.coordinate.point.position.longitude]

# Wrapper to run the async function
def getLoc():
    return asyncio.run(getCoords())

# Generate Google Maps link
def generate_google_maps_link(latitude, longitude):
    return f"https://www.google.com/maps/place/{latitude},{longitude}"

# Show location in GUI
def show_location():
    try:
        latitude, longitude = getLoc()
        google_maps_link = generate_google_maps_link(latitude, longitude)
        lat_label.config(text=f"Latitude: {latitude}")
        lng_label.config(text=f"Longitude: {longitude}")
        link_label.config(text=f"Google Maps Link:\n{google_maps_link}")
        status_label.config(text="")
    except Exception as e:
        status_label.config(text=f"Error: {e}")

# Send WhatsApp emergency message
def send_emergency():
    try:
        recipient_number = "+917907656865"  # Use your valid phone number with country code
        latitude, longitude = getLoc()
        google_maps_link = generate_google_maps_link(latitude, longitude)
        emergency_message = f"🚨 Emergency!\nHelp needed at:\n{google_maps_link}"
        pywhatkit.sendwhatmsg_instantly(recipient_number, emergency_message)
        status_label.config(text="Emergency message sent!")
    except Exception as e:
        status_label.config(text=f"Error: {e}")

# Tkinter GUI setup
window = tk.Tk()
window.title("My Location Tracker")
window.geometry("500x300")
window.configure(bg="#F0F8FF")

lat_label = tk.Label(window, text="Latitude: ", font=("Arial", 14), bg="#F0F8FF", fg="#0000CD")
lng_label = tk.Label(window, text="Longitude: ", font=("Arial", 14), bg="#F0F8FF", fg="#0000CD")
link_label = tk.Label(window, text="Google Maps Link: ", font=("Arial", 12), bg="#F0F8FF", fg="#0000CD", wraplength=480)
status_label = tk.Label(window, text="", bg="#F0F8FF", fg="red", font=("Arial", 12))

show_button = tk.Button(window, text="Show Location", command=show_location, font=("Arial", 12, "bold"), bg="#87CEFA", fg="#FFFFFF")
emergency_button = tk.Button(window, text="Send Emergency", command=send_emergency, font=("Arial", 12, "bold"), bg="#FF6347", fg="#FFFFFF")

lat_label.pack(pady=5)
lng_label.pack(pady=5)
link_label.pack(pady=5)
show_button.pack(pady=10)
emergency_button.pack(pady=10)
status_label.pack(pady=10)

window.mainloop()
