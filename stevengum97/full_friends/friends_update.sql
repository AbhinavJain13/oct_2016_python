UPDATE friends
SET first_name = "Steve",
	last_name = "Gum",
    email = "steven.gum@gmail.com",
    updated_at = current_timestamp()
WHERE id=1;