from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback

class ReadLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):

        if messageProtocolEntity.getType() == 'text':
            self.onTextMessage(messageProtocolEntity)
        elif messageProtocolEntity.getType() == 'media':
            self.onMediaMessage(messageProtocolEntity)

        self.toLower(messageProtocolEntity.ack())
        self.toLower(messageProtocolEntity.ack(True))


    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        self.toLower(entity.ack())

    def onTextMessage(self,messageProtocolEntity):
        # just print info
        print("{ \"text\": \"%s\", \"mobile\": \"%s\", \"type\": \"text\" }" % (messageProtocolEntity.getBody(), messageProtocolEntity.getFrom(False)))

    def onMediaMessage(self, messageProtocolEntity):
        # just print info
        if messageProtocolEntity.media_type == "image":
            print("{ \"text\": \"%s\", \"mobile\": \"%s\", \"type\": \"image\" }" % (messageProtocolEntity.url, messageProtocolEntity.getFrom(False)))

        elif messageProtocolEntity.media_type == "location":
            print("{ \"text\": \"latitude: %s, longitude: %s\", \"mobile\": \"%s\", \"type\": \"location\" }" % (messageProtocolEntity.proto.degrees_latitude, messageProtocolEntity.degrees_longitude, messageProtocolEntity.getFrom(False)))

        elif messageProtocolEntity.media_type == "contact":
            print("{ \"text\": \"name: %s, number: %s\", \"mobile\": \"%s\", \"type\": \"contact\" }" % (messageProtocolEntity.getName(), messageProtocolEntity.getCardData(), messageProtocolEntity.getFrom(False)))
