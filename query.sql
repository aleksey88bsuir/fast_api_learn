SELECT users.name, users.id
FROM users ORDER BY users.id;

SELECT profiles.first_name AS profiles_first_name,
profiles.last_name AS profiles_last_name,
profiles.bio AS profiles_bio, profiles.id AS profiles_id,
profiles.user_id AS profiles_user_id
FROM profiles
WHERE ? = profiles.user_id


SELECT users.name,
users.id,
profiles_1.first_name,
profiles_1.last_name,
profiles_1.bio,
profiles_1.id AS id_1,
profiles_1.user_id
FROM users LEFT OUTER JOIN profiles AS profiles_1
ON users.id = profiles_1.user_id ORDER BY users.id
