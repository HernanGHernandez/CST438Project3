# CST438Project3

## Parking Reservation

##### Group 9

## APP / Project Description
Interactive chat app where where students can find parking spots

## Tech Stack
* Android Studio
* Django 
* Firebase

## Tentative API
#### User
* GET &ensp;&ensp;&ensp;&ensp;&ensp;&ensp; /user
* POST  &ensp;&ensp;&ensp;&ensp;&nbsp; /user
* GET   &ensp;&ensp;&ensp;&ensp;&ensp;&nbsp; /user/{userId}
* PUT   &ensp;&ensp;&ensp;&ensp;&ensp;&nbsp; /user/{userId}
* DELETE  &ensp;&ensp; /user/{userId}
* GET   &nbsp;&ensp;&ensp;&ensp;&ensp;&nbsp;&nbsp; /user/{userId}/parkingId
* DELETE &nbsp;&nbsp;&nbsp;&nbsp; /user/{userId}/parking
* GET   &ensp;&ensp;&ensp;&ensp;&ensp;&nbsp; /user/{userId}/messages
* DELETE &nbsp;&nbsp;&nbsp; /user/{userId}/messages

#### Parking
* POST  &ensp;&ensp;&ensp;&nbsp;  /parking
* GET   &ensp;&ensp;&ensp;&nbsp;&nbsp;&nbsp;    /parking/{parkingId}
* GET   &ensp;&ensp;&ensp;&nbsp;&nbsp;&nbsp;    /parking/{parkingId}/messages
* PUT   &ensp;&ensp;&ensp;&ensp;&nbsp;   /parking/{parkingId}

#### Messages
* POST &ensp;&ensp;&ensp;&nbsp; /messages
* PUT &ensp;&ensp;&ensp;&ensp;&nbsp; /messages
* GET &ensp;&ensp;&ensp;&nbsp;&nbsp;&nbsp; /messages

## Layout
<p align="center">
  <img width="700" alt="Screen Shot 2021-10-28 at 11 58 37 AM" align="center" src="https://user-images.githubusercontent.com/67992122/139318570-26500c81-3449-48da-831b-185a57e124d4.png">
</p>

## ERD
<p align="center">
    <img width="700" src="https://user-images.githubusercontent.com/67992122/139318012-b9a85f0f-adbe-467b-a54f-442df57a4ce0.png">
</p>

