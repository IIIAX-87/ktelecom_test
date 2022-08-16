after clone

#Start backend
cd k_telecom_test
docker-compose up --build
username admin
password admin

#Start frontend
cd k_telecom_test/frontend/equipment
npm install
npm run serve


#not work:
pagination, filter, validation on form