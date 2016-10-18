INSERT INTO users(firstname, lastname, created_at, updated_at)
VALUES ('mike', 'choi', now(), now()), ('mike', 'choi', now(), now()), ('mike', 'choi', now(), now()),('Diana', 'Smith', now(), now()),(' James','Johnson', now(), now());
        
INSERT INTO friendships(users_id, friends_id, created_at, updated_at)
VALUES (6, 6, now(), now()), (5, 5, now(), now()), (4, 4, now(), now()),(3, 3, now(), now()),(2, 2, now(), now()),(1,1,now(),now()
    
    
SELECT users.firstname, users.lastname, users2.firstname as friendfirstname, users2.lastname as friendlastname FROM users
LEFT JOIN friends On users.id = friends.users_id
LEFT JOIN users as users2
ON users2.id = friends.friends_id;