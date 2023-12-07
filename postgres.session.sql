UPDATE users
SET 
  email = 'bob@bob.com',
  hashed_password = '$2b$12$De.bQUrydqS1.FDMxh8LpOvlhl4HdznbJygp2alOUlMx3ZUMaczHy',
  is_active = true,
  is_superuser = true,
  username = 'bob@bob.com'
WHERE id = 3;

