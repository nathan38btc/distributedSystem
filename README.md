# distributedSystem
Appliction Pédagogique

Lancer Docker en administrateur,
Dans l'invite de commande cmd : "docker pull mongo:latest",
cmd : aller dans le dossier ou l'on veut placer la base de donné
cmd : run "docker run -d -p 6379:6379 --name my-mongodb mongo"
cmd : run "docker exec -it my-mongodb bash"
cmd : run "mongo"
cmd : run "use databinance"

python : run "pip install pymongo" pour avoir la librairie
executer code.py pour récuperer les datas de binances et les mettres dans mongo Db
