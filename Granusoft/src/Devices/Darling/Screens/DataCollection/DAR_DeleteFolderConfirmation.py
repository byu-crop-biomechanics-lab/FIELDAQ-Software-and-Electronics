import shutil
from kivy.lang import Builder
import Devices.Darling.configurator as config
from util.BaseScreen import BaseScreen
from util.getKVPath import getKVPath
import os
from util.TestLog import TestLog
Builder.load_file(getKVPath(os.getcwd(), __file__))

class DAR_DeleteFolderConfirmation(BaseScreen):
    
    def delete_folder_yes(self):
        folder_list = config.get('folders', 0)
        selected_folder = config.get('unwanted_folder', 0)
        try:
            shutil.rmtree('Tests/'+selected_folder)
            folder_list.remove(selected_folder)
            config.set('folders', folder_list)
        except:
            pass

    def on_enter(self):
        
        log=TestLog()
        log.connection("Entered DAR_DeleteFolderConfirmation")

