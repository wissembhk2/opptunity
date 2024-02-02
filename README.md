In order to run this project you just need docker and docker compose :
you need to execute : <b>docker compose up</b> in the root folder ( opptunity/freelance) 
in this project : - signup works ( localhost:3000/signup ) 
                  - sigin works ( localhost:3000/signin ) ( for now i only created a prototype so is doesn't generate a token it just check the email and password ) 
                  - signup with google or microsoft ( not implemented yet ) 
                  -mail confirmation (not implemented yet in the backend ) you can test the front on ( loacalhost:3000/emailconfirmation ) 
                  - you can check add details page via ( localhost:3000/adddetails ) ( front implemented ) 

-This project is only for testing purposes in order to use it in prod env you must hide you credentials in an .env file or use Vault 
-you must also generate a token in the signin 
-you must create routers files in the backend and avoid routing in main.py 
                  
