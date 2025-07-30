# bot/utils/texts.py

def get_welcome_text(lang: str) -> str:
    if lang == "hi":
        return (
            "🌟 <b>यश पैलेस में आपका स्वागत है!</b> 🌟\n\n"
            "हम आपको शानदार होटल सेवाएं प्रदान करने के लिए यहाँ हैं। 🏨✨\n\n"
            "<b>आप क्या कर सकते हैं:</b>\n"
            "🛏️ रूम बुक करें\n"
            "📋 अपनी बुकिंग देखें\n"
            "🎁 ऑफ़र और सिफारिशें पाएं\n"
            "📞 सहायता लें और अधिक जानें\n\n"
            "👇 नीचे दिए गए मेनू से शुरुआत करें!"
        )
    else:
        return (
            "🌟 <b>Welcome to Yash Palace!</b> 🌟\n\n"
            "We are here to provide you with premium hotel services. 🏨✨\n\n"
            "<b>What you can do:</b>\n"
            "🛏️ Book a room\n"
            "📋 View your bookings\n"
            "🎁 Get offers & recommendations\n"
            "📞 Get support and know more\n\n"
            "👇 Use the menu below to get started!"
        )


def get_menu_options(lang: str) -> list[str]:
    if lang == "hi":
        return [
            "🔍 होटल खोजें",
            "🛏️ कमरा बुक करें",
            "📋 बुकिंग देखें",
            "🤖 सिफारिशें",
            "🎁 ऑफ़र",
            "🛎️ सुविधाएं",
            "📞 सहायता",
            "📝 फीडबैक",
            "⚙️ सेटिंग्स",
            "ℹ️ हमारे बारे में"
        ]
    else:
        return [
            "🔍 Search Hotels",
            "🛏️ Book a Room",
            "📋 View Bookings",
            "🤖 Recommendations",
            "🎁 Offers",
            "🛎️ Amenities",
            "📞 Support",
            "📝 Feedback",
            "⚙️ Preferences",
            "ℹ️ About Us"
        ]
