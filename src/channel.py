import json
import os
from googleapiclient.discovery import build


api_key = os.getenv('YT_API_KEY')


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel_info = youtube.channels().list(id=channel_id, part='brandingSettings,statistics').execute()
        self.__channel_id = channel_id
        self.title = self.channel_info['items'][0]['brandingSettings']['channel']['title']
        self.description = self.channel_info['items'][0]['brandingSettings']['channel']['description']
        self.url = f"https://www.youtube.com/channel/{self.channel_info['items'][0]['id']}"
        self.subscriber_count = self.channel_info['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel_info['items'][0]['statistics']['videoCount']
        self.view_count = self.channel_info['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_info = json.dumps(self.channel_info, indent=2, ensure_ascii=False)
        print(channel_info)
