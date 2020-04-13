import SN_utils as snu

# Comment related functions
print(snu.get_comment_reskey())
print(snu.get_comment_by_cid(27698))


# Story realted functions
print(snu.get_story_reskey())

# User related functions
print(snu.get_maxuid())
print(snu.get_uid("The Mighty Buzzard"))
print(snu.get_nick(18))
print(snu.get_nick(18000))
print(snu.get_user(18)["realname"])

