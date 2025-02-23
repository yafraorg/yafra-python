#!/usr/bin/env python
# Event Grid Namespace client
client = EventGridPublisherClient(endpoint, credential, namespace_topic=YOUR_TOPIC_NAME)

# Event Grid Basic Client
client = EventGridPublisherClient(endpoint, credential)