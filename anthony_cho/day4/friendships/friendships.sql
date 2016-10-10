INSERT INTO users(first_name, last_name, created_at, updated_at)
VALUES ('Kevin', 'Bacon', Now(), Now()),
		('Mike', 'Choi', Now(), Now()),
        ('Martin', 'Garrix', Now(), Now()),
        ('Jeff', 'Goldbloom', Now(), Now()),
        ('Albert', 'Kid', Now(), Now());
        
SELECT * FROM users;

SELECT * FROM friendships;

INSERT INTO friendships(user_id, friend_id, created_at, updated_at)
VALUES (1, 2, Now(), Now()),
	(1, 3, Now(), Now()),
    (4, 5, Now(), Now()),
    (2, 3, Now(), Now());
    
    
SELECT users.first_name, users.last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name
FROM users 
LEFT JOIN friendships 
On users.id = friendships.user_id
LEFT JOIN users as users2
ON users2.id = friendships.friend_id;