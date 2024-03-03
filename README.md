#Used conda to create an enviorment with python=3.9 argument 
conda create -n rasa python=3.9

#Acticate the enciorment
conda activate rasa

#Install tensorflow with pip
pip install tensorflow 

#Install rasa using pip
pip install rasa

#Run the action file (check the port number from the rndpoints.yml file and make sure the port number is same in both the places i.e, the command below and the endpoints.yml file)
python -m rasa_sdk --actions actions --port 5055

#And then to run this project run, 
rasa train

#To run the bot in the command file 
rasa shell

And enjoy
