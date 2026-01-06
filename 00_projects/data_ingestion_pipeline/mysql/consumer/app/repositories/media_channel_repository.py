from sqlalchemy.orm import Session
from app.models.media_channel import MediaChannel

class MediaChannelRepository:
    db: Session
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, media_channel: MediaChannel):
        self.db.add(media_channel)
        self.db.commit()
        self.db.refresh(media_channel)
        return media_channel
    
    def get_all(self):
        return self.db.query(MediaChannel).all()
    