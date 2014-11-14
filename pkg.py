#--* coding:utf-8 *--

import zipfile, shutil



def generateChannelPackage(name):

    file_object = open('channelNames.txt')
    channels = file_object.readlines()
    file_object.close()

    for channel in channels:
        channelName = channel.replace('\r', '').replace('\n', '')
        if len(channelName) > 0:
            shutil.copyfile(name+".apk", "./result/"+name+"("+channelName+").apk")
            zipped = zipfile.ZipFile("./result/"+name+"("+channelName+").apk", 'a', zipfile.ZIP_DEFLATED)
            empty_channel_file = "META-INF/channel_{channel}".format(channel=channelName)
            zipped.write('emptyfile', empty_channel_file)
            zipped.close()


if __name__ == '__main__':
    generateChannelPackage("Test")
