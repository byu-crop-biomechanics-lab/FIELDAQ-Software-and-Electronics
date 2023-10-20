import shutil
from kivy.lang import Builder
import configurator as config
from view.BaseScreen import BaseScreen

Builder.load_file('view/screens/main/testing/DeleteFolderConfirmation.kv')

class DeleteFolderConfirmation(BaseScreen):
    
    def delete_folder_yes(self):
        folder_list = config.get('folders', 0)
        selected_folder = config.get('unwanted_folder', 0)
        try:
            shutil.rmtree('Tests/'+selected_folder)
            folder_list.remove(selected_folder)
            config.set('folders', folder_list)
        except:
            pass

