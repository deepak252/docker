from app.kafka.producer import KafkaProducer
from app.kafka.topics import MCHANNEL_CREATED
from app.utils import MEDIA_CHANNELS
from app.schemas.media_channel import MediaChannel

class MediaChannelService:
    kafka: KafkaProducer

    def __init__(self):
        self.kafka = KafkaProducer()

    def publish_media_channel(self, mchannel: MediaChannel):
        self.kafka.publish(
            topic = MCHANNEL_CREATED,
            key = "mchannel",
            payload=mchannel.model_dump()
        )

    def produce_media_channels(self):
        for mchannel in MEDIA_CHANNELS:
            mchannel = MediaChannel(
                name = mchannel[0],
                type = mchannel[1]
            )
            self.kafka.publish(
                topic = MCHANNEL_CREATED,
                key = "mchannel",
                payload=mchannel.model_dump()
            )
        return len(MEDIA_CHANNELS)
