import shutil
from kivy.lang import Builder
import Devices.Rodney.Settings.configurator as config
from util.BaseScreen import BaseScreen
from util.getKVPath import getKVPath
import os
import traceback

Builder.load_file(getKVPath(os.getcwd(), __file__))

class ROD_DeleteFolderConfirmation(BaseScreen):
    
    def delete_folder_yes(self):
        folder_list = config.get('folders', 0)
        selected_folder = config.get('unwanted_folder', 0)
        print("Inside delete_folder_yes function")
        try:
            shutil.rmtree('Tests/'+selected_folder)
            folder_list = folder_list.replace(selected_folder, "")
            print("I am here")
            for f in folder_list:
                print(f)
            config.set('folders', folder_list)
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            traceback.print_exc()  # This prints the traceback to help diagnose the issue

