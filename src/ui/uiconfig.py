# #This is a simple way of reading the config file.        

# from configparser import ConfigParser

# class Config:
#     def __init__(self,config_path=".src/ui/uiconfig.ini"):
#         self.config=ConfigParser()
#         self.connfig.read(config_path)
        
# #Now creating separate functions for each constant

#     def _get_page_title(self):
#         return self.config["DEFAULT"].get("page_title")
    
#     def _get_llm_options(self):
#         return self.config["DEFAULT"].get("LLM_options").split(", ")
    
#     def _get_usecase_options(self):
#         return self.config["DEFAULT"].get("Usecase_options").split(", ")
    
#     def _get_groqModel_options(self):
#         return self.config["DEFAULT"].get("GROQ_Model_Options").split(", ")