import os
import telebot

# Render-এর Environment Variable থেকে টোকেন সংগ্রহ করা
BOT_TOKEN = os.environ.get('BOT_TOKEN')

# প্রশ্ন এবং উত্তরের ডিকশনারি
questions_answers = {
    "তুমি কেমন আছো?": "আমি ভালো আছি, ধন্যবাদ! আপনার দিনটি কেমন কাটছে?",
    "তোমার নাম কি?": "আমার নাম ইকো-অ্যাসিস্ট্যান্ট বট। আমি সাধারণ প্রশ্নের উত্তর দিতে পারি।",
    "কে তোমাকে তৈরি করেছে?": "আমাকে একজন ডেভেলপার তৈরি করেছেন, যিনি পাইথন এবং টেলিগ্রাম বট এপিআই ব্যবহার করেছেন।",
    "ধন্যবাদ": "আপনাকে স্বাগতম!",
}

# কোড শুরু হওয়ার আগে টোকেন চেক করা
if not BOT_TOKEN:
    print("গুরুত্বপূর্ণ ত্রুটি: BOT_TOKEN এনভায়রনমেন্ট ভেরিয়েবল সেট করা হয়নি।")
else:
    # বটের একটি ইনস্ট্যান্স তৈরি করা
    bot = telebot.TeleBot(BOT_TOKEN)

    # /start এবং /hello কমান্ড হ্যান্ডেল করার ফাংশন
    @bot.message_handler(commands=['start', 'hello'])
    def send_welcome(message):
        bot.reply_to(message, "হ্যালো! আমি একটি বট। আমাকে কিছু প্রশ্ন করতে পারেন অথবা যেকোনো মেসেজ পাঠাতে পারেন।")

    # নির্দিষ্ট প্রশ্নগুলো হ্যান্ডেল করার ফাংশন
    @bot.message_handler(func=lambda message: message.text in questions_answers)
    def handle_questions(message):
        response = questions_answers[message.text]
        bot.reply_to(message, response)

    # উপরের কোনোটির সাথে না মিললে, এই ইকো ফাংশনটি কাজ করবে
    @bot.message_handler(func=lambda msg: True)
    def echo_all(message):
        bot.reply_to(message, "আপনার প্রশ্নটি বুঝতে পারিনি। আমি আপনার বার্তাটির প্রতিধ্বনি করছি: " + message.text)

    # বটকে ক্রমাগত চালানোর জন্য
    print("বট সফলভাবে চালু হচ্ছে এবং মেসেজের জন্য অপেক্ষা করছে...")
    bot.infinity_polling()
