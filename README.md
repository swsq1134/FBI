# FBI

install requirements from requirements.txt. 
Run the following command after running cmd in your root folder of the project:
pip install -r requirements.txt

Steps:
1. model is already trained. (Do no re run train.py it consumes limited api calls)
2. run log analyser if you want to create templates for production logs. Already created in result/
3. run main.py
4. Open http://127.0.0.1:5000
5. enter an example error (ex: Did not manage to compute risk indicators. ARD application failed with the following exception: The key CZK/EUR not found in dictionary)
6. you may look at logs.log for more exaamples. Enter an error message similar to the ones you see.
7. click on submit. you would see the source application and the impacted ones

NOTE: use the commented out API key in main.py if the current one expires

![image](https://github.com/swsq1134/FBI/assets/51440121/834938bb-b499-4059-9b6a-5e62f0cee079)
