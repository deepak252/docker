from app.repositories.media_channel_repository import MediaChannelRepository
from app.schemas.media_channel import MediaChannelCreate
from app.models.media_channel import MediaChannel

class MediaChannelService:
    repo: MediaChannelRepository

    def __init__(self, repo: MediaChannelRepository):
        self.repo = repo

    def create_media_channel(self, payload: MediaChannelCreate):
        m_channel = MediaChannel(name=payload.name, type=payload.type)
        return self.repo.create(m_channel)
    
    def get_all_media_channels(self):
        return self.repo.get_all()
    
        
    