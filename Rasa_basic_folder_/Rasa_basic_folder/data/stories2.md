
* greet
    - utter_greet
* ask_restaurant{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* ask_restaurant
    - utter_ask_budget
* ask_budget
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "yasodanagella@gmail.com"}
    - slot{"email": "yasodanagella@gmail.com"}
    - action_send_email
    - utter_confirm_email
* bye
    - utter_thanks_response
    - action_restart

* greet
    - utter_greet
* ask_restaurant{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* ask_restaurant{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* ask_budget{"budget": "300"}
    - slot{"budget": "300"}
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "yashu@gmail.com"}
    - slot{"email": "yashu@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_bye
    - action_restart

* ask_restaurant
    - utter_ask_location
* ask_restaurant{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* ask_restaurant{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* ask_budget{"budget": "1000"}
    - slot{"budget": "1000"}
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "upgrad123@gmail.com"}
    - slot{"email": "upgrad123@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_bye
    - action_restart

* ask_restaurant{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* ask_restaurant{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_budget
* ask_budget{"budget": "456"}
    - slot{"budget": "456"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "abcd@gmail.com"}
    - slot{"email": "abcd@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_bye
