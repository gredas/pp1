class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on == True:
            if len(self.channels)==0:
                print(f'TV IS on, CHANNEL {self.channel_no}, VOLUME {self.volume}')
            else:
                print(f'TV IS on, CHANNEL {self.channel_no} {self.channels[self.channel_no-1]}, VOLUME {self.volume}')
        else:
            if len(self.channels)==0:
                print(f'TV IS OFF, CHANNEL {self.channel_no}, VOLUME {self.volume}')
            else:
                print(f'TV IS OFF, CHANNEL {self.channel_no} {self.channels[self.channel_no-1]}, VOLUME {self.volume}')
    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no
    def set_channels(self,channel_list):
        self.channels = channel_list
    def show_channels(self):
        print(self.channels)
    def volume_up(self):
        if self.volume == 10:
            print('MAX')
        else:
            self.volume+=1
    def volume_down(self):
        if self.volume == 0:
            print('MIN')
        else:
            self.volume-=1
tv = TV()
tv.show_status()
tv.set_channels(['TVP1','TVP2','POLSAT','TVN','FILMBOX','DISCOVERY'])
tv.set_channel(1)
tv.show_status()
tv.volume_down()
tv.show_status()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.show_status()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.show_status()



