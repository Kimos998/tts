from TTS.api import TTS

# تحميل النموذج
tts = TTS(model_name="tts_models/multilingual/multi-dataset/coqui/XTTS-v2")

# نص عربي
text_ar = "مرحباً بك في عالم تحويل النصوص إلى كلام!"

# تحويل النص إلى صوت
tts.tts_to_file(text=text_ar, file_path="output_ar.wav")

print("تم تحويل النص إلى الصوت. تحقق من الملف 'output_ar.wav'.")
