import telebot
import modules.creating_inline_button as c_inline_bt
import modules.creating_bot as c_bot

inline_keyboard1 = telebot.types.InlineKeyboardMarkup(row_width= 2)
inline_keyboard1.add(c_inline_bt.inline_bt, c_inline_bt.inline_bt1)

inline_keyboard2 = telebot.types.InlineKeyboardMarkup(row_width= 2)
inline_keyboard2.add(c_inline_bt.inline_bt, c_inline_bt.inline_bt2)

inline_keyboard3 = telebot.types.InlineKeyboardMarkup(row_width= 2)
inline_keyboard3.add(c_inline_bt.inline_bt, c_inline_bt.inline_bt3)

inline_keyboard4 = telebot.types.InlineKeyboardMarkup(row_width= 2)
inline_keyboard4.add(c_inline_bt.inline_bt, c_inline_bt.inline_bt4)

inline_keyboard5 = telebot.types.InlineKeyboardMarkup(row_width= 2)
inline_keyboard5.add(c_inline_bt.inline_bt, c_inline_bt.inline_bt5)