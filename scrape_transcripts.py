import csv
import time
import random
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def get_transcript(video_id):
    try:
        # Пытаемся получить список доступных транскриптов
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # Ищем транскрипт на русском (созданный вручную или автоматически)
        try:
            transcript = transcript_list.find_transcript(['ru'])
        except Exception:
            try:
                 # Если русского нет, берем английский и переводим
                 transcript = transcript_list.find_transcript(['en']).translate('ru')
            except Exception:
                 # Если и это не вышло, берем первый попавшийся и переводим
                 first_transcript = list(transcript_list)[0]
                 transcript = first_transcript.translate('ru')

        # Получаем данные субтитров
        transcript_data = transcript.fetch()

        # Форматируем в чистый текст
        formatter = TextFormatter()
        text = formatter.format_transcript(transcript_data)

        # Убираем лишние переносы строк
        text = text.replace('\n', ' ')
        return text
    except Exception as e:
        return f"Не удалось получить текст: {e}"

def main():
    input_file = 'voronovich_videos.tsv'
    output_file = 'voronovich_knowledge_base.txt'

    videos = []
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split('\t', 1)
                if len(parts) == 2:
                    videos.append(parts)
    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден. Убедитесь, что он лежит в той же папке.")
        return

    total_videos = len(videos)
    print(f"Найдено {total_videos} видео для обработки. Начинаем парсинг...")

    with open(output_file, 'w', encoding='utf-8') as out_f:
        for index, (video_id, title) in enumerate(videos, 1):
            print(f"[{index}/{total_videos}] Скачиваю субтитры для: {title}")

            transcript_text = get_transcript(video_id)

            # Записываем заголовок
            out_f.write(f"--- Видео: {title} ---\n")
            # Записываем текст
            out_f.write(transcript_text + "\n\n")

            # Чтобы YouTube не заблокировал за спам, делаем небольшую паузу
            time.sleep(random.uniform(1.0, 3.0))

    print(f"Готово! База знаний успешно сохранена в файл {output_file}")

if __name__ == '__main__':
    main()
