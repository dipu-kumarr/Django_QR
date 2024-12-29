token=http://127.0.0.1:8000/api/token/refresh/
        http://127.0.0.1:8000/api/token/

http://127.0.0.1:8000/api/users/?name=john
http://127.0.0.1:8000/api/users/?id=1
http://127.0.0.1:8000/api/users/?mobile=983525....


2. POST Request to Create a User and QR User Link
Endpoint URL:

plaintext
Copy code
http://127.0.0.1:8000/api/qr-users-link
HTTP Method: POST

Headers:

Key: Content-Type
Value: application/json
Body (JSON): In Postman, select Body > raw > JSON and enter the following:

json
Copy code
{
    "user": {
        "name": "John Doe",
        "age": 30,
        "address": "123 Elm Street",
        "mobile": "1234567890"
    },
    "qr_unique_id": "abc123"
}
Steps:

Paste the URL (http://127.0.0.1:8000/api/qr-users-link) in Postman.
Select POST.
Add the headers and body.
Click Send.
Response Example:

json
Copy code
{
    "id": 1,
    "user": {
        "id": 1,
        "name": "John Doe",
        "age": 30,
        "address": "123 Elm Street",
        "mobile": "1234567890"
    },
    "qr_unique_id": "abc123"
}
3. GET Request to Search a User
You can search by name, mobile, or QR unique ID.

Example 1: Search by Mobile
Endpoint URL:

plaintext
Copy code
http://127.0.0.1:8000/api/search?mobile=1234567890
HTTP Method: GET

Paste the URL (http://127.0.0.1:8000/api/search?mobile=1234567890) in Postman.
Select GET.
Click Send.
Response Example:

json
Copy code
{
    "id": 1,
    "name": "John Doe",
    "age": 30,
    "address": "123 Elm Street",
    "mobile": "1234567890"
}
Example 2: Search by QR Unique ID
Endpoint URL:

plaintext
Copy code
http://127.0.0.1:8000/api/search?qr_unique_id=abc123
HTTP Method: GET