import os
import csv
import time
import random
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def get_transcript(video_id):
    try:
        # Проверяем версию библиотеки и вызываем нужный метод
        if hasattr(YouTubeTranscriptApi, 'list_transcripts'):
            # Версии ~0.4.x до 1.x
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        elif hasattr(YouTubeTranscriptApi, 'get_transcript'):
            # Очень старые версии < 0.3.x
            transcript_data = YouTubeTranscriptApi.get_transcript(video_id, languages=['ru', 'en'])
            text = " ".join([item['text'] for item in transcript_data])
            text = text.replace('\n', ' ')
            return text
        else:
            # Версия >= 1.2.x (текущая)
            ytt_api = YouTubeTranscriptApi()
            transcript_list = ytt_api.list(video_id)

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
    # Ищем файл с учетом того, что Windows может добавлять скрытые расширения
    possible_names = ['voronovich_videos.tsv', 'voronovich_videos.tsv.txt', 'voronovich_videos.txt']
    input_file = None
    for name in possible_names:
        if os.path.exists(name):
            input_file = name
            break

    output_file = 'voronovich_knowledge_base.txt'

    if not input_file:
        print(f"Ошибка: Файл со списком видео (voronovich_videos.tsv) не найден.")
        print(f"Убедитесь, что вы распаковали архив и оба файла лежат в одной папке.")
        return

    videos = []
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                # В файле может быть как настоящая табуляция, так и буквальные символы \t
                clean_line = line.strip()
                if '\\t' in clean_line:
                    parts = clean_line.split('\\t', 1)
                else:
                    parts = clean_line.split('\t', 1)

                if len(parts) == 2:
                    videos.append(parts)
    except Exception as e:
        print(f"Ошибка при чтении файла {input_file}: {e}")
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
