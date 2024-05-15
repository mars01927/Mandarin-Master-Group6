import tkinter as tk
from tkinter import filedialog, messagebox
import sounddevice as sd
import wave
import tempfile
import threading
import simpleaudio as sa
import requests
import json
import re

API_KEY = "8JX9tTtoyKv0KF8NEs2bE0Do"
SECRET_KEY = "PVKSXaSLrvRqdWmYGkPwm5vNEup4bpEj"

def verify_credentials(username, password):
    return username == "admin" and password == "admin"


def login():
    username = username_entry.get()
    password = password_entry.get()
    if verify_credentials(username, password):
        open_main_interface()
        root.withdraw()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def logout(main_window):
    main_window.destroy()
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    root.deiconify()


def open_main_interface():
    main_window = tk.Toplevel(root)
    main_window.title("Main Interface")

    tk.Button(main_window, text="广东话翻译学习", command=lambda: open_translation_learning(main_window)).pack(pady=10)
    tk.Button(main_window, text="广东话读音学习", command=lambda: open_pronunciation_learning(main_window)).pack(
        pady=10)
    tk.Button(main_window, text="考试", command=lambda: open_examination(main_window)).pack(pady=10)
    tk.Button(main_window, text="登出", command=lambda: logout(main_window)).pack(pady=10)
    tk.Button(main_window, text="关闭", command=lambda: close_application(main_window)).pack(pady=10)


def open_translation_learning(parent_window):
    TranslationLearning(parent_window, parent_window)


class TranslationLearning:
    def __init__(self, master, parent_window):
        self.master = tk.Toplevel(master)
        self.parent_window = parent_window  # 保存主菜单窗口的引用
        self.master.title("广东话翻译学习")

        self.current_audio_index = 0
        self.audios = ["audio1.wav", "audio2.wav", "audio3.wav", "audio4.wav", "audio5.wav",
                       "audio6.wav", "audio7.wav", "audio8.wav", "audio9.wav", "audio10.wav"]
        self.correct_translations = [
            "你吃了吗？", "我不知道。", "去哪里啊？", "非常感谢。", "不用客气。",
            "你叫什么名字？", "今晚有空吗？", "我迟到了。", "你住在哪里？", "我们走吧。"
        ]

        self.translation_entry = tk.Entry(self.master)
        self.translation_entry.pack()

        self.play_button = tk.Button(self.master, text="播放/重播", command=self.play_current_audio)
        self.play_button.pack()

        self.submit_button = tk.Button(self.master, text="提交翻译", command=self.submit_translation)
        self.submit_button.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def play_current_audio(self):
        if self.current_audio_index < len(self.audios):
            play_audio(self.audios[self.current_audio_index])
    
    def get_access_token(self):
        url = "https://aip.baidubce.com/oauth/2.0/token"
        params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
        return str(requests.post(url, params=params).json().get("access_token"))

    def evaluate_translation(self, input_text, correct_text):
        text = f"现在请你扮演一个语言学习软件的评分助手，请评估这两个句子之间相似的百分比。请注意，你只需要提供一个数字。只提供数字。'{input_text}' 和 '{correct_text}'。"
        url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + self.get_access_token()
        payload = json.dumps({
            "messages": [
                {
                    "role": "user",
                    "content": text
                }
            ]
        })
        headers = {
            'Content-Type': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)
        response_text = response.text
        data = json.loads(response_text)
        result_value = data['result'] 
        
        # 使用正则表达式提取百分比数字部分
        percentage_str = re.findall(r'\d+', result_value)[0]  # 假设百分比数字是连续的，不包含任何字符分隔符或其他文本描述。如果格式不同，请调整正则表达式以适应实际情况。
        percentage = int(percentage_str)  # 将提取的数字转换为整数类型（假设确实是一个整数）

        return percentage, percentage >= 70


    def submit_translation(self):
        user_translation = self.translation_entry.get()
        correct_translation = self.correct_translations[self.current_audio_index]
        similarity, is_correct = self.evaluate_translation(user_translation, correct_translation)

        print(f"Similarity: {similarity:.2f}%, Correct: {is_correct}")

        self.result_label.config(text=f"相似度: {similarity:.2f}%, 正确答案: {correct_translation}")
        self.current_audio_index += 1

        if self.current_audio_index >= len(self.audios):
            messagebox.showinfo("完成", "翻译练习完成！")
            self.master.destroy()  # 关闭翻译练习窗口
            self.parent_window.deiconify()  # 显示主菜单窗口
            self.current_audio_index = 0  # 重置为第一个音频，以便重复练习
        else:
            self.translation_entry.delete(0, tk.END)  # 清空输入框并继续

# # This method is used for using chatgpt api to evaluate translation similarity
# def evaluate_translation(input_text, correct_text):
#     try:
#         response = openai.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a translation comparison tool."},
#                 {"role": "user", "content": f"Please assess the percentage of phonetic similarity between these two sentences. Note, you should only provide A NUMBER. '{input_text}' and '{correct_text}'."},
#             ]
#         )

#         result = response['choices'][0]['message']['content']
#         print(result)  # Debugging: Print the result to see the response

#         # Extract the similarity and correctness from the GPT-3.5-turbo response
#         # Note: You'll need to parse the response appropriately to extract similarity score and correctness
#         similarity = re.findall(r'\d+', result)  # Placeholder: Replace with actual similarity extraction logic
#         is_correct = similarity >= 70  # Placeholder: Replace with actual correctness extraction logic

#         return similarity, is_correct
#     except Exception as e:
#         print(f"Error calling OpenAI API: {e}")
#         return 0, False

def open_pronunciation_learning(parent_window):
    # 创建新窗口
    new_window = tk.Toplevel(parent_window)
    new_window.title("广东话读音学习")

    # 当新窗口关闭时，显示父窗口
    new_window.protocol("WM_DELETE_WINDOW", lambda: on_close_pronunciation_window(new_window, parent_window))

    # 初始化广东话读音学习界面
    CantonesePronunciationLearning(new_window)


def on_close_pronunciation_window(child_window, parent_window):
    child_window.destroy()
    parent_window.deiconify()

class CantonesePronunciationLearning:
    def __init__(self, master):
        self.master = tk.Toplevel(master)
        self.master.title("广东话读音学习")

        # Define the sample rate
        self.fs = 44100  # Sample rate, 44100 Hz is a common rate for audio

        self.sentences = [
            "早晨，你好吗？",
            "请问，洗手间在哪里？",
            "我想点一杯咖啡。",
            "这个多少钱？",
            "谢谢你的帮助！"
        ]
        self.audio_files = ["sentence1.wav", "sentence2.wav", "sentence3.wav", "sentence4.wav", "sentence5.wav"]
        self.current_sentence_index = 0

        self.audio_play_obj = None
        self.recorded_audio_file = None

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.master, text="点击播放学习广东话").pack()
        play_button = tk.Button(self.master, text="播放", command=self.play_audio)
        play_button.pack()

        self.record_button = tk.Button(self.master, text="录音", command=self.record_audio)
        self.record_button.pack()

        self.stop_button = tk.Button(self.master, text="停止", command=self.stop_audio, state='disabled')
        self.stop_button.pack()

    def play_audio(self):
        if self.audio_play_obj and self.audio_play_obj.is_playing():
            self.audio_play_obj.stop()

        file_path = self.audio_files[self.current_sentence_index]
        wave_obj = sa.WaveObject.from_wave_file(file_path)
        self.audio_play_obj = wave_obj.play()

        self.stop_button.config(state='normal')

    def stop_audio(self):
        if self.audio_play_obj and self.audio_play_obj.is_playing():
            self.audio_play_obj.stop()
        self.stop_button.config(state='disabled')

    def record_audio(self):
        duration = 15  # seconds
        # Change channels to 1 for mono recording
        recording = sd.rec(int(duration * self.fs), samplerate=self.fs, channels=1)
        sd.wait()  # Wait until recording is finished

        self.recorded_audio_file = tempfile.mktemp(".wav")

        wf = wave.open(self.recorded_audio_file, 'wb')
        wf.setnchannels(1)  # Set to 1 channel for mono audio
        wf.setsampwidth(2)  # Typically 2 bytes for PCM
        wf.setframerate(self.fs)
        wf.writeframes(recording.tobytes())
        wf.close()

        # Assuming play_audio can handle mono audio
        play_audio(self.recorded_audio_file)    


def record_audio(duration):
    fs = 44100  # Sample rate
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    return myrecording, fs


def save_audio(recording, fs):
    file = tempfile.mktemp(".wav")
    wf = wave.open(file, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(fs)
    wf.writeframes(recording.tobytes())
    wf.close()
    return file


def play_audio(file_path):
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing

def open_examination(parent_window):
    examination_window = tk.Toplevel(parent_window)
    examination_window.title("Examination")
    tk.Label(examination_window, text="Examination Interface").pack()


def close_application(main_window):
    main_window.destroy()
    root.quit()


root = tk.Tk()
root.title("Login")

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()
