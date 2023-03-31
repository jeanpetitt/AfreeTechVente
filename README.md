# AfreeTechVente

AfreetechVente est projet de vente en ligne des fruits qui permet au commerçant de vendre leur fruit.

## Pré requis
ce project comporte deux stack, <strong>le backend et le frontend</strong>
pour executer ce projet en local rassurez-vous d'avoir une version de python >= 3.7, 14<=nodejs<=16, docker, npm et Postgresql<br>
Dans le cas contraire suivre les étape en fonction de son systeme.
- utilisateur windows

cliquer sur [installer python](https://www.python.org/downloads/), [installer nodejs](https://nodejs.org/fr/download/releases), [installer git](https://git-scm.com/download/win),[installer postgresal](https://www.postgresql.org/download/windows/), [installer docker](https://docs.docker.com/desktop/install/windows-install/)

- utilisateur Linux(debian, ubuntu)
par défaut python2 est deja installer sur linux vous n'avez qu'a mettre a jour pour passer a python3 en executant la commande: <br>
```
sudo apt-get upgrade
```
pour installer nodejs proceder comme suit:
- installer le paquet curl
```
sudo apt install curl
```
- installer nodejs a l'aide de curl
```
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
```
```
sudo apt update
sudo apt install nodejs
nodejs --version
npm --versiom
```
- installer postgresql
```
sudo apt install software-properties-common apt-transport-https wget -y
```
```
sudo wget -O- https://www.postgresql.org/media/keys/ACCC4CF8.asc | gpg --dearmor | sudo tee /usr/share/keyrings/postgresql.gpg
```
```
echo deb [arch=amd64,arm64,ppc64el signed-by=/usr/share/keyrings/postgresql.gpg] http://apt.postgresql.org/pub/repos/apt/ focal-pgdg main | sudo tee /etc/apt/sources.list.d/postgresql.list
```
```
echo deb [arch=amd64,arm64,ppc64el signed-by=/usr/share/keyrings/postgresql.gpg] http://apt.postgresql.org/pub/repos/apt/ focal-pgdg-testing main | sudo tee /etc/apt/sources.list.d/postgresql-testing.list
```
```
sudo apt-get update
sudo apt install postgresql-client postgresql -y
```
pour installer docker sur linux il suffit de le telecharger dans le appstore

## A propos des Stack

### backend 
naviguer dans le dossier backend et executer
```
docker-compose up
```
cette application met notre application en developpememt et ordonne a l'application de pacourir le [Dockerfile](./backend/Dockerfile) et le [docker-compose.yml](./docker-compose.yml) pour installer differentes dependances.<br>
Une fois les dependances installer l'application va se mettre en route sur le 0.0.0.0:8080<br>
pour plus de detail cliquer sur [backend](./backend/README.md)

### frontend
naviguer dans le dossier frontend et executer la commande:
```
npm install
```
cela va installer toute les dependances necessaires pour le lancement de l'application

```
npm start
```
cette commance va mettre en route l'application sur le localhost:3000.

pour plus de detail cliquer sur [frontend](./frontend/README.md)



## Deployement


# Autheur
@jeanpetit