# oc_lit_review

:books: Made for an [OpenClassrooms](https://openclassrooms.com) studies project.

`oc_lit_review` is a Django-based book review platform.


# Features

This project was aimed to be a minimal functional prototype. This repository covers Django backend and basic frontend features.

In its current state, the platform allows a user to sign up and log in.
A user can then create a ticket (A book review demand), respond to a ticket with a review or just post a review with a form combining ticket and review creation.
A user also have the ability to follow other users, thereby their tickets and reviews will appear in user dashboard feed.
In the latter, reviews in respond to user tickets made by other users he does not follow will also be displayed.

# Setup

- First clone this repository and navigate to downloaded folder:
  ``` bash
  git clone https://github.com/PabloLec/oc_lit_review.git
  cd oc_lit_review
  ```

- Then, start a virtual environment:
  ``` bash
  python3 -m venv env
  source env/bin/activate
  ```

- Before running, install the project requirements with:
  ``` bash
  python3 -m pip install -r requirements.txt
  ```

- Finally, you can navigate to Django project directory and run the server:
  ``` bash
  cd oc_lit_review
  python3 -m manage runserver   
  ```

- Website should be served at `127.0.0.1:8000`.
