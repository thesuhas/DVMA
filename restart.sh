sudo docker-compose down
./build_images.sh
sudo docker-compose up -d
sleep 10s
./reset-db.sh