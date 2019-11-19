# API Documentation
## This is an API that facilitates creation of classrooms
### Requirements
- An API interactve client eg Postman or RapidAPI.

### GET all data (Using Postman)
1. visit the base URL/classes eg localhost:5000/class
2. Set the API call to GET request (The default in postman is already GET)
3. Hit **Send** and retrieve the data.

### GET specific data using 'id'
> **NOTE**: The only available retrieve parameter available is the 'id'
1. visit the base URL/classes eg localhost:5000/class
2. append the data id after a forward slash to the end eg localhost:5000/class/2, where 2 is the id
3. Set the API call to GET request
4. Hit send

### POST data to the database, create a class
1. visit the base URL/classes eg localhost:5000/class
2. Go to **Headers** in the postman client and set **Content-Type** to **application/json**
3. Go to **Body** and input the url and action in a JSON format with keys 'url' and 'action' eg 
>{
>
>    "url": "crowdclassroom.com",
>
>    "action": "Created crowdclassroom"
>
>}
4. Hit **Send**
#### NOTE
- ALways use a double-quote when creating JSON objects for POST and PUT request
- The id parameter is auto-incremented and should  not be tampered with.

### PUT (Update Specific data)
1. visit the base URL/classes eg localhost:5000/class
2. append the data id to be updated after a forward slash to the end eg localhost:5000/class/2, where 2 is the id
3. Input the new JSON data 
4. Hit **Send**

### DELETE (Delete Specific data)
1. visit the base URL/classes eg localhost:5000/class
2. append the data id to be deleted after a forward slash to the end eg localhost:5000/class/2, where 2 is the id
3. Hit **Send**
