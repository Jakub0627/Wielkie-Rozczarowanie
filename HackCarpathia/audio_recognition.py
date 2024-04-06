from pydub import AudioSegment
import speech_recognition as sr


def convert_to_wav(input_audio, output_mp3):
    audio = AudioSegment.from_file(input_audio)
    audio.export(output_mp3, format="wav")


def recognize_speech_from_audio_file(file_path, language='pl-PL'):
    r = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = r.record(source)
    try:
        recognized_text = r.recognize_google(audio_data, language=language)
        return recognized_text
    except sr.UnknownValueError:
        return "Nie można rozpoznać mowy"
    except sr.RequestError as e:
        return "Błąd serwera: " + str(e)
