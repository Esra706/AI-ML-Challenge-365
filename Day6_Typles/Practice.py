

# My favorite subjects vs a friend's favorite subjects
my_subjects = {"Math", "Computer Science", "English", "Physics", "Urdu"}
friend_subjects = {"Math", "Chemistry", "Computer Science", "Biology", "Urdu"}

common = my_subjects & friend_subjects
only_mine = my_subjects - friend_subjects
only_friend = friend_subjects - my_subjects

print("My subjects:", my_subjects)
print("Friend's subjects:", friend_subjects)
print("Common subjects:", common)
print("Only I like:", only_mine)
print("Only friend likes:", only_friend)