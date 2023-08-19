
![Manual](./assets/Screenshot%20from%202023-08-17%2021-18-41.png)
# Table of contents
Project Code | Project Name | Description
------- | -------- | -----------
[0x00] | [Get all states](./0-select_states.py) | A  script that lists all states from the database hbtn_0e_0_usa
[0x01] | [Filter states](./1-filter_states.py) | A  script that lists all states from the database hbtn_0e_0_usa that start with letter "N"
[0x02] | [Filter states by user input](./2-my_filter_states.py) | A  script that lists all states from the database hbtn_0e_0_usa where name is the last argument passed.
[0x03] | [SQL Injection...](./3-my_safe_filter_states.py) | An SQL injection proof script that lists all states from the database hbtn_0e_0_usa where name is the last argument passed.
[0x04] | [Cities by states](./4-cities_by_state.py) | An SQL injection proof script that lists all cities from the database hbtn_0e_0_usa.
[0x05] | [Cities by states](./5-filter_cities.py) | An SQL injection proof script that lists all cities from the database hbtn_0e_0_usa.
[0x06] | [First state model](./model_state.py) | A python file defining State class from Base creating table states
[0x07] | [ First state](./8-model_state_fetch_first.py) | A script that uses sqlalchemy orm to list the first state.
[0x09] | [Contains `a`](./9-model_state_filter_a.py) | A script that uses sqlalchemy orm to list states that contain letter a
[0x10] | [Get a state](./10-model_state_my_get.py) | A SQL injection free script that prints the id of a given state.
[0x11] | [Add a new state](./11-model_state_insert.py) | A SQL injection free script that adds a new state and prints its ID.
[0x12] | [Update state](./12-model_state_update_id_2.py) | A SQL injection free script that updates a new state and prints its ID
[0x13] | [Delete states](./13-model_state_delete_a.py) | A SQL injection free script that deletes state containing "a"