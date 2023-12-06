UPDATE users
SET 
  email = 'jon@birchumhvac.com',
  hashed_password = '$2b$12$p.EwI0QwWUuYeC0SjhdodOw0nd26GxBe1UxHtg7COXRL/vNh5twoW',
  is_active = true,
  is_superuser = true,
  username = 'JonAdmin'
WHERE id = 1;

